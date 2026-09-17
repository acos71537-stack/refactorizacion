import os
import json
import time
from datetime import datetime

# Variables globales
API_CACHE_INVALIDATION_CONFIG_FILE = "api_cache_invalidation_config.json"
api_cache_invalidation_config = {}

def load_api_cache_invalidation_config():
    """Carga configuración de invalidación de caché de API"""
    global api_cache_invalidation_config
    
    if os.path.exists(API_CACHE_INVALIDATION_CONFIG_FILE):
        with open(API_CACHE_INVALIDATION_CONFIG_FILE, 'r') as f:
            api_cache_invalidation_config = json.load(f)
    else:
        api_cache_invalidation_config = {
            "enabled": True,
            "strategy": "time-based",
            "invalidate_on_error": True,
            "invalidate_on_write": False
        }

def save_api_cache_invalidation_config():
    """Guarda configuración de invalidación de caché de API"""
    with open(API_CACHE_INVALIDATION_CONFIG_FILE, 'w') as f:
        json.dump(api_cache_invalidation_config, f, indent=4)

def get_api_cache_invalidation_setting(key):
    """Obtiene configuración de invalidación de caché de API"""
    return api_cache_invalidation_config.get(key)

def set_api_cache_invalidation_setting(key, value):
    """Establece configuración de invalidación de caché de API"""
    api_cache_invalidation_config[key] = value
    save_api_cache_invalidation_config()

def get_all_api_cache_invalidation_settings():
    """Obtiene todas las configuraciones de invalidación de caché de API"""
    return api_cache_invalidation_config.copy()

def reset_api_cache_invalidation_config():
    """Resetea configuración de invalidación de caché de API"""
    global api_cache_invalidation_config
    api_cache_invalidation_config = {
        "enabled": True,
        "strategy": "time-based",
        "invalidate_on_error": True,
        "invalidate_on_write": False
    }
    save_api_cache_invalidation_config()

def is_cache_invalidation_enabled():
    """Verifica si invalidación de caché está habilitada"""
    return api_cache_invalidation_config.get("enabled", True)

def enable_cache_invalidation():
    """Habilita invalidación de caché"""
    api_cache_invalidation_config["enabled"] = True
    save_api_cache_invalidation_config()

def disable_cache_invalidation():
    """Deshabilita invalidación de caché"""
    api_cache_invalidation_config["enabled"] = False
    save_api_cache_invalidation_config()

def get_invalidation_strategy():
    """Obtiene estrategia de invalidación"""
    return api_cache_invalidation_config.get("strategy", "time-based")

def set_invalidation_strategy(strategy):
    """Establece estrategia de invalidación"""
    api_cache_invalidation_config["strategy"] = strategy
    save_api_cache_invalidation_config()

def is_invalidate_on_error_enabled():
    """Verifica si invalidar en error está habilitado"""
    return api_cache_invalidation_config.get("invalidate_on_error", True)

def enable_invalidate_on_error():
    """Habilita invalidar en error"""
    api_cache_invalidation_config["invalidate_on_error"] = True
    save_api_cache_invalidation_config()

def disable_invalidate_on_error():
    """Deshabilita invalidar en error"""
    api_cache_invalidation_config["invalidate_on_error"] = False
    save_api_cache_invalidation_config()

def is_invalidate_on_write_enabled():
    """Verifica si invalidar en escritura está habilitado"""
    return api_cache_invalidation_config.get("invalidate_on_write", False)

def enable_invalidate_on_write():
    """Habilita invalidar en escritura"""
    api_cache_invalidation_config["invalidate_on_write"] = True
    save_api_cache_invalidation_config()

def disable_invalidate_on_write():
    """Deshabilita invalidar en escritura"""
    api_cache_invalidation_config["invalidate_on_write"] = False
    save_api_cache_invalidation_config()

def export_api_cache_invalidation_config(filename):
    """Exporta configuración de invalidación de caché de API"""
    with open(filename, 'w') as f:
        json.dump(api_cache_invalidation_config, f, indent=4)

def import_api_cache_invalidation_config(filename):
    """Importa configuración de invalidación de caché de API"""
    global api_cache_invalidation_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            api_cache_invalidation_config = json.load(f)
        save_api_cache_invalidation_config()
        return True
    return False

def validate_api_cache_invalidation_config():
    """Valida configuración de invalidación de caché de API"""
    errors = []
    
    for key in ["enabled", "invalidate_on_error", "invalidate_on_write"]:
        if key in api_cache_invalidation_config:
            if not isinstance(api_cache_invalidation_config[key], bool):
                errors.append(key + " must be boolean")
    
    return errors

def backup_api_cache_invalidation_config():
    """Crea backup de configuración de invalidación de caché de API"""
    backup_name = "api_cache_invalidation_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_api_cache_invalidation_config(backup_name)
    return backup_name

def restore_api_cache_invalidation_config(backup_name):
    """Restaura configuración de invalidación de caché de API desde backup"""
    return import_api_cache_invalidation_config(backup_name)

def get_api_cache_invalidation_config_summary():
    """Obtiene resumen de configuración de invalidación de caché de API"""
    return {
        "enabled": is_cache_invalidation_enabled(),
        "strategy": get_invalidation_strategy(),
        "invalidate_on_error": is_invalidate_on_error_enabled()
    }

# Cargar configuración de invalidación de caché de API al importar
load_api_cache_invalidation_config()
