# Auditoría de archivos `*_config.py` no usados

Documento de cierre del punto 5 de la Fase 1: identificar y documentar los
archivos `*_config.py` que **no eran utilizados** por ningún módulo.

## Objetivo

Dejar constancia, archivo por archivo, de qué módulos `*_config.py` eran código
muerto (cero importadores), su justificación y la acción tomada sobre ellos.

## Metodología

Análisis estático sobre los 118 módulos `.py` del directorio raíz del proyecto:

1. Se extrajeron todas las sentencias `import` / `from … import` de cada archivo.
2. Se buscaron importaciones dinámicas: `__import__`, `importlib`, `exec(`, `eval(`.
3. Se comparó cada nombre de módulo local contra quién lo importaba.

Resultado del análisis:

- El **único** import entre módulos locales del proyecto era `main.py → api_movies`
  (mediante `from api_movies import *`).
- **Ningún** archivo importaba un módulo `*_config.py`.
- No existían importaciones dinámicas.
- Cada `*_config.py` ejecutaba `load_..._config()` al final del archivo, pero como
  nunca era importado por nadie, ese código no se ejecutaba en la aplicación.

## Resumen

| Métrica | Cantidad |
|---------|---------:|
| Archivos `*_config.py` analizados | 88 |
| Con 0 importadores (código muerto) | 88 (100%) |
| `api_cache_*_config.py` | 48 |
| Otros `api_*_config.py` | 19 |
| Otros `*_config.py` | 21 |

## Inventario

Todos los archivos listados tienen **0 importadores**. Estado: eliminados en el
commit `95c2a9d`.

| # | Archivo | Categoría | Importadores | Estado |
|---:|---------|-----------|:---:|--------|
| 1 | `accessibility_config.py` | general | 0 | Eliminado |
| 2 | `api_auth_config.py` | API | 0 | Eliminado |
| 3 | `api_bulkhead_config.py` | API | 0 | Eliminado |
| 4 | `api_cache_alerting_config.py` | cache API | 0 | Eliminado |
| 5 | `api_cache_analytics_config.py` | cache API | 0 | Eliminado |
| 6 | `api_cache_architecture_config.py` | cache API | 0 | Eliminado |
| 7 | `api_cache_best_practices_config.py` | cache API | 0 | Eliminado |
| 8 | `api_cache_cleanup_config.py` | cache API | 0 | Eliminado |
| 9 | `api_cache_collaboration_config.py` | cache API | 0 | Eliminado |
| 10 | `api_cache_compliance_config.py` | cache API | 0 | Eliminado |
| 11 | `api_cache_compression_config.py` | cache API | 0 | Eliminado |
| 12 | `api_cache_config.py` | cache API | 0 | Eliminado |
| 13 | `api_cache_debug_config.py` | cache API | 0 | Eliminado |
| 14 | `api_cache_deprecation_config.py` | cache API | 0 | Eliminado |
| 15 | `api_cache_deprecation_schedule_config.py` | cache API | 0 | Eliminado |
| 16 | `api_cache_disaster_recovery_config.py` | cache API | 0 | Eliminado |
| 17 | `api_cache_distribution_config.py` | cache API | 0 | Eliminado |
| 18 | `api_cache_documentation_config.py` | cache API | 0 | Eliminado |
| 19 | `api_cache_evolution_config.py` | cache API | 0 | Eliminado |
| 20 | `api_cache_failover_config.py` | cache API | 0 | Eliminado |
| 21 | `api_cache_future_config.py` | cache API | 0 | Eliminado |
| 22 | `api_cache_governance_config.py` | cache API | 0 | Eliminado |
| 23 | `api_cache_innovation_config.py` | cache API | 0 | Eliminado |
| 24 | `api_cache_integration_config.py` | cache API | 0 | Eliminado |
| 25 | `api_cache_intelligence_config.py` | cache API | 0 | Eliminado |
| 26 | `api_cache_invalidation_config.py` | cache API | 0 | Eliminado |
| 27 | `api_cache_legacy_config.py` | cache API | 0 | Eliminado |
| 28 | `api_cache_lifecycle_config.py` | cache API | 0 | Eliminado |
| 29 | `api_cache_load_testing_config.py` | cache API | 0 | Eliminado |
| 30 | `api_cache_mentoring_config.py` | cache API | 0 | Eliminado |
| 31 | `api_cache_metrics_config.py` | cache API | 0 | Eliminado |
| 32 | `api_cache_migration_config.py` | cache API | 0 | Eliminado |
| 33 | `api_cache_migration_schedule_config.py` | cache API | 0 | Eliminado |
| 34 | `api_cache_monitoring_config.py` | cache API | 0 | Eliminado |
| 35 | `api_cache_observability_config.py` | cache API | 0 | Eliminado |
| 36 | `api_cache_performance_config.py` | cache API | 0 | Eliminado |
| 37 | `api_cache_performance_testing_config.py` | cache API | 0 | Eliminado |
| 38 | `api_cache_preloading_config.py` | cache API | 0 | Eliminado |
| 39 | `api_cache_recommendations_config.py` | cache API | 0 | Eliminado |
| 40 | `api_cache_recovery_config.py` | cache API | 0 | Eliminado |
| 41 | `api_cache_reporting_config.py` | cache API | 0 | Eliminado |
| 42 | `api_cache_resilience_testing_config.py` | cache API | 0 | Eliminado |
| 43 | `api_cache_scalability_config.py` | cache API | 0 | Eliminado |
| 44 | `api_cache_security_config.py` | cache API | 0 | Eliminado |
| 45 | `api_cache_security_testing_config.py` | cache API | 0 | Eliminado |
| 46 | `api_cache_serialization_config.py` | cache API | 0 | Eliminado |
| 47 | `api_cache_stress_testing_config.py` | cache API | 0 | Eliminado |
| 48 | `api_cache_testing_config.py` | cache API | 0 | Eliminado |
| 49 | `api_cache_training_config.py` | cache API | 0 | Eliminado |
| 50 | `api_cache_validation_config.py` | cache API | 0 | Eliminado |
| 51 | `api_cache_warming_config.py` | cache API | 0 | Eliminado |
| 52 | `api_caching_strategy_config.py` | API | 0 | Eliminado |
| 53 | `api_circuit_breaker_config.py` | API | 0 | Eliminado |
| 54 | `api_config.py` | API | 0 | Eliminado |
| 55 | `api_debug_config.py` | API | 0 | Eliminado |
| 56 | `api_degradation_config.py` | API | 0 | Eliminado |
| 57 | `api_error_handling_config.py` | API | 0 | Eliminado |
| 58 | `api_failover_config.py` | API | 0 | Eliminado |
| 59 | `api_logging_config.py` | API | 0 | Eliminado |
| 60 | `api_monitoring_config.py` | API | 0 | Eliminado |
| 61 | `api_performance_config.py` | API | 0 | Eliminado |
| 62 | `api_rate_limit_config.py` | API | 0 | Eliminado |
| 63 | `api_rate_limiter_config.py` | API | 0 | Eliminado |
| 64 | `api_retry_config.py` | API | 0 | Eliminado |
| 65 | `api_security_config.py` | API | 0 | Eliminado |
| 66 | `api_testing_config.py` | API | 0 | Eliminado |
| 67 | `api_timeout_config.py` | API | 0 | Eliminado |
| 68 | `api_timeout_retry_config.py` | API | 0 | Eliminado |
| 69 | `backup_config.py` | general | 0 | Eliminado |
| 70 | `cache_config.py` | general | 0 | Eliminado |
| 71 | `cache_expiry_config.py` | general | 0 | Eliminado |
| 72 | `database_config.py` | general | 0 | Eliminado |
| 73 | `debug_config.py` | general | 0 | Eliminado |
| 74 | `display_config.py` | general | 0 | Eliminado |
| 75 | `email_config.py` | general | 0 | Eliminado |
| 76 | `language_config.py` | general | 0 | Eliminado |
| 77 | `log_config.py` | general | 0 | Eliminado |
| 78 | `maintenance_config.py` | general | 0 | Eliminado |
| 79 | `network_config.py` | general | 0 | Eliminado |
| 80 | `notification_config.py` | general | 0 | Eliminado |
| 81 | `performance_config.py` | general | 0 | Eliminado |
| 82 | `privacy_config.py` | general | 0 | Eliminado |
| 83 | `proxy_config.py` | general | 0 | Eliminado |
| 84 | `search_config.py` | general | 0 | Eliminado |
| 85 | `security_config.py` | general | 0 | Eliminado |
| 86 | `storage_config.py` | general | 0 | Eliminado |
| 87 | `theme_config.py` | general | 0 | Eliminado |
| 88 | `ui_config.py` | general | 0 | Eliminado |

