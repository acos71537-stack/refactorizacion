"""Tests del servicio de series."""

from __future__ import annotations

import pytest

from movies_app.exceptions import InvalidInputError, SeriesNotFoundError
from movies_app.models.series import Series
from movies_app.repositories.history import HistoryRepository
from movies_app.services.series_service import SeriesService
from tests.fakes import StubSeriesCatalog


def test_search_records_history(history: HistoryRepository) -> None:
    catalog = StubSeriesCatalog([Series(id=1, name="A")])
    service = SeriesService(catalog, history)

    result = service.search("A")

    assert [series.name for series in result] == ["A"]
    assert history.load()[0].search_type == "series"


def test_get_returns_detail(history: HistoryRepository) -> None:
    catalog = StubSeriesCatalog([Series(id=9, name="Detail")])
    service = SeriesService(catalog, history)
    assert service.get(9).name == "Detail"


def test_get_missing_series_raises(history: HistoryRepository) -> None:
    service = SeriesService(StubSeriesCatalog([]), history)
    with pytest.raises(SeriesNotFoundError, match="404"):
        service.get(404)


def test_search_without_results(history: HistoryRepository) -> None:
    service = SeriesService(StubSeriesCatalog([]), history)
    assert service.search("nada") == []


def test_empty_name_raises_invalid_input(history: HistoryRepository) -> None:
    service = SeriesService(StubSeriesCatalog([]), history)
    with pytest.raises(InvalidInputError, match="serie"):
        service.search("   ")
