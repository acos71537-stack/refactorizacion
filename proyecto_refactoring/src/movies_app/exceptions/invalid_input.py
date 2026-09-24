"""Excepciones para entradas invalidas del usuario."""

from __future__ import annotations

from movies_app.exceptions.base import MoviesAppError


class InvalidInputError(MoviesAppError):
    """La entrada del usuario no es valida."""

    def __init__(self, message: str) -> None:
        super().__init__(f"Entrada invalida: {message}")
