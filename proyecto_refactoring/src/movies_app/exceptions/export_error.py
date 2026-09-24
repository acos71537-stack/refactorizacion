"""Excepciones para errores de exportacion/importacion."""

from __future__ import annotations

from movies_app.exceptions.base import MoviesAppError


class ExportError(MoviesAppError):
    """Error durante la exportacion o importacion de datos."""

    def __init__(self, message: str) -> None:
        super().__init__(f"Error de exportacion: {message}")
