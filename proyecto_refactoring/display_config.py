import os
import json
import time
from datetime import datetime

# Variables globales
DISPLAY_CONFIG_FILE = "display_config.json"
display_config = {}

def load_display_config():
    """Carga configuración de visualización"""
    global display_config
    
    if os.path.exists(DISPLAY_CONFIG_FILE):
        with open(DISPLAY_CONFIG_FILE, 'r') as f:
            display_config = json.load(f)
    else:
        display_config = {
            "theme": "dark",
            "font_size": 14,
            "show_icons": True,
            "animations": True,
            "compact_mode": False
        }

def save_display_config():
    """Guarda configuración de visualización"""
    with open(DISPLAY_CONFIG_FILE, 'w') as f:
        json.dump(display_config, f, indent=4)

def get_display_setting(key):
    """Obtiene configuración de visualización"""
    return display_config.get(key)

def set_display_setting(key, value):
    """Establece configuración de visualización"""
    display_config[key] = value
    save_display_config()

def get_all_display_settings():
    """Obtiene todas las configuraciones de visualización"""
    return display_config.copy()

def reset_display_config():
    """Resetea configuración de visualización"""
    global display_config
    display_config = {
        "theme": "dark",
        "font_size": 14,
        "show_icons": True,
        "animations": True,
        "compact_mode": False
    }
    save_display_config()

def get_theme():
    """Obtiene tema"""
    return display_config.get("theme", "dark")

def set_theme(theme):
    """Establece tema"""
    display_config["theme"] = theme
    save_display_config()

def get_font_size():
    """Obtiene tamaño de fuente"""
    return display_config.get("font_size", 14)

def set_font_size(size):
    """Establece tamaño de fuente"""
    display_config["font_size"] = size
    save_display_config()

def is_icons_enabled():
    """Verifica si iconos están habilitados"""
    return display_config.get("show_icons", True)

def enable_icons():
    """Habilita iconos"""
    display_config["show_icons"] = True
    save_display_config()

def disable_icons():
    """Deshabilita iconos"""
    display_config["show_icons"] = False
    save_display_config()

def is_animations_enabled():
    """Verifica si animaciones están habilitadas"""
    return display_config.get("animations", True)

def enable_animations():
    """Habilita animaciones"""
    display_config["animations"] = True
    save_display_config()

def disable_animations():
    """Deshabilita animaciones"""
    display_config["animations"] = False
    save_display_config()

def is_compact_mode():
    """Verifica si modo compacto está habilitado"""
    return display_config.get("compact_mode", False)

def enable_compact_mode():
    """Habilita modo compacto"""
    display_config["compact_mode"] = True
    save_display_config()

def disable_compact_mode():
    """Deshabilita modo compacto"""
    display_config["compact_mode"] = False
    save_display_config()

def export_display_config(filename):
    """Exporta configuración de visualización"""
    with open(filename, 'w') as f:
        json.dump(display_config, f, indent=4)

def import_display_config(filename):
    """Importa configuración de visualización"""
    global display_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            display_config = json.load(f)
        save_display_config()
        return True
    return False

def validate_display_config():
    """Valida configuración de visualización"""
    errors = []
    
    if "font_size" in display_config:
        if not isinstance(display_config["font_size"], int):
            errors.append("font_size must be integer")
    
    return errors

def backup_display_config():
    """Crea backup de configuración de visualización"""
    backup_name = "display_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_display_config(backup_name)
    return backup_name

def restore_display_config(backup_name):
    """Restaura configuración de visualización desde backup"""
    return import_display_config(backup_name)

def get_display_config_summary():
    """Obtiene resumen de configuración de visualización"""
    return {
        "theme": get_theme(),
        "font_size": get_font_size(),
        "show_icons": is_icons_enabled()
    }

# Cargar configuración de visualización al importar
load_display_config()
