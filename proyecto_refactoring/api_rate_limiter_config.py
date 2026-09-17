import os
import json
import time
from datetime import datetime

# Variables globales
API_RATE_LIMITER_CONFIG_FILE = "api_rate_limiter_config.json"
api_rate_limiter_config = {}

def load_api_rate_limiter_config():
    """Carga configuración de limitador de tasa de API"""
    global api_rate_limiter_config
    
    if os.path.exists(API_RATE_LIMITER_CONFIG_FILE):
        with open(API_RATE_LIMITER_CONFIG_FILE, 'r') as f:
            api_rate_limiter_config = json.load(f)
    else:
        api_rate_limiter_config = {
            "enabled": True,
            "algorithm": "token-bucket",
            "bucket_size": 10,
            "refill_rate": 1
        }

def save_api_rate_limiter_config():
    """Guarda configuración de limitador de tasa de API"""
    with open(API_RATE_LIMITER_CONFIG_FILE, 'w') as f:
        json.dump(api_rate_limiter_config, f, indent=4)

def get_api_rate_limiter_setting(key):
    """Obtiene configuración de limitador de tasa de API"""
    return api_rate_limiter_config.get(key)

def set_api_rate_limiter_setting(key, value):
    """Establece configuración de limitador de tasa de API"""
    api_rate_limiter_config[key] = value
    save_api_rate_limiter_config()

def get_all_api_rate_limiter_settings():
    """Obtiene todas las configuraciones de limitador de tasa de API"""
    return api_rate_limiter_config.copy()

def reset_api_rate_limiter_config():
    """Resetea configuración de limitador de tasa de API"""
    global api_rate_limiter_config
    api_rate_limiter_config = {
        "enabled": True,
        "algorithm": "token-bucket",
        "bucket_size": 10,
        "refill_rate": 1
    }
    save_api_rate_limiter_config()

def is_rate_limiter_enabled():
    """Verifica si limitador de tasa está habilitado"""
    return api_rate_limiter_config.get("enabled", True)

def enable_rate_limiter():
    """Habilita limitador de tasa"""
    api_rate_limiter_config["enabled"] = True
    save_api_rate_limiter_config()

def disable_rate_limiter():
    """Deshabilita limitador de tasa"""
    api_rate_limiter_config["enabled"] = False
    save_api_rate_limiter_config()

def get_rate_limiter_algorithm():
    """Obtiene algoritmo de limitador de tasa"""
    return api_rate_limiter_config.get("algorithm", "token-bucket")

def set_rate_limiter_algorithm(algorithm):
    """Establece algoritmo de limitador de tasa"""
    api_rate_limiter_config["algorithm"] = algorithm
    save_api_rate_limiter_config()

def get_bucket_size():
    """Obtiene tamaño de bucket"""
    return api_rate_limiter_config.get("bucket_size", 10)

def set_bucket_size(size):
    """Establece tamaño de bucket"""
    api_rate_limiter_config["bucket_size"] = size
    save_api_rate_limiter_config()

def get_refill_rate():
    """Obtiene tasa de relleno"""
    return api_rate_limiter_config.get("refill_rate", 1)

def set_refill_rate(rate):
    """Establece tasa de relleno"""
    api_rate_limiter_config["refill_rate"] = rate
    save_api_rate_limiter_config()

def export_api_rate_limiter_config(filename):
    """Exporta configuración de limitador de tasa de API"""
    with open(filename, 'w') as f:
        json.dump(api_rate_limiter_config, f, indent=4)

def import_api_rate_limiter_config(filename):
    """Importa configuración de limitador de tasa de API"""
    global api_rate_limiter_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            api_rate_limiter_config = json.load(f)
        save_api_rate_limiter_config()
        return True
    return False

def validate_api_rate_limiter_config():
    """Valida configuración de limitador de tasa de API"""
    errors = []
    
    if "enabled" in api_rate_limiter_config:
        if not isinstance(api_rate_limiter_config["enabled"], bool):
            errors.append("enabled must be boolean")
    
    for key in ["bucket_size", "refill_rate"]:
        if key in api_rate_limiter_config:
            if not isinstance(api_rate_limiter_config[key], int):
                errors.append(key + " must be integer")
    
    return errors

def backup_api_rate_limiter_config():
    """Crea backup de configuración de limitador de tasa de API"""
    backup_name = "api_rate_limiter_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_api_rate_limiter_config(backup_name)
    return backup_name

def restore_api_rate_limiter_config(backup_name):
    """Restaura configuración de limitador de tasa de API desde backup"""
    return import_api_rate_limiter_config(backup_name)

def get_api_rate_limiter_config_summary():
    """Obtiene resumen de configuración de limitador de tasa de API"""
    return {
        "enabled": is_rate_limiter_enabled(),
        "algorithm": get_rate_limiter_algorithm(),
        "bucket_size": get_bucket_size()
    }

# Cargar configuración de limitador de tasa de API al importar
load_api_rate_limiter_config()
