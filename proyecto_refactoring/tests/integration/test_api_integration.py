"""Tests de integracion para las APIs externas."""

from __future__ import annotations

import pytest
import responses

from movies_app.api.omdb import OmdbApi
from movies_app.api.tvmaze import TvmazeApi
from movies_app.clients.base import HttpClient
from movies_app.config import Settings
from movies_app.exceptions import ApiResponseError, ResourceNotFoundError


@responses.activate
def test_omdb_api_search_by_title_returns_movie() -> None:
    responses.add(
        responses.GET,
        "https://www.omdbapi.com/?t=Inception&apikey=test-key",
        json={"Response": "True", "Title": "Inception", "Year": "2010"},
        status=200,
    )
    settings = Settings(omdb_api_key="test-key")
    http = HttpClient(settings)
    api = OmdbApi(http, settings)
    result = api.search_by_title("Inception")
    assert result is not None
    assert result.title == "Inception"


@responses.activate
def test_omdb_api_search_by_title_not_found() -> None:
    responses.add(
        responses.GET,
        "https://www.omdbapi.com/",
        json={"Response": "False", "Error": "Movie not found!"},
        status=404,
    )
    settings = Settings(omdb_api_key="test-key")
    http = HttpClient(settings)
    api = OmdbApi(http, settings)
    with pytest.raises(ResourceNotFoundError):
        api.search_by_title("zzz")


@responses.activate
def test_omdb_api_search_by_actor_returns_movies() -> None:
    responses.add(
        responses.GET,
        "https://www.omdbapi.com/?s=keanu&type=movie&apikey=test-key",
        json={"Response": "True", "Search": [{"Title": "A", "Year": "2001"}]},
        status=200,
    )
    settings = Settings(omdb_api_key="test-key")
    http = HttpClient(settings)
    api = OmdbApi(http, settings)
    results = api.search_by_actor("keanu")
    assert len(results) == 1
    assert results[0].title == "A"


@responses.activate
def test_omdb_api_bad_payload_raises() -> None:
    responses.add(
        responses.GET,
        "https://www.omdbapi.com/?t=x&apikey=test-key",
        json=["not-an-object"],
        status=200,
    )
    settings = Settings(omdb_api_key="test-key")
    http = HttpClient(settings)
    api = OmdbApi(http, settings)
    with pytest.raises(ApiResponseError):
        api.search_by_title("x")


@responses.activate
def test_tvmaze_api_search_returns_series() -> None:
    responses.add(
        responses.GET,
        "https://api.tvmaze.com/search/shows?q=dark",
        json=[{"score": 1.0, "show": {"id": 1, "name": "Dark"}}],
        status=200,
    )
    settings = Settings(omdb_api_key="test-key")
    http = HttpClient(settings)
    api = TvmazeApi(http, settings)
    results = api.search("dark")
    assert len(results) == 1
    assert results[0].name == "Dark"


@responses.activate
def test_tvmaze_api_get_by_id_returns_series() -> None:
    responses.add(
        responses.GET,
        "https://api.tvmaze.com/shows/1",
        json={"id": 1, "name": "Dark", "status": "Ended"},
        status=200,
    )
    settings = Settings(omdb_api_key="test-key")
    http = HttpClient(settings)
    api = TvmazeApi(http, settings)
    result = api.get_by_id(1)
    assert result.id == 1
    assert result.name == "Dark"


@responses.activate
def test_tvmaze_api_bad_payload_raises() -> None:
    responses.add(
        responses.GET,
        "https://api.tvmaze.com/search/shows?q=x",
        json={"not": "a-list"},
        status=200,
    )
    settings = Settings(omdb_api_key="test-key")
    http = HttpClient(settings)
    api = TvmazeApi(http, settings)
    with pytest.raises(ApiResponseError):
        api.search("x")


@responses.activate
def test_omdb_api_404_raises_resource_not_found() -> None:
    responses.add(
        responses.GET,
        "https://www.omdbapi.com/?t=x&apikey=test-key",
        status=404,
    )
    settings = Settings(omdb_api_key="test-key")
    http = HttpClient(settings)
    api = OmdbApi(http, settings)
    with pytest.raises(ResourceNotFoundError):
        api.search_by_title("x")


@responses.activate
def test_omdb_api_500_retries() -> None:
    responses.add(
        responses.GET,
        "https://www.omdbapi.com/?t=x&apikey=test-key",
        status=500,
    )
    responses.add(
        responses.GET,
        "https://www.omdbapi.com/?t=x&apikey=test-key",
        json={"Response": "True", "Title": "A", "Year": "2000"},
        status=200,
    )
    settings = Settings(omdb_api_key="test-key", max_retries=1, backoff_factor=0.0)
    http = HttpClient(settings)
    api = OmdbApi(http, settings)
    result = api.search_by_title("x")
    assert result is not None
    assert result.title == "A"
    assert len(responses.calls) == 2
