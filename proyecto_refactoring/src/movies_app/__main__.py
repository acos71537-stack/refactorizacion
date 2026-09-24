"""Punto de entrada de la aplicacion.

Composition root: construye las dependencias y las inyecta en la UI.
Ejecutar con ``python -m movies_app``.
"""

from __future__ import annotations

from dotenv import load_dotenv

from movies_app import constants
from movies_app.api import OmdbApi, TvmazeApi
from movies_app.clients.base import HttpClient
from movies_app.config import Settings
from movies_app.logging_config import configure_logging, get_logger
from movies_app.repositories.favorites import FavoritesRepository
from movies_app.repositories.history import HistoryRepository
from movies_app.services.export_service import ExportService
from movies_app.services.movie_service import MovieService
from movies_app.services.series_service import SeriesService
from movies_app.ui.display import DisplayRenderer
from movies_app.ui.menu import MenuApp

_logger = get_logger("main")


def build_app(settings: Settings) -> MenuApp:
    """Construye la aplicacion con todas sus dependencias.

    Args:
        settings: Configuracion de la aplicacion.

    Returns:
        La aplicacion lista para ejecutarse.
    """
    http = HttpClient(settings)
    favorites = FavoritesRepository(settings.data_dir / constants.FAVORITES_FILENAME)
    history = HistoryRepository(settings.data_dir / constants.HISTORY_FILENAME)

    movies = MovieService(OmdbApi(http, settings), favorites, history)
    series = SeriesService(TvmazeApi(http, settings), history)
    export = ExportService(favorites, history)
    return MenuApp(movies, series, export, DisplayRenderer())


def main() -> int:
    """Punto de entrada principal.

    Returns:
        Codigo de salida del proceso.
    """
    load_dotenv()
    settings = Settings.from_env()
    configure_logging(settings)
    try:
        build_app(settings).run()
    except KeyboardInterrupt:
        _logger.info("Programa interrumpido")
        return 130
    except Exception as exc:
        _logger.exception("Error inesperado: %s", exc)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
