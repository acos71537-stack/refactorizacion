"""Servicio de negocio para peliculas."""

from __future__ import annotations

from movies_app import constants
from movies_app.logging_config import get_logger
from movies_app.models.movie import Movie
from movies_app.models.search import SearchEntry
from movies_app.protocols import MovieCatalog
from movies_app.repositories.favorites import FavoritesRepository
from movies_app.repositories.history import HistoryRepository
from movies_app.services.curated import ALL_CURATED_MOVIES, MOVIES_BY_GENRE, POPULAR_MOVIES

_logger = get_logger("movie_service")


class MovieService:
    """Orquesta busqueda, favoritos e historial de peliculas.

    Attributes:
        catalog: Fuente de datos de peliculas (OMDB u otro).
    """

    def __init__(
        self,
        catalog: MovieCatalog,
        favorites: FavoritesRepository,
        history: HistoryRepository,
    ) -> None:
        self._catalog = catalog
        self._favorites = favorites
        self._history = history
        self._cache: dict[str, Movie | None] = {}

    def search_by_title(self, title: str) -> Movie | None:
        """Busca una pelicula por titulo, usando cache en memoria.

        Args:
            title: Titulo a buscar.

        Returns:
            La pelicula o ``None`` si no se encuentra.
        """
        key = title.strip().lower()
        if not key:
            return None
        if key not in self._cache:
            _logger.debug("Cache miss para '%s', consultando catalogo", key)
            self._cache[key] = self._catalog.search_by_title(title)
        else:
            _logger.debug("Cache hit para '%s'", key)
        movie = self._cache[key]
        self._history.add(SearchEntry(title, 1 if movie else 0, constants.SEARCH_TYPE_MOVIE))
        return movie

    def search_by_actor(self, actor: str) -> list[Movie]:
        """Busca peliculas por actor y registra la busqueda.

        Args:
            actor: Nombre del actor.

        Returns:
            Lista de peliculas (puede estar vacia).
        """
        movies = self._catalog.search_by_actor(actor)
        _logger.debug("Busqueda por actor '%s': %d resultados", actor, len(movies))
        self._history.add(SearchEntry(actor, len(movies), constants.SEARCH_TYPE_ACTOR))
        return movies

    def popular_movies(self) -> list[Movie]:
        """Devuelve la lista curada de peliculas populares."""
        return list(POPULAR_MOVIES)

    def movies_by_genre(self, genre: str) -> list[Movie]:
        """Devuelve peliculas curadas por genero.

        Args:
            genre: Genero buscado (``"accion"``, ``"comedia"``).

        Returns:
            Peliculas del genero, o todas las curadas si el genero es desconocido.
        """
        key = genre.strip().lower()
        movies = MOVIES_BY_GENRE.get(key)
        return list(movies) if movies is not None else list(ALL_CURATED_MOVIES)

    def add_favorite(self, movie: Movie) -> bool:
        """Agrega una pelicula a favoritos.

        Returns:
            ``True`` si se agrego; ``False`` si ya existia.
        """
        return self._favorites.add(movie)

    def remove_favorite(self, title: str) -> bool:
        """Elimina una pelicula de favoritos por titulo."""
        return self._favorites.remove(title)

    def favorites(self) -> list[Movie]:
        """Devuelve las peliculas favoritas persistidas."""
        return self._favorites.load()

    def history(self) -> list[SearchEntry]:
        """Devuelve el historial de busquedas."""
        return self._history.load()

    def clear_history(self) -> None:
        """Vacia el historial de busquedas."""
        self._history.clear()

    def stats(self) -> dict[str, int]:
        """Devuelve contadores de favoritos e historial."""
        return {
            "total_favoritas": len(self._favorites.load()),
            "total_historial": len(self._history.load()),
        }
