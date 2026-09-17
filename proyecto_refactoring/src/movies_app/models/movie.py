"""Modelo de dominio para peliculas."""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any

from movies_app.models._parsing import clean_str, parse_float, parse_int, parse_year


@dataclass(frozen=True, slots=True)
class Movie:
    """Pelicula normalizada, independiente del formato de la API.

    Attributes:
        title: Titulo de la pelicula.
        year: Anio de estreno.
        imdb_rating: Puntuacion de IMDb.
        genre: Generos separados por coma.
        director: Director(es).
        actors: Reparto principal.
        plot: Sinopsis.
        country: Pais(es) de produccion.
        awards: Premios.
        poster: URL del poster.
        language: Idioma original.
    """

    title: str
    year: int | None = None
    imdb_rating: float | None = None
    genre: str | None = None
    director: str | None = None
    actors: str | None = None
    plot: str | None = None
    country: str | None = None
    awards: str | None = None
    poster: str | None = None
    language: str | None = None

    @classmethod
    def from_omdb(cls, payload: Mapping[str, Any]) -> Movie:
        """Construye un ``Movie`` desde un payload JSON de OMDB.

        Args:
            payload: Diccionario devuelto por OMDB.

        Returns:
            La pelicula normalizada.
        """
        return cls(
            title=clean_str(payload.get("Title")) or "N/A",
            year=parse_year(payload.get("Year")),
            imdb_rating=parse_float(payload.get("imdbRating")),
            genre=clean_str(payload.get("Genre")),
            director=clean_str(payload.get("Director")),
            actors=clean_str(payload.get("Actors")),
            plot=clean_str(payload.get("Plot")),
            country=clean_str(payload.get("Country")),
            awards=clean_str(payload.get("Awards")),
            poster=clean_str(payload.get("Poster")),
            language=clean_str(payload.get("Language")),
        )

    def to_dict(self) -> dict[str, Any]:
        """Serializa la pelicula a un diccionario JSON-compatible."""
        return {
            "title": self.title,
            "year": self.year,
            "imdb_rating": self.imdb_rating,
            "genre": self.genre,
            "director": self.director,
            "actors": self.actors,
            "plot": self.plot,
            "country": self.country,
            "awards": self.awards,
            "poster": self.poster,
            "language": self.language,
        }

    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> Movie:
        """Reconstruye un ``Movie`` desde la salida de ``to_dict``.

        Args:
            data: Diccionario previamente serializado.

        Returns:
            La pelicula reconstruida.
        """
        return cls(
            title=clean_str(data.get("title")) or "N/A",
            year=parse_int(data.get("year")),
            imdb_rating=parse_float(data.get("imdb_rating")),
            genre=clean_str(data.get("genre")),
            director=clean_str(data.get("director")),
            actors=clean_str(data.get("actors")),
            plot=clean_str(data.get("plot")),
            country=clean_str(data.get("country")),
            awards=clean_str(data.get("awards")),
            poster=clean_str(data.get("poster")),
            language=clean_str(data.get("language")),
        )
