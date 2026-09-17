import os
import json
import time
from datetime import datetime

# Variables globales
API_CACHE_DEPRECATION_CONFIG_FILE = "api_cache_deprecation_config.json"
api_cache_deprecation_config = {}

def load_api_cache_deprecation_config():
    """Carga configuración de deprecación de caché de API"""
    global api_cache_deprecation_config
    
    if os.path.exists(API_CACHE_DEPRECATION_CONFIG_FILE):
        with open(API_CACHE_DEPRECATION_CONFIG_FILE, 'r') as f:
            api_cache_deprecation_config = json.load(f)
    else:
        api_cache_deprecation_config = {
            "enabled": True,
            "deprecation_warnings": True,
            "auto_remove_expired": True,
            "grace_period_days": 30
        }

def save_api_cache_deprecation_config():
    """Guarda configuración de deprecación de caché de API"""
    with open(API_CACHE_DEPRECATION_CONFIG_FILE, 'w') as f:
        json.dump(api_cache_deprecation_config, f, indent=4)

def get_api_cache_deprecation_setting(key):
    """Obtiene configuración de deprecación de caché de API"""
    return api_cache_deprecation_config.get(key)

def set_api_cache_deprecation_setting(key, value):
    """Establece configuración de deprecación de caché de API"""
    api_cache_deprecation_config[key] = value
    save_api_cache_deprecation_config()

def get_all_api_cache_deprecation_settings():
    """Obtiene todas las configuraciones de deprecación de caché de API"""
    return api_cache_deprecation_config.copy()

def reset_api_cache_deprecation_config():
    """Resetea configuración de deprecación de caché de API"""
    global api_cache_deprecation_config
    api_cache_deprecation_config = {
        "enabled": True,
        "deprecation_warnings": True,
        "auto_remove_expired": True,
        "grace_period_days": 30
    }
    save_api_cache_deprecation_config()

def is_cache_deprecation_enabled():
    """Verifica si deprecación de caché está habilitada"""
    return api_cache_deprecation_config.get("enabled", True)

def enable_cache_deprecation():
    """Habilita deprecación de caché"""
    api_cache_deprecation_config["enabled"] = True
    save_api_cache_deprecation_config()

def disable_cache_deprecation():
    """Deshabilita deprecación de caché"""
    api_cache_deprecation_config["enabled"] = False
    save_api_cache_deprecation_config()

def is_deprecation_warnings_enabled():
    """Verifica si advertencias de deprecación están habilitadas"""
    return api_cache_deprecation_config.get("deprecation_warnings", True)

def enable_deprecation_warnings():
    """Habilita advertencias de deprecación"""
    api_cache_deprecation_config["deprecation_warnings"] = True
    save_api_cache_deprecation_config()

def disable_deprecation_warnings():
    """Deshabilita advertencias de deprecación"""
    api_cache_deprecation_config["deprecation_warnings"] = False
    save_api_cache_deprecation_config()

def is_auto_remove_expired_enabled():
    """Verifica si eliminación automática de expirados está habilitada"""
    return api_cache_deprecation_config.get("auto_remove_expired", True)

def enable_auto_remove_expired():
    """Habilita eliminación automática de expirados"""
    api_cache_deprecation_config["auto_remove_expired"] = True
    save_api_cache_deprecation_config()

def disable_auto_remove_expired():
    """Deshabilita eliminación automática de expirados"""
    api_cache_deprecation_config["auto_remove_expired"] = False
    save_api_cache_deprecation_config()

def get_grace_period_days():
    """Obtiene período de gracia en días"""
    return api_cache_deprecation_config.get("grace_period_days", 30)

def set_grace_period_days(days):
    """Establece período de gracia en días"""
    api_cache_deprecation_config["grace_period_days"] = days
    save_api_cache_deprecation_config()

def export_api_cache_deprecation_config(filename):
    """Exporta configuración de deprecación de caché de API"""
    with open(filename, 'w') as f:
        json.dump(api_cache_deprecation_config, f, indent=4)

def import_api_cache_deprecation_config(filename):
    """Importa configuración de deprecación de caché de API"""
    global api_cache_deprecation_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            api_cache_deprecation_config = json.load(f)
        save_api_cache_deprecation_config()
        return True
    return False

def validate_api_cache_deprecation_config():
    """Valida configuración de deprecación de caché de API"""
    errors = []
    
    for key in ["enabled", "deprecation_warnings", "auto_remove_expired"]:
        if key in api_cache_deprecation_config:
            if not isinstance(api_cache_deprecation_config[key], bool):
                errors.append(key + " must be boolean")
    
    if "grace_period_days" in api_cache_deprecation_config:
        if not isinstance(api_cache_deprecation_config["grace_period_days"], int):
            errors.append("grace_period_days must be integer")
    
    return errors

def backup_api_cache_deprecation_config():
    """Crea backup de configuración de deprecación de caché de API"""
    backup_name = "api_cache_deprecation_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_api_cache_deprecation_config(backup_name)
    return backup_name

def restore_api_cache_deprecation_config(backup_name):
    """Restaura configuración de deprecación de caché de API desde backup"""
    return import_api_cache_deprecation_config(backup_name)

def get_api_cache_deprecation_config_summary():
    """Obtiene resumen de configuración de deprecación de caché de API"""
    return {
        "enabled": is_cache_deprecation_enabled(),
        "deprecation_warnings": is_deprecation_warnings_enabled(),
        "grace_period_days": get_grace_period_days()
    }

# Cargar configuración de deprecación de caché de API al importar
load_api_cache_deprecation_config()
