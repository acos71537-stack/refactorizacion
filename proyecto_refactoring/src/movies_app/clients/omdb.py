"""Cliente de la API OMDB."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Any

from movies_app.config import Settings
from movies_app.exceptions import ApiResponseError
from movies_app.logging_config import get_logger
from movies_app.models.movie import Movie
from movies_app.protocols import JsonClient

_logger = get_logger("omdb")


class OmdbClient:
    """Fuente de datos de peliculas respaldada por OMDB.

    Implementa el protocolo ``MovieCatalog``.

    Attributes:
        settings: Configuracion con la clave y URL base de OMDB.
    """

    def __init__(self, http: JsonClient, settings: Settings) -> None:
        self._http = http
        self._settings = settings

    def search_by_title(self, title: str) -> Movie | None:
        """Busca una pelicula por titulo.

        Args:
            title: Titulo a buscar.

        Returns:
            La pelicula encontrada o ``None`` si no existe.

        Raises:
            ApiResponseError: Si la respuesta de OMDB no es un objeto JSON.
        """
        query = title.strip()
        if not query:
            return None
        payload = self._http.get_json(
            self._settings.omdb_base_url,
            params={"t": query, "apikey": self._settings.omdb_api_key},
        )
        if not isinstance(payload, Mapping):
            raise ApiResponseError("OMDB devolvio un payload inesperado al buscar por titulo")
        if not _omdb_success(payload):
            _logger.debug("OMDB sin resultados para %r: %s", query, payload.get("Error"))
            return None
        return Movie.from_omdb(payload)

    def search_by_actor(self, actor: str) -> list[Movie]:
        """Busca peliculas en las que participa un actor.

        Args:
            actor: Nombre del actor.

        Returns:
            Lista de peliculas (puede estar vacia).

        Raises:
            ApiResponseError: Si la respuesta de OMDB no es un objeto JSON.
        """
        query = actor.strip()
        if not query:
            return []
        payload = self._http.get_json(
            self._settings.omdb_base_url,
            params={"s": query, "type": "movie", "apikey": self._settings.omdb_api_key},
        )
        if not isinstance(payload, Mapping):
            raise ApiResponseError("OMDB devolvio un payload inesperado al buscar por actor")
        if not _omdb_success(payload):
            return []
        results = payload.get("Search")
        if not isinstance(results, Sequence) or isinstance(results, (str, bytes)):
            return []
        return [Movie.from_omdb(item) for item in results if isinstance(item, Mapping)]


def _omdb_success(payload: Mapping[str, Any]) -> bool:
    return str(payload.get("Response", "")).strip().lower() == "true"
