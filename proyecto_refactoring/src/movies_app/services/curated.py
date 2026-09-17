"""Datos curados usados como respaldo cuando no se consulta una API real.

Reemplaza las listas hardcodeadas de ``obtener_peliculas_populares`` y
``buscar_peliculas_por_genero`` de ``api_movies.py``.
"""

from __future__ import annotations

from movies_app import constants
from movies_app.models.movie import Movie

POPULAR_MOVIES: tuple[Movie, ...] = (
    Movie(title="The Shawshank Redemption", year=1994, imdb_rating=9.3),
    Movie(title="The Godfather", year=1972, imdb_rating=9.2),
    Movie(title="The Dark Knight", year=2008, imdb_rating=9.0),
    Movie(title="Pulp Fiction", year=1994, imdb_rating=8.9),
    Movie(title="Forrest Gump", year=1994, imdb_rating=8.8),
)

MOVIES_BY_GENRE: dict[str, tuple[Movie, ...]] = {
    constants.GENRE_ACTION: (
        Movie(title="Die Hard", year=1988, imdb_rating=8.2),
        Movie(title="Mad Max Fury Road", year=2015, imdb_rating=8.1),
    ),
    constants.GENRE_COMEDY: (
        Movie(title="Superbad", year=2007, imdb_rating=7.6),
        Movie(title="The Hangover", year=2009, imdb_rating=7.7),
    ),
}

ALL_CURATED_MOVIES: tuple[Movie, ...] = tuple(
    movie for movies in MOVIES_BY_GENRE.values() for movie in movies
)
