# Arquitectura

La versión refactorizada de la aplicación está organizada como un paquete Python por capas. El objetivo es separar dominio, acceso a APIs, persistencia, lógica de negocio y presentación, con dependencias unidireccionales y contratos explícitos.

## Principios

1. No usar variables globales mutables; el estado se inyecta en objetos.
2. Mantener dependencias en una sola dirección: `ui -> services -> api/repositories -> clients/models/config`.
3. Definir contratos con `typing.Protocol` para permitir fakes y sustituir implementaciones.
4. Mantener type hints completos y `mypy --strict` en verde.
5. Traducir errores de infraestructura a excepciones de dominio específicas.
6. Aislar la persistencia JSON en repositorios reutilizables.
7. Centralizar la configuración en `Settings` y obtener la clave de OMDB desde el entorno.

## Estructura de paquetes

```text
proyecto_refactoring/
├── pyproject.toml
├── ARCHITECTURE.md
├── CHANGELOG.md
├── .env.example
├── src/movies_app/
│   ├── __init__.py
│   ├── __main__.py
│   ├── config.py
│   ├── constants.py
│   ├── logging_config.py
│   ├── protocols.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── omdb.py
│   │   └── tvmaze.py
│   ├── clients/
│   │   ├── __init__.py
│   │   └── base.py
│   ├── exceptions/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── export_error.py
│   │   ├── invalid_input.py
│   │   ├── movie_not_found.py
│   │   └── series_not_found.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── curated.py
│   │   ├── movie.py
│   │   ├── search.py
│   │   └── series.py
│   ├── repositories/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── favorites.py
│   │   └── history.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── export_service.py
│   │   ├── movie_service.py
│   │   └── series_service.py
│   └── ui/
│       ├── __init__.py
│       ├── constants.py
│       ├── console.py
│       ├── display.py
│       └── menu.py
└── tests/
    ├── __init__.py
    ├── fakes.py
    ├── unit/
    └── integration/
```

## Responsabilidades por capa

| Capa | Responsabilidad | Puede depender de |
|---|---|---|
| `models` | Entidades y datos curados del dominio | `constants` |
| `config` | Configuración tipada y lectura del entorno | `constants` |
| `exceptions` | Jerarquía de errores de dominio | — |
| `protocols` | Contratos para APIs y repositorios | `models` |
| `clients` | Transporte HTTP, timeout, reintentos y traducción HTTP | `config`, `exceptions` |
| `api` | Integración específica con OMDB y TVMaze; mapeo de payloads | `clients`, `config`, `models`, `exceptions`, `protocols` |
| `repositories` | Persistencia JSON de favoritos e historial | `models`, `exceptions` |
| `services` | Lógica de negocio y orquestación | `repositories`, `models`, `protocols`, `exceptions` |
| `ui` | Entrada y salida de consola | `services`, `models`, `exceptions` |
| `logging_config` | Configuración de logging | `config` |

Una capa no importa una capa superior. Las implementaciones de API dependen del transporte HTTP, mientras que los servicios dependen de contratos y no de una API concreta.

## Composition root

`__main__.py` construye las dependencias y las inyecta:

```python
settings = Settings.from_env()
http = HttpClient(settings)
favorites = FavoritesRepository(settings.data_dir / "favorites.json")
history = HistoryRepository(settings.data_dir / "history.json")

movies = MovieService(OmdbApi(http, settings), favorites, history)
series = SeriesService(TvmazeApi(http, settings), history)
export = ExportService(favorites, history)
MenuApp(movies, series, export, DisplayRenderer()).run()
```

No se utiliza `global` en la aplicación refactorizada. Los tests inyectan `FakeJsonClient`, `StubMovieCatalog` y `StubSeriesCatalog` mediante los contratos.

## Manejo de errores

```text
MoviesAppError
├── ApiError
│   ├── ApiTimeoutError
│   ├── ApiConnectionError
│   ├── ApiResponseError
│   └── ResourceNotFoundError
├── InvalidInputError
├── MovieNotFoundError
├── SeriesNotFoundError
└── PersistenceError
    └── ExportError
```

- `HttpClient` traduce timeouts, errores de conexión, códigos HTTP y JSON inválido.
- `MovieService` registra la búsqueda y lanza `MovieNotFoundError` cuando el catálogo no devuelve una película.
- `SeriesService` lanza `SeriesNotFoundError` cuando un identificador no existe.
- `ExportService` lanza `ExportError` para fallos de exportación o importación y `InvalidInputError` para rutas inseguras.
- Los repositorios usan `PersistenceError` para fallos de lectura o escritura.
- La UI captura `MoviesAppError`, registra el detalle y muestra un mensaje al usuario.

## Configuración y seguridad

- `OMDB_API_KEY` es obligatoria y no existe un valor por defecto en el código; se lee del entorno o de `.env`, que `__main__.py` carga con `python-dotenv` antes de construir `Settings`.
- Las rutas de exportación rechazan traversal (`..`) y nombres de archivo no permitidos.
- Los payloads se validan antes de convertirlos en modelos.
- Los secretos no se escriben en logs ni se almacenan en el repositorio.

## Estrategia de pruebas

- `tests/unit/` prueba modelos, servicios, repositorios, UI y configuración sin red.
- `tests/integration/` prueba adaptadores de API con respuestas HTTP simuladas y flujos E2E.
- `tests/fakes.py` contiene dobles de prueba reutilizables.
- `pytest-cov` exige una cobertura superior al 90%.

Comandos de validación:

```bash
python -m pytest
python -m ruff check src tests
python -m black --check src tests
python -m mypy --strict src tests
```

## Migración desde la versión legacy

| Responsabilidad legacy | Ubicación actual |
|---|---|
| Menú y salida por consola | `ui/menu.py`, `ui/console.py`, `ui/display.py` |
| Integraciones OMDB/TVMaze | `api/omdb.py`, `api/tvmaze.py` |
| Transporte HTTP | `clients/base.py` |
| Lógica de negocio | `services/` |
| Favoritos e historial | `repositories/` |
| Configuración distribuida | `config.py`, `constants.py` |
| Logging | `logging_config.py` |
| Errores de dominio | `exceptions/` |
| Datos de películas curadas | `models/curated.py` |
