# Guía de inicio rápido

## Prerrequisitos

- Python 3.11 o superior
- pip

## Instalación

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

## Configuración

Edita `.env` y define una clave válida:

```dotenv
OMDB_API_KEY=tu_clave_aqui
```

`OMDB_API_KEY` es obligatoria. Las variables opcionales son:

| Variable | Descripción | Valor por defecto |
|---|---|---|
| `MOVIES_TIMEOUT` | Timeout HTTP en segundos | `30` |
| `MOVIES_MAX_RETRIES` | Reintentos para fallos transitorios | `3` |
| `MOVIES_BACKOFF_FACTOR` | Factor de backoff exponencial | `0.5` |
| `MOVIES_DEBUG` | Activa logs debug | `false` |
| `MOVIES_VERBOSE` | Activa trazas detalladas | `false` |
| `MOVIES_DATA_DIR` | Directorio de favoritos e historial | `data` |

La aplicación carga `.env` automáticamente al arrancar (`python-dotenv` en `__main__.py`). Las variables ya definidas en el entorno tienen prioridad sobre el archivo. `.env` es local y está ignorado por Git; comparte únicamente `.env.example`.

Si prefieres definir la variable sin usar `.env`:

Windows PowerShell:

```powershell
$env:OMDB_API_KEY = "tu_clave_aqui"
```

Linux/macOS:

```bash
export OMDB_API_KEY="tu_clave_aqui"
```

Nunca subas `.env` al repositorio; comparte únicamente `.env.example`.

## Ejecución

```bash
python -m movies_app
```

Con el entorno virtual de Windows:

```powershell
.\.venv\Scripts\python.exe -m movies_app
```

## Pruebas

```bash
python -m pytest
python -m pytest tests/unit/
python -m pytest tests/integration/
python -m pytest --cov=movies_app --cov-report=term-missing
```

## Calidad del código

```bash
python -m mypy --strict src tests
python -m ruff check src tests
python -m black --check src tests
```

## Estructura del proyecto

```text
proyecto_refactoring/
├── pyproject.toml
├── .env.example
├── CHANGELOG.md
├── ARCHITECTURE.md
├── docs/
│   ├── getting-started.md
│   ├── testing.md
│   └── api-reference.md
├── src/movies_app/
│   ├── __main__.py
│   ├── config.py
│   ├── constants.py
│   ├── exceptions/
│   ├── logging_config.py
│   ├── models/
│   │   ├── curated.py
│   │   ├── movie.py
│   │   ├── search.py
│   │   └── series.py
│   ├── protocols.py
│   ├── api/
│   ├── clients/
│   ├── services/
│   └── ui/
├── tests/
│   ├── fakes.py
│   ├── unit/
│   └── integration/
└── SKILL_*.md
```
