"""Tests de los modelos de dominio."""

from __future__ import annotations

from datetime import datetime

import pytest

from movies_app.models.movie import Movie
from movies_app.models.search import SearchEntry
from movies_app.models.series import Series


def test_movie_from_omdb_parses_fields() -> None:
    movie = Movie.from_omdb(
        {"Title": "Inception", "Year": "2010", "imdbRating": "8.8", "Genre": "Sci-Fi"}
    )
    assert movie.title == "Inception"
    assert movie.year == 2010
    assert movie.imdb_rating == 8.8
    assert movie.genre == "Sci-Fi"


def test_movie_from_omdb_handles_not_available() -> None:
    movie = Movie.from_omdb({"Title": "X", "Year": "N/A", "imdbRating": "N/A"})
    assert movie.year is None
    assert movie.imdb_rating is None


def test_movie_from_omdb_parses_year_range() -> None:
    assert Movie.from_omdb({"Title": "X", "Year": "1994-1995"}).year == 1994


def test_movie_missing_title_defaults() -> None:
    assert Movie.from_omdb({}).title == "N/A"


def test_movie_roundtrip() -> None:
    movie = Movie(title="A", year=2000, imdb_rating=7.5, genre="Drama")
    assert Movie.from_dict(movie.to_dict()) == movie


def test_series_from_tvmaze() -> None:
    series = Series.from_tvmaze(
        {
            "id": 5,
            "name": "Dark",
            "genres": ["Drama", "Sci-Fi"],
            "rating": {"average": 8.8},
            "runtime": 60,
            "premiered": "2017-12-01",
        }
    )
    assert series.id == 5
    assert series.genres == ("Drama", "Sci-Fi")
    assert series.rating == 8.8
    assert series.runtime == 60


def test_series_from_search_result() -> None:
    series = Series.from_search_result({"score": 1.0, "show": {"id": 1, "name": "Show"}})
    assert series.name == "Show"


def test_series_from_search_result_without_show_raises() -> None:
    with pytest.raises(ValueError, match="show"):
        Series.from_search_result({"score": 1.0})


def test_series_without_id_raises() -> None:
    with pytest.raises(ValueError, match="id"):
        Series.from_tvmaze({"name": "Sin id"})


def test_series_roundtrip() -> None:
    series = Series(id=2, name="B", genres=("Drama",), rating=7.0)
    assert Series.from_dict(series.to_dict()) == series


def test_search_entry_roundtrip() -> None:
    entry = SearchEntry("matrix", 3, "movie", datetime(2026, 1, 2, 3, 4, 5))
    assert SearchEntry.from_dict(entry.to_dict()) == entry


def test_search_entry_invalid_timestamp_falls_back() -> None:
    entry = SearchEntry.from_dict({"query": "q", "timestamp": "no-es-fecha"})
    assert entry.query == "q"
    assert isinstance(entry.timestamp, datetime)
