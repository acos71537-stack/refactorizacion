"""Renderizado especifico del dominio.

Toda la logica de presentacion de peliculas, series, favoritos, historial
y estadisticas se concentra aqui; solo hereda el framework de salida
de ConsoleRenderer.
"""

from __future__ import annotations

import sys
from collections.abc import Sequence
from typing import TextIO

from movies_app.models.movie import Movie
from movies_app.models.search import SearchEntry
from movies_app.models.series import Series
from movies_app.ui.constants import CONSOLE_WIDTH, SUMMARY_MAX_LENGTH


def _display(value: object | None) -> str:
    return "N/A" if value is None else str(value)


class DisplayRenderer:
    """Escribe la salida de presentacion de la aplicacion.

    Hereda de ConsoleRenderer para las operaciones de framework
    (write, separator, header) y agrega metodos de renderizado por dominio.

    Attributes:
        output: Stream de salida.
        width: Ancho de los separadores.
    """

    def __init__(self, output: TextIO | None = None, width: int = CONSOLE_WIDTH) -> None:
        self._output = output if output is not None else sys.stdout
        self._width = width

    def write(self, text: str = "") -> None:
        """Escribe una linea en el stream de salida."""
        print(text, file=self._output)

    def separator(self, char: str = "=") -> None:
        """Escribe un separador horizontal."""
        self.write(char * self._width)

    def header(self, text: str) -> None:
        """Escribe un encabezado centrado entre separadores."""
        self.separator()
        self.write(text.upper().center(self._width))
        self.separator()

    def movie(self, movie: Movie | None) -> None:
        """Muestra el detalle de una pelicula."""
        self.separator()
        if movie is None:
            self.write("No se encontro la pelicula")
            self.separator()
            return
        rows: tuple[tuple[str, object], ...] = (
            ("Titulo", movie.title),
            ("Anio", movie.year),
            ("Rating IMDB", movie.imdb_rating),
            ("Genero", movie.genre),
            ("Director", movie.director),
            ("Actores", movie.actors),
            ("Trama", movie.plot),
            ("Pais", movie.country),
            ("Premios", movie.awards),
        )
        for label, value in rows:
            self.write(f"{label}: {_display(value)}")
        self.separator()

    def series(self, series: Series) -> None:
        """Muestra el detalle de una serie."""
        self.separator()
        summary = series.summary or "N/A"
        if len(summary) > SUMMARY_MAX_LENGTH:
            summary = summary[:SUMMARY_MAX_LENGTH] + "..."
        rows: tuple[tuple[str, object], ...] = (
            ("Nombre", series.name),
            ("Idioma", series.language),
            ("Generos", ", ".join(series.genres) or "N/A"),
            ("Rating", series.rating),
            ("Estado", series.status),
            ("Estreno", series.premiered),
            ("Final", series.ended),
            ("Episodios", series.runtime),
            ("Resumen", summary),
        )
        for label, value in rows:
            self.write(f"{label}: {_display(value)}")
        self.separator()

    def movie_list(self, movies: Sequence[Movie]) -> None:
        """Muestra una lista numerada de peliculas."""
        if not movies:
            self.write("No se encontraron peliculas")
            return
        for index, movie in enumerate(movies, start=1):
            year = _display(movie.year)
            rating = f" - {movie.imdb_rating}" if movie.imdb_rating is not None else ""
            self.write(f"{index}. {movie.title} ({year}){rating}")

    def series_list(self, series: Sequence[Series]) -> None:
        """Muestra una lista numerada de series."""
        if not series:
            self.write("No se encontraron series")
            return
        for index, item in enumerate(series, start=1):
            self.write(f"{index}. {item.name} ({_display(item.status)})")

    def favorites(self, movies: Sequence[Movie]) -> None:
        """Muestra la lista de favoritos."""
        if not movies:
            self.write("No tienes peliculas favoritas")
            return
        for index, movie in enumerate(movies, start=1):
            self.write(f"{index}. {movie.title}")

    def history(self, entries: Sequence[SearchEntry]) -> None:
        """Muestra el historial de busquedas."""
        if not entries:
            self.write("No hay historial")
            return
        for index, entry in enumerate(entries, start=1):
            stamp = entry.timestamp.strftime("%Y-%m-%d %H:%M")
            self.write(f"{index}. {entry.query} [{entry.search_type}] ({stamp})")

    def stats(self, data: dict[str, int]) -> None:
        """Muestra contadores de la aplicacion."""
        self.write(f"Total favoritas: {data.get('total_favoritas', 0)}")
        self.write(f"Total historial: {data.get('total_historial', 0)}")
