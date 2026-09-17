"""Fixtures compartidas de la suite de tests."""

from __future__ import annotations

from pathlib import Path

import pytest

from movies_app.config import Settings
from movies_app.repositories.favorites import FavoritesRepository
from movies_app.repositories.history import HistoryRepository


@pytest.fixture
def settings(tmp_path: Path) -> Settings:
    """Configuracion de prueba sin reintentos ni esperas."""
    return Settings(
        omdb_api_key="test-key",
        data_dir=tmp_path / "data",
        max_retries=0,
        backoff_factor=0.0,
    )


@pytest.fixture
def favorites(tmp_path: Path) -> FavoritesRepository:
    """Repositorio de favoritos aislado en un directorio temporal."""
    return FavoritesRepository(tmp_path / "favorites.json")


@pytest.fixture
def history(tmp_path: Path) -> HistoryRepository:
    """Repositorio de historial aislado, limitado a 3 entradas."""
    return HistoryRepository(tmp_path / "history.json", max_entries=3)
