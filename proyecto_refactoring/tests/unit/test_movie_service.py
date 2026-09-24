"""Tests del servicio de peliculas."""

from __future__ import annotations

import pytest

from movies_app.exceptions import InvalidInputError
from movies_app.models.movie import Movie
from movies_app.repositories.favorites import FavoritesRepository
from movies_app.repositories.history import HistoryRepository
from movies_app.services.movie_service import MovieService
from tests.fakes import StubMovieCatalog


def test_search_by_title_uses_cache(
    favorites: FavoritesRepository, history: HistoryRepository
) -> None:
    catalog = StubMovieCatalog({"Matrix": Movie(title="The Matrix")})
    service = MovieService(catalog, favorites, history)

    first = service.search_by_title("Matrix")
    second = service.search_by_title("matrix")

    assert first is not None and first.title == "The Matrix"
    assert second == first
    assert catalog.title_calls == 1


def test_search_records_history(favorites: FavoritesRepository, history: HistoryRepository) -> None:
    catalog = StubMovieCatalog({"X": Movie(title="X")})
    service = MovieService(catalog, favorites, history)

    service.search_by_title("X")
    service.search_by_title("missing")

    entries = service.history()
    assert len(entries) == 2
    assert entries[0].results_count == 0
    assert entries[1].results_count == 1


def test_empty_title_raises_invalid_input(
    favorites: FavoritesRepository, history: HistoryRepository
) -> None:
    catalog = StubMovieCatalog()
    service = MovieService(catalog, favorites, history)
    with pytest.raises(InvalidInputError, match="titulo"):
        service.search_by_title("   ")
    assert catalog.title_calls == 0


def test_empty_actor_raises_invalid_input(
    favorites: FavoritesRepository, history: HistoryRepository
) -> None:
    service = MovieService(StubMovieCatalog(), favorites, history)
    with pytest.raises(InvalidInputError, match="actor"):
        service.search_by_actor("   ")


def test_empty_genre_raises_invalid_input(
    favorites: FavoritesRepository, history: HistoryRepository
) -> None:
    service = MovieService(StubMovieCatalog(), favorites, history)
    with pytest.raises(InvalidInputError, match="genero"):
        service.movies_by_genre("   ")


def test_favorites_flow(favorites: FavoritesRepository, history: HistoryRepository) -> None:
    service = MovieService(StubMovieCatalog(), favorites, history)
    movie = Movie(title="A")

    assert service.add_favorite(movie) is True
    assert service.favorites()[0].title == "A"
    assert service.remove_favorite("A") is True
    assert service.favorites() == []


def test_popular_movies_returns_curated(
    favorites: FavoritesRepository, history: HistoryRepository
) -> None:
    service = MovieService(StubMovieCatalog(), favorites, history)
    assert len(service.popular_movies()) == 5


def test_movies_by_genre_and_fallback(
    favorites: FavoritesRepository, history: HistoryRepository
) -> None:
    service = MovieService(StubMovieCatalog(), favorites, history)
    assert len(service.movies_by_genre("accion")) == 2
    assert len(service.movies_by_genre("desconocido")) == 4


def test_stats_counts(favorites: FavoritesRepository, history: HistoryRepository) -> None:
    service = MovieService(StubMovieCatalog(), favorites, history)
    service.add_favorite(Movie(title="A"))
    service.search_by_actor("x")

    assert service.stats() == {"total_favoritas": 1, "total_historial": 1}


def test_clear_history(favorites: FavoritesRepository, history: HistoryRepository) -> None:
    service = MovieService(StubMovieCatalog(), favorites, history)
    service.search_by_actor("x")
    service.clear_history()
    assert service.history() == []
