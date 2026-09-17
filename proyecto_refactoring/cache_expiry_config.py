import os
import json
import time
from datetime import datetime

# Variables globales
CACHE_EXPIRY_CONFIG_FILE = "cache_expiry_config.json"
cache_expiry_config = {}

def load_cache_expiry_config():
    """Carga configuración de expiración de caché"""
    global cache_expiry_config
    
    if os.path.exists(CACHE_EXPIRY_CONFIG_FILE):
        with open(CACHE_EXPIRY_CONFIG_FILE, 'r') as f:
            cache_expiry_config = json.load(f)
    else:
        cache_expiry_config = {
            "movie_expiry_hours": 24,
            "series_expiry_hours": 48,
            "search_expiry_hours": 12,
            "default_expiry_hours": 24
        }

def save_cache_expiry_config():
    """Guarda configuración de expiración de caché"""
    with open(CACHE_EXPIRY_CONFIG_FILE, 'w') as f:
        json.dump(cache_expiry_config, f, indent=4)

def get_cache_expiry_setting(key):
    """Obtiene configuración de expiración de caché"""
    return cache_expiry_config.get(key)

def set_cache_expiry_setting(key, value):
    """Establece configuración de expiración de caché"""
    cache_expiry_config[key] = value
    save_cache_expiry_config()

def get_all_cache_expiry_settings():
    """Obtiene todas las configuraciones de expiración de caché"""
    return cache_expiry_config.copy()

def reset_cache_expiry_config():
    """Resetea configuración de expiración de caché"""
    global cache_expiry_config
    cache_expiry_config = {
        "movie_expiry_hours": 24,
        "series_expiry_hours": 48,
        "search_expiry_hours": 12,
        "default_expiry_hours": 24
    }
    save_cache_expiry_config()

def get_movie_expiry_hours():
    """Obtiene horas de expiración de películas"""
    return cache_expiry_config.get("movie_expiry_hours", 24)

def set_movie_expiry_hours(hours):
    """Establece horas de expiración de películas"""
    cache_expiry_config["movie_expiry_hours"] = hours
    save_cache_expiry_config()

def get_series_expiry_hours():
    """Obtiene horas de expiración de series"""
    return cache_expiry_config.get("series_expiry_hours", 48)

def set_series_expiry_hours(hours):
    """Establece horas de expiración de series"""
    cache_expiry_config["series_expiry_hours"] = hours
    save_cache_expiry_config()

def get_search_expiry_hours():
    """Obtiene horas de expiración de búsquedas"""
    return cache_expiry_config.get("search_expiry_hours", 12)

def set_search_expiry_hours(hours):
    """Establece horas de expiración de búsquedas"""
    cache_expiry_config["search_expiry_hours"] = hours
    save_cache_expiry_config()

def get_default_expiry_hours():
    """Obtiene horas de expiración por defecto"""
    return cache_expiry_config.get("default_expiry_hours", 24)

def set_default_expiry_hours(hours):
    """Establece horas de expiración por defecto"""
    cache_expiry_config["default_expiry_hours"] = hours
    save_cache_expiry_config()

def export_cache_expiry_config(filename):
    """Exporta configuración de expiración de caché"""
    with open(filename, 'w') as f:
        json.dump(cache_expiry_config, f, indent=4)

def import_cache_expiry_config(filename):
    """Importa configuración de expiración de caché"""
    global cache_expiry_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            cache_expiry_config = json.load(f)
        save_cache_expiry_config()
        return True
    return False

def validate_cache_expiry_config():
    """Valida configuración de expiración de caché"""
    errors = []
    
    for key in ["movie_expiry_hours", "series_expiry_hours", "search_expiry_hours", "default_expiry_hours"]:
        if key in cache_expiry_config:
            if not isinstance(cache_expiry_config[key], int):
                errors.append(key + " must be integer")
    
    return errors

def backup_cache_expiry_config():
    """Crea backup de configuración de expiración de caché"""
    backup_name = "cache_expiry_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_cache_expiry_config(backup_name)
    return backup_name

def restore_cache_expiry_config(backup_name):
    """Restaura configuración de expiración de caché desde backup"""
    return import_cache_expiry_config(backup_name)

def get_cache_expiry_config_summary():
    """Obtiene resumen de configuración de expiración de caché"""
    return {
        "movie_expiry_hours": get_movie_expiry_hours(),
        "series_expiry_hours": get_series_expiry_hours(),
        "default_expiry_hours": get_default_expiry_hours()
    }

# Cargar configuración de expiración de caché al importar
load_cache_expiry_config()
