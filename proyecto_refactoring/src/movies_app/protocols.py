"""Contratos (interfaces) para clientes de API y repositorios.

Permiten inyeccion de dependencias y sustitucion por dobles en tests sin
acoplarse a implementaciones concretas.
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Protocol, TypeVar, runtime_checkable

from movies_app.models.movie import Movie
from movies_app.models.series import Series

T = TypeVar("T")


@runtime_checkable
class JsonClient(Protocol):
    """Cliente HTTP que devuelve JSON parseado."""

    def get_json(self, url: str, params: Mapping[str, str] | None = None) -> Any:
        """Ejecuta un GET y devuelve el cuerpo JSON."""
        ...


@runtime_checkable
class MovieCatalog(Protocol):
    """Fuente de datos de peliculas."""

    def search_by_title(self, title: str) -> Movie | None:
        """Busca una pelicula por titulo exacto o aproximado."""
        ...

    def search_by_actor(self, actor: str) -> list[Movie]:
        """Devuelve las peliculas en las que participa un actor."""
        ...


@runtime_checkable
class SeriesCatalog(Protocol):
    """Fuente de datos de series."""

    def search(self, name: str) -> list[Series]:
        """Busca series por nombre."""
        ...

    def get_by_id(self, series_id: int) -> Series | None:
        """Obtiene el detalle de una serie por su identificador."""
        ...


@runtime_checkable
class Repository(Protocol[T]):
    """Persistencia de una coleccion de entidades."""

    def load(self) -> list[T]:
        """Carga todas las entidades persistidas."""
        ...

    def save(self, items: list[T]) -> None:
        """Persiste la coleccion completa."""
        ...
