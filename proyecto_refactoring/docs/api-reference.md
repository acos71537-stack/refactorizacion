# Referencia de API

## Alcance

Esta aplicación es una interfaz de consola; no expone un servidor HTTP propio. Esta referencia documenta los contratos públicos de Python, los catálogos externos que consume y los errores que forman parte de esos contratos.

## Arquitectura de acceso

Las dependencias siguen esta dirección:

```text
MenuApp → MovieService / SeriesService / ExportService
       → Protocols / Repositories
       → OmdbApi / TvmazeApi
       → HttpClient
       → OMDB / TVMaze
```

Los servicios dependen de `MovieCatalog`, `SeriesCatalog` y `Repository` mediante `typing.Protocol`; no dependen directamente de una implementación concreta de API.

## Configuración

`Settings.from_env()` crea la configuración y exige `OMDB_API_KEY`. Las variables disponibles son:

| Variable | Tipo | Valor por defecto | Uso |
|---|---|---:|---|
| `OMDB_API_KEY` | `str` | — | Credencial obligatoria de OMDB |
| `MOVIES_TIMEOUT` | `float` | `30.0` | Timeout de cada petición |
| `MOVIES_MAX_RETRIES` | `int` | `3` | Reintentos tras fallos transitorios |
| `MOVIES_BACKOFF_FACTOR` | `float` | `0.5` | Base del backoff exponencial |
| `MOVIES_DEBUG` | `bool` | `false` | Activa logs `DEBUG` |
| `MOVIES_VERBOSE` | `bool` | `false` | Activa trazas detalladas |
| `MOVIES_DATA_DIR` | `Path` | `data` | Directorio de favoritos e historial |

`Settings` valida la clave, las URLs, el timeout, los reintentos, el backoff y el directorio de datos.

## Cliente HTTP

### `HttpClient.get_json`

```python
HttpClient.get_json(url: str, params: Mapping[str, str] | None = None) -> Any
```

Ejecuta un `GET` y devuelve el cuerpo JSON. Aplica timeout y reintentos con backoff exponencial.

| Situación | Resultado |
|---|---|
| Timeout agotado | Lanza `ApiTimeoutError` |
| Fallo de conexión | Lanza `ApiConnectionError` |
| HTTP 404 | Lanza `ResourceNotFoundError` |
| HTTP 5xx | Reintenta; al agotar intentos lanza `ApiResponseError` |
| Otro HTTP no exitoso | Lanza `ApiResponseError` |
| JSON inválido | Lanza `ApiResponseError` |

## Catálogo de películas: OMDB

### `OmdbApi.search_by_title`

```python
OmdbApi.search_by_title(title: str) -> Movie | None
```

Consulta `GET https://www.omdbapi.com/` con los parámetros `t` y `apikey`. Devuelve `None` para una consulta vacía o cuando OMDB no encuentra resultados. Si la respuesta no es un objeto JSON válido, lanza `ApiResponseError`.

### `OmdbApi.search_by_actor`

```python
OmdbApi.search_by_actor(actor: str) -> list[Movie]
```

Consulta `GET https://www.omdbapi.com/` con `s`, `type=movie` y `apikey`. Devuelve una lista vacía para consultas vacías o sin resultados. Lanza `ApiResponseError` si el payload tiene una forma inesperada.

## Catálogo de series: TVMaze

### `TvmazeApi.search`

```python
TvmazeApi.search(name: str) -> list[Series]
```

Consulta `GET https://api.tvmaze.com/search/shows` con `q`. Omite resultados inválidos y registra una advertencia en el logger. Una respuesta que no sea una lista JSON lanza `ApiResponseError`.

### `TvmazeApi.get_by_id`

```python
TvmazeApi.get_by_id(series_id: int) -> Series | None
```

Consulta `GET https://api.tvmaze.com/shows/{series_id}`. Devuelve `None` cuando TVMaze responde 404. Lanza `ApiResponseError` si la respuesta no es un objeto válido y `ValueError` si falta un identificador utilizable.

## Contratos de dominio

Los contratos están definidos en `src/movies_app/protocols.py`:

| Protocolo | Método | Resultado |
|---|---|---|
| `JsonClient` | `get_json(url, params=None)` | JSON parseado |
| `MovieCatalog` | `search_by_title(title)` | `Movie | None` |
| `MovieCatalog` | `search_by_actor(actor)` | `list[Movie]` |
| `SeriesCatalog` | `search(name)` | `list[Series]` |
| `SeriesCatalog` | `get_by_id(series_id)` | `Series | None` |
| `Repository[T]` | `load()` | `list[T]` |
| `Repository[T]` | `save(items)` | `None` |

Una implementación alternativa de Movies, Series o JSON puede sustituir a las implementaciones de producción sin cambiar los servicios.

## Servicios

### `MovieService`

- `search_by_title(title: str) -> Movie`: valida la entrada, usa caché en memoria, registra la búsqueda y lanza `MovieNotFoundError` si no encuentra la película.
- `search_by_actor(actor: str) -> list[Movie]`: valida la entrada y registra la búsqueda.
- `popular_movies() -> list[Movie]`: devuelve los datos curados de películas populares.
- `movies_by_genre(genre: str) -> list[Movie]`: devuelve las películas del género o todas las curadas si el género no existe.
- `add_favorite(movie: Movie) -> bool`: agrega una película sin duplicar por título.
- `remove_favorite(title: str) -> bool`: elimina una película por título.
- `favorites() -> list[Movie]`, `history() -> list[SearchEntry]`, `clear_history() -> None`: consultan o modifican la persistencia.
- `stats() -> dict[str, int]`: devuelve los contadores de favoritos e historial.

### `SeriesService`

- `search(name: str) -> list[Series]`: valida la entrada, consulta el catálogo y registra la búsqueda.
- `get(series_id: int) -> Series`: devuelve el detalle o lanza `SeriesNotFoundError` si el catálogo devuelve `None`.

### `ExportService`

- `export_json(path: Path) -> None`: exporta favoritos e historial en un objeto JSON.
- `import_json(path: Path) -> None`: reemplaza los datos desde un archivo JSON válido.
- Rechaza rutas con `..` y nombres que no cumplan `[a-zA-Z0-9_.-]+`.

## Persistencia

`FavoritesRepository` y `HistoryRepository` usan `JsonRepository` con escritura atómica mediante un archivo temporal. `HistoryRepository` conserva las entradas más recientes primero y aplica su límite configurado.

Los archivos derivados de `Settings.data_dir` son:

- `favorites.json`: películas favoritas.
- `history.json`: entradas de búsqueda.

## Errores

```text
MoviesAppError
├── ApiError
│   ├── ApiTimeoutError
│   ├── ApiConnectionError
│   ├── ApiResponseError
│   └── ResourceNotFoundError
├── PersistenceError
│   └── ExportError
├── InvalidInputError
├── MovieNotFoundError
└── SeriesNotFoundError
```

Las operaciones de la UI capturan `MoviesAppError`; el entrypoint registra errores inesperados y devuelve un código de salida distinto de cero.

## Ejemplo de composición

El punto de entrada construye el cliente, los catálogos, los repositorios y los servicios:

```python
from movies_app.__main__ import build_app
from movies_app.config import Settings

settings = Settings.from_env()
app = build_app(settings)
app.run()
```

La aplicación requiere la variable `OMDB_API_KEY`; TVMaze no requiere credencial.
