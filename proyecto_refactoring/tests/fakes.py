"""Dobles de prueba reutilizables (fakes y stubs)."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from movies_app.models.movie import Movie
from movies_app.models.series import Series


class FakeJsonClient:
    """Cliente JSON que devuelve respuestas predefinidas en orden.

    Attributes:
        calls: Registro de ``(url, params)`` de cada invocacion.
    """

    def __init__(self, responses: list[Any]) -> None:
        self._responses = list(responses)
        self.calls: list[tuple[str, dict[str, str] | None]] = []

    def get_json(self, url: str, params: Mapping[str, str] | None = None) -> Any:
        """Devuelve la siguiente respuesta o lanza la excepcion encolada."""
        self.calls.append((url, dict(params) if params is not None else None))
        if not self._responses:
            raise AssertionError(f"FakeJsonClient sin respuestas para {url}")
        result = self._responses.pop(0)
        if isinstance(result, Exception):
            raise result
        return result


class StubMovieCatalog:
    """Catalogo de peliculas en memoria para tests."""

    def __init__(
        self,
        by_title: Mapping[str, Movie] | None = None,
        by_actor: list[Movie] | None = None,
    ) -> None:
        self._by_title = dict(by_title or {})
        self._by_actor = list(by_actor or [])
        self.title_calls = 0
        self.actor_calls = 0

    def search_by_title(self, title: str) -> Movie | None:
        self.title_calls += 1
        return self._by_title.get(title)

    def search_by_actor(self, _actor: str) -> list[Movie]:
        self.actor_calls += 1
        return list(self._by_actor)


class StubSeriesCatalog:
    """Catalogo de series en memoria para tests."""

    def __init__(self, series: list[Series] | None = None) -> None:
        self._series = list(series or [])

    def search(self, _name: str) -> list[Series]:
        return list(self._series)

    def get_by_id(self, series_id: int) -> Series:
        for item in self._series:
            if item.id == series_id:
                return item
        raise AssertionError(f"Serie {series_id} no encontrada en el stub")
