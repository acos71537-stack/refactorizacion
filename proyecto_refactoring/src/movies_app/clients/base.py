"""Cliente HTTP con timeout, reintentos con backoff y traduccion de errores."""

from __future__ import annotations

import time
from collections.abc import Mapping
from typing import Any

import requests

from movies_app.config import Settings
from movies_app.exceptions import (
    ApiConnectionError,
    ApiError,
    ApiResponseError,
    ApiTimeoutError,
    ResourceNotFoundError,
)
from movies_app.logging_config import get_logger

_logger = get_logger("http")

_RETRYABLE_STATUS = 500


class HttpClient:
    """Envoltorio de ``requests`` con politica de reintentos.

    Attributes:
        settings: Configuracion usada para timeout y reintentos.
    """

    def __init__(self, settings: Settings, session: requests.Session | None = None) -> None:
        self._settings = settings
        self._session = session if session is not None else requests.Session()

    def get_json(
        self,
        url: str,
        params: Mapping[str, str] | None = None,
    ) -> Any:
        """Ejecuta un GET y devuelve el JSON parseado.

        Reintenta ante timeouts, errores de conexion y respuestas 5xx, con
        backoff exponencial. Los errores 4xx (excepto 404) no se reintentan.

        Args:
            url: URL absoluta del recurso.
            params: Parametros de query opcionales.

        Returns:
            El cuerpo de la respuesta parseado como JSON.

        Raises:
            ApiTimeoutError: Si se agota el tiempo de espera.
            ApiConnectionError: Si no hay conectividad.
            ResourceNotFoundError: Si la respuesta es 404.
            ApiResponseError: Si el status o el JSON no son validos.
        """
        attempts = self._settings.max_retries + 1
        last_error: ApiError | None = None

        for attempt in range(attempts):
            _logger.debug("GET %s (intento %d/%d) params=%s", url, attempt + 1, attempts, params)
            try:
                response = self._session.get(
                    url, params=dict(params) if params else None, timeout=self._settings.timeout
                )
            except requests.Timeout as exc:
                last_error = ApiTimeoutError(f"Timeout al solicitar {url}: {exc}")
            except requests.RequestException as exc:
                last_error = ApiConnectionError(f"Error de conexion a {url}: {exc}")
            else:
                if response.status_code == 404:
                    raise ResourceNotFoundError(f"Recurso no encontrado: {url}")
                if response.status_code >= _RETRYABLE_STATUS:
                    last_error = ApiResponseError(
                        f"HTTP {response.status_code} al solicitar {url}",
                        status_code=response.status_code,
                    )
                elif not response.ok:
                    raise ApiResponseError(
                        f"HTTP {response.status_code} al solicitar {url}",
                        status_code=response.status_code,
                    )
                else:
                    try:
                        return response.json()
                    except ValueError as exc:
                        raise ApiResponseError(f"Respuesta no-JSON de {url}") from exc

            if attempt < attempts - 1:
                delay = self._settings.backoff_factor * (2**attempt)
                _logger.warning("Reintentando %s en %.2fs: %s", url, delay, last_error)
                if delay > 0:
                    time.sleep(delay)

        if last_error is None:
            last_error = ApiConnectionError(f"No se pudo completar la peticion a {url}")
        raise last_error
