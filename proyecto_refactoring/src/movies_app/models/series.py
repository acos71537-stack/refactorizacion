"""Modelo de dominio para series de TV."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from typing import Any

from movies_app.models._parsing import clean_str, parse_float, parse_int


def _parse_genres(value: Any) -> tuple[str, ...]:
    if not isinstance(value, Sequence) or isinstance(value, (str, bytes)):
        return ()
    return tuple(clean_str(item) or "" for item in value if clean_str(item))


def _parse_rating(value: Any) -> float | None:
    if isinstance(value, Mapping):
        return parse_float(value.get("average"))
    return parse_float(value)


def _parse_date(value: Any) -> str | None:
    return clean_str(value)


@dataclass(frozen=True, slots=True)
class Series:
    """Serie normalizada a partir de TVMaze.

    Attributes:
        id: Identificador de TVMaze.
        name: Nombre de la serie.
        language: Idioma original.
        genres: Generos.
        rating: Puntuacion promedio.
        status: Estado de emision.
        premiered: Fecha de estreno.
        ended: Fecha de finalizacion.
        runtime: Duracion por episodio, en minutos.
        summary: Sinopsis (puede contener HTML).
    """

    id: int
    name: str
    language: str | None = None
    genres: tuple[str, ...] = ()
    rating: float | None = None
    status: str | None = None
    premiered: str | None = None
    ended: str | None = None
    runtime: int | None = None
    summary: str | None = None

    @classmethod
    def from_tvmaze(cls, payload: Mapping[str, Any]) -> Series:
        """Construye una ``Series`` desde el objeto ``show`` de TVMaze.

        Args:
            payload: Diccionario del show (ya desenvuelto de ``{"show": ...}``).

        Returns:
            La serie normalizada.

        Raises:
            ValueError: Si el payload no contiene un ``id`` valido.
        """
        series_id = parse_int(payload.get("id"))
        if series_id is None:
            raise ValueError("Payload de TVMaze sin 'id' valido")
        return cls(
            id=series_id,
            name=clean_str(payload.get("name")) or "N/A",
            language=clean_str(payload.get("language")),
            genres=_parse_genres(payload.get("genres")),
            rating=_parse_rating(payload.get("rating")),
            status=clean_str(payload.get("status")),
            premiered=_parse_date(payload.get("premiered")),
            ended=_parse_date(payload.get("ended")),
            runtime=parse_int(payload.get("runtime")),
            summary=clean_str(payload.get("summary")),
        )

    @classmethod
    def from_search_result(cls, payload: Mapping[str, Any]) -> Series:
        """Construye una ``Series`` desde un resultado de busqueda de TVMaze.

        Los resultados de ``/search/shows`` tienen la forma
        ``{"score": float, "show": {...}}``.
        """
        show = payload.get("show")
        if not isinstance(show, Mapping):
            raise ValueError("Resultado de busqueda de TVMaze sin 'show'")
        return cls.from_tvmaze(show)

    def to_dict(self) -> dict[str, Any]:
        """Serializa la serie a un diccionario JSON-compatible."""
        return {
            "id": self.id,
            "name": self.name,
            "language": self.language,
            "genres": list(self.genres),
            "rating": self.rating,
            "status": self.status,
            "premiered": self.premiered,
            "ended": self.ended,
            "runtime": self.runtime,
            "summary": self.summary,
        }

    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> Series:
        """Reconstruye una ``Series`` desde la salida de ``to_dict``."""
        series_id = parse_int(data.get("id"))
        if series_id is None:
            raise ValueError("Serie persistida sin 'id' valido")
        return cls(
            id=series_id,
            name=clean_str(data.get("name")) or "N/A",
            language=clean_str(data.get("language")),
            genres=_parse_genres(data.get("genres")),
            rating=parse_float(data.get("rating")),
            status=clean_str(data.get("status")),
            premiered=clean_str(data.get("premiered")),
            ended=clean_str(data.get("ended")),
            runtime=parse_int(data.get("runtime")),
            summary=clean_str(data.get("summary")),
        )
