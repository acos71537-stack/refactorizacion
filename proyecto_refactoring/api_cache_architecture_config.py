import os
import json
import time
from datetime import datetime

# Variables globales
API_CACHE_ARCHITECTURE_CONFIG_FILE = "api_cache_architecture_config.json"
api_cache_architecture_config = {}

def load_api_cache_architecture_config():
    """Carga configuración de arquitectura de caché de API"""
    global api_cache_architecture_config
    
    if os.path.exists(API_CACHE_ARCHITECTURE_CONFIG_FILE):
        with open(API_CACHE_ARCHITECTURE_CONFIG_FILE, 'r') as f:
            api_cache_architecture_config = json.load(f)
    else:
        api_cache_architecture_config = {
            "cache_type": "in-memory",
            "persistence": False,
            "clustering": False,
            "eviction_strategy": "lru"
        }

def save_api_cache_architecture_config():
    """Guarda configuración de arquitectura de caché de API"""
    with open(API_CACHE_ARCHITECTURE_CONFIG_FILE, 'w') as f:
        json.dump(api_cache_architecture_config, f, indent=4)

def get_api_cache_architecture_setting(key):
    """Obtiene configuración de arquitectura de caché de API"""
    return api_cache_architecture_config.get(key)

def set_api_cache_architecture_setting(key, value):
    """Establece configuración de arquitectura de caché de API"""
    api_cache_architecture_config[key] = value
    save_api_cache_architecture_config()

def get_all_api_cache_architecture_settings():
    """Obtiene todas las configuraciones de arquitectura de caché de API"""
    return api_cache_architecture_config.copy()

def reset_api_cache_architecture_config():
    """Resetea configuración de arquitectura de caché de API"""
    global api_cache_architecture_config
    api_cache_architecture_config = {
        "cache_type": "in-memory",
        "persistence": False,
        "clustering": False,
        "eviction_strategy": "lru"
    }
    save_api_cache_architecture_config()

def get_cache_type():
    """Obtiene tipo de caché"""
    return api_cache_architecture_config.get("cache_type", "in-memory")

def set_cache_type(cache_type):
    """Establece tipo de caché"""
    api_cache_architecture_config["cache_type"] = cache_type
    save_api_cache_architecture_config()

def is_persistence_enabled():
    """Verifica si persistencia está habilitada"""
    return api_cache_architecture_config.get("persistence", False)

def enable_persistence():
    """Habilita persistencia"""
    api_cache_architecture_config["persistence"] = True
    save_api_cache_architecture_config()

def disable_persistence():
    """Deshabilita persistencia"""
    api_cache_architecture_config["persistence"] = False
    save_api_cache_architecture_config()

def is_clustering_enabled():
    """Verifica si clustering está habilitado"""
    return api_cache_architecture_config.get("clustering", False)

def enable_clustering():
    """Habilita clustering"""
    api_cache_architecture_config["clustering"] = True
    save_api_cache_architecture_config()

def disable_clustering():
    """Deshabilita clustering"""
    api_cache_architecture_config["clustering"] = False
    save_api_cache_architecture_config()

def get_eviction_strategy():
    """Obtiene estrategia de evicción"""
    return api_cache_architecture_config.get("eviction_strategy", "lru")

def set_eviction_strategy(strategy):
    """Establece estrategia de evicción"""
    api_cache_architecture_config["eviction_strategy"] = strategy
    save_api_cache_architecture_config()

def export_api_cache_architecture_config(filename):
    """Exporta configuración de arquitectura de caché de API"""
    with open(filename, 'w') as f:
        json.dump(api_cache_architecture_config, f, indent=4)

def import_api_cache_architecture_config(filename):
    """Importa configuración de arquitectura de caché de API"""
    global api_cache_architecture_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            api_cache_architecture_config = json.load(f)
        save_api_cache_architecture_config()
        return True
    return False

def validate_api_cache_architecture_config():
    """Valida configuración de arquitectura de caché de API"""
    errors = []
    
    for key in ["persistence", "clustering"]:
        if key in api_cache_architecture_config:
            if not isinstance(api_cache_architecture_config[key], bool):
                errors.append(key + " must be boolean")
    
    return errors

def backup_api_cache_architecture_config():
    """Crea backup de configuración de arquitectura de caché de API"""
    backup_name = "api_cache_architecture_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_api_cache_architecture_config(backup_name)
    return backup_name

def restore_api_cache_architecture_config(backup_name):
    """Restaura configuración de arquitectura de caché de API desde backup"""
    return import_api_cache_architecture_config(backup_name)

def get_api_cache_architecture_config_summary():
    """Obtiene resumen de configuración de arquitectura de caché de API"""
    return {
        "cache_type": get_cache_type(),
        "persistence": is_persistence_enabled(),
        "clustering": is_clustering_enabled()
    }

# Cargar configuración de arquitectura de caché de API al importar
load_api_cache_architecture_config()
