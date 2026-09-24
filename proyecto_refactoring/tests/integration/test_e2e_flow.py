"""Tests de flujo end-to-end completos."""

from __future__ import annotations

import io
import tempfile
from collections.abc import Callable
from pathlib import Path

import pytest

from movies_app import __main__ as entry
from movies_app.config import Settings
from movies_app.models.movie import Movie
from movies_app.models.search import SearchEntry
from movies_app.models.series import Series
from movies_app.repositories.favorites import FavoritesRepository
from movies_app.repositories.history import HistoryRepository
from movies_app.services.export_service import ExportService
from movies_app.services.movie_service import MovieService
from movies_app.services.series_service import SeriesService
from movies_app.ui.display import DisplayRenderer
from movies_app.ui.menu import MenuApp
from tests.fakes import StubMovieCatalog, StubSeriesCatalog


def _reader(values: list[str]) -> Callable[[str], str]:
    iterator = iter(values)

    def _read(_prompt: str) -> str:
        try:
            return next(iterator)
        except StopIteration:
            raise EOFError from None

    return _read


def _build_e2e_app(
    values: list[str],
    output: io.StringIO,
    tmp_path: Path,
    movie_catalog: StubMovieCatalog | None = None,
    series_catalog: StubSeriesCatalog | None = None,
) -> MenuApp:
    favorites = FavoritesRepository(tmp_path / "favorites.json")
    history = HistoryRepository(tmp_path / "history.json")
    movies = MovieService(movie_catalog or StubMovieCatalog(), favorites, history)
    series = SeriesService(series_catalog or StubSeriesCatalog(), history)
    export = ExportService(favorites, history)
    return MenuApp(movies, series, export, DisplayRenderer(output), input_func=_reader(values))


def test_e2e_search_movie_add_favorite_export(tmp_path: Path) -> None:
    output = io.StringIO()
    catalog = StubMovieCatalog({"Matrix": Movie(title="The Matrix", year=1999)})
    app = _build_e2e_app(
        ["1", "Matrix", "s", "", "9", "dump", "11"],
        output,
        tmp_path=tmp_path,
        movie_catalog=catalog,
    )
    app.run()
    content = output.getvalue()
    assert "The Matrix" in content
    assert "Agregada a favoritos!" in content


def test_e2e_search_series_add_favorite(tmp_path: Path) -> None:
    output = io.StringIO()
    series_catalog = StubSeriesCatalog([Series(id=1, name="Dark", status="Ended")])
    app = _build_e2e_app(
        ["3", "dark", "1", "", "11"],
        output,
        tmp_path=tmp_path,
        series_catalog=series_catalog,
    )
    app.run()
    content = output.getvalue()
    assert "Dark" in content


def test_e2e_empty_search_shows_error(tmp_path: Path) -> None:
    output = io.StringIO()
    app = _build_e2e_app(
        ["1", "", "11"],
        output,
        tmp_path=tmp_path,
    )
    app.run()
    content = output.getvalue()
    assert "Entrada invalida" in content


def test_e2e_full_flow_main_returns_zero(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("OMDB_API_KEY", "test-key")
    monkeypatch.setattr(MenuApp, "run", lambda self: None)
    assert entry.main() == 0


def test_e2e_main_keyboard_interrupt(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("OMDB_API_KEY", "test-key")
    monkeypatch.setattr(MenuApp, "run", lambda self: (_ for _ in ()).throw(KeyboardInterrupt))
    assert entry.main() == 130


def test_build_app_returns_menu(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("OMDB_API_KEY", "test-key")
    settings = Settings(omdb_api_key="test-key")
    app = entry.build_app(settings)
    assert isinstance(app, MenuApp)


def test_e2e_export_import_roundtrip() -> None:
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir)
        favorites = FavoritesRepository(tmp_path / "favorites.json")
        history = HistoryRepository(tmp_path / "history.json")
        export = ExportService(favorites, history)

        movie = Movie(title="Test Movie", year=2024)
        favorites.add(movie)
        history.add(SearchEntry("test", 1, "movie"))

        export_path = tmp_path / "test_export.json"
        export.export_json(export_path)
        assert export_path.exists()

        favorites.remove("Test Movie")
        history.clear()
        export.import_json(export_path)
        assert len(favorites.load()) == 1
        assert favorites.load()[0].title == "Test Movie"
