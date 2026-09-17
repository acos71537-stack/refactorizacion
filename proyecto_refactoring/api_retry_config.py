import os
import json
import time
from datetime import datetime

# Variables globales
API_RETRY_CONFIG_FILE = "api_retry_config.json"
api_retry_config = {}

def load_api_retry_config():
    """Carga configuración de reintentos de API"""
    global api_retry_config
    
    if os.path.exists(API_RETRY_CONFIG_FILE):
        with open(API_RETRY_CONFIG_FILE, 'r') as f:
            api_retry_config = json.load(f)
    else:
        api_retry_config = {
            "max_retries": 3,
            "retry_delay": 1,
            "exponential_backoff": True,
            "max_retry_delay": 30
        }

def save_api_retry_config():
    """Guarda configuración de reintentos de API"""
    with open(API_RETRY_CONFIG_FILE, 'w') as f:
        json.dump(api_retry_config, f, indent=4)

def get_api_retry_setting(key):
    """Obtiene configuración de reintentos de API"""
    return api_retry_config.get(key)

def set_api_retry_setting(key, value):
    """Establece configuración de reintentos de API"""
    api_retry_config[key] = value
    save_api_retry_config()

def get_all_api_retry_settings():
    """Obtiene todas las configuraciones de reintentos de API"""
    return api_retry_config.copy()

def reset_api_retry_config():
    """Resetea configuración de reintentos de API"""
    global api_retry_config
    api_retry_config = {
        "max_retries": 3,
        "retry_delay": 1,
        "exponential_backoff": True,
        "max_retry_delay": 30
    }
    save_api_retry_config()

def get_max_retries():
    """Obtiene máximo de reintentos"""
    return api_retry_config.get("max_retries", 3)

def set_max_retries(max_retries):
    """Establece máximo de reintentos"""
    api_retry_config["max_retries"] = max_retries
    save_api_retry_config()

def get_retry_delay():
    """Obtiene delay de reintentos"""
    return api_retry_config.get("retry_delay", 1)

def set_retry_delay(delay):
    """Establece delay de reintentos"""
    api_retry_config["retry_delay"] = delay
    save_api_retry_config()

def is_exponential_backoff_enabled():
    """Verifica si backoff exponencial está habilitado"""
    return api_retry_config.get("exponential_backoff", True)

def enable_exponential_backoff():
    """Habilita backoff exponencial"""
    api_retry_config["exponential_backoff"] = True
    save_api_retry_config()

def disable_exponential_backoff():
    """Deshabilita backoff exponencial"""
    api_retry_config["exponential_backoff"] = False
    save_api_retry_config()

def get_max_retry_delay():
    """Obtiene delay máximo de reintentos"""
    return api_retry_config.get("max_retry_delay", 30)

def set_max_retry_delay(delay):
    """Establece delay máximo de reintentos"""
    api_retry_config["max_retry_delay"] = delay
    save_api_retry_config()

def export_api_retry_config(filename):
    """Exporta configuración de reintentos de API"""
    with open(filename, 'w') as f:
        json.dump(api_retry_config, f, indent=4)

def import_api_retry_config(filename):
    """Importa configuración de reintentos de API"""
    global api_retry_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            api_retry_config = json.load(f)
        save_api_retry_config()
        return True
    return False

def validate_api_retry_config():
    """Valida configuración de reintentos de API"""
    errors = []
    
    for key in ["max_retries", "retry_delay", "max_retry_delay"]:
        if key in api_retry_config:
            if not isinstance(api_retry_config[key], int):
                errors.append(key + " must be integer")
    
    return errors

def backup_api_retry_config():
    """Crea backup de configuración de reintentos de API"""
    backup_name = "api_retry_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_api_retry_config(backup_name)
    return backup_name

def restore_api_retry_config(backup_name):
    """Restaura configuración de reintentos de API desde backup"""
    return import_api_retry_config(backup_name)

def get_api_retry_config_summary():
    """Obtiene resumen de configuración de reintentos de API"""
    return {
        "max_retries": get_max_retries(),
        "retry_delay": get_retry_delay(),
        "exponential_backoff": is_exponential_backoff_enabled()
    }

# Cargar configuración de reintentos de API al importar
load_api_retry_config()
