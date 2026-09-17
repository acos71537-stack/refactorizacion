import os
import json
import time
from datetime import datetime

# Variables globales
API_CACHE_COMPRESSION_CONFIG_FILE = "api_cache_compression_config.json"
api_cache_compression_config = {}

def load_api_cache_compression_config():
    """Carga configuración de compresión de caché de API"""
    global api_cache_compression_config
    
    if os.path.exists(API_CACHE_COMPRESSION_CONFIG_FILE):
        with open(API_CACHE_COMPRESSION_CONFIG_FILE, 'r') as f:
            api_cache_compression_config = json.load(f)
    else:
        api_cache_compression_config = {
            "enabled": True,
            "algorithm": "gzip",
            "min_size_bytes": 1024,
            "compression_level": 6
        }

def save_api_cache_compression_config():
    """Guarda configuración de compresión de caché de API"""
    with open(API_CACHE_COMPRESSION_CONFIG_FILE, 'w') as f:
        json.dump(api_cache_compression_config, f, indent=4)

def get_api_cache_compression_setting(key):
    """Obtiene configuración de compresión de caché de API"""
    return api_cache_compression_config.get(key)

def set_api_cache_compression_setting(key, value):
    """Establece configuración de compresión de caché de API"""
    api_cache_compression_config[key] = value
    save_api_cache_compression_config()

def get_all_api_cache_compression_settings():
    """Obtiene todas las configuraciones de compresión de caché de API"""
    return api_cache_compression_config.copy()

def reset_api_cache_compression_config():
    """Resetea configuración de compresión de caché de API"""
    global api_cache_compression_config
    api_cache_compression_config = {
        "enabled": True,
        "algorithm": "gzip",
        "min_size_bytes": 1024,
        "compression_level": 6
    }
    save_api_cache_compression_config()

def is_cache_compression_enabled():
    """Verifica si compresión de caché está habilitada"""
    return api_cache_compression_config.get("enabled", True)

def enable_cache_compression():
    """Habilita compresión de caché"""
    api_cache_compression_config["enabled"] = True
    save_api_cache_compression_config()

def disable_cache_compression():
    """Deshabilita compresión de caché"""
    api_cache_compression_config["enabled"] = False
    save_api_cache_compression_config()

def get_compression_algorithm():
    """Obtiene algoritmo de compresión"""
    return api_cache_compression_config.get("algorithm", "gzip")

def set_compression_algorithm(algorithm):
    """Establece algoritmo de compresión"""
    api_cache_compression_config["algorithm"] = algorithm
    save_api_cache_compression_config()

def get_min_size_bytes():
    """Obtiene tamaño mínimo en bytes"""
    return api_cache_compression_config.get("min_size_bytes", 1024)

def set_min_size_bytes(size):
    """Establece tamaño mínimo en bytes"""
    api_cache_compression_config["min_size_bytes"] = size
    save_api_cache_compression_config()

def get_compression_level():
    """Obtiene nivel de compresión"""
    return api_cache_compression_config.get("compression_level", 6)

def set_compression_level(level):
    """Establece nivel de compresión"""
    api_cache_compression_config["compression_level"] = level
    save_api_cache_compression_config()

def export_api_cache_compression_config(filename):
    """Exporta configuración de compresión de caché de API"""
    with open(filename, 'w') as f:
        json.dump(api_cache_compression_config, f, indent=4)

def import_api_cache_compression_config(filename):
    """Importa configuración de compresión de caché de API"""
    global api_cache_compression_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            api_cache_compression_config = json.load(f)
        save_api_cache_compression_config()
        return True
    return False

def validate_api_cache_compression_config():
    """Valida configuración de compresión de caché de API"""
    errors = []
    
    if "enabled" in api_cache_compression_config:
        if not isinstance(api_cache_compression_config["enabled"], bool):
            errors.append("enabled must be boolean")
    
    for key in ["min_size_bytes", "compression_level"]:
        if key in api_cache_compression_config:
            if not isinstance(api_cache_compression_config[key], int):
                errors.append(key + " must be integer")
    
    return errors

def backup_api_cache_compression_config():
    """Crea backup de configuración de compresión de caché de API"""
    backup_name = "api_cache_compression_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_api_cache_compression_config(backup_name)
    return backup_name

def restore_api_cache_compression_config(backup_name):
    """Restaura configuración de compresión de caché de API desde backup"""
    return import_api_cache_compression_config(backup_name)

def get_api_cache_compression_config_summary():
    """Obtiene resumen de configuración de compresión de caché de API"""
    return {
        "enabled": is_cache_compression_enabled(),
        "algorithm": get_compression_algorithm(),
        "compression_level": get_compression_level()
    }

# Cargar configuración de compresión de caché de API al importar
load_api_cache_compression_config()
