"""Modelo para entradas del historial de busquedas."""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any

from movies_app import constants
from movies_app.models._parsing import clean_str, parse_int


def _utc_now() -> datetime:
    return datetime.now()


@dataclass(frozen=True, slots=True)
class SearchEntry:
    """Registro de una busqueda realizada por el usuario.

    Attributes:
        query: Texto buscado.
        results_count: Cantidad de resultados obtenidos.
        search_type: Tipo de busqueda (``"movie"``, ``"series"``, ``"actor"``).
        timestamp: Momento en que se realizo la busqueda.
    """

    query: str
    results_count: int = 0
    search_type: str = constants.SEARCH_TYPE_MOVIE
    timestamp: datetime = field(default_factory=_utc_now)

    def to_dict(self) -> dict[str, Any]:
        """Serializa la entrada a un diccionario JSON-compatible."""
        return {
            "query": self.query,
            "results_count": self.results_count,
            "search_type": self.search_type,
            "timestamp": self.timestamp.isoformat(),
        }

    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> SearchEntry:
        """Reconstruye una ``SearchEntry`` desde ``to_dict``.

        Args:
            data: Diccionario previamente serializado.

        Returns:
            La entrada reconstruida.
        """
        raw_timestamp = clean_str(data.get("timestamp"))
        try:
            timestamp = datetime.fromisoformat(raw_timestamp) if raw_timestamp else _utc_now()
        except ValueError:
            timestamp = _utc_now()
        return cls(
            query=clean_str(data.get("query")) or "",
            results_count=parse_int(data.get("results_count")) or 0,
            search_type=clean_str(data.get("search_type")) or constants.SEARCH_TYPE_MOVIE,
            timestamp=timestamp,
        )
