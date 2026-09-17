"""Tests del punto de entrada y del composition root."""

from __future__ import annotations

from pathlib import Path

import pytest

from movies_app import __main__ as entry
from movies_app.config import Settings
from movies_app.ui.menu import MenuApp


def test_build_app_returns_menu(settings: Settings) -> None:
    assert isinstance(entry.build_app(settings), MenuApp)


def test_main_returns_zero(monkeypatch: pytest.MonkeyPatch) -> None:
    def _noop_run(_self: MenuApp) -> None:
        return None

    monkeypatch.setattr(MenuApp, "run", _noop_run)
    assert entry.main() == 0


def test_main_handles_keyboard_interrupt(monkeypatch: pytest.MonkeyPatch) -> None:
    def _interrupt(_self: MenuApp) -> None:
        raise KeyboardInterrupt

    monkeypatch.setattr(MenuApp, "run", _interrupt)
    assert entry.main() == 130


def test_settings_use_data_dir(tmp_path: Path) -> None:
    settings = Settings(data_dir=tmp_path)
    app = entry.build_app(settings)
    assert isinstance(app, MenuApp)
