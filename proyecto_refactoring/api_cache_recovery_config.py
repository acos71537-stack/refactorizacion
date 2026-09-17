import os
import json
import time
from datetime import datetime

# Variables globales
API_CACHE_RECOVERY_CONFIG_FILE = "api_cache_recovery_config.json"
api_cache_recovery_config = {}

def load_api_cache_recovery_config():
    """Carga configuración de recuperación de caché de API"""
    global api_cache_recovery_config
    
    if os.path.exists(API_CACHE_RECOVERY_CONFIG_FILE):
        with open(API_CACHE_RECOVERY_CONFIG_FILE, 'r') as f:
            api_cache_recovery_config = json.load(f)
    else:
        api_cache_recovery_config = {
            "enabled": True,
            "auto_recovery": True,
            "recovery_strategy": "last-known-good",
            "max_recovery_attempts": 3
        }

def save_api_cache_recovery_config():
    """Guarda configuración de recuperación de caché de API"""
    with open(API_CACHE_RECOVERY_CONFIG_FILE, 'w') as f:
        json.dump(api_cache_recovery_config, f, indent=4)

def get_api_cache_recovery_setting(key):
    """Obtiene configuración de recuperación de caché de API"""
    return api_cache_recovery_config.get(key)

def set_api_cache_recovery_setting(key, value):
    """Establece configuración de recuperación de caché de API"""
    api_cache_recovery_config[key] = value
    save_api_cache_recovery_config()

def get_all_api_cache_recovery_settings():
    """Obtiene todas las configuraciones de recuperación de caché de API"""
    return api_cache_recovery_config.copy()

def reset_api_cache_recovery_config():
    """Resetea configuración de recuperación de caché de API"""
    global api_cache_recovery_config
    api_cache_recovery_config = {
        "enabled": True,
        "auto_recovery": True,
        "recovery_strategy": "last-known-good",
        "max_recovery_attempts": 3
    }
    save_api_cache_recovery_config()

def is_cache_recovery_enabled():
    """Verifica si recuperación de caché está habilitada"""
    return api_cache_recovery_config.get("enabled", True)

def enable_cache_recovery():
    """Habilita recuperación de caché"""
    api_cache_recovery_config["enabled"] = True
    save_api_cache_recovery_config()

def disable_cache_recovery():
    """Deshabilita recuperación de caché"""
    api_cache_recovery_config["enabled"] = False
    save_api_cache_recovery_config()

def is_auto_recovery_enabled():
    """Verifica si recuperación automática está habilitada"""
    return api_cache_recovery_config.get("auto_recovery", True)

def enable_auto_recovery():
    """Habilita recuperación automática"""
    api_cache_recovery_config["auto_recovery"] = True
    save_api_cache_recovery_config()

def disable_auto_recovery():
    """Deshabilita recuperación automática"""
    api_cache_recovery_config["auto_recovery"] = False
    save_api_cache_recovery_config()

def get_recovery_strategy():
    """Obtiene estrategia de recuperación"""
    return api_cache_recovery_config.get("recovery_strategy", "last-known-good")

def set_recovery_strategy(strategy):
    """Establece estrategia de recuperación"""
    api_cache_recovery_config["recovery_strategy"] = strategy
    save_api_cache_recovery_config()

def get_max_recovery_attempts():
    """Obtiene máximo de intentos de recuperación"""
    return api_cache_recovery_config.get("max_recovery_attempts", 3)

def set_max_recovery_attempts(attempts):
    """Establece máximo de intentos de recuperación"""
    api_cache_recovery_config["max_recovery_attempts"] = attempts
    save_api_cache_recovery_config()

def export_api_cache_recovery_config(filename):
    """Exporta configuración de recuperación de caché de API"""
    with open(filename, 'w') as f:
        json.dump(api_cache_recovery_config, f, indent=4)

def import_api_cache_recovery_config(filename):
    """Importa configuración de recuperación de caché de API"""
    global api_cache_recovery_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            api_cache_recovery_config = json.load(f)
        save_api_cache_recovery_config()
        return True
    return False

def validate_api_cache_recovery_config():
    """Valida configuración de recuperación de caché de API"""
    errors = []
    
    for key in ["enabled", "auto_recovery"]:
        if key in api_cache_recovery_config:
            if not isinstance(api_cache_recovery_config[key], bool):
                errors.append(key + " must be boolean")
    
    if "max_recovery_attempts" in api_cache_recovery_config:
        if not isinstance(api_cache_recovery_config["max_recovery_attempts"], int):
            errors.append("max_recovery_attempts must be integer")
    
    return errors

def backup_api_cache_recovery_config():
    """Crea backup de configuración de recuperación de caché de API"""
    backup_name = "api_cache_recovery_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_api_cache_recovery_config(backup_name)
    return backup_name

def restore_api_cache_recovery_config(backup_name):
    """Restaura configuración de recuperación de caché de API desde backup"""
    return import_api_cache_recovery_config(backup_name)

def get_api_cache_recovery_config_summary():
    """Obtiene resumen de configuración de recuperación de caché de API"""
    return {
        "enabled": is_cache_recovery_enabled(),
        "auto_recovery": is_auto_recovery_enabled(),
        "recovery_strategy": get_recovery_strategy()
    }

# Cargar configuración de recuperación de caché de API al importar
load_api_cache_recovery_config()
