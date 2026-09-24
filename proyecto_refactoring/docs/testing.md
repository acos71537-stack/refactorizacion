# Guía de pruebas

## Objetivo

La suite verifica el comportamiento observable de la aplicación sin realizar llamadas reales a OMDB ni a TVMaze. Las pruebas unitarias cubren componentes aislados y las pruebas de integración cubren el flujo entre servicios, repositorios y UI.

## Requisitos

Instala las dependencias de desarrollo desde la raíz del proyecto:

```bash
python -m pip install -e ".[dev]"
```

En Windows, usando el entorno virtual del proyecto:

```powershell
.\.venv\Scripts\python.exe -m pip install -e ".[dev]"
```

## Ejecución de la suite

La configuración de `pyproject.toml` activa la cobertura y establece un mínimo obligatorio del 90 %:

```bash
python -m pytest
python -m ruff check src tests
python -m black --check src tests
python -m mypy --strict src tests
```

Con el entorno virtual de Windows:

```powershell
.\.venv\Scripts\python.exe -m pytest
.\.venv\Scripts\python.exe -m ruff check src tests
.\.venv\Scripts\python.exe -m black --check src tests
.\.venv\Scripts\python.exe -m mypy --strict src tests
```

La suite completa debe pasar los cuatro controles. El comando `pytest` incluye `--cov=movies_app`, el informe de líneas faltantes y `--cov-fail-under=90`.

## Organización

| Ruta | Tipo | Alcance |
|---|---|---|
| `tests/unit/` | Unitarias | Componentes y casos de error con dobles o simulaciones |
| `tests/integration/` | Integración | Flujos entre servicios, persistencia y UI |
| `tests/fakes.py` | Dobles reutilizables | `FakeJsonClient`, `StubMovieCatalog` y `StubSeriesCatalog` |
| `tests/unit/conftest.py` | Fixtures | Configuración y repositorios aislados con `tmp_path` |
| `tests/integration/conftest.py` | Fixtures | Aplicación completa con catálogos simulados |

La suite actual contiene 113 pruebas: 97 unitarias y 16 de integración.

## Estrategia de aislamiento

- Las pruebas unitarias no acceden a la red. Sustituyen el cliente HTTP o el catálogo mediante `FakeJsonClient` y los stubs de `tests/fakes.py`.
- Las pruebas de integración que necesitan HTTP usan `responses` para registrar respuestas simuladas.
- Las pruebas de persistencia usan `tmp_path`; ningún test modifica el directorio `data` del usuario.
- `monkeypatch` se utiliza para sustituir funciones de sistema, como el tiempo o la entrada estándar.
- Cada test debe ser independiente y no debe depender del orden de ejecución.

## Casos que deben cubrirse

Al añadir una prueba, incluye, cuando corresponda:

1. El camino feliz y el resultado exacto esperado.
2. Entradas vacías, espacios o valores límite.
3. Datos remotos ausentes o malformados.
4. Errores HTTP, timeouts, errores de conexión y reintentos.
5. Persistencia, serialización y corrupción de archivos.
6. Validación de rutas y errores de exportación.

Usa aserciones específicas sobre valores observables. Evita comprobar únicamente que un resultado sea verdadero o falso.

## Ejecutar subconjuntos

Para ejecutar únicamente una parte durante el desarrollo:

```bash
python -m pytest tests/unit
python -m pytest tests/integration
python -m pytest tests/unit/test_http_client.py
```

El umbral de cobertura está diseñado para la suite completa. Si pytest rechaza un subconjunto por cobertura inferior al 90 %, ejecuta ese subconjunto con la cobertura desactivada:

```bash
python -m pytest tests/unit --no-cov
python -m pytest tests/integration --no-cov
```

## Cobertura

Para consultar el detalle de líneas faltantes:

```bash
python -m pytest --cov=movies_app --cov-report=term-missing
```

Para generar un informe HTML local:

```bash
python -m pytest --cov=movies_app --cov-report=html
```

El informe se crea en `htmlcov/`. Antes de entregar el proyecto, ejecuta la suite completa y comprueba que la cobertura se mantiene en, al menos, 90 %.
