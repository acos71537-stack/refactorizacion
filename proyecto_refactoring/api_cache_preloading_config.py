import os
import json
import time
from datetime import datetime

# Variables globales
API_CACHE_PRELOADING_CONFIG_FILE = "api_cache_preloading_config.json"
api_cache_preloading_config = {}

def load_api_cache_preloading_config():
    """Carga configuración de precarga de caché de API"""
    global api_cache_preloading_config
    
    if os.path.exists(API_CACHE_PRELOADING_CONFIG_FILE):
        with open(API_CACHE_PRELOADING_CONFIG_FILE, 'r') as f:
            api_cache_preloading_config = json.load(f)
    else:
        api_cache_preloading_config = {
            "enabled": False,
            "preload_on_startup": True,
            "preload_interval": 600,
            "max_preload_items": 50
        }

def save_api_cache_preloading_config():
    """Guarda configuración de precarga de caché de API"""
    with open(API_CACHE_PRELOADING_CONFIG_FILE, 'w') as f:
        json.dump(api_cache_preloading_config, f, indent=4)

def get_api_cache_preloading_setting(key):
    """Obtiene configuración de precarga de caché de API"""
    return api_cache_preloading_config.get(key)

def set_api_cache_preloading_setting(key, value):
    """Establece configuración de precarga de caché de API"""
    api_cache_preloading_config[key] = value
    save_api_cache_preloading_config()

def get_all_api_cache_preloading_settings():
    """Obtiene todas las configuraciones de precarga de caché de API"""
    return api_cache_preloading_config.copy()

def reset_api_cache_preloading_config():
    """Resetea configuración de precarga de caché de API"""
    global api_cache_preloading_config
    api_cache_preloading_config = {
        "enabled": False,
        "preload_on_startup": True,
        "preload_interval": 600,
        "max_preload_items": 50
    }
    save_api_cache_preloading_config()

def is_cache_preloading_enabled():
    """Verifica si precarga de caché está habilitada"""
    return api_cache_preloading_config.get("enabled", False)

def enable_cache_preloading():
    """Habilita precarga de caché"""
    api_cache_preloading_config["enabled"] = True
    save_api_cache_preloading_config()

def disable_cache_preloading():
    """Deshabilita precarga de caché"""
    api_cache_preloading_config["enabled"] = False
    save_api_cache_preloading_config()

def is_preload_on_startup_enabled():
    """Verifica si precarga al inicio está habilitada"""
    return api_cache_preloading_config.get("preload_on_startup", True)

def enable_preload_on_startup():
    """Habilita precarga al inicio"""
    api_cache_preloading_config["preload_on_startup"] = True
    save_api_cache_preloading_config()

def disable_preload_on_startup():
    """Deshabilita precarga al inicio"""
    api_cache_preloading_config["preload_on_startup"] = False
    save_api_cache_preloading_config()

def get_preload_interval():
    """Obtiene intervalo de precarga"""
    return api_cache_preloading_config.get("preload_interval", 600)

def set_preload_interval(interval):
    """Establece intervalo de precarga"""
    api_cache_preloading_config["preload_interval"] = interval
    save_api_cache_preloading_config()

def get_max_preload_items():
    """Obtiene máximo de items de precarga"""
    return api_cache_preloading_config.get("max_preload_items", 50)

def set_max_preload_items(max_items):
    """Establece máximo de items de precarga"""
    api_cache_preloading_config["max_preload_items"] = max_items
    save_api_cache_preloading_config()

def export_api_cache_preloading_config(filename):
    """Exporta configuración de precarga de caché de API"""
    with open(filename, 'w') as f:
        json.dump(api_cache_preloading_config, f, indent=4)

def import_api_cache_preloading_config(filename):
    """Importa configuración de precarga de caché de API"""
    global api_cache_preloading_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            api_cache_preloading_config = json.load(f)
        save_api_cache_preloading_config()
        return True
    return False

def validate_api_cache_preloading_config():
    """Valida configuración de precarga de caché de API"""
    errors = []
    
    for key in ["enabled", "preload_on_startup"]:
        if key in api_cache_preloading_config:
            if not isinstance(api_cache_preloading_config[key], bool):
                errors.append(key + " must be boolean")
    
    for key in ["preload_interval", "max_preload_items"]:
        if key in api_cache_preloading_config:
            if not isinstance(api_cache_preloading_config[key], int):
                errors.append(key + " must be integer")
    
    return errors

def backup_api_cache_preloading_config():
    """Crea backup de configuración de precarga de caché de API"""
    backup_name = "api_cache_preloading_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_api_cache_preloading_config(backup_name)
    return backup_name

def restore_api_cache_preloading_config(backup_name):
    """Restaura configuración de precarga de caché de API desde backup"""
    return import_api_cache_preloading_config(backup_name)

def get_api_cache_preloading_config_summary():
    """Obtiene resumen de configuración de precarga de caché de API"""
    return {
        "enabled": is_cache_preloading_enabled(),
        "preload_on_startup": is_preload_on_startup_enabled(),
        "preload_interval": get_preload_interval()
    }

# Cargar configuración de precarga de caché de API al importar
load_api_cache_preloading_config()
