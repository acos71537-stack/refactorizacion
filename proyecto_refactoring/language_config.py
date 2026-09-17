import os
import json
import time
from datetime import datetime

# Variables globales
LANGUAGE_CONFIG_FILE = "language_config.json"
language_config = {}

def load_language_config():
    """Carga configuración de idioma"""
    global language_config
    
    if os.path.exists(LANGUAGE_CONFIG_FILE):
        with open(LANGUAGE_CONFIG_FILE, 'r') as f:
            language_config = json.load(f)
    else:
        language_config = {
            "current": "es",
            "available": ["es", "en", "pt"],
            "fallback": "en"
        }

def save_language_config():
    """Guarda configuración de idioma"""
    with open(LANGUAGE_CONFIG_FILE, 'w') as f:
        json.dump(language_config, f, indent=4)

def get_language_setting(key):
    """Obtiene configuración de idioma"""
    return language_config.get(key)

def set_language_setting(key, value):
    """Establece configuración de idioma"""
    language_config[key] = value
    save_language_config()

def get_all_language_settings():
    """Obtiene todas las configuraciones de idioma"""
    return language_config.copy()

def reset_language_config():
    """Resetea configuración de idioma"""
    global language_config
    language_config = {
        "current": "es",
        "available": ["es", "en", "pt"],
        "fallback": "en"
    }
    save_language_config()

def get_current_language():
    """Obtiene idioma actual"""
    return language_config.get("current", "es")

def set_current_language(language):
    """Establece idioma actual"""
    language_config["current"] = language
    save_language_config()

def get_available_languages():
    """Obtiene idiomas disponibles"""
    return language_config.get("available", ["es", "en", "pt"])

def add_language(language):
    """Agrega idioma disponible"""
    if "available" not in language_config:
        language_config["available"] = []
    
    if language not in language_config["available"]:
        language_config["available"].append(language)
        save_language_config()
        return True
    return False

def remove_language(language):
    """Elimina idioma disponible"""
    if "available" in language_config:
        if language in language_config["available"]:
            language_config["available"].remove(language)
            save_language_config()
            return True
    return False

def get_fallback_language():
    """Obtiene idioma de respaldo"""
    return language_config.get("fallback", "en")

def set_fallback_language(language):
    """Establece idioma de respaldo"""
    language_config["fallback"] = language
    save_language_config()

def is_language_available(language):
    """Verifica si idioma está disponible"""
    return language in get_available_languages()

def export_language_config(filename):
    """Exporta configuración de idioma"""
    with open(filename, 'w') as f:
        json.dump(language_config, f, indent=4)

def import_language_config(filename):
    """Importa configuración de idioma"""
    global language_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            language_config = json.load(f)
        save_language_config()
        return True
    return False

def validate_language_config():
    """Valida configuración de idioma"""
    errors = []
    
    if "current" in language_config:
        if not is_language_available(language_config["current"]):
            errors.append("Current language not in available languages")
    
    return errors

def backup_language_config():
    """Crea backup de configuración de idioma"""
    backup_name = "language_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_language_config(backup_name)
    return backup_name

def restore_language_config(backup_name):
    """Restaura configuración de idioma desde backup"""
    return import_language_config(backup_name)

def get_language_config_summary():
    """Obtiene resumen de configuración de idioma"""
    return {
        "current": get_current_language(),
        "available_count": len(get_available_languages()),
        "fallback": get_fallback_language()
    }

# Cargar configuración de idioma al importar
load_language_config()
