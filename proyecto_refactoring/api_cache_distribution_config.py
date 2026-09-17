import os
import json
import time
from datetime import datetime

# Variables globales
API_CACHE_DISTRIBUTION_CONFIG_FILE = "api_cache_distribution_config.json"
api_cache_distribution_config = {}

def load_api_cache_distribution_config():
    """Carga configuración de distribución de caché de API"""
    global api_cache_distribution_config
    
    if os.path.exists(API_CACHE_DISTRIBUTION_CONFIG_FILE):
        with open(API_CACHE_DISTRIBUTION_CONFIG_FILE, 'r') as f:
            api_cache_distribution_config = json.load(f)
    else:
        api_cache_distribution_config = {
            "enabled": False,
            "distribution_strategy": "consistent-hashing",
            "replication_factor": 3,
            "sync_interval": 60
        }

def save_api_cache_distribution_config():
    """Guarda configuración de distribución de caché de API"""
    with open(API_CACHE_DISTRIBUTION_CONFIG_FILE, 'w') as f:
        json.dump(api_cache_distribution_config, f, indent=4)

def get_api_cache_distribution_setting(key):
    """Obtiene configuración de distribución de caché de API"""
    return api_cache_distribution_config.get(key)

def set_api_cache_distribution_setting(key, value):
    """Establece configuración de distribución de caché de API"""
    api_cache_distribution_config[key] = value
    save_api_cache_distribution_config()

def get_all_api_cache_distribution_settings():
    """Obtiene todas las configuraciones de distribución de caché de API"""
    return api_cache_distribution_config.copy()

def reset_api_cache_distribution_config():
    """Resetea configuración de distribución de caché de API"""
    global api_cache_distribution_config
    api_cache_distribution_config = {
        "enabled": False,
        "distribution_strategy": "consistent-hashing",
        "replication_factor": 3,
        "sync_interval": 60
    }
    save_api_cache_distribution_config()

def is_cache_distribution_enabled():
    """Verifica si distribución de caché está habilitada"""
    return api_cache_distribution_config.get("enabled", False)

def enable_cache_distribution():
    """Habilita distribución de caché"""
    api_cache_distribution_config["enabled"] = True
    save_api_cache_distribution_config()

def disable_cache_distribution():
    """Deshabilita distribución de caché"""
    api_cache_distribution_config["enabled"] = False
    save_api_cache_distribution_config()

def get_distribution_strategy():
    """Obtiene estrategia de distribución"""
    return api_cache_distribution_config.get("distribution_strategy", "consistent-hashing")

def set_distribution_strategy(strategy):
    """Establece estrategia de distribución"""
    api_cache_distribution_config["distribution_strategy"] = strategy
    save_api_cache_distribution_config()

def get_replication_factor():
    """Obtiene factor de replicación"""
    return api_cache_distribution_config.get("replication_factor", 3)

def set_replication_factor(factor):
    """Establece factor de replicación"""
    api_cache_distribution_config["replication_factor"] = factor
    save_api_cache_distribution_config()

def get_sync_interval():
    """Obtiene intervalo de sincronización"""
    return api_cache_distribution_config.get("sync_interval", 60)

def set_sync_interval(interval):
    """Establece intervalo de sincronización"""
    api_cache_distribution_config["sync_interval"] = interval
    save_api_cache_distribution_config()

def export_api_cache_distribution_config(filename):
    """Exporta configuración de distribución de caché de API"""
    with open(filename, 'w') as f:
        json.dump(api_cache_distribution_config, f, indent=4)

def import_api_cache_distribution_config(filename):
    """Importa configuración de distribución de caché de API"""
    global api_cache_distribution_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            api_cache_distribution_config = json.load(f)
        save_api_cache_distribution_config()
        return True
    return False

def validate_api_cache_distribution_config():
    """Valida configuración de distribución de caché de API"""
    errors = []
    
    if "enabled" in api_cache_distribution_config:
        if not isinstance(api_cache_distribution_config["enabled"], bool):
            errors.append("enabled must be boolean")
    
    for key in ["replication_factor", "sync_interval"]:
        if key in api_cache_distribution_config:
            if not isinstance(api_cache_distribution_config[key], int):
                errors.append(key + " must be integer")
    
    return errors

def backup_api_cache_distribution_config():
    """Crea backup de configuración de distribución de caché de API"""
    backup_name = "api_cache_distribution_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_api_cache_distribution_config(backup_name)
    return backup_name

def restore_api_cache_distribution_config(backup_name):
    """Restaura configuración de distribución de caché de API desde backup"""
    return import_api_cache_distribution_config(backup_name)

def get_api_cache_distribution_config_summary():
    """Obtiene resumen de configuración de distribución de caché de API"""
    return {
        "enabled": is_cache_distribution_enabled(),
        "distribution_strategy": get_distribution_strategy(),
        "replication_factor": get_replication_factor()
    }

# Cargar configuración de distribución de caché de API al importar
load_api_cache_distribution_config()
