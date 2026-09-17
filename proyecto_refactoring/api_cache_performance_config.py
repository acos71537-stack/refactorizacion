import os
import json
import time
from datetime import datetime

# Variables globales
API_CACHE_PERFORMANCE_CONFIG_FILE = "api_cache_performance_config.json"
api_cache_performance_config = {}

def load_api_cache_performance_config():
    """Carga configuración de rendimiento de caché de API"""
    global api_cache_performance_config
    
    if os.path.exists(API_CACHE_PERFORMANCE_CONFIG_FILE):
        with open(API_CACHE_PERFORMANCE_CONFIG_FILE, 'r') as f:
            api_cache_performance_config = json.load(f)
    else:
        api_cache_performance_config = {
            "optimize_for_read": True,
            "optimize_for_write": False,
            "batch_operations": True,
            "async_operations": False
        }

def save_api_cache_performance_config():
    """Guarda configuración de rendimiento de caché de API"""
    with open(API_CACHE_PERFORMANCE_CONFIG_FILE, 'w') as f:
        json.dump(api_cache_performance_config, f, indent=4)

def get_api_cache_performance_setting(key):
    """Obtiene configuración de rendimiento de caché de API"""
    return api_cache_performance_config.get(key)

def set_api_cache_performance_setting(key, value):
    """Establece configuración de rendimiento de caché de API"""
    api_cache_performance_config[key] = value
    save_api_cache_performance_config()

def get_all_api_cache_performance_settings():
    """Obtiene todas las configuraciones de rendimiento de caché de API"""
    return api_cache_performance_config.copy()

def reset_api_cache_performance_config():
    """Resetea configuración de rendimiento de caché de API"""
    global api_cache_performance_config
    api_cache_performance_config = {
        "optimize_for_read": True,
        "optimize_for_write": False,
        "batch_operations": True,
        "async_operations": False
    }
    save_api_cache_performance_config()

def is_optimize_for_read_enabled():
    """Verifica si optimización para lectura está habilitada"""
    return api_cache_performance_config.get("optimize_for_read", True)

def enable_optimize_for_read():
    """Habilita optimización para lectura"""
    api_cache_performance_config["optimize_for_read"] = True
    save_api_cache_performance_config()

def disable_optimize_for_read():
    """Deshabilita optimización para lectura"""
    api_cache_performance_config["optimize_for_read"] = False
    save_api_cache_performance_config()

def is_optimize_for_write_enabled():
    """Verifica si optimización para escritura está habilitada"""
    return api_cache_performance_config.get("optimize_for_write", False)

def enable_optimize_for_write():
    """Habilita optimización para escritura"""
    api_cache_performance_config["optimize_for_write"] = True
    save_api_cache_performance_config()

def disable_optimize_for_write():
    """Deshabilita optimización para escritura"""
    api_cache_performance_config["optimize_for_write"] = False
    save_api_cache_performance_config()

def is_batch_operations_enabled():
    """Verifica si operaciones por lotes están habilitadas"""
    return api_cache_performance_config.get("batch_operations", True)

def enable_batch_operations():
    """Habilita operaciones por lotes"""
    api_cache_performance_config["batch_operations"] = True
    save_api_cache_performance_config()

def disable_batch_operations():
    """Deshabilita operaciones por lotes"""
    api_cache_performance_config["batch_operations"] = False
    save_api_cache_performance_config()

def is_async_operations_enabled():
    """Verifica si operaciones asíncronas están habilitadas"""
    return api_cache_performance_config.get("async_operations", False)

def enable_async_operations():
    """Habilita operaciones asíncronas"""
    api_cache_performance_config["async_operations"] = True
    save_api_cache_performance_config()

def disable_async_operations():
    """Deshabilita operaciones asíncronas"""
    api_cache_performance_config["async_operations"] = False
    save_api_cache_performance_config()

def export_api_cache_performance_config(filename):
    """Exporta configuración de rendimiento de caché de API"""
    with open(filename, 'w') as f:
        json.dump(api_cache_performance_config, f, indent=4)

def import_api_cache_performance_config(filename):
    """Importa configuración de rendimiento de caché de API"""
    global api_cache_performance_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            api_cache_performance_config = json.load(f)
        save_api_cache_performance_config()
        return True
    return False

def validate_api_cache_performance_config():
    """Valida configuración de rendimiento de caché de API"""
    errors = []
    
    for key in ["optimize_for_read", "optimize_for_write", "batch_operations", "async_operations"]:
        if key in api_cache_performance_config:
            if not isinstance(api_cache_performance_config[key], bool):
                errors.append(key + " must be boolean")
    
    return errors

def backup_api_cache_performance_config():
    """Crea backup de configuración de rendimiento de caché de API"""
    backup_name = "api_cache_performance_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_api_cache_performance_config(backup_name)
    return backup_name

def restore_api_cache_performance_config(backup_name):
    """Restaura configuración de rendimiento de caché de API desde backup"""
    return import_api_cache_performance_config(backup_name)

def get_api_cache_performance_config_summary():
    """Obtiene resumen de configuración de rendimiento de caché de API"""
    return {
        "optimize_for_read": is_optimize_for_read_enabled(),
        "batch_operations": is_batch_operations_enabled(),
        "async_operations": is_async_operations_enabled()
    }

# Cargar configuración de rendimiento de caché de API al importar
load_api_cache_performance_config()
