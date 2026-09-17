import os
import json
import time
from datetime import datetime

# Variables globales
UI_CONFIG_FILE = "ui_config.json"
ui_config = {}

def load_ui_config():
    """Carga configuración de UI"""
    global ui_config
    
    if os.path.exists(UI_CONFIG_FILE):
        with open(UI_CONFIG_FILE, 'r') as f:
            ui_config = json.load(f)
    else:
        ui_config = {
            "theme": "dark",
            "language": "es",
            "items_per_page": 10,
            "show_posters": True,
            "animations": True,
            "font_size": 14,
            "color_scheme": "default"
        }

def save_ui_config():
    """Guarda configuración de UI"""
    with open(UI_CONFIG_FILE, 'w') as f:
        json.dump(ui_config, f, indent=4)

def get_ui_setting(key):
    """Obtiene configuración de UI"""
    return ui_config.get(key)

def set_ui_setting(key, value):
    """Establece configuración de UI"""
    ui_config[key] = value
    save_ui_config()

def get_all_ui_settings():
    """Obtiene todas las configuraciones de UI"""
    return ui_config.copy()

def reset_ui_config():
    """Resetea configuración de UI"""
    global ui_config
    ui_config = {
        "theme": "dark",
        "language": "es",
        "items_per_page": 10,
        "show_posters": True,
        "animations": True,
        "font_size": 14,
        "color_scheme": "default"
    }
    save_ui_config()

def get_theme():
    """Obtiene tema"""
    return ui_config.get("theme", "dark")

def set_theme(theme):
    """Establece tema"""
    ui_config["theme"] = theme
    save_ui_config()

def get_language():
    """Obtiene idioma"""
    return ui_config.get("language", "es")

def set_language(language):
    """Establece idioma"""
    ui_config["language"] = language
    save_ui_config()

def get_items_per_page():
    """Obtiene elementos por página"""
    return ui_config.get("items_per_page", 10)

def set_items_per_page(items):
    """Establece elementos por página"""
    ui_config["items_per_page"] = items
    save_ui_config()

def toggle_posters():
    """Alterna mostrar posters"""
    ui_config["show_posters"] = not ui_config.get("show_posters", True)
    save_ui_config()

def toggle_animations():
    """Alterna animaciones"""
    ui_config["animations"] = not ui_config.get("animations", True)
    save_ui_config()

def export_ui_config(filename):
    """Exporta configuración de UI"""
    with open(filename, 'w') as f:
        json.dump(ui_config, f, indent=4)

def import_ui_config(filename):
    """Importa configuración de UI"""
    global ui_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            ui_config = json.load(f)
        save_ui_config()
        return True
    return False

def validate_ui_config():
    """Valida configuración de UI"""
    errors = []
    
    if "theme" in ui_config:
        if ui_config["theme"] not in ["dark", "light"]:
            errors.append("Invalid theme")
    
    if "items_per_page" in ui_config:
        if not isinstance(ui_config["items_per_page"], int):
            errors.append("items_per_page must be integer")
    
    return errors

def backup_ui_config():
    """Crea backup de configuración de UI"""
    backup_name = "ui_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_ui_config(backup_name)
    return backup_name

def restore_ui_config(backup_name):
    """Restaura configuración de UI desde backup"""
    return import_ui_config(backup_name)

def get_ui_config_summary():
    """Obtiene resumen de configuración de UI"""
    return {
        "theme": get_theme(),
        "language": get_language(),
        "items_per_page": get_items_per_page()
    }

# Cargar configuración de UI al importar
load_ui_config()
