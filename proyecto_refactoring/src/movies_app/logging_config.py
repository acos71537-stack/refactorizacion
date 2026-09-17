"""Configuracion central de logging.

Reemplaza el uso de ``print`` y los modulos duplicados ``logger.py`` /
``log_manager.py``.
"""

from __future__ import annotations

import logging

from movies_app.config import Settings

_LOG_FORMAT = "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def configure_logging(settings: Settings) -> None:
    """Configura el logging raiz segun ``settings``.

    Args:
        settings: Configuracion de la aplicacion.
    """
    level = logging.DEBUG if settings.debug else logging.INFO
    logging.basicConfig(level=level, format=_LOG_FORMAT, datefmt=_DATE_FORMAT)
    package_logger = logging.getLogger("movies_app")
    package_logger.setLevel(logging.DEBUG if (settings.debug or settings.verbose) else level)


def get_logger(name: str) -> logging.Logger:
    """Devuelve un logger bajo el namespace ``movies_app``.

    Args:
        name: Nombre corto del modulo (p. ej. ``"omdb"``).

    Returns:
        Un ``logging.Logger`` namespaced.
    """
    return logging.getLogger(f"movies_app.{name}")
