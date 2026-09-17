"""Repositorios de persistencia."""

from __future__ import annotations

from movies_app.repositories.base import JsonRepository
from movies_app.repositories.favorites import FavoritesRepository
from movies_app.repositories.history import HistoryRepository

__all__ = ["FavoritesRepository", "HistoryRepository", "JsonRepository"]
