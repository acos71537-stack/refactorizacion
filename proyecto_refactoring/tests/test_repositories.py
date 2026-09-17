"""Tests de los repositorios de persistencia."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from movies_app.exceptions import PersistenceError
from movies_app.models.movie import Movie
from movies_app.models.search import SearchEntry
from movies_app.repositories.base import JsonRepository
from movies_app.repositories.favorites import FavoritesRepository
from movies_app.repositories.history import HistoryRepository


def _movie_repo(path: Path) -> JsonRepository[Movie]:
    return JsonRepository(path, Movie.to_dict, Movie.from_dict)


def test_json_repository_empty_when_missing(tmp_path: Path) -> None:
    assert _movie_repo(tmp_path / "none.json").load() == []


def test_json_repository_roundtrip(tmp_path: Path) -> None:
    repo = _movie_repo(tmp_path / "movies.json")
    repo.save([Movie(title="A", year=2000), Movie(title="B")])
    assert [movie.title for movie in repo.load()] == ["A", "B"]


def test_json_repository_invalid_json_raises(tmp_path: Path) -> None:
    path = tmp_path / "bad.json"
    path.write_text("{not-json", encoding="utf-8")
    with pytest.raises(PersistenceError):
        _movie_repo(path).load()


def test_json_repository_non_list_raises(tmp_path: Path) -> None:
    path = tmp_path / "obj.json"
    path.write_text('{"a": 1}', encoding="utf-8")
    with pytest.raises(PersistenceError):
        _movie_repo(path).load()


def test_json_repository_skips_corrupt_entries(tmp_path: Path) -> None:
    path = tmp_path / "mix.json"
    path.write_text(json.dumps([{"title": "A"}, 42, {"title": "B"}]), encoding="utf-8")
    assert [movie.title for movie in _movie_repo(path).load()] == ["A", "B"]


def test_favorites_add_and_remove(favorites: FavoritesRepository) -> None:
    movie = Movie(title="A")
    assert favorites.add(movie) is True
    assert favorites.add(movie) is False
    assert favorites.contains("A") is True
    assert favorites.remove("A") is True
    assert favorites.remove("A") is False
    assert favorites.load() == []


def test_history_respects_limit(history: HistoryRepository) -> None:
    for index in range(5):
        history.add(SearchEntry(f"q{index}", index, "movie"))
    entries = history.load()
    assert len(entries) == 3
    assert entries[0].query == "q4"


def test_history_clear(history: HistoryRepository) -> None:
    history.add(SearchEntry("q"))
    history.clear()
    assert history.load() == []


def test_history_rejects_invalid_limit(tmp_path: Path) -> None:
    with pytest.raises(ValueError, match="max_entries"):
        HistoryRepository(tmp_path / "h.json", max_entries=0)
