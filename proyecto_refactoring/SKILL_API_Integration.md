# SKILL: API Integration

**Proposito**: Conectar a APIs REST de forma robusta y mantenible usando Python 3.11+.

**Trigger**: "conectar API", "integracion REST", "consumir API externa", "API client", "rest integration"

## Workflow

1. **Analizar dominio** — Entender el modelo de datos, endpoints y flujo de la API
2. **Diseñar cliente** — Crear una clase que envuelva `requests.Session` con timeout y reintentos
3. **Implementar** — Usar `skill: python-pro` para type hints y estilo
4. **Manejar errores** — Traducir errores HTTP a excepciones de dominio
5. **Test con mock** — Usar `responses` library para tests de integracion
6. **Validar** — Ejecutar `mypy --strict`, `ruff check`, `pytest tests/integration/`

## Estructura del Cliente

```python
class ApiClient:
    """Cliente HTTP con timeout, reintentos y traduccion de errores."""

    def __init__(self, settings: Settings, session: requests.Session | None = None) -> None:
        self._settings = settings
        self._session = session if session is not None else requests.Session()

    def get_json(self, url: str, params: Mapping[str, str] | None = None) -> Any:
        """Ejecuta un GET y devuelve el JSON parseado."""
        ...
```

## Patrones de Error Handling

Todos los errores HTTP deben traducirse a excepciones de dominio:

| Error HTTP | Excepcion |
|------------|-----------|
| 404 | `ResourceNotFoundError` |
| 500+ | `ApiResponseError` con `status_code` |
| Timeout | `ApiTimeoutError` |
| Conexion | `ApiConnectionError` |
| Generico | `ApiResponseError` |

Todos heredan de `MoviesAppError` (o `ApiError`).

## Comandos de Validacion

```bash
mypy --strict src tests
ruff check src tests
black --check src tests
pytest tests/integration/ --cov=movies_app --cov-report=term-missing
```

## Restricciones

### MUST DO
- Type hints para todas las funciones y clases
- `requests.Session` para reutilizar conexiones
- Timeout configurable en Settings
- Retrans con backoff exponencial (`delay = backoff_factor * (2**attempt)`)
- Logging de requests y responses con `get_logger`
- Traducir errores HTTP a excepciones de dominio
- Timeout y retries en `Settings`
- Usar `responses` library en tests de integracion
- Protocolos (`Protocol`) para inyeccion de dependencias
- Docstrings Google style en todos los metodos
- PEP 8 compliance con black

### MUST NOT DO
- Llamar a APIs reales en tests unitarios
- Usar `requests.get()` directamente (envolver en `HttpClient`)
- Hardcodear URLs o claves de API
- Ignorar timeouts en requests
- Usar `bare except` para errores HTTP
- Saltar type annotations
- Mezclar sync y async sin razon

## Patrones de Test para APIs

```python
@responses.activate
def test_api_search_returns_results() -> None:
    responses.add(
        responses.GET,
        "https://api.example.com/search",
        json=[{"id": 1, "name": "Item"}],
        status=200,
    )
    result = api.search("query")
    assert len(result) == 1
```

Usar `responses.matchers.query_param_matcher()` para validar params especificos.

## Ejemplo Completo

**Configuracion:**
```python
@dataclass(slots=True)
class Settings:
    omdb_api_key: str = ""
    omdb_base_url: str = "https://www.omdbapi.com/"
    timeout: float = 30.0
    max_retries: int = 3
```

**Cliente:**
```python
class OmdbApi(MovieCatalog):
    def __init__(self, http: HttpClient, settings: Settings) -> None:
        self._http = http
        self._settings = settings

    def search_by_title(self, title: str) -> Movie | None:
        payload = self._http.get_json(
            self._settings.omdb_base_url,
            params={"t": query, "apikey": self._settings.omdb_api_key},
        )
        ...
```

## Output Checklist

1. Archivo de cliente con type hints completos
2. Protocolo para inyeccion de dependencias
3. Tests de integracion con `responses` library
4. Tests de excepciones para cada tipo de error HTTP
5. Confirmacion de `mypy --strict` pasa
6. Breve explificacion de patrones usadas
