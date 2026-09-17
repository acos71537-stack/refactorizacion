"""Tests del bucle interactivo de la consola."""

from __future__ import annotations

import io
from collections.abc import Callable

from movies_app.exceptions import ApiResponseError
from movies_app.models.movie import Movie
from movies_app.models.search import SearchEntry
from movies_app.models.series import Series
from movies_app.repositories.favorites import FavoritesRepository
from movies_app.repositories.history import HistoryRepository
from movies_app.services.export_service import ExportService
from movies_app.services.movie_service import MovieService
from movies_app.services.series_service import SeriesService
from movies_app.ui.console import ConsoleRenderer
from movies_app.ui.menu import MenuApp
from tests.fakes import StubMovieCatalog, StubSeriesCatalog


def _reader(values: list[str]) -> Callable[[str], str]:
    iterator = iter(values)

    def _read(_prompt: str) -> str:
        try:
            return next(iterator)
        except StopIteration:
            raise EOFError from None

    return _read


def _build_app(
    favorites: FavoritesRepository,
    history: HistoryRepository,
    output: io.StringIO,
    values: list[str],
    movie_catalog: StubMovieCatalog | None = None,
    series_catalog: StubSeriesCatalog | None = None,
) -> MenuApp:
    movies = MovieService(movie_catalog or StubMovieCatalog(), favorites, history)
    series = SeriesService(series_catalog or StubSeriesCatalog(), history)
    export = ExportService(favorites, history)
    return MenuApp(movies, series, export, ConsoleRenderer(output), input_func=_reader(values))


def test_exit_option(favorites: FavoritesRepository, history: HistoryRepository) -> None:
    output = io.StringIO()
    _build_app(favorites, history, output, ["11"]).run()
    assert "Hasta luego!" in output.getvalue()


def test_eof_stops_gracefully(favorites: FavoritesRepository, history: HistoryRepository) -> None:
    output = io.StringIO()
    _build_app(favorites, history, output, []).run()
    assert "Entrada finalizada" in output.getvalue()


def test_invalid_option(favorites: FavoritesRepository, history: HistoryRepository) -> None:
    output = io.StringIO()
    _build_app(favorites, history, output, ["99", "", "11"]).run()
    assert "Opcion invalida" in output.getvalue()


def test_search_movie_and_add_favorite(
    favorites: FavoritesRepository, history: HistoryRepository
) -> None:
    output = io.StringIO()
    catalog = StubMovieCatalog({"Matrix": Movie(title="The Matrix", year=1999)})
    _build_app(
        favorites, history, output, ["1", "Matrix", "s", "", "11"], movie_catalog=catalog
    ).run()
    assert "The Matrix" in output.getvalue()
    assert "Agregada a favoritos!" in output.getvalue()
    assert favorites.load()[0].title == "The Matrix"


def test_search_movie_not_found(favorites: FavoritesRepository, history: HistoryRepository) -> None:
    output = io.StringIO()
    _build_app(favorites, history, output, ["1", "Nope", "", "11"]).run()
    assert "No se encontro la pelicula" in output.getvalue()


def test_search_actor_flow(favorites: FavoritesRepository, history: HistoryRepository) -> None:
    output = io.StringIO()
    catalog = StubMovieCatalog(by_actor=[Movie(title="John Wick")])
    _build_app(
        favorites, history, output, ["2", "keanu", "", "", "11"], movie_catalog=catalog
    ).run()
    assert "John Wick" in output.getvalue()


def test_search_series_flow(favorites: FavoritesRepository, history: HistoryRepository) -> None:
    output = io.StringIO()
    series_catalog = StubSeriesCatalog([Series(id=1, name="Dark", status="Ended")])
    _build_app(
        favorites, history, output, ["3", "dark", "1", "", "11"], series_catalog=series_catalog
    ).run()
    assert "Nombre: Dark" in output.getvalue()


def test_popular_and_genre(favorites: FavoritesRepository, history: HistoryRepository) -> None:
    output = io.StringIO()
    _build_app(favorites, history, output, ["4", "", "5", "accion", "", "11"]).run()
    assert "PELICULAS POPULARES" in output.getvalue()
    assert "Die Hard" in output.getvalue()


def test_favorites_empty(favorites: FavoritesRepository, history: HistoryRepository) -> None:
    output = io.StringIO()
    _build_app(favorites, history, output, ["6", "", "11"]).run()
    assert "No tienes peliculas favoritas" in output.getvalue()


def test_history_flow(favorites: FavoritesRepository, history: HistoryRepository) -> None:
    history.add(SearchEntry("matrix", 1, "movie"))
    output = io.StringIO()
    _build_app(favorites, history, output, ["7", "n", "", "11"]).run()
    assert "matrix" in output.getvalue()


def test_stats(favorites: FavoritesRepository, history: HistoryRepository) -> None:
    output = io.StringIO()
    _build_app(favorites, history, output, ["8", "", "11"]).run()
    assert "Total favoritas: 0" in output.getvalue()


class _FailingCatalog:
    def search_by_title(self, _title: str) -> Movie | None:
        raise ApiResponseError("boom")

    def search_by_actor(self, _actor: str) -> list[Movie]:
        raise ApiResponseError("boom")


def test_api_error_is_handled(favorites: FavoritesRepository, history: HistoryRepository) -> None:
    output = io.StringIO()
    app = MenuApp(
        MovieService(_FailingCatalog(), favorites, history),
        SeriesService(StubSeriesCatalog(), history),
        ExportService(favorites, history),
        ConsoleRenderer(output),
        input_func=_reader(["1", "X", "", "11"]),
    )
    app.run()
    assert "Error: boom" in output.getvalue()
