"""Configuracion central y tipada de la aplicacion.

Reemplaza la variable global ``CONFIG`` de ``api_movies.py`` y los ~88 archivos
``*_config.py``.
"""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path


def _env_bool(name: str, default: bool) -> bool:
    raw = os.getenv(name)
    if raw is None:
        return default
    return raw.strip().lower() in {"1", "true", "yes", "on"}


@dataclass(slots=True)
class Settings:
    """Valores de configuracion de la aplicacion.

    Attributes:
        omdb_api_key: Clave de OMDB (la demo publica es ``trilogy``).
        omdb_base_url: URL base de OMDB.
        tvmaze_base_url: URL base de TVMaze.
        timeout: Timeout por peticion HTTP, en segundos.
        max_retries: Numero de reintentos ante fallos transitorios.
        backoff_factor: Factor de espera para el backoff exponencial.
        debug: Activa logs de nivel DEBUG.
        verbose: Activa trazas detalladas del paquete.
        data_dir: Directorio donde se persisten favoritos e historial.

    Raises:
        ValueError: Si algun valor no cumple las restricciones.
    """

    omdb_api_key: str = "trilogy"
    omdb_base_url: str = "https://www.omdbapi.com/"
    tvmaze_base_url: str = "https://api.tvmaze.com"
    timeout: float = 30.0
    max_retries: int = 3
    backoff_factor: float = 0.5
    debug: bool = False
    verbose: bool = False
    data_dir: Path = field(default_factory=lambda: Path("data"))

    def __post_init__(self) -> None:
        if not self.omdb_api_key:
            raise ValueError("omdb_api_key no puede estar vacia")
        for name, url in (
            ("omdb_base_url", self.omdb_base_url),
            ("tvmaze_base_url", self.tvmaze_base_url),
        ):
            if not url.startswith(("http://", "https://")):
                raise ValueError(f"{name} debe ser una URL http(s), recibido: {url!r}")
        if self.timeout <= 0:
            raise ValueError(f"timeout debe ser > 0, recibido: {self.timeout}")
        if self.max_retries < 0:
            raise ValueError(f"max_retries debe ser >= 0, recibido: {self.max_retries}")
        if self.backoff_factor < 0:
            raise ValueError(f"backoff_factor debe ser >= 0, recibido: {self.backoff_factor}")
        if isinstance(self.data_dir, str):
            self.data_dir = Path(self.data_dir)

    @classmethod
    def from_env(cls) -> Settings:
        """Construye la configuracion a partir de variables de entorno.

        Variables reconocidas: ``OMDB_API_KEY``, ``MOVIES_TIMEOUT``,
        ``MOVIES_MAX_RETRIES``, ``MOVIES_BACKOFF_FACTOR``, ``MOVIES_DEBUG``,
        ``MOVIES_VERBOSE`` y ``MOVIES_DATA_DIR``.
        """
        return cls(
            omdb_api_key=os.getenv("OMDB_API_KEY", "trilogy"),
            timeout=float(os.getenv("MOVIES_TIMEOUT", "30")),
            max_retries=int(os.getenv("MOVIES_MAX_RETRIES", "3")),
            backoff_factor=float(os.getenv("MOVIES_BACKOFF_FACTOR", "0.5")),
            debug=_env_bool("MOVIES_DEBUG", False),
            verbose=_env_bool("MOVIES_VERBOSE", False),
            data_dir=Path(os.getenv("MOVIES_DATA_DIR", "data")),
        )
