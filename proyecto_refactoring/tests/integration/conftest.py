"""Fixtures para tests de integracion."""

from __future__ import annotations

from pathlib import Path

import pytest

from movies_app.config import Settings
from movies_app.repositories.favorites import FavoritesRepository
from movies_app.repositories.history import HistoryRepository
from movies_app.services.export_service import ExportService
from movies_app.services.movie_service import MovieService
from movies_app.services.series_service import SeriesService
from movies_app.ui.display import DisplayRenderer
from movies_app.ui.menu import MenuApp
from tests.fakes import StubMovieCatalog, StubSeriesCatalog


@pytest.fixture
def integration_settings(tmp_path: Path) -> Settings:
    return Settings(
        omdb_api_key="test-key",
        data_dir=tmp_path / "data",
        max_retries=0,
        backoff_factor=0.0,
    )


@pytest.fixture
def full_app(
    integration_settings: Settings,
    tmp_path: Path,
) -> MenuApp:
    favorites = FavoritesRepository(tmp_path / "favorites.json")
    history = HistoryRepository(tmp_path / "history.json", max_entries=100)
    movies = MovieService(StubMovieCatalog(), favorites, history)
    series = SeriesService(StubSeriesCatalog(), history)
    export = ExportService(favorites, history)
    return MenuApp(movies, series, export, DisplayRenderer(), input_func=lambda _: "")


@pytest.fixture
def exporter(
    integration_settings: Settings,
    tmp_path: Path,
) -> ExportService:
    favorites = FavoritesRepository(tmp_path / "favorites.json")
    history = HistoryRepository(tmp_path / "history.json")
    return ExportService(favorites, history)
