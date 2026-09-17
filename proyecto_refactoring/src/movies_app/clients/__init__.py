"""Clientes de APIs externas."""

from __future__ import annotations

from movies_app.clients.base import HttpClient
from movies_app.clients.omdb import OmdbClient
from movies_app.clients.tvmaze import TvmazeClient

__all__ = ["HttpClient", "OmdbClient", "TvmazeClient"]
