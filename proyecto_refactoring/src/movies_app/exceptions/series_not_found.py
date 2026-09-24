"""Excepciones especificas para series."""

from __future__ import annotations

from movies_app.exceptions.base import MoviesAppError


class SeriesNotFoundError(MoviesAppError):
    """No se encontro la serie solicitada."""

    def __init__(self, series_id: int) -> None:
        self.series_id = series_id
        super().__init__(f"No se encontro la serie con id: {series_id}")
