"""Tests del cliente HTTP (reintentos, timeouts y traduccion de errores)."""

from __future__ import annotations

import pytest
import requests
import responses

from movies_app.clients.base import HttpClient
from movies_app.config import Settings
from movies_app.exceptions import (
    ApiConnectionError,
    ApiResponseError,
    ApiTimeoutError,
    ResourceNotFoundError,
)

URL = "https://example.test/resource"


@responses.activate
def test_get_json_success(settings: Settings) -> None:
    responses.add(responses.GET, URL, json={"ok": True})
    assert HttpClient(settings).get_json(URL) == {"ok": True}


@responses.activate
def test_get_json_sends_params(settings: Settings) -> None:
    responses.add(responses.GET, URL, json={})
    HttpClient(settings).get_json(URL, params={"a": "b"})
    assert responses.calls[0].request.url == f"{URL}?a=b"


@responses.activate
def test_get_json_404_raises_not_found(settings: Settings) -> None:
    responses.add(responses.GET, URL, status=404)
    with pytest.raises(ResourceNotFoundError):
        HttpClient(settings).get_json(URL)


@responses.activate
def test_get_json_client_error_is_not_retried(settings: Settings) -> None:
    responses.add(responses.GET, URL, status=400)
    with pytest.raises(ApiResponseError) as excinfo:
        HttpClient(settings).get_json(URL)
    assert excinfo.value.status_code == 400
    assert len(responses.calls) == 1


@responses.activate
def test_get_json_retries_on_5xx() -> None:
    settings = Settings(omdb_api_key="k", max_retries=1, backoff_factor=0.0)
    responses.add(responses.GET, URL, status=503)
    responses.add(responses.GET, URL, json={"ok": 1})
    assert HttpClient(settings).get_json(URL) == {"ok": 1}
    assert len(responses.calls) == 2


@responses.activate
def test_get_json_exhausts_retries() -> None:
    settings = Settings(omdb_api_key="k", max_retries=2, backoff_factor=0.0)
    for _ in range(3):
        responses.add(responses.GET, URL, status=500)
    with pytest.raises(ApiResponseError):
        HttpClient(settings).get_json(URL)
    assert len(responses.calls) == 3


@responses.activate
def test_get_json_timeout(settings: Settings) -> None:
    responses.add(responses.GET, URL, body=requests.Timeout("boom"))
    with pytest.raises(ApiTimeoutError):
        HttpClient(settings).get_json(URL)


@responses.activate
def test_get_json_connection_error(settings: Settings) -> None:
    responses.add(responses.GET, URL, body=requests.ConnectionError("down"))
    with pytest.raises(ApiConnectionError):
        HttpClient(settings).get_json(URL)


@responses.activate
def test_get_json_non_json_body(settings: Settings) -> None:
    responses.add(responses.GET, URL, body="<html></html>")
    with pytest.raises(ApiResponseError):
        HttpClient(settings).get_json(URL)
