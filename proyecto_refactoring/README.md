# Proyecto de Refactoring - Películas y Series

Aplicación educativa de consola para consultar películas mediante OMDB y series mediante TVMaze. El repositorio conserva la versión legacy como referencia y mantiene una implementación refactorizada en `src/movies_app/`.

## Versión refactorizada

La aplicación usa una arquitectura por capas, inyección de dependencias, type hints completos, manejo de errores de dominio y logging. La configuración se carga desde variables de entorno y la API key de OMDB no está almacenada en el código.

- [Guía de inicio rápido](docs/getting-started.md)
- [Arquitectura](ARCHITECTURE.md)
- [Changelog](CHANGELOG.md)

### Estructura principal

```text
src/movies_app/
├── __main__.py             # composition root y entrypoint
├── config.py               # Settings tipado
├── constants.py            # constantes de API, HTTP, persistencia y dominio
├── logging_config.py       # configuración de logging
├── protocols.py            # contratos con typing.Protocol
├── api/                    # OmdbApi y TvmazeApi
├── clients/                # HttpClient (transporte HTTP)
├── exceptions/             # excepciones de dominio
├── models/                 # Movie, Series, SearchEntry y datos curados
├── repositories/           # persistencia JSON de favoritos e historial
├── services/               # lógica de negocio
└── ui/                     # consola, menú y constantes de presentación

tests/
├── unit/                   # pruebas aisladas
├── integration/            # pruebas de integración y flujo E2E
└── fakes.py                # dobles de prueba reutilizables
```

### Instalación

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e ".[dev]"
Copy-Item .env.example .env
```

Linux/macOS:

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install -e ".[dev]"
cp .env.example .env
```

### Configuración

Define `OMDB_API_KEY` antes de ejecutar la aplicación. Las demás variables tienen valores por defecto:

| Variable | Descripción | Valor por defecto |
|---|---|---|
| `OMDB_API_KEY` | Clave de OMDB, obligatoria | — |
| `MOVIES_TIMEOUT` | Timeout HTTP en segundos | `30` |
| `MOVIES_MAX_RETRIES` | Reintentos para fallos transitorios | `3` |
| `MOVIES_BACKOFF_FACTOR` | Factor de backoff exponencial | `0.5` |
| `MOVIES_DEBUG` | Activa logs debug | `false` |
| `MOVIES_VERBOSE` | Activa trazas detalladas | `false` |
| `MOVIES_DATA_DIR` | Directorio de favoritos e historial | `data` |

### Ejecución

```bash
python -m movies_app
```

En Windows, usando el entorno virtual:

```powershell
.\.venv\Scripts\python.exe -m movies_app
```

### Calidad

```bash
python -m pytest
python -m ruff check src tests
python -m black --check src tests
python -m mypy --strict src tests
```

La suite incluye pruebas unitarias, integración con respuestas HTTP simuladas y un flujo E2E. La cobertura objetivo es superior al 90%.

## APIs utilizadas

- **OMDB API**: requiere `OMDB_API_KEY`.
- **TVMaze API**: pública, sin clave.

## Versión legacy

Los módulos Python de la raíz se conservan como referencia histórica del problema. La nueva aplicación no los importa. Entre los problemas corregidos están:

- Variables globales mutables y uso de `global`.
- Ausencia de separación de responsabilidades y type hints.
- Importaciones wildcard y bloques `except:` desnudos.
- Código duplicado y configuración distribuida.
- Persistencia y manejo de errores acoplados a la lógica de negocio.
- Falta de tests automatizados y logging estructurado.
