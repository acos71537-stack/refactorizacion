import os
import json
import time
from datetime import datetime

# Variables globales
THEME_CONFIG_FILE = "theme_config.json"
theme_config = {}

def load_theme_config():
    """Carga configuración de tema"""
    global theme_config
    
    if os.path.exists(THEME_CONFIG_FILE):
        with open(THEME_CONFIG_FILE, 'r') as f:
            theme_config = json.load(f)
    else:
        theme_config = {
            "name": "dark",
            "primary_color": "#007bff",
            "secondary_color": "#6c757d",
            "background_color": "#1a1a1a",
            "text_color": "#ffffff"
        }

def save_theme_config():
    """Guarda configuración de tema"""
    with open(THEME_CONFIG_FILE, 'w') as f:
        json.dump(theme_config, f, indent=4)

def get_theme_setting(key):
    """Obtiene configuración de tema"""
    return theme_config.get(key)

def set_theme_setting(key, value):
    """Establece configuración de tema"""
    theme_config[key] = value
    save_theme_config()

def get_all_theme_settings():
    """Obtiene todas las configuraciones de tema"""
    return theme_config.copy()

def reset_theme_config():
    """Resetea configuración de tema"""
    global theme_config
    theme_config = {
        "name": "dark",
        "primary_color": "#007bff",
        "secondary_color": "#6c757d",
        "background_color": "#1a1a1a",
        "text_color": "#ffffff"
    }
    save_theme_config()

def get_theme_name():
    """Obtiene nombre del tema"""
    return theme_config.get("name", "dark")

def set_theme_name(name):
    """Establece nombre del tema"""
    theme_config["name"] = name
    save_theme_config()

def get_primary_color():
    """Obtiene color primario"""
    return theme_config.get("primary_color", "#007bff")

def set_primary_color(color):
    """Establece color primario"""
    theme_config["primary_color"] = color
    save_theme_config()

def get_secondary_color():
    """Obtiene color secundario"""
    return theme_config.get("secondary_color", "#6c757d")

def set_secondary_color(color):
    """Establece color secundario"""
    theme_config["secondary_color"] = color
    save_theme_config()

def get_background_color():
    """Obtiene color de fondo"""
    return theme_config.get("background_color", "#1a1a1a")

def set_background_color(color):
    """Establece color de fondo"""
    theme_config["background_color"] = color
    save_theme_config()

def get_text_color():
    """Obtiene color de texto"""
    return theme_config.get("text_color", "#ffffff")

def set_text_color(color):
    """Establece color de texto"""
    theme_config["text_color"] = color
    save_theme_config()

def export_theme_config(filename):
    """Exporta configuración de tema"""
    with open(filename, 'w') as f:
        json.dump(theme_config, f, indent=4)

def import_theme_config(filename):
    """Importa configuración de tema"""
    global theme_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            theme_config = json.load(f)
        save_theme_config()
        return True
    return False

def validate_theme_config():
    """Valida configuración de tema"""
    errors = []
    
    for key in ["primary_color", "secondary_color", "background_color", "text_color"]:
        if key in theme_config:
            if not theme_config[key].startswith("#"):
                errors.append(key + " must be a valid hex color")
    
    return errors

def backup_theme_config():
    """Crea backup de configuración de tema"""
    backup_name = "theme_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_theme_config(backup_name)
    return backup_name

def restore_theme_config(backup_name):
    """Restaura configuración de tema desde backup"""
    return import_theme_config(backup_name)

def get_theme_config_summary():
    """Obtiene resumen de configuración de tema"""
    return {
        "name": get_theme_name(),
        "primary_color": get_primary_color(),
        "background_color": get_background_color()
    }

# Cargar configuración de tema al importar
load_theme_config()
