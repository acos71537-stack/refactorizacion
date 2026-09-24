"""Servicio de exportacion e importacion de datos."""

from __future__ import annotations

import json
import re
from collections.abc import Mapping
from pathlib import Path

from movies_app.exceptions import ExportError, InvalidInputError
from movies_app.models.movie import Movie
from movies_app.models.search import SearchEntry
from movies_app.repositories.favorites import FavoritesRepository
from movies_app.repositories.history import HistoryRepository

_SAFE_FILENAME_RE = re.compile(r"^[a-zA-Z0-9_.-]+$")


class ExportService:
    """Exporta e importa favoritos e historial en un unico archivo JSON.

    Reemplaza ``exportar_a_json`` / ``importar_de_json`` de ``api_movies.py``.
    """

    def __init__(
        self,
        favorites: FavoritesRepository,
        history: HistoryRepository,
    ) -> None:
        self._favorites = favorites
        self._history = history

    def export_json(self, path: Path) -> None:
        """Escribe favoritos e historial en ``path``.

        Args:
            path: Archivo de destino.

        Raises:
            ExportError: Si falla la escritura.
            InvalidInputError: Si la ruta contiene traversal o es invalida.
        """
        self._validate_export_path(path)
        payload = {
            "favorites": [movie.to_dict() for movie in self._favorites.load()],
            "history": [entry.to_dict() for entry in self._history.load()],
        }
        try:
            path.parent.mkdir(parents=True, exist_ok=True)
            with path.open("w", encoding="utf-8") as handle:
                json.dump(payload, handle, indent=4, ensure_ascii=False)
        except OSError as exc:
            raise ExportError(f"No se pudo exportar a {path}: {exc}") from exc

    def import_json(self, path: Path) -> None:
        """Reemplaza favoritos e historial con el contenido de ``path``.

        Args:
            path: Archivo de origen.

        Raises:
            ExportError: Si el archivo no existe o no es valido.
            InvalidInputError: Si la ruta contiene traversal o es invalida.
        """
        self._validate_export_path(path)
        try:
            with path.open(encoding="utf-8") as handle:
                payload = json.load(handle)
        except (OSError, json.JSONDecodeError) as exc:
            raise ExportError(f"No se pudo importar desde {path}: {exc}") from exc
        if not isinstance(payload, Mapping):
            raise ExportError(f"El archivo {path} no contiene un objeto JSON")

        raw_favorites = payload.get("favorites", [])
        if isinstance(raw_favorites, list):
            movies = [Movie.from_dict(item) for item in raw_favorites if isinstance(item, Mapping)]
            self._favorites.save(movies)

        raw_history = payload.get("history", [])
        if isinstance(raw_history, list):
            entries = [
                SearchEntry.from_dict(item) for item in raw_history if isinstance(item, Mapping)
            ]
            self._history.save(entries[: self._history.max_entries])

    def _validate_export_path(self, path: Path) -> None:
        """Valida que la ruta del archivo no contenga traversal ni caracteres peligrosos.

        Args:
            path: Ruta a validar.

        Raises:
            InvalidInputError: Si la ruta es invalida o contiene traversal.
        """
        if ".." in path.parts:
            raise InvalidInputError("La ruta no puede contener '..'")
        name = path.name
        if not _SAFE_FILENAME_RE.match(name):
            raise InvalidInputError(
                f"Nombre de archivo invalido: {name}. "
                "Solo se permiten letras, digitos, puntos, guiones y guiones bajos."
            )
