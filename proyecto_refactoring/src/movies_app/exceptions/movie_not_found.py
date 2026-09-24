"""Excepciones especificas para peliculas."""

from __future__ import annotations

from movies_app.exceptions.base import MoviesAppError


class MovieNotFoundError(MoviesAppError):
    """No se encontro la pelicula solicitada."""

    def __init__(self, title: str) -> None:
        self.title = title
        super().__init__(f"No se encontro la pelicula: {title}")
