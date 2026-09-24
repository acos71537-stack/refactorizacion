# SKILL: Testing

**Proposito**: Crear tests automaticos con pytest para validar el codigo Python 3.11+.

**Trigger**: "escribir tests", "agregar test", "pytest", "testing", "crear test suite"

## Workflow

1. **Definir scope** — Identificar que probar: unidad, integracion, o e2e
2. **Crear estrategia** — Planificar approach: happy paths + error/edge cases
3. **Escribir tests** — Implementar con `skill: test-master` para guia de testing
4. **Ejecutar** — Ejecutar con `pytest --cov=movies_app --cov-report=term-missing`
5. **Reportar** — Verificar >90% cobertura, corregir gaps
6. **Validar** — Ejecutar `mypy --strict src tests`, `ruff check src tests`

## Estructura de Tests

```
tests/
  __init__.py
  conftest.py              # Fixtures compartidos
  fakes.py                 # Dobles de prueba reutilizables
  unit/
    __init__.py
    conftest.py            # Fixtures para unit tests
    test_config.py
    test_movie_service.py
    test_series_service.py
    test_models.py
    test_repositories.py
    test_http_client.py
    test_menu.py
    test_main.py
    test_export_service.py
  integration/
    __init__.py
    conftest.py            # Fixtures para integracion
    test_api_integration.py
    test_e2e_flow.py
```

## Patrones de Fixtures

```python
@pytest.fixture
def settings(tmp_path: Path) -> Settings:
    """Configuracion de prueba sin reintentos ni esperas."""
    return Settings(
        omdb_api_key="test-key",
        data_dir=tmp_path / "data",
        max_retries=0,
        backoff_factor=0.0,
    )
```

## Patrones de Dobles (tests/fakes.py)

- `FakeJsonClient` — Cliente JSON que devuelve respuestas predefinidas
- `StubMovieCatalog` — Catalogo de peliculas en memoria
- `StubSeriesCatalog` — Catalogo de series en memoria

## Comandos de Validacion

```bash
mypy --strict src tests
ruff check src tests
black --check src tests
pytest --cov=movies_app --cov-report=term-missing
```

**Criterio de aceptacion**: >90% cobertura, 0 errores mypy/ruff, 0 cambios black.

## Restricciones

### MUST DO
- Test happy paths Y error/edge cases (empty input, null, boundary values)
- Mock de dependencias externas — nunca llamar APIs reales en unit tests
- Descripciones significativas en test names (`test_search_by_title_uses_cache`)
- Asserts especificos (`assert result.title == "Inception"`)
- `@pytest.fixture` para datos de prueba
- `monkeypatch.setenv()` para variables de entorno
- `responses.activate` para mock de HTTP
- `tmp_path` para archivos temporales
- `@pytest.mark.parametrize` para parametrizacion
- Arrange-Act-Assert pattern
- Docstrings Google style en tests
- Type hints en todos los test files

### MUST NOT DO
- Saltar error-path testing
- Usar datos de produccion en tests
- Crear tests dependientes del orden
- Ignorar tests flaky
- Testar implementacion interna (testear comportamiento observable)
- Usar `pytest.raises` sin verificar el mensaje
- Hardcodear valores en fixtures sin parametrizacion
- Usar `from __future__ import annotations` sin type hints

## Patrones de Parametrizacion

```python
@pytest.mark.parametrize("title,expected", [
    ("Inception", "Inception"),
    ("  ", None),   # empty/whitespace
    ("Z", None),    # not found
])
def test_search_by_title(title: str, expected: str | None) -> None:
    ...
```

## Ejemplo de Test Completo

```python
def test_search_by_title_uses_cache(
    favorites: FavoritesRepository, history: HistoryRepository
) -> None:
    catalog = StubMovieCatalog({"Matrix": Movie(title="The Matrix")})
    service = MovieService(catalog, favorites, history)

    first = service.search_by_title("Matrix")
    second = service.search_by_title("matrix")

    assert first is not None and first.title == "The Matrix"
    assert second == first
    assert catalog.title_calls == 1
```

## Integracion con APIs

```python
@responses.activate
def test_omdb_api_search_by_title_returns_movie() -> None:
    responses.add(
        responses.GET,
        "https://www.omdbapi.com/?t=Inception&apikey=test-key",
        json={"Response": "True", "Title": "Inception", "Year": "2010"},
        status=200,
    )
    settings = Settings(omdb_api_key="test-key")
    http = HttpClient(settings)
    api = OmdbApi(http, settings)
    result = api.search_by_title("Inception")
    assert result is not None
    assert result.title == "Inception"
```

## Output Checklist

1. Test file con fixtures y type hints
2. Tests para happy paths Y casos de error
3. Tests de integracion con `responses` library
4. Tests parametrizados donde aplique
5. Confirmacion de `mypy --strict` pasa en tests
6. Confirmacion de >90% cobertura
7. Breve explificacion de patrones usadas
