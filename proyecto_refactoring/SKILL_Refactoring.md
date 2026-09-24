# SKILL: Refactoring

**Proposito**: Eliminar malas practicas del codigo y mejorar su estructura de forma sistematica.

**Trigger**: "refactorizar", "malas practicas", "limpiar codigo", "mejorar estructura", "code smell"

## Workflow

1. **Analizar codebase** — Revisar estructura, dependencias, cobertura de tipos, suite de tests
2. **Identificar malas practicas** — Buscar variables globales, imports wildcard, strings concatenadas, falta de type hints, codigo duplicado, bare except
3. **Planificar refactoring** — Priorizar por impacto: seguridad > estructura > rendimiento
4. **Aplicar cambios** — Usar `skill: python-pro` para guia de estilo
5. **Validar** — Ejecutar `mypy --strict src tests`, `ruff check src tests`, `black --check src tests`, `pytest`
6. **Iterar** — Si mypy/ruff/black/pytest fallan, corregir y re-validar

## Comandos de Validacion

```bash
mypy --strict src tests
ruff check src tests
black --check src tests
pytest --cov=movies_app --cov-report=term-missing
```

**Criterio de aceptacion**: 0 errores mypy, 0 errores ruff, 0 cambios black, >90% cobertura pytest.

## Patrones a Eliminar

- Variables globales mutables → reemplazar con `dataclass` o `Settings.from_env()`
- `print()` en produccion → reemplazar con `logging`
- Imports wildcard → imports especificos
- Concatenacion de strings → f-strings
- Falta de type hints → agregar type hints a todas las funciones publicas
- Codigo duplicado → extraer a funciones reutilizables
- Bare `except:` → excepciones especificas
- Configuracion hardcodeada → variables de entorno con `dataclass`
- Dependencias acopladas -> inyeccion de dependencias

## Restricciones

### MUST DO
- Type hints para todas las funciones y clases
- PEP 8 compliance con black
- Docstrings completos (Google style)
- Test coverage >90% con pytest
- Usar `X | None` en vez de `Optional[X]`
- Usar `pathlib` en vez de `os.path`
- Dataclasses para modelos de datos
- Inyeccion de dependencias via constructores
- Logging en vez de `print()`

### MUST NOT DO
- Saltar type annotations en APIs publicas
- Usar argumentos default mutables
- Ignorar errores mypy en modo strict
- Usar `except:` bare
- Hardcodear secretos o configuracion
- Usar modulo `os.path` (usar `pathlib`)
- Modificar archivos sin validar con mypy/ruff/black

## Ejemplo de Refactoring

**Antes (variable global):**
```python
CONFIG = {"api_key": "hardcoded"}
```

**Despues (dataclass con env):**
```python
@dataclass(slots=True)
class Settings:
    omdb_api_key: str = ""

    @classmethod
    def from_env(cls) -> Settings:
        api_key = os.getenv("OMDB_API_KEY")
        if not api_key:
            raise ValueError("OMDB_API_KEY no esta definida")
        return cls(omdb_api_key=api_key)
```

## Output Template

1. Archivo con type hints completos
2. Test file con fixtures
3. Confirmacion de `mypy --strict` pasa
4. Breve explificacion de patrones usadas
