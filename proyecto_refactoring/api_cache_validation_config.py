import os
import json
import time
from datetime import datetime

# Variables globales
API_CACHE_VALIDATION_CONFIG_FILE = "api_cache_validation_config.json"
api_cache_validation_config = {}

def load_api_cache_validation_config():
    """Carga configuración de validación de caché de API"""
    global api_cache_validation_config
    
    if os.path.exists(API_CACHE_VALIDATION_CONFIG_FILE):
        with open(API_CACHE_VALIDATION_CONFIG_FILE, 'r') as f:
            api_cache_validation_config = json.load(f)
    else:
        api_cache_validation_config = {
            "enabled": True,
            "validate_on_read": True,
            "validate_checksum": False,
            "strict_validation": False
        }

def save_api_cache_validation_config():
    """Guarda configuración de validación de caché de API"""
    with open(API_CACHE_VALIDATION_CONFIG_FILE, 'w') as f:
        json.dump(api_cache_validation_config, f, indent=4)

def get_api_cache_validation_setting(key):
    """Obtiene configuración de validación de caché de API"""
    return api_cache_validation_config.get(key)

def set_api_cache_validation_setting(key, value):
    """Establece configuración de validación de caché de API"""
    api_cache_validation_config[key] = value
    save_api_cache_validation_config()

def get_all_api_cache_validation_settings():
    """Obtiene todas las configuraciones de validación de caché de API"""
    return api_cache_validation_config.copy()

def reset_api_cache_validation_config():
    """Resetea configuración de validación de caché de API"""
    global api_cache_validation_config
    api_cache_validation_config = {
        "enabled": True,
        "validate_on_read": True,
        "validate_checksum": False,
        "strict_validation": False
    }
    save_api_cache_validation_config()

def is_cache_validation_enabled():
    """Verifica si validación de caché está habilitada"""
    return api_cache_validation_config.get("enabled", True)

def enable_cache_validation():
    """Habilita validación de caché"""
    api_cache_validation_config["enabled"] = True
    save_api_cache_validation_config()

def disable_cache_validation():
    """Deshabilita validación de caché"""
    api_cache_validation_config["enabled"] = False
    save_api_cache_validation_config()

def is_validate_on_read_enabled():
    """Verifica si validación en lectura está habilitada"""
    return api_cache_validation_config.get("validate_on_read", True)

def enable_validate_on_read():
    """Habilita validación en lectura"""
    api_cache_validation_config["validate_on_read"] = True
    save_api_cache_validation_config()

def disable_validate_on_read():
    """Deshabilita validación en lectura"""
    api_cache_validation_config["validate_on_read"] = False
    save_api_cache_validation_config()

def is_validate_checksum_enabled():
    """Verifica si validación de checksum está habilitada"""
    return api_cache_validation_config.get("validate_checksum", False)

def enable_validate_checksum():
    """Habilita validación de checksum"""
    api_cache_validation_config["validate_checksum"] = True
    save_api_cache_validation_config()

def disable_validate_checksum():
    """Deshabilita validación de checksum"""
    api_cache_validation_config["validate_checksum"] = False
    save_api_cache_validation_config()

def is_strict_validation_enabled():
    """Verifica si validación estricta está habilitada"""
    return api_cache_validation_config.get("strict_validation", False)

def enable_strict_validation():
    """Habilita validación estricta"""
    api_cache_validation_config["strict_validation"] = True
    save_api_cache_validation_config()

def disable_strict_validation():
    """Deshabilita validación estricta"""
    api_cache_validation_config["strict_validation"] = False
    save_api_cache_validation_config()

def export_api_cache_validation_config(filename):
    """Exporta configuración de validación de caché de API"""
    with open(filename, 'w') as f:
        json.dump(api_cache_validation_config, f, indent=4)

def import_api_cache_validation_config(filename):
    """Importa configuración de validación de caché de API"""
    global api_cache_validation_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            api_cache_validation_config = json.load(f)
        save_api_cache_validation_config()
        return True
    return False

def validate_api_cache_validation_config():
    """Valida configuración de validación de caché de API"""
    errors = []
    
    for key in ["enabled", "validate_on_read", "validate_checksum", "strict_validation"]:
        if key in api_cache_validation_config:
            if not isinstance(api_cache_validation_config[key], bool):
                errors.append(key + " must be boolean")
    
    return errors

def backup_api_cache_validation_config():
    """Crea backup de configuración de validación de caché de API"""
    backup_name = "api_cache_validation_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_api_cache_validation_config(backup_name)
    return backup_name

def restore_api_cache_validation_config(backup_name):
    """Restaura configuración de validación de caché de API desde backup"""
    return import_api_cache_validation_config(backup_name)

def get_api_cache_validation_config_summary():
    """Obtiene resumen de configuración de validación de caché de API"""
    return {
        "enabled": is_cache_validation_enabled(),
        "validate_on_read": is_validate_on_read_enabled(),
        "validate_checksum": is_validate_checksum_enabled()
    }

# Cargar configuración de validación de caché de API al importar
load_api_cache_validation_config()
