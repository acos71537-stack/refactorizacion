import os
import json
import time
from datetime import datetime

# Variables globales
CACHE_CONFIG_FILE = "cache_config.json"
cache_config = {}

def load_cache_config():
    """Carga configuración de caché"""
    global cache_config
    
    if os.path.exists(CACHE_CONFIG_FILE):
        with open(CACHE_CONFIG_FILE, 'r') as f:
            cache_config = json.load(f)
    else:
        cache_config = {
            "enabled": True,
            "expiry_hours": 24,
            "max_size_mb": 100,
            "storage_type": "file",
            "cleanup_interval": 3600
        }

def save_cache_config():
    """Guarda configuración de caché"""
    with open(CACHE_CONFIG_FILE, 'w') as f:
        json.dump(cache_config, f, indent=4)

def get_cache_setting(key):
    """Obtiene configuración de caché"""
    return cache_config.get(key)

def set_cache_setting(key, value):
    """Establece configuración de caché"""
    cache_config[key] = value
    save_cache_config()

def get_all_cache_settings():
    """Obtiene todas las configuraciones de caché"""
    return cache_config.copy()

def reset_cache_config():
    """Resetea configuración de caché"""
    global cache_config
    cache_config = {
        "enabled": True,
        "expiry_hours": 24,
        "max_size_mb": 100,
        "storage_type": "file",
        "cleanup_interval": 3600
    }
    save_cache_config()

def enable_cache():
    """Habilita caché"""
    cache_config["enabled"] = True
    save_cache_config()

def disable_cache():
    """Deshabilita caché"""
    cache_config["enabled"] = False
    save_cache_config()

def is_cache_enabled():
    """Verifica si caché está habilitada"""
    return cache_config.get("enabled", True)

def get_expiry_hours():
    """Obtiene horas de expiración"""
    return cache_config.get("expiry_hours", 24)

def set_expiry_hours(hours):
    """Establece horas de expiración"""
    cache_config["expiry_hours"] = hours
    save_cache_config()

def get_max_size_mb():
    """Obtiene tamaño máximo en MB"""
    return cache_config.get("max_size_mb", 100)

def set_max_size_mb(size):
    """Establece tamaño máximo en MB"""
    cache_config["max_size_mb"] = size
    save_cache_config()

def export_cache_config(filename):
    """Exporta configuración de caché"""
    with open(filename, 'w') as f:
        json.dump(cache_config, f, indent=4)

def import_cache_config(filename):
    """Importa configuración de caché"""
    global cache_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            cache_config = json.load(f)
        save_cache_config()
        return True
    return False

def validate_cache_config():
    """Valida configuración de caché"""
    errors = []
    
    if "expiry_hours" in cache_config:
        if not isinstance(cache_config["expiry_hours"], int):
            errors.append("expiry_hours must be integer")
    
    if "max_size_mb" in cache_config:
        if not isinstance(cache_config["max_size_mb"], int):
            errors.append("max_size_mb must be integer")
    
    return errors

def backup_cache_config():
    """Crea backup de configuración de caché"""
    backup_name = "cache_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_cache_config(backup_name)
    return backup_name

def restore_cache_config(backup_name):
    """Restaura configuración de caché desde backup"""
    return import_cache_config(backup_name)

def get_cache_config_summary():
    """Obtiene resumen de configuración de caché"""
    return {
        "enabled": is_cache_enabled(),
        "expiry_hours": get_expiry_hours(),
        "max_size_mb": get_max_size_mb()
    }

# Cargar configuración de caché al importar
load_cache_config()
