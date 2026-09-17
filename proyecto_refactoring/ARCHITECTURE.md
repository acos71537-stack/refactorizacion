# Arquitectura objetivo

Documento de diseño para la refactorización del sistema de películas y series.
Reemplaza el diseño actual (118 archivos planos, variables globales y sin capas)
por un paquete Python con responsabilidades separadas y dependencias unidireccionales.

## Principios

1. **Sin variables globales mutables.** Todo el estado vive en objetos inyectados.
2. **Dependencias unidireccionales:** `ui -> services -> (clients, repositories) -> models/config`.
3. **Contratos explícitos:** interfaces con `typing.Protocol`; implementaciones intercambiables (DI).
4. **Type hints completos** y `mypy --strict` en verde.
5. **Errores específicos:** excepciones de dominio, nunca `except:` desnudo.
6. **Persistencia aislada** en repositorios JSON reutilizables.
7. **Configuración centralizada** en un único `Settings` (dataclass), sin 88 archivos `*_config.py`.

## Estructura de paquetes

```
proyecto_refactoring/
├── pyproject.toml
├── ARCHITECTURE.md
├── src/
│   └── movies_app/
│       ├── __init__.py
│       ├── __main__.py            # entrypoint: python -m movies_app
│       ├── config.py              # Settings (dataclass) - reemplaza global CONFIG/api_config
│       ├── exceptions.py          # jerarquía de errores de dominio
│       ├── logging_config.py      # configuración de logging (reemplaza print/logger.py)
│       ├── protocols.py           # Protocol: MovieCatalog, SeriesCatalog, Repository
│       ├── models/
│       │   ├── __init__.py
│       │   ├── movie.py           # Movie (dataclass) + Movie.from_omdb
│       │   ├── series.py          # Series (dataclass) + Series.from_tvmaze
│       │   └── search.py          # SearchEntry
│       ├── clients/
│       │   ├── __init__.py
│       │   ├── base.py            # HttpClient: timeout, retries, errores HTTP
│       │   ├── omdb.py            # OmdbClient(MovieCatalog)
│       │   └── tvmaze.py          # TvmazeClient(SeriesCatalog)
│       ├── repositories/
│       │   ├── __init__.py
│       │   ├── base.py            # JsonRepository[T] genérico (load/save atómico)
│       │   ├── favorites.py       # FavoritesRepository
│       │   └── history.py         # HistoryRepository
│       ├── services/
│       │   ├── __init__.py
│       │   ├── movie_service.py   # MovieService: orquesta cliente + repos + cache
│       │   └── series_service.py  # SeriesService
│       └── ui/
│           ├── __init__.py
│           ├── console.py         # ConsoleRenderer (presentación pura)
│           └── menu.py            # MenuApp (bucle de la aplicación)
└── tests/
    ├── conftest.py
    ├── test_omdb_client.py
    ├── test_tvmaze_client.py
    ├── test_movie_service.py
    ├── test_repositories.py
    └── test_models.py
```

## Responsabilidades por capa

| Capa | Responsabilidad | Puede depender de |
|------|-----------------|-------------------|
| `models` | Entidades inmutables y parseo de payloads de API | — (solo stdlib) |
| `config` | Valores de configuración tipados | `models` |
| `exceptions` | Errores de dominio | — |
| `protocols` | Contratos (interfaces) | `models` |
| `clients` | HTTP contra OMDB/TVMaze; traducen JSON -> modelos | `models`, `exceptions`, `config`, `protocols` |
| `repositories` | Persistencia JSON de favoritos/historial | `models`, `exceptions`, `protocols` |
| `services` | Lógica de negocio; orquestan clients + repos | `clients`, `repositories`, `models` |
| `ui` | Entrada/salida de consola | `services`, `models` |
| `logging_config` | Configuración de `logging` | `config` |

Regla: una capa **nunca** importa de una capa superior.

## Mapeo origen -> destino

| Archivo actual | Destino |
|----------------|---------|
| `api_movies.py` (globals, requests, cache) | `clients/omdb.py`, `clients/tvmaze.py`, `services/movie_service.py`, `services/series_service.py` |
| `main.py` (menú + print) | `ui/menu.py`, `ui/console.py`, `__main__.py` |
| `app.py` (duplicado de main) | Eliminado (cubierto por `ui/`) |
| `utils.py` (13 bare except) | Utilidades absorbidas por `ui/console.py` y modelos |
| `favorites_manager.py`, `history_manager.py` | `repositories/favorites.py`, `repositories/history.py` |
| `data_manager.py`, `export_manager.py` | `repositories/base.py` + `services` |
| `stats_manager.py` | `services` (contadores) |
| `logger.py`, `log_manager.py` | `logging_config.py` |
| `cache_manager.py`, `cache_manager_v2.py` | `clients/base.py` (caché en memoria) |
| `config_manager.py`, `config_manager_v2.py`, `api_config.py`, `api_cache_config.py` | `config.py` |
| 88 `*_config.py` (47 `api_cache_*`) | Eliminados (sin importadores) |

## Gestión de dependencias (DI)

```python
# __main__.py (composition root)
settings = Settings.from_env()
client = OmdbClient(HttpClient(settings), settings)
favorites = FavoritesRepository(settings.data_dir / "favorites.json")
history = HistoryRepository(settings.data_dir / "history.json")
service = MovieService(client, favorites, history)
MenuApp(service, SeriesService(...), ConsoleRenderer()).run()
```

Ninguna función usa `global`. Los tests inyectan dobles (fakes/mocks) vía los `Protocol`.

## Manejo de errores

```
MoviesAppError
├── ApiError
│   ├── ApiTimeoutError
│   ├── ApiConnectionError
│   └── ApiResponseError      # status HTTP != 2xx o JSON inválido
├── ResourceNotFoundError
└── PersistenceError          # fallo de lectura/escritura JSON
```

Los clientes traducen `requests`/`json` a estas excepciones; los servicios deciden
si degradar (p. ej. devolver lista vacía) y la UI muestra mensajes.

## Fases de ejecución

- **Fase 2 (esta):** diseño, `pyproject.toml`, esqueleto e interfaces (modelos, errores, config, protocols).
- **Fase 3:** implementar `clients` + `services` y cablear `__main__.py`.
- **Fase 4:** eliminar duplicados (`app.py`, `*_v2`, `logger/log_manager`) y los 88 `*_config.py`.
- **Fase 5:** tests con `pytest`, `mypy --strict`, `ruff`, `black`.
