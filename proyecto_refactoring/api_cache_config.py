import os
import json
import time
from datetime import datetime

# Variables globales
API_CACHE_CONFIG_FILE = "api_cache_config.json"
api_cache_config = {}

def load_api_cache_config():
    """Carga configuración de caché de API"""
    global api_cache_config
    
    if os.path.exists(API_CACHE_CONFIG_FILE):
        with open(API_CACHE_CONFIG_FILE, 'r') as f:
            api_cache_config = json.load(f)
    else:
        api_cache_config = {
            "enable_api_cache": True,
            "api_cache_size_mb": 50,
            "api_cache_expiry_hours": 12,
            "cache_responses": True
        }

def save_api_cache_config():
    """Guarda configuración de caché de API"""
    with open(API_CACHE_CONFIG_FILE, 'w') as f:
        json.dump(api_cache_config, f, indent=4)

def get_api_cache_setting(key):
    """Obtiene configuración de caché de API"""
    return api_cache_config.get(key)

def set_api_cache_setting(key, value):
    """Establece configuración de caché de API"""
    api_cache_config[key] = value
    save_api_cache_config()

def get_all_api_cache_settings():
    """Obtiene todas las configuraciones de caché de API"""
    return api_cache_config.copy()

def reset_api_cache_config():
    """Resetea configuración de caché de API"""
    global api_cache_config
    api_cache_config = {
        "enable_api_cache": True,
        "api_cache_size_mb": 50,
        "api_cache_expiry_hours": 12,
        "cache_responses": True
    }
    save_api_cache_config()

def is_api_cache_enabled():
    """Verifica si caché de API está habilitado"""
    return api_cache_config.get("enable_api_cache", True)

def enable_api_cache():
    """Habilita caché de API"""
    api_cache_config["enable_api_cache"] = True
    save_api_cache_config()

def disable_api_cache():
    """Deshabilita caché de API"""
    api_cache_config["enable_api_cache"] = False
    save_api_cache_config()

def get_api_cache_size_mb():
    """Obtiene tamaño de caché de API en MB"""
    return api_cache_config.get("api_cache_size_mb", 50)

def set_api_cache_size_mb(size):
    """Establece tamaño de caché de API en MB"""
    api_cache_config["api_cache_size_mb"] = size
    save_api_cache_config()

def get_api_cache_expiry_hours():
    """Obtiene horas de expiración de caché de API"""
    return api_cache_config.get("api_cache_expiry_hours", 12)

def set_api_cache_expiry_hours(hours):
    """Establece horas de expiración de caché de API"""
    api_cache_config["api_cache_expiry_hours"] = hours
    save_api_cache_config()

def is_cache_responses_enabled():
    """Verifica si cacheo de respuestas está habilitado"""
    return api_cache_config.get("cache_responses", True)

def enable_cache_responses():
    """Habilita cacheo de respuestas"""
    api_cache_config["cache_responses"] = True
    save_api_cache_config()

def disable_cache_responses():
    """Deshabilita cacheo de respuestas"""
    api_cache_config["cache_responses"] = False
    save_api_cache_config()

def export_api_cache_config(filename):
    """Exporta configuración de caché de API"""
    with open(filename, 'w') as f:
        json.dump(api_cache_config, f, indent=4)

def import_api_cache_config(filename):
    """Importa configuración de caché de API"""
    global api_cache_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            api_cache_config = json.load(f)
        save_api_cache_config()
        return True
    return False

def validate_api_cache_config():
    """Valida configuración de caché de API"""
    errors = []
    
    for key in ["api_cache_size_mb", "api_cache_expiry_hours"]:
        if key in api_cache_config:
            if not isinstance(api_cache_config[key], int):
                errors.append(key + " must be integer")
    
    return errors

def backup_api_cache_config():
    """Crea backup de configuración de caché de API"""
    backup_name = "api_cache_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_api_cache_config(backup_name)
    return backup_name

def restore_api_cache_config(backup_name):
    """Restaura configuración de caché de API desde backup"""
    return import_api_cache_config(backup_name)

def get_api_cache_config_summary():
    """Obtiene resumen de configuración de caché de API"""
    return {
        "enable_api_cache": is_api_cache_enabled(),
        "api_cache_size_mb": get_api_cache_size_mb(),
        "api_cache_expiry_hours": get_api_cache_expiry_hours()
    }

# Cargar configuración de caché de API al importar
load_api_cache_config()
