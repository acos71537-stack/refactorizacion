import os
import json
import time
from datetime import datetime

# Variables globales
API_CACHE_CLEANUP_CONFIG_FILE = "api_cache_cleanup_config.json"
api_cache_cleanup_config = {}

def load_api_cache_cleanup_config():
    """Carga configuración de limpieza de caché de API"""
    global api_cache_cleanup_config
    
    if os.path.exists(API_CACHE_CLEANUP_CONFIG_FILE):
        with open(API_CACHE_CLEANUP_CONFIG_FILE, 'r') as f:
            api_cache_cleanup_config = json.load(f)
    else:
        api_cache_cleanup_config = {
            "enabled": True,
            "cleanup_interval": 3600,
            "max_cache_size_mb": 100,
            "eviction_policy": "lru"
        }

def save_api_cache_cleanup_config():
    """Guarda configuración de limpieza de caché de API"""
    with open(API_CACHE_CLEANUP_CONFIG_FILE, 'w') as f:
        json.dump(api_cache_cleanup_config, f, indent=4)

def get_api_cache_cleanup_setting(key):
    """Obtiene configuración de limpieza de caché de API"""
    return api_cache_cleanup_config.get(key)

def set_api_cache_cleanup_setting(key, value):
    """Establece configuración de limpieza de caché de API"""
    api_cache_cleanup_config[key] = value
    save_api_cache_cleanup_config()

def get_all_api_cache_cleanup_settings():
    """Obtiene todas las configuraciones de limpieza de caché de API"""
    return api_cache_cleanup_config.copy()

def reset_api_cache_cleanup_config():
    """Resetea configuración de limpieza de caché de API"""
    global api_cache_cleanup_config
    api_cache_cleanup_config = {
        "enabled": True,
        "cleanup_interval": 3600,
        "max_cache_size_mb": 100,
        "eviction_policy": "lru"
    }
    save_api_cache_cleanup_config()

def is_cache_cleanup_enabled():
    """Verifica si limpieza de caché está habilitada"""
    return api_cache_cleanup_config.get("enabled", True)

def enable_cache_cleanup():
    """Habilita limpieza de caché"""
    api_cache_cleanup_config["enabled"] = True
    save_api_cache_cleanup_config()

def disable_cache_cleanup():
    """Deshabilita limpieza de caché"""
    api_cache_cleanup_config["enabled"] = False
    save_api_cache_cleanup_config()

def get_cleanup_interval():
    """Obtiene intervalo de limpieza"""
    return api_cache_cleanup_config.get("cleanup_interval", 3600)

def set_cleanup_interval(interval):
    """Establece intervalo de limpieza"""
    api_cache_cleanup_config["cleanup_interval"] = interval
    save_api_cache_cleanup_config()

def get_max_cache_size_mb():
    """Obtiene tamaño máximo de caché en MB"""
    return api_cache_cleanup_config.get("max_cache_size_mb", 100)

def set_max_cache_size_mb(size):
    """Establece tamaño máximo de caché en MB"""
    api_cache_cleanup_config["max_cache_size_mb"] = size
    save_api_cache_cleanup_config()

def get_eviction_policy():
    """Obtiene política de evicción"""
    return api_cache_cleanup_config.get("eviction_policy", "lru")

def set_eviction_policy(policy):
    """Establece política de evicción"""
    api_cache_cleanup_config["eviction_policy"] = policy
    save_api_cache_cleanup_config()

def export_api_cache_cleanup_config(filename):
    """Exporta configuración de limpieza de caché de API"""
    with open(filename, 'w') as f:
        json.dump(api_cache_cleanup_config, f, indent=4)

def import_api_cache_cleanup_config(filename):
    """Importa configuración de limpieza de caché de API"""
    global api_cache_cleanup_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            api_cache_cleanup_config = json.load(f)
        save_api_cache_cleanup_config()
        return True
    return False

def validate_api_cache_cleanup_config():
    """Valida configuración de limpieza de caché de API"""
    errors = []
    
    if "enabled" in api_cache_cleanup_config:
        if not isinstance(api_cache_cleanup_config["enabled"], bool):
            errors.append("enabled must be boolean")
    
    for key in ["cleanup_interval", "max_cache_size_mb"]:
        if key in api_cache_cleanup_config:
            if not isinstance(api_cache_cleanup_config[key], int):
                errors.append(key + " must be integer")
    
    return errors

def backup_api_cache_cleanup_config():
    """Crea backup de configuración de limpieza de caché de API"""
    backup_name = "api_cache_cleanup_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_api_cache_cleanup_config(backup_name)
    return backup_name

def restore_api_cache_cleanup_config(backup_name):
    """Restaura configuración de limpieza de caché de API desde backup"""
    return import_api_cache_cleanup_config(backup_name)

def get_api_cache_cleanup_config_summary():
    """Obtiene resumen de configuración de limpieza de caché de API"""
    return {
        "enabled": is_cache_cleanup_enabled(),
        "cleanup_interval": get_cleanup_interval(),
        "eviction_policy": get_eviction_policy()
    }

# Cargar configuración de limpieza de caché de API al importar
load_api_cache_cleanup_config()
