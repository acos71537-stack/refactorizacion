"""Tests del cliente de TVMaze."""

from __future__ import annotations

import pytest

from movies_app.api.tvmaze import TvmazeApi
from movies_app.config import Settings
from movies_app.exceptions import ApiResponseError
from tests.fakes import FakeJsonClient


def test_search_returns_series(settings: Settings) -> None:
    client = FakeJsonClient(
        [
            [
                {"score": 1.0, "show": {"id": 1, "name": "A"}},
                {"score": 0.5, "show": {"id": 2, "name": "B"}},
            ]
        ]
    )
    result = TvmazeApi(client, settings).search("a")  # type: ignore[arg-type]
    assert [series.name for series in result] == ["A", "B"]
    assert client.calls[0][0].endswith("/search/shows")
    assert client.calls[0][1] == {"q": "a"}


def test_search_empty_query_skips_call(settings: Settings) -> None:
    client = FakeJsonClient([])
    assert TvmazeApi(client, settings).search("  ") == []  # type: ignore[arg-type]
    assert client.calls == []


def test_search_skips_invalid_items(settings: Settings) -> None:
    client = FakeJsonClient(
        [
            [
                {"score": 1.0, "show": {"name": "sin id"}},
                {"score": 1.0, "show": {"id": 3, "name": "Ok"}},
            ]
        ]
    )
    result = TvmazeApi(client, settings).search("x")  # type: ignore[arg-type]
    assert [series.name for series in result] == ["Ok"]


def test_search_bad_payload_raises(settings: Settings) -> None:
    client = FakeJsonClient([{"no": "es-lista"}])
    with pytest.raises(ApiResponseError):
        TvmazeApi(client, settings).search("x")  # type: ignore[arg-type]


def test_get_by_id_returns_series(settings: Settings) -> None:
    client = FakeJsonClient([{"id": 7, "name": "Show"}])
    assert TvmazeApi(client, settings).get_by_id(7).id == 7  # type: ignore[arg-type]


def test_get_by_id_bad_payload_raises(settings: Settings) -> None:
    client = FakeJsonClient([[1, 2, 3]])
    with pytest.raises(ApiResponseError):
        TvmazeApi(client, settings).get_by_id(1)  # type: ignore[arg-type]
