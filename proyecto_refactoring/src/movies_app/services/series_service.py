"""Servicio de negocio para series."""

from __future__ import annotations

from movies_app import constants
from movies_app.logging_config import get_logger
from movies_app.models.search import SearchEntry
from movies_app.models.series import Series
from movies_app.protocols import SeriesCatalog
from movies_app.repositories.history import HistoryRepository

_logger = get_logger("series_service")


class SeriesService:
    """Orquesta busqueda y detalle de series.

    Attributes:
        catalog: Fuente de datos de series (TVMaze u otro).
    """

    def __init__(self, catalog: SeriesCatalog, history: HistoryRepository) -> None:
        self._catalog = catalog
        self._history = history

    def search(self, name: str) -> list[Series]:
        """Busca series por nombre y registra la busqueda.

        Args:
            name: Nombre a buscar.

        Returns:
            Lista de series encontradas (puede estar vacia).
        """
        series = self._catalog.search(name)
        _logger.debug("Busqueda de serie '%s': %d resultados", name, len(series))
        self._history.add(SearchEntry(name, len(series), constants.SEARCH_TYPE_SERIES))
        return series

    def get(self, series_id: int) -> Series:
        """Obtiene el detalle de una serie por su id.

        Args:
            series_id: Identificador de TVMaze.

        Returns:
            La serie solicitada.
        """
        return self._catalog.get_by_id(series_id)
