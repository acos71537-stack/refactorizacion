import os
import json
import time
from datetime import datetime

# Variables globales
PERFORMANCE_CONFIG_FILE = "performance_config.json"
performance_config = {}

def load_performance_config():
    """Carga configuración de rendimiento"""
    global performance_config
    
    if os.path.exists(PERFORMANCE_CONFIG_FILE):
        with open(PERFORMANCE_CONFIG_FILE, 'r') as f:
            performance_config = json.load(f)
    else:
        performance_config = {
            "cache_size_mb": 100,
            "max_concurrent_requests": 5,
            "connection_pool_size": 10,
            "enable_compression": True
        }

def save_performance_config():
    """Guarda configuración de rendimiento"""
    with open(PERFORMANCE_CONFIG_FILE, 'w') as f:
        json.dump(performance_config, f, indent=4)

def get_performance_setting(key):
    """Obtiene configuración de rendimiento"""
    return performance_config.get(key)

def set_performance_setting(key, value):
    """Establece configuración de rendimiento"""
    performance_config[key] = value
    save_performance_config()

def get_all_performance_settings():
    """Obtiene todas las configuraciones de rendimiento"""
    return performance_config.copy()

def reset_performance_config():
    """Resetea configuración de rendimiento"""
    global performance_config
    performance_config = {
        "cache_size_mb": 100,
        "max_concurrent_requests": 5,
        "connection_pool_size": 10,
        "enable_compression": True
    }
    save_performance_config()

def get_cache_size_mb():
    """Obtiene tamaño de caché en MB"""
    return performance_config.get("cache_size_mb", 100)

def set_cache_size_mb(size):
    """Establece tamaño de caché en MB"""
    performance_config["cache_size_mb"] = size
    save_performance_config()

def get_max_concurrent_requests():
    """Obtiene máximo de requests concurrentes"""
    return performance_config.get("max_concurrent_requests", 5)

def set_max_concurrent_requests(max_requests):
    """Establece máximo de requests concurrentes"""
    performance_config["max_concurrent_requests"] = max_requests
    save_performance_config()

def get_connection_pool_size():
    """Obtiene tamaño de pool de conexiones"""
    return performance_config.get("connection_pool_size", 10)

def set_connection_pool_size(size):
    """Establece tamaño de pool de conexiones"""
    performance_config["connection_pool_size"] = size
    save_performance_config()

def is_compression_enabled():
    """Verifica si compresión está habilitada"""
    return performance_config.get("enable_compression", True)

def enable_compression():
    """Habilita compresión"""
    performance_config["enable_compression"] = True
    save_performance_config()

def disable_compression():
    """Deshabilita compresión"""
    performance_config["enable_compression"] = False
    save_performance_config()

def export_performance_config(filename):
    """Exporta configuración de rendimiento"""
    with open(filename, 'w') as f:
        json.dump(performance_config, f, indent=4)

def import_performance_config(filename):
    """Importa configuración de rendimiento"""
    global performance_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            performance_config = json.load(f)
        save_performance_config()
        return True
    return False

def validate_performance_config():
    """Valida configuración de rendimiento"""
    errors = []
    
    for key in ["cache_size_mb", "max_concurrent_requests", "connection_pool_size"]:
        if key in performance_config:
            if not isinstance(performance_config[key], int):
                errors.append(key + " must be integer")
    
    return errors

def backup_performance_config():
    """Crea backup de configuración de rendimiento"""
    backup_name = "performance_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_performance_config(backup_name)
    return backup_name

def restore_performance_config(backup_name):
    """Restaura configuración de rendimiento desde backup"""
    return import_performance_config(backup_name)

def get_performance_config_summary():
    """Obtiene resumen de configuración de rendimiento"""
    return {
        "cache_size_mb": get_cache_size_mb(),
        "max_concurrent_requests": get_max_concurrent_requests(),
        "enable_compression": is_compression_enabled()
    }

# Cargar configuración de rendimiento al importar
load_performance_config()
