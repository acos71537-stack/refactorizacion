import os
import json
import time
from datetime import datetime

# Variables globales
API_CACHE_LIFECYCLE_CONFIG_FILE = "api_cache_lifecycle_config.json"
api_cache_lifecycle_config = {}

def load_api_cache_lifecycle_config():
    """Carga configuración de ciclo de vida de caché de API"""
    global api_cache_lifecycle_config
    
    if os.path.exists(API_CACHE_LIFECYCLE_CONFIG_FILE):
        with open(API_CACHE_LIFECYCLE_CONFIG_FILE, 'r') as f:
            api_cache_lifecycle_config = json.load(f)
    else:
        api_cache_lifecycle_config = {
            "enabled": True,
            "ttl_enabled": True,
            "max_idle_time": 3600,
            "max_lifetime": 86400
        }

def save_api_cache_lifecycle_config():
    """Guarda configuración de ciclo de vida de caché de API"""
    with open(API_CACHE_LIFECYCLE_CONFIG_FILE, 'w') as f:
        json.dump(api_cache_lifecycle_config, f, indent=4)

def get_api_cache_lifecycle_setting(key):
    """Obtiene configuración de ciclo de vida de caché de API"""
    return api_cache_lifecycle_config.get(key)

def set_api_cache_lifecycle_setting(key, value):
    """Establece configuración de ciclo de vida de caché de API"""
    api_cache_lifecycle_config[key] = value
    save_api_cache_lifecycle_config()

def get_all_api_cache_lifecycle_settings():
    """Obtiene todas las configuraciones de ciclo de vida de caché de API"""
    return api_cache_lifecycle_config.copy()

def reset_api_cache_lifecycle_config():
    """Resetea configuración de ciclo de vida de caché de API"""
    global api_cache_lifecycle_config
    api_cache_lifecycle_config = {
        "enabled": True,
        "ttl_enabled": True,
        "max_idle_time": 3600,
        "max_lifetime": 86400
    }
    save_api_cache_lifecycle_config()

def is_cache_lifecycle_enabled():
    """Verifica si ciclo de vida de caché está habilitado"""
    return api_cache_lifecycle_config.get("enabled", True)

def enable_cache_lifecycle():
    """Habilita ciclo de vida de caché"""
    api_cache_lifecycle_config["enabled"] = True
    save_api_cache_lifecycle_config()

def disable_cache_lifecycle():
    """Deshabilita ciclo de vida de caché"""
    api_cache_lifecycle_config["enabled"] = False
    save_api_cache_lifecycle_config()

def is_ttl_enabled():
    """Verifica si TTL está habilitado"""
    return api_cache_lifecycle_config.get("ttl_enabled", True)

def enable_ttl():
    """Habilita TTL"""
    api_cache_lifecycle_config["ttl_enabled"] = True
    save_api_cache_lifecycle_config()

def disable_ttl():
    """Deshabilita TTL"""
    api_cache_lifecycle_config["ttl_enabled"] = False
    save_api_cache_lifecycle_config()

def get_max_idle_time():
    """Obtiene tiempo máximo de inactividad"""
    return api_cache_lifecycle_config.get("max_idle_time", 3600)

def set_max_idle_time(time_seconds):
    """Establece tiempo máximo de inactividad"""
    api_cache_lifecycle_config["max_idle_time"] = time_seconds
    save_api_cache_lifecycle_config()

def get_max_lifetime():
    """Obtiene tiempo de vida máximo"""
    return api_cache_lifecycle_config.get("max_lifetime", 86400)

def set_max_lifetime(lifetime):
    """Establece tiempo de vida máximo"""
    api_cache_lifecycle_config["max_lifetime"] = lifetime
    save_api_cache_lifecycle_config()

def export_api_cache_lifecycle_config(filename):
    """Exporta configuración de ciclo de vida de caché de API"""
    with open(filename, 'w') as f:
        json.dump(api_cache_lifecycle_config, f, indent=4)

def import_api_cache_lifecycle_config(filename):
    """Importa configuración de ciclo de vida de caché de API"""
    global api_cache_lifecycle_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            api_cache_lifecycle_config = json.load(f)
        save_api_cache_lifecycle_config()
        return True
    return False

def validate_api_cache_lifecycle_config():
    """Valida configuración de ciclo de vida de caché de API"""
    errors = []
    
    for key in ["enabled", "ttl_enabled"]:
        if key in api_cache_lifecycle_config:
            if not isinstance(api_cache_lifecycle_config[key], bool):
                errors.append(key + " must be boolean")
    
    for key in ["max_idle_time", "max_lifetime"]:
        if key in api_cache_lifecycle_config:
            if not isinstance(api_cache_lifecycle_config[key], int):
                errors.append(key + " must be integer")
    
    return errors

def backup_api_cache_lifecycle_config():
    """Crea backup de configuración de ciclo de vida de caché de API"""
    backup_name = "api_cache_lifecycle_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_api_cache_lifecycle_config(backup_name)
    return backup_name

def restore_api_cache_lifecycle_config(backup_name):
    """Restaura configuración de ciclo de vida de caché de API desde backup"""
    return import_api_cache_lifecycle_config(backup_name)

def get_api_cache_lifecycle_config_summary():
    """Obtiene resumen de configuración de ciclo de vida de caché de API"""
    return {
        "enabled": is_cache_lifecycle_enabled(),
        "ttl_enabled": is_ttl_enabled(),
        "max_lifetime": get_max_lifetime()
    }

# Cargar configuración de ciclo de vida de caché de API al importar
load_api_cache_lifecycle_config()
