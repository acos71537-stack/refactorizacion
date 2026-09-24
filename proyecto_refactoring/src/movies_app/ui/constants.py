"""Constantes de presentacion de la interfaz de consola."""

from __future__ import annotations

CONSOLE_WIDTH = 60
SUMMARY_MAX_LENGTH = 200
EXIT_OPTION = "11"
MENU_OPTIONS: tuple[str, ...] = (
    "1. Buscar pelicula por titulo",
    "2. Buscar por actor",
    "3. Buscar series",
    "4. Ver peliculas populares",
    "5. Buscar por genero",
    "6. Ver favoritos",
    "7. Ver historial",
    "8. Ver estadisticas",
    "9. Exportar datos",
    "10. Importar datos",
    f"{EXIT_OPTION}. Salir",
)

__all__ = ["CONSOLE_WIDTH", "EXIT_OPTION", "MENU_OPTIONS", "SUMMARY_MAX_LENGTH"]
