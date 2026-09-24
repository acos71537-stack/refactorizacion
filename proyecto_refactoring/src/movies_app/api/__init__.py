"""Clientes de APIs externas (lógica de negocio por API)."""

from __future__ import annotations

from movies_app.api.omdb import OmdbApi
from movies_app.api.tvmaze import TvmazeApi

__all__ = ["OmdbApi", "TvmazeApi"]
