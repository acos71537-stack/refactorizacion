import os
import json
import time
from datetime import datetime

# Variables globales
API_CACHE_WARMING_CONFIG_FILE = "api_cache_warming_config.json"
api_cache_warming_config = {}

def load_api_cache_warming_config():
    """Carga configuración de cache warming de API"""
    global api_cache_warming_config
    
    if os.path.exists(API_CACHE_WARMING_CONFIG_FILE):
        with open(API_CACHE_WARMING_CONFIG_FILE, 'r') as f:
            api_cache_warming_config = json.load(f)
    else:
        api_cache_warming_config = {
            "enabled": False,
            "warming_interval": 300,
            "warming_strategy": "predictive",
            "max_warming_items": 100
        }

def save_api_cache_warming_config():
    """Guarda configuración de cache warming de API"""
    with open(API_CACHE_WARMING_CONFIG_FILE, 'w') as f:
        json.dump(api_cache_warming_config, f, indent=4)

def get_api_cache_warming_setting(key):
    """Obtiene configuración de cache warming de API"""
    return api_cache_warming_config.get(key)

def set_api_cache_warming_setting(key, value):
    """Establece configuración de cache warming de API"""
    api_cache_warming_config[key] = value
    save_api_cache_warming_config()

def get_all_api_cache_warming_settings():
    """Obtiene todas las configuraciones de cache warming de API"""
    return api_cache_warming_config.copy()

def reset_api_cache_warming_config():
    """Resetea configuración de cache warming de API"""
    global api_cache_warming_config
    api_cache_warming_config = {
        "enabled": False,
        "warming_interval": 300,
        "warming_strategy": "predictive",
        "max_warming_items": 100
    }
    save_api_cache_warming_config()

def is_cache_warming_enabled():
    """Verifica si cache warming está habilitado"""
    return api_cache_warming_config.get("enabled", False)

def enable_cache_warming():
    """Habilita cache warming"""
    api_cache_warming_config["enabled"] = True
    save_api_cache_warming_config()

def disable_cache_warming():
    """Deshabilita cache warming"""
    api_cache_warming_config["enabled"] = False
    save_api_cache_warming_config()

def get_warming_interval():
    """Obtiene intervalo de warming"""
    return api_cache_warming_config.get("warming_interval", 300)

def set_warming_interval(interval):
    """Establece intervalo de warming"""
    api_cache_warming_config["warming_interval"] = interval
    save_api_cache_warming_config()

def get_warming_strategy():
    """Obtiene estrategia de warming"""
    return api_cache_warming_config.get("warming_strategy", "predictive")

def set_warming_strategy(strategy):
    """Establece estrategia de warming"""
    api_cache_warming_config["warming_strategy"] = strategy
    save_api_cache_warming_config()

def get_max_warming_items():
    """Obtiene máximo de items de warming"""
    return api_cache_warming_config.get("max_warming_items", 100)

def set_max_warming_items(max_items):
    """Establece máximo de items de warming"""
    api_cache_warming_config["max_warming_items"] = max_items
    save_api_cache_warming_config()

def export_api_cache_warming_config(filename):
    """Exporta configuración de cache warming de API"""
    with open(filename, 'w') as f:
        json.dump(api_cache_warming_config, f, indent=4)

def import_api_cache_warming_config(filename):
    """Importa configuración de cache warming de API"""
    global api_cache_warming_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            api_cache_warming_config = json.load(f)
        save_api_cache_warming_config()
        return True
    return False

def validate_api_cache_warming_config():
    """Valida configuración de cache warming de API"""
    errors = []
    
    if "enabled" in api_cache_warming_config:
        if not isinstance(api_cache_warming_config["enabled"], bool):
            errors.append("enabled must be boolean")
    
    for key in ["warming_interval", "max_warming_items"]:
        if key in api_cache_warming_config:
            if not isinstance(api_cache_warming_config[key], int):
                errors.append(key + " must be integer")
    
    return errors

def backup_api_cache_warming_config():
    """Crea backup de configuración de cache warming de API"""
    backup_name = "api_cache_warming_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_api_cache_warming_config(backup_name)
    return backup_name

def restore_api_cache_warming_config(backup_name):
    """Restaura configuración de cache warming de API desde backup"""
    return import_api_cache_warming_config(backup_name)

def get_api_cache_warming_config_summary():
    """Obtiene resumen de configuración de cache warming de API"""
    return {
        "enabled": is_cache_warming_enabled(),
        "warming_interval": get_warming_interval(),
        "warming_strategy": get_warming_strategy()
    }

# Cargar configuración de cache warming de API al importar
load_api_cache_warming_config()
