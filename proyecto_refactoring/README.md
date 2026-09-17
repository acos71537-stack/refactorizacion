# Proyecto de Refactoring - Películas y Series

Proyecto educativo que conecta a APIs públicas de películas (OMDB y TVMaze) sin
requerir API keys. Incluye una versión original con malas prácticas
intencionales y su refactorización completa.

## Versión refactorizada (nueva)

El paquete `src/movies_app/` implementa una arquitectura por capas, sin variables
globales, con type hints completos, inyección de dependencias, manejo de errores
específico y tests.

Ver [`ARCHITECTURE.md`](ARCHITECTURE.md) para el diseño detallado y el mapeo
desde los módulos originales.

```
src/movies_app/
├── config.py            # Settings (dataclass) - reemplaza los 88 *_config.py
├── exceptions.py        # jerarquía de errores de dominio
├── logging_config.py    # logging centralizado (reemplaza logger/log_manager)
├── protocols.py         # contratos: JsonClient, MovieCatalog, SeriesCatalog, Repository
├── models/              # Movie, Series, SearchEntry (dataclasses inmutables)
├── clients/             # HttpClient + OmdbClient + TvmazeClient
├── repositories/        # persistencia JSON atómica (favoritos, historial)
├── services/            # lógica de negocio (MovieService, SeriesService, ExportService)
└── ui/                  # ConsoleRenderer + MenuApp
```

### Instalación

```bash
python -m venv .venv
.venv\Scripts\python.exe -m pip install -e ".[dev]"   # Windows
# source .venv/bin/activate && pip install -e ".[dev]"  # Linux/macOS
```

### Ejecución

```bash
python -m movies_app
```

Variables de entorno opcionales: `OMDB_API_KEY`, `MOVIES_TIMEOUT`,
`MOVIES_MAX_RETRIES`, `MOVIES_BACKOFF_FACTOR`, `MOVIES_DEBUG`, `MOVIES_VERBOSE`,
`MOVIES_DATA_DIR`.

### Calidad

```bash
python -m pytest          # tests + cobertura (>=90%)
python -m ruff check src tests
python -m black --check src tests
python -m mypy src tests  # modo estricto
```

## APIs Utilizadas

- **OMDB API**: demo key `trilogy` (no requiere registro).
- **TVMaze API**: pública, sin key.

## Versión original (legacy)

Los siguientes módulos del directorio raíz se conservan como referencia de las
malas prácticas originales: `main.py`, `api_movies.py` y los `*_manager.py`.

Malas prácticas que la refactorización corrigió:

- Variables globales mutables y `global` en todas partes.
- Sin separación de responsabilidades ni principio SOLID.
- 88 archivos `*_config.py` sin importadores (código muerto) — eliminados.
- Módulos duplicados (`app.py`, `*_v2`, `logger.py`/`log_manager.py`) — eliminados.
- Sin type hints, `from api_movies import *`, `bare except:` (27 casos).
- Strings hardcodeados, concatenación en vez de f-strings, sin `logging`.
- Sin tests, sin virtual environment.

### Ejecutar la versión legacy

```bash
python main.py
```
