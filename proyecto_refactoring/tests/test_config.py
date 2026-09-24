"""Tests de la configuracion central."""

from __future__ import annotations

from pathlib import Path

import pytest

from movies_app.config import Settings


def test_defaults() -> None:
    settings = Settings(omdb_api_key="test-key")
    assert settings.omdb_api_key == "test-key"
    assert settings.omdb_base_url == "https://www.omdbapi.com/"
    assert settings.timeout == 30.0
    assert settings.max_retries == 3
    assert settings.data_dir == Path("data")


def test_missing_api_key_raises() -> None:
    with pytest.raises(ValueError, match="omdb_api_key"):
        Settings(omdb_api_key="")


def test_invalid_values_raise() -> None:
    with pytest.raises(ValueError):
        Settings(timeout=0)
    with pytest.raises(ValueError):
        Settings(max_retries=-1)
    with pytest.raises(ValueError):
        Settings(backoff_factor=-1.0)
    with pytest.raises(ValueError):
        Settings(omdb_api_key="")


def test_invalid_url_raises() -> None:
    with pytest.raises(ValueError):
        Settings(tvmaze_base_url="ftp://example.test")


def test_from_env(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("OMDB_API_KEY", "abc")
    monkeypatch.setenv("MOVIES_DEBUG", "true")
    monkeypatch.setenv("MOVIES_VERBOSE", "yes")
    monkeypatch.setenv("MOVIES_TIMEOUT", "5")
    monkeypatch.setenv("MOVIES_MAX_RETRIES", "1")
    monkeypatch.setenv("MOVIES_BACKOFF_FACTOR", "0.1")
    monkeypatch.setenv("MOVIES_DATA_DIR", "custom")

    settings = Settings.from_env()

    assert settings.omdb_api_key == "abc"
    assert settings.debug is True
    assert settings.verbose is True
    assert settings.timeout == 5.0
    assert settings.max_retries == 1
    assert settings.backoff_factor == 0.1
    assert settings.data_dir == Path("custom")


def test_from_env_missing_api_key_raises(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("OMDB_API_KEY", raising=False)
    with pytest.raises(ValueError, match="OMDB_API_KEY"):
        Settings.from_env()
