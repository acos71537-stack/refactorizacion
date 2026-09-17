"""Helpers de parseo tolerante para payloads heterogeneos de las APIs."""

from __future__ import annotations

from typing import Any

_NOT_AVAILABLE = {"N/A", "NA", "NONE", "NULL", "-"}


def clean_str(value: Any) -> str | None:
    """Normaliza un valor a texto, devolviendo ``None`` si no es util.

    Args:
        value: Valor crudo proveniente de una API.

    Returns:
        El texto limpio o ``None`` si esta vacio / es ``"N/A"``.
    """
    if value is None:
        return None
    text = str(value).strip()
    if not text or text.upper() in _NOT_AVAILABLE:
        return None
    return text


def parse_int(value: Any) -> int | None:
    """Convierte un valor a ``int`` de forma segura."""
    text = clean_str(value)
    if text is None:
        return None
    try:
        return int(text)
    except ValueError:
        return None


def parse_float(value: Any) -> float | None:
    """Convierte un valor a ``float`` de forma segura."""
    text = clean_str(value)
    if text is None:
        return None
    try:
        return float(text)
    except ValueError:
        return None


def parse_year(value: Any) -> int | None:
    """Extrae el anio de valores como ``"1994"`` o ``"1994-1995"``."""
    text = clean_str(value)
    if text is None:
        return None
    digits = ""
    for char in text:
        if not char.isdigit():
            break
        digits += char
        if len(digits) == 4:
            break
    return int(digits) if len(digits) == 4 else None
