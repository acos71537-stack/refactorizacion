"""Bucle interactivo de la aplicacion de consola."""

from __future__ import annotations

from collections.abc import Callable
from pathlib import Path

from movies_app import constants
from movies_app.exceptions import MoviesAppError
from movies_app.logging_config import get_logger
from movies_app.services.export_service import ExportService
from movies_app.services.movie_service import MovieService
from movies_app.services.series_service import SeriesService
from movies_app.ui.display import DisplayRenderer

InputFunc = Callable[[str], str]

_logger = get_logger("menu")


class MenuApp:
    """Coordina la interaccion del usuario con los servicios.

    Attributes:
        renderer: Componente de presentacion.
    """

    def __init__(
        self,
        movies: MovieService,
        series: SeriesService,
        export: ExportService,
        renderer: DisplayRenderer,
        input_func: InputFunc = input,
    ) -> None:
        self._movies = movies
        self._series = series
        self._export = export
        self._renderer = renderer
        self._input = input_func

    def run(self) -> None:
        """Ejecuta el bucle principal hasta que el usuario sale o hay EOF."""
        while True:
            self._render_menu()
            try:
                choice = self._input("\nSeleccione una opcion: ").strip()
            except EOFError:
                self._renderer.write("\nEntrada finalizada. Saliendo.")
                return
            if choice == constants.EXIT_OPTION:
                self._renderer.write("Hasta luego!")
                return
            self._dispatch(choice)

    def _dispatch(self, choice: str) -> None:
        handlers: dict[str, Callable[[], None]] = {
            "1": self._search_movie,
            "2": self._search_actor,
            "3": self._search_series,
            "4": self._popular,
            "5": self._by_genre,
            "6": self._favorites,
            "7": self._history,
            "8": self._stats,
            "9": self._export_data,
            "10": self._import_data,
        }
        handler = handlers.get(choice)
        if handler is None:
            self._renderer.write("Opcion invalida")
            self._pause()
            return
        try:
            handler()
        except MoviesAppError as exc:
            _logger.error("Error de aplicacion: %s", exc)
            self._renderer.write(f"Error: {exc}")
            self._pause()

    def _render_menu(self) -> None:
        self._renderer.header("Sistema de peliculas y series")
        for line in constants.MENU_OPTIONS:
            self._renderer.write(line)

    def _search_movie(self) -> None:
        title = self._input("Ingrese el titulo de la pelicula: ")
        movie = self._movies.search_by_title(title)
        self._renderer.movie(movie)
        if movie is not None:
            answer = self._input("\n¿Agregar a favoritos? (s/n): ").strip().lower()
            if answer == "s":
                added = self._movies.add_favorite(movie)
                self._renderer.write("Agregada a favoritos!" if added else "Ya esta en favoritos")
        self._pause()

    def _search_actor(self) -> None:
        actor = self._input("Ingrese el nombre del actor: ")
        movies = self._movies.search_by_actor(actor)
        self._renderer.movie_list(movies)
        if movies:
            selection = self._input(
                "\nSeleccione una pelicula para ver detalles (0 para volver): "
            ).strip()
            index = self._parse_selection(selection, len(movies))
            if index is not None:
                self._renderer.movie(self._movies.search_by_title(movies[index].title))
        self._pause()

    def _search_series(self) -> None:
        name = self._input("Ingrese el nombre de la serie: ")
        series = self._series.search(name)
        self._renderer.series_list(series)
        if series:
            selection = self._input(
                "\nSeleccione una serie para ver detalles (0 para volver): "
            ).strip()
            index = self._parse_selection(selection, len(series))
            if index is not None:
                self._renderer.series(self._series.get(series[index].id))
        self._pause()

    def _popular(self) -> None:
        self._renderer.header("Peliculas populares")
        self._renderer.movie_list(self._movies.popular_movies())
        self._pause()

    def _by_genre(self) -> None:
        self._renderer.write("Generos disponibles: accion, comedia")
        genre = self._input("Ingrese el genero: ")
        self._renderer.movie_list(self._movies.movies_by_genre(genre))
        self._pause()

    def _favorites(self) -> None:
        self._renderer.header("Mis favoritos")
        favorites = self._movies.favorites()
        self._renderer.favorites(favorites)
        if favorites:
            selection = self._input(
                "\n¿Desea eliminar alguna? (numero o Enter para volver): "
            ).strip()
            index = self._parse_selection(selection, len(favorites))
            if index is not None:
                removed = self._movies.remove_favorite(favorites[index].title)
                self._renderer.write("Eliminada de favoritos" if removed else "No se pudo eliminar")
        self._pause()

    def _history(self) -> None:
        self._renderer.header("Historial de busquedas")
        entries = self._movies.history()
        self._renderer.history(entries)
        if entries:
            answer = self._input("\n¿Limpiar historial? (s/n): ").strip().lower()
            if answer == "s":
                self._movies.clear_history()
                self._renderer.write("Historial limpiado")
        self._pause()

    def _stats(self) -> None:
        self._renderer.header("Estadisticas")
        self._renderer.stats(self._movies.stats())
        self._pause()

    def _export_data(self) -> None:
        name = self._input("Nombre del archivo (sin extension): ").strip()
        try:
            self._export.export_json(Path(f"{name}.json"))
            self._renderer.write(f"Exportado a {name}.json")
        except Exception as exc:
            _logger.exception("Error al exportar: %s", exc)
            self._renderer.write(f"Error al exportar: {exc}")
        self._pause()

    def _import_data(self) -> None:
        name = self._input("Nombre del archivo (sin extension): ").strip()
        try:
            self._export.import_json(Path(f"{name}.json"))
            self._renderer.write(f"Importado desde {name}.json")
        except Exception as exc:
            _logger.exception("Error al importar: %s", exc)
            self._renderer.write(f"Error al importar: {exc}")
        self._pause()

    def _pause(self) -> None:
        self._input("\nPresione Enter para continuar...")

    @staticmethod
    def _parse_selection(selection: str, count: int) -> int | None:
        if not selection.isdigit():
            return None
        index = int(selection) - 1
        if 0 <= index < count:
            return index
        return None
