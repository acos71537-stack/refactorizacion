# Changelog

Todos los cambios significativos de la refactorización se documentan aquí.

## [Unreleased]

### Fase 8: Evaluación final y documentación

- Mover los datos curados de `services/curated.py` a `models/curated.py`.
- Extraer las constantes de presentación a `ui/constants.py`.
- Usar `MovieNotFoundError` y `SeriesNotFoundError` en los servicios.
- Usar `ExportError` para operaciones de exportación e importación.
- Actualizar contratos y fakes para soportar series no encontradas.
- Actualizar la documentación de arquitectura, README y guía de inicio rápido.
- Validación final: 113 tests, 92% de cobertura, `mypy --strict`, `ruff` y `black` en verde.

### Fase 7: Skills de proyecto

- Crear `SKILL_Refactoring.md` con workflow, patrones a eliminar y restricciones.
- Crear `SKILL_API_Integration.md` con clientes HTTP, errores y pruebas con `responses`.
- Crear `SKILL_Testing.md` con estructura de pruebas, fixtures y cobertura.

### Fase 6: Seguridad

- Eliminar `DEFAULT_OMDB_API_KEY = "trilogy"` de `constants.py`.
- Hacer que `Settings.from_env()` requiera `OMDB_API_KEY` como variable de entorno.
- Crear `.env.example` con las variables soportadas.
- Validar entradas con `InvalidInputError` en menú, servicios y exportación.
- Proteger la exportación contra path traversal.

### Fase 5: Estructura de pruebas

- Crear `tests/unit/` e `tests/integration/`.
- Mover los tests existentes a `tests/unit/`.
- Crear `tests/fakes.py` con dobles reutilizables.
- Añadir pruebas de integración de APIs y flujo E2E.
- Resultado anterior: 111 tests y 92% de cobertura.

### Fase 4: Manejo de errores

- Crear el paquete `src/movies_app/exceptions/`.
- Sustituir `print()` por logging en la composición de la aplicación.
- Añadir logging a servicios y menú.
- Eliminar el módulo legacy `exceptions.py`.

### Fase 3: Separación de responsabilidades

- Crear `src/movies_app/api/` con `OmdbApi` y `TvmazeApi`.
- Crear `ui/display.py` con `DisplayRenderer`.
- Refactorizar `ui/console.py` a una capa de transporte de salida.
- Integrar los servicios con la nueva capa de APIs.

## Historial anterior

- **Versión 0.1 (legacy):** módulos planos, configuración distribuida, acoplamiento de responsabilidades y cobertura de pruebas insuficiente.
