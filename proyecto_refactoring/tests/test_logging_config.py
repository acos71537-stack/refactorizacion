"""Tests de la configuracion de logging."""

from __future__ import annotations

import logging

from movies_app.config import Settings
from movies_app.logging_config import configure_logging, get_logger


def test_configure_logging_sets_debug_level() -> None:
    configure_logging(Settings(debug=True))
    assert logging.getLogger("movies_app").level == logging.DEBUG


def test_configure_logging_defaults_to_info() -> None:
    configure_logging(Settings(debug=False))
    assert logging.getLogger("movies_app").level == logging.INFO


def test_get_logger_is_namespaced() -> None:
    assert get_logger("omdb").name == "movies_app.omdb"
