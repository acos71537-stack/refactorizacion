"""Valores constantes y por defecto de la aplicacion.

Centraliza los literales que antes estaban dispersos: claves de API, URLs,
nombres de archivo, tipos de busqueda, generos y textos de la interfaz.
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

# --- Presentacion ---
CONSOLE_WIDTH = 60
SUMMARY_MAX_LENGTH = 200
EXIT_OPTION = "11"
MENU_OPTIONS: tuple[str, ...] = (
    "1. Buscar pelicula por titulo",
    "2. Buscar por actor",
    "3. Buscar series",
    "4. Ver peliculas populares",
    "5. Buscar por genero",
    "6. Ver favoritos",
    "7. Ver historial",
    "8. Ver estadisticas",
    "9. Exportar datos",
    "10. Importar datos",
    f"{EXIT_OPTION}. Salir",
)
