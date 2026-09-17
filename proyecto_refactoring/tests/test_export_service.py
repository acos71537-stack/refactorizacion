"""Tests del servicio de exportacion e importacion."""

from __future__ import annotations

from pathlib import Path

import pytest

from movies_app.exceptions import PersistenceError
from movies_app.models.movie import Movie
from movies_app.models.search import SearchEntry
from movies_app.repositories.favorites import FavoritesRepository
from movies_app.repositories.history import HistoryRepository
from movies_app.services.export_service import ExportService


def test_export_import_roundtrip(
    favorites: FavoritesRepository,
    history: HistoryRepository,
    tmp_path: Path,
) -> None:
    favorites.add(Movie(title="A", year=2000))
    history.add(SearchEntry("q", 1, "movie"))
    exporter = ExportService(favorites, history)
    path = tmp_path / "dump.json"

    exporter.export_json(path)
    assert path.exists()

    favorites.remove("A")
    history.clear()
    exporter.import_json(path)

    assert favorites.load()[0].title == "A"
    assert history.load()[0].query == "q"


def test_import_missing_file_raises(
    favorites: FavoritesRepository, history: HistoryRepository, tmp_path: Path
) -> None:
    with pytest.raises(PersistenceError):
        ExportService(favorites, history).import_json(tmp_path / "nope.json")


def test_import_invalid_json_raises(
    favorites: FavoritesRepository, history: HistoryRepository, tmp_path: Path
) -> None:
    path = tmp_path / "bad.json"
    path.write_text("no-json", encoding="utf-8")
    with pytest.raises(PersistenceError):
        ExportService(favorites, history).import_json(path)


def test_import_non_object_raises(
    favorites: FavoritesRepository, history: HistoryRepository, tmp_path: Path
) -> None:
    path = tmp_path / "arr.json"
    path.write_text("[1, 2, 3]", encoding="utf-8")
    with pytest.raises(PersistenceError):
        ExportService(favorites, history).import_json(path)


def test_import_ignores_non_list_sections(
    favorites: FavoritesRepository, history: HistoryRepository, tmp_path: Path
) -> None:
    path = tmp_path / "partial.json"
    path.write_text('{"favorites": "oops", "history": []}', encoding="utf-8")
    ExportService(favorites, history).import_json(path)
    assert favorites.load() == []
