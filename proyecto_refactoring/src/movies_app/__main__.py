"""Punto de entrada de la aplicacion.

Composition root: construye las dependencias y las inyecta en la UI.
Ejecutar con ``python -m movies_app``.
"""

from __future__ import annotations

from movies_app.clients.base import HttpClient
from movies_app.clients.omdb import OmdbClient
from movies_app.clients.tvmaze import TvmazeClient
from movies_app.config import Settings
from movies_app.logging_config import configure_logging
from movies_app.repositories.favorites import FavoritesRepository
from movies_app.repositories.history import HistoryRepository
from movies_app.services.export_service import ExportService
from movies_app.services.movie_service import MovieService
from movies_app.services.series_service import SeriesService
from movies_app.ui.console import ConsoleRenderer
from movies_app.ui.menu import MenuApp


def build_app(settings: Settings) -> MenuApp:
    """Construye la aplicacion con todas sus dependencias.

    Args:
        settings: Configuracion de la aplicacion.

    Returns:
        La aplicacion lista para ejecutarse.
    """
    http = HttpClient(settings)
    favorites = FavoritesRepository(settings.data_dir / "favorites.json")
    history = HistoryRepository(settings.data_dir / "history.json")

    movies = MovieService(OmdbClient(http, settings), favorites, history)
    series = SeriesService(TvmazeClient(http, settings), history)
    export = ExportService(favorites, history)
    return MenuApp(movies, series, export, ConsoleRenderer())


def main() -> int:
    """Punto de entrada principal.

    Returns:
        Codigo de salida del proceso.
    """
    settings = Settings.from_env()
    configure_logging(settings)
    try:
        build_app(settings).run()
    except KeyboardInterrupt:
        print("\nPrograma interrumpido")
        return 130
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
