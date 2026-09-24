"""Valores constantes y por defecto de la aplicacion.

Centraliza los literales que antes estaban dispersos: claves de API, URLs,
nombres de archivo, tipos de busqueda y generos.
La presentacion se define en ``ui/constants.py``.
"""

from __future__ import annotations

# --- API ---
OMDB_BASE_URL = "https://www.omdbapi.com/"
TVMAZE_BASE_URL = "https://api.tvmaze.com"
OMDB_API_KEY_ENV_VAR = "OMDB_API_KEY"

# --- HTTP ---
DEFAULT_TIMEOUT_SECONDS = 30.0
DEFAULT_MAX_RETRIES = 3
DEFAULT_BACKOFF_FACTOR = 0.5
RETRYABLE_HTTP_STATUS = 500

# --- Persistencia ---
DEFAULT_DATA_DIR = "data"
FAVORITES_FILENAME = "favorites.json"
HISTORY_FILENAME = "history.json"
DEFAULT_MAX_HISTORY = 100

# --- Dominio ---
SEARCH_TYPE_MOVIE = "movie"
SEARCH_TYPE_SERIES = "series"
SEARCH_TYPE_ACTOR = "actor"
GENRE_ACTION = "accion"
GENRE_COMEDY = "comedia"
