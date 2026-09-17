"""Repositorio del historial de busquedas."""

from __future__ import annotations

from pathlib import Path

from movies_app import constants
from movies_app.models.search import SearchEntry
from movies_app.repositories.base import JsonRepository


class HistoryRepository:
    """Persistencia del historial de busquedas, limitado a un maximo.

    Attributes:
        max_entries: Numero maximo de entradas conservadas.
    """

    def __init__(self, path: Path, max_entries: int = constants.DEFAULT_MAX_HISTORY) -> None:
        if max_entries <= 0:
            raise ValueError(f"max_entries debe ser > 0, recibido: {max_entries}")
        self._repo: JsonRepository[SearchEntry] = JsonRepository(
            path, SearchEntry.to_dict, SearchEntry.from_dict
        )
        self._max_entries = max_entries

    @property
    def max_entries(self) -> int:
        """Maximo de entradas configurado."""
        return self._max_entries

    def load(self) -> list[SearchEntry]:
        """Devuelve el historial (mas reciente primero)."""
        return self._repo.load()

    def save(self, items: list[SearchEntry]) -> None:
        """Persiste el historial completo."""
        self._repo.save(items)

    def add(self, entry: SearchEntry) -> None:
        """Agrega una entrada al inicio, respetando el limite.

        Args:
            entry: Entrada de busqueda a registrar.
        """
        entries = [entry, *self.load()][: self._max_entries]
        self._repo.save(entries)

    def clear(self) -> None:
        """Vacia el historial."""
        self._repo.save([])
