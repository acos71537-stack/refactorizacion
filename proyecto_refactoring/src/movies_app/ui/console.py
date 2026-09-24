"""Renderizado de la interfaz de consola.

Framework de salida (write, separator, header); no conoce el dominio.
La presentacion especifica esta en ui/display.py.
"""

from __future__ import annotations

import sys
from typing import TextIO

from movies_app.ui.constants import CONSOLE_WIDTH


class ConsoleRenderer:
    """Escribe la salida de la aplicacion en un stream de texto.

    Attributes:
        width: Ancho de los separadores.
    """

    def __init__(self, output: TextIO | None = None, width: int = CONSOLE_WIDTH) -> None:
        self._out = output if output is not None else sys.stdout
        self._width = width

    def write(self, text: str = "") -> None:
        """Escribe una linea en el stream de salida."""
        print(text, file=self._out)

    def separator(self, char: str = "=") -> None:
        """Escribe un separador horizontal."""
        self.write(char * self._width)

    def header(self, text: str) -> None:
        """Escribe un encabezado centrado entre separadores."""
        self.separator()
        self.write(text.upper().center(self._width))
        self.separator()

    def write_line(self, label: str, value: object) -> None:
        """Escribe una linea etiqueta-valor."""
        self.write(f"{label}: {value}")
