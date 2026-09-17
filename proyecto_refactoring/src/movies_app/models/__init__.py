"""Modelos de dominio de la aplicacion."""

from __future__ import annotations

from movies_app.models.movie import Movie
from movies_app.models.search import SearchEntry
from movies_app.models.series import Series

__all__ = ["Movie", "SearchEntry", "Series"]
