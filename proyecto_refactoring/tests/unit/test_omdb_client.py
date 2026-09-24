"""Tests del cliente de OMDB."""

from __future__ import annotations

import pytest

from movies_app.api.omdb import OmdbApi
from movies_app.config import Settings
from movies_app.exceptions import ApiResponseError
from tests.fakes import FakeJsonClient


def test_search_by_title_found(settings: Settings) -> None:
    client = FakeJsonClient([{"Response": "True", "Title": "Inception", "Year": "2010"}])
    movie = OmdbApi(client, settings).search_by_title("Inception")  # type: ignore[arg-type]
    assert movie is not None
    assert movie.title == "Inception"
    assert client.calls[0][1] == {"t": "Inception", "apikey": "test-key"}


def test_search_by_title_not_found(settings: Settings) -> None:
    client = FakeJsonClient([{"Response": "False", "Error": "Movie not found!"}])
    assert OmdbApi(client, settings).search_by_title("zzz") is None  # type: ignore[arg-type]


def test_search_by_title_empty_query_skips_call(settings: Settings) -> None:
    client = FakeJsonClient([])
    assert OmdbApi(client, settings).search_by_title("   ") is None  # type: ignore[arg-type]
    assert client.calls == []


def test_search_by_actor_returns_movies(settings: Settings) -> None:
    client = FakeJsonClient(
        [{"Response": "True", "Search": [{"Title": "A", "Year": "2001"}, {"Title": "B"}]}]
    )
    movies = OmdbApi(client, settings).search_by_actor("keanu")  # type: ignore[arg-type]
    assert [movie.title for movie in movies] == ["A", "B"]


def test_search_by_actor_no_results(settings: Settings) -> None:
    client = FakeJsonClient([{"Response": "False"}])
    assert OmdbApi(client, settings).search_by_actor("nadie") == []  # type: ignore[arg-type]


def test_search_by_actor_empty_query_skips_call(settings: Settings) -> None:
    client = FakeJsonClient([])
    assert OmdbApi(client, settings).search_by_actor("  ") == []  # type: ignore[arg-type]
    assert client.calls == []


def test_search_by_title_bad_payload_raises(settings: Settings) -> None:
    client = FakeJsonClient([["no-es-objeto"]])
    with pytest.raises(ApiResponseError):
        OmdbApi(client, settings).search_by_title("x")  # type: ignore[arg-type]


def test_search_by_actor_bad_payload_raises(settings: Settings) -> None:
    client = FakeJsonClient([["no-es-objeto"]])
    with pytest.raises(ApiResponseError):
        OmdbApi(client, settings).search_by_actor("x")  # type: ignore[arg-type]
