"""Repositorio JSON generico con escritura atomica."""

from __future__ import annotations

import json
from collections.abc import Callable, Mapping
from pathlib import Path
from typing import Generic, TypeVar

from movies_app.exceptions import PersistenceError
from movies_app.logging_config import get_logger

T = TypeVar("T")

_logger = get_logger("repository")


class JsonRepository(Generic[T]):
    """Persistencia generica de una coleccion de entidades en un archivo JSON.

    La escritura es atomica: se serializa a un archivo temporal y luego se
    reemplaza el destino, evitando corrupcion ante fallos.

    Attributes:
        path: Ruta del archivo JSON de respaldo.
    """

    def __init__(
        self,
        path: Path,
        to_dict: Callable[[T], dict[str, object]],
        from_dict: Callable[[Mapping[str, object]], T],
    ) -> None:
        self._path = path
        self._to_dict = to_dict
        self._from_dict = from_dict

    @property
    def path(self) -> Path:
        """Ruta del archivo persistido."""
        return self._path

    def load(self) -> list[T]:
        """Carga las entidades persistidas, ignorando entradas corruptas.

        Returns:
            La lista de entidades; vacia si el archivo no existe.

        Raises:
            PersistenceError: Si el archivo no se puede leer o no es una lista.
        """
        if not self._path.exists():
            return []
        try:
            with self._path.open(encoding="utf-8") as handle:
                raw = json.load(handle)
        except (OSError, json.JSONDecodeError) as exc:
            raise PersistenceError(f"No se pudo leer {self._path}: {exc}") from exc
        if not isinstance(raw, list):
            raise PersistenceError(f"El archivo {self._path} no contiene una lista JSON")

        items: list[T] = []
        for index, entry in enumerate(raw):
            if not isinstance(entry, Mapping):
                _logger.warning("Entrada %d en %s no es un objeto; se omite", index, self._path)
                continue
            try:
                items.append(self._from_dict(entry))
            except (ValueError, KeyError, TypeError) as exc:
                _logger.warning("Entrada %d invalida en %s: %s", index, self._path, exc)
        return items

    def save(self, items: list[T]) -> None:
        """Persiste la coleccion completa de forma atomica.

        Args:
            items: Entidades a guardar.

        Raises:
            PersistenceError: Si falla la escritura en disco.
        """
        try:
            self._path.parent.mkdir(parents=True, exist_ok=True)
            payload = [self._to_dict(item) for item in items]
            temp_path = self._path.with_name(self._path.name + ".tmp")
            with temp_path.open("w", encoding="utf-8") as handle:
                json.dump(payload, handle, indent=4, ensure_ascii=False)
            temp_path.replace(self._path)
        except OSError as exc:
            raise PersistenceError(f"No se pudo escribir {self._path}: {exc}") from exc