## Acción tomada y recuperación

- Los 88 archivos fueron **eliminados** en el commit `95c2a9d`.
- Su funcionalidad quedó reemplazada por:
  - `src/movies_app/config.py` — `Settings` (dataclass) con validación y `from_env`.
  - `src/movies_app/constants.py` — valores constantes y por defecto.
- Para recuperar cualquiera de ellos:

  ```bash
  git checkout 95c2a9d^ -- proyecto_refactoring/<archivo>.py
  ```

## Anexo: otros duplicados eliminados

Además de los 88 `*_config.py`, el commit `95c2a9d` eliminó 5 módulos duplicados
(93 archivos en total). Todos eran islas sin importadores.

| Archivo | Motivo | Reemplazo en `src/` |
|---------|--------|---------------------|
| `app.py` | Duplicado de `main.py` + `api_movies.py` (menú y lógica OMDB/TVMaze embebidos) | `ui/menu.py`, `ui/console.py`, `services/`, `clients/` |
| `cache_manager.py` vs `cache_manager_v2.py` | Dos implementaciones del mismo gestor de caché | `clients/base.py` (caché en memoria) y `repositories/` |
| `config_manager.py` vs `config_manager_v2.py` | Dos implementaciones del mismo gestor de configuración | `config.py` |
| `logger.py` vs `log_manager.py` | Dos implementaciones del mismo sistema de logging | `logging_config.py` |

Recuperación de cualquiera de ellos:

```bash
git checkout 95c2a9d^ -- proyecto_refactoring/<archivo>.py
```

> Nota: `main.py`, `api_movies.py` y los `*_manager.py` restantes se conservaron
> como referencia de la versión original con malas prácticas.
