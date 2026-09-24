"""Jerarquia de excepciones de dominio de la aplicacion.

Clases base (base.py) y excepciones especificas para peliculas,
series, entradas invalidas y operaciones de exportacion.
"""

from __future__ import annotations

from movies_app.exceptions.base import (
    ApiConnectionError,
    ApiError,
    ApiResponseError,
    ApiTimeoutError,
    MoviesAppError,
    PersistenceError,
    ResourceNotFoundError,
)
from movies_app.exceptions.export_error import ExportError
from movies_app.exceptions.invalid_input import InvalidInputError
from movies_app.exceptions.movie_not_found import MovieNotFoundError
from movies_app.exceptions.series_not_found import SeriesNotFoundError

__all__ = [
    "ApiConnectionError",
    "ApiError",
    "ApiResponseError",
    "ApiTimeoutError",
    "ExportError",
    "InvalidInputError",
    "MovieNotFoundError",
    "MoviesAppError",
    "PersistenceError",
    "ResourceNotFoundError",
    "SeriesNotFoundError",
]
