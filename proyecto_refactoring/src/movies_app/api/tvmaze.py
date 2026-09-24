"""Logica de la API TVMaze.

Transforma las respuestas de TVMaze en modelos de dominio (Series).
Depende de clients.base.HttpClient para el transporte y de models para el mapeo.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence

from movies_app.clients.base import HttpClient
from movies_app.config import Settings
from movies_app.exceptions import ApiResponseError, ResourceNotFoundError
from movies_app.logging_config import get_logger
from movies_app.models.series import Series
from movies_app.protocols import SeriesCatalog

_logger = get_logger("tvmaze")


class TvmazeApi(SeriesCatalog):
    """Fuente de datos de series respaldada por TVMaze.

    Implementa el protocolo ``SeriesCatalog``.

    Attributes:
        http: Cliente HTTP para realizar peticiones.
        settings: Configuracion con la URL base de TVMaze.
    """

    def __init__(self, http: HttpClient, settings: Settings) -> None:
        self._http = http
        self._settings = settings

    def search(self, name: str) -> list[Series]:
        """Busca series por nombre.

        Args:
            name: Nombre a buscar.

        Returns:
            Lista de series encontradas (puede estar vacia).

        Raises:
            ApiResponseError: Si la respuesta de TVMaze no es una lista JSON.
        """
        query = name.strip()
        if not query:
            return []
        payload = self._http.get_json(
            f"{self._settings.tvmaze_base_url}/search/shows", params={"q": query}
        )
        if not isinstance(payload, Sequence) or isinstance(payload, (str, bytes)):
            raise ApiResponseError("TVMaze devolvio un payload inesperado al buscar series")

        series: list[Series] = []
        for item in payload:
            if not isinstance(item, Mapping):
                continue
            try:
                series.append(Series.from_search_result(item))
            except ValueError as exc:
                _logger.warning("Resultado de TVMaze invalido, se omite: %s", exc)
        return series

    def get_by_id(self, series_id: int) -> Series | None:
        """Obtiene el detalle de una serie por su id.

        Args:
            series_id: Identificador de TVMaze.

        Returns:
            La serie solicitada o ``None`` si no existe.

        Raises:
            ApiResponseError: Si la respuesta no es un objeto JSON valido.
            ValueError: Si el payload no contiene un ``id`` valido.
        """
        try:
            payload = self._http.get_json(f"{self._settings.tvmaze_base_url}/shows/{series_id}")
        except ResourceNotFoundError:
            return None
        if not isinstance(payload, Mapping):
            raise ApiResponseError(
                f"TVMaze devolvio un payload inesperado para el show {series_id}"
            )
        return Series.from_tvmaze(payload)
