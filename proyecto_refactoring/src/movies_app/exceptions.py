"""Jerarquia de excepciones de dominio de la aplicacion."""

from __future__ import annotations


class MoviesAppError(Exception):
    """Excepcion base de la aplicacion."""


class ApiError(MoviesAppError):
    """Error generico al comunicarse con una API externa."""


class ApiTimeoutError(ApiError):
    """La peticion excedio el timeout configurado."""


class ApiConnectionError(ApiError):
    """No fue posible establecer conexion con el servicio."""


class ApiResponseError(ApiError):
    """La API respondio con un status invalido o un payload no parseable."""

    def __init__(self, message: str, status_code: int | None = None) -> None:
        super().__init__(message)
        self.status_code = status_code


class ResourceNotFoundError(ApiError):
    """El recurso solicitado no existe en la API."""


class PersistenceError(MoviesAppError):
    """Fallo al leer o escribir datos persistentes."""
