"""Repositorio de peliculas favoritas."""

from __future__ import annotations

from pathlib import Path

from movies_app.models.movie import Movie
from movies_app.repositories.base import JsonRepository


class FavoritesRepository:
    """Persistencia de peliculas favoritas, sin duplicados por titulo.

    Attributes:
        path: Ruta del archivo JSON de favoritos.
    """

    def __init__(self, path: Path) -> None:
        self._repo: JsonRepository[Movie] = JsonRepository(path, Movie.to_dict, Movie.from_dict)

    @property
    def path(self) -> Path:
        """Ruta del archivo de favoritos."""
        return self._repo.path

    def load(self) -> list[Movie]:
        """Devuelve todas las peliculas favoritas."""
        return self._repo.load()

    def save(self, items: list[Movie]) -> None:
        """Persiste la lista completa de favoritos."""
        self._repo.save(items)

    def contains(self, title: str) -> bool:
        """Indica si una pelicula ya esta en favoritos."""
        return any(movie.title == title for movie in self.load())

    def add(self, movie: Movie) -> bool:
        """Agrega una pelicula a favoritos si no existe.

        Args:
            movie: Pelicula a agregar.

        Returns:
            ``True`` si se agrego; ``False`` si ya estaba presente.
        """
        favorites = self.load()
        if any(existing.title == movie.title for existing in favorites):
            return False
        favorites.append(movie)
        self.save(favorites)
        return True

    def remove(self, title: str) -> bool:
        """Elimina una pelicula de favoritos por titulo.

        Args:
            title: Titulo exacto a eliminar.

        Returns:
            ``True`` si se elimino; ``False`` si no existia.
        """
        favorites = self.load()
        remaining = [movie for movie in favorites if movie.title != title]
        if len(remaining) == len(favorites):
            return False
        self.save(remaining)
        return True
