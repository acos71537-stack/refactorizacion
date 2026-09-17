import os
import json
import time
from datetime import datetime

# Variables globales
API_RATE_LIMIT_CONFIG_FILE = "api_rate_limit_config.json"
api_rate_limit_config = {}

def load_api_rate_limit_config():
    """Carga configuración de límite de tasa de API"""
    global api_rate_limit_config
    
    if os.path.exists(API_RATE_LIMIT_CONFIG_FILE):
        with open(API_RATE_LIMIT_CONFIG_FILE, 'r') as f:
            api_rate_limit_config = json.load(f)
    else:
        api_rate_limit_config = {
            "omdb_requests_per_minute": 10,
            "tvmaze_requests_per_minute": 20,
            "enable_rate_limiting": True,
            "rate_limit_window": 60
        }

def save_api_rate_limit_config():
    """Guarda configuración de límite de tasa de API"""
    with open(API_RATE_LIMIT_CONFIG_FILE, 'w') as f:
        json.dump(api_rate_limit_config, f, indent=4)

def get_api_rate_limit_setting(key):
    """Obtiene configuración de límite de tasa de API"""
    return api_rate_limit_config.get(key)

def set_api_rate_limit_setting(key, value):
    """Establece configuración de límite de tasa de API"""
    api_rate_limit_config[key] = value
    save_api_rate_limit_config()

def get_all_api_rate_limit_settings():
    """Obtiene todas las configuraciones de límite de tasa de API"""
    return api_rate_limit_config.copy()

def reset_api_rate_limit_config():
    """Resetea configuración de límite de tasa de API"""
    global api_rate_limit_config
    api_rate_limit_config = {
        "omdb_requests_per_minute": 10,
        "tvmaze_requests_per_minute": 20,
        "enable_rate_limiting": True,
        "rate_limit_window": 60
    }
    save_api_rate_limit_config()

def get_omdb_requests_per_minute():
    """Obtiene requests por minuto de OMDB"""
    return api_rate_limit_config.get("omdb_requests_per_minute", 10)

def set_omdb_requests_per_minute(requests):
    """Establece requests por minuto de OMDB"""
    api_rate_limit_config["omdb_requests_per_minute"] = requests
    save_api_rate_limit_config()

def get_tvmaze_requests_per_minute():
    """Obtiene requests por minuto de TVMaze"""
    return api_rate_limit_config.get("tvmaze_requests_per_minute", 20)

def set_tvmaze_requests_per_minute(requests):
    """Establece requests por minuto de TVMaze"""
    api_rate_limit_config["tvmaze_requests_per_minute"] = requests
    save_api_rate_limit_config()

def is_rate_limiting_enabled():
    """Verifica si límite de tasa está habilitado"""
    return api_rate_limit_config.get("enable_rate_limiting", True)

def enable_rate_limiting():
    """Habilita límite de tasa"""
    api_rate_limit_config["enable_rate_limiting"] = True
    save_api_rate_limit_config()

def disable_rate_limiting():
    """Deshabilita límite de tasa"""
    api_rate_limit_config["enable_rate_limiting"] = False
    save_api_rate_limit_config()

def get_rate_limit_window():
    """Obtiene ventana de límite de tasa"""
    return api_rate_limit_config.get("rate_limit_window", 60)

def set_rate_limit_window(window):
    """Establece ventana de límite de tasa"""
    api_rate_limit_config["rate_limit_window"] = window
    save_api_rate_limit_config()

def export_api_rate_limit_config(filename):
    """Exporta configuración de límite de tasa de API"""
    with open(filename, 'w') as f:
        json.dump(api_rate_limit_config, f, indent=4)

def import_api_rate_limit_config(filename):
    """Importa configuración de límite de tasa de API"""
    global api_rate_limit_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            api_rate_limit_config = json.load(f)
        save_api_rate_limit_config()
        return True
    return False

def validate_api_rate_limit_config():
    """Valida configuración de límite de tasa de API"""
    errors = []
    
    for key in ["omdb_requests_per_minute", "tvmaze_requests_per_minute", "rate_limit_window"]:
        if key in api_rate_limit_config:
            if not isinstance(api_rate_limit_config[key], int):
                errors.append(key + " must be integer")
    
    return errors

def backup_api_rate_limit_config():
    """Crea backup de configuración de límite de tasa de API"""
    backup_name = "api_rate_limit_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_api_rate_limit_config(backup_name)
    return backup_name

def restore_api_rate_limit_config(backup_name):
    """Restaura configuración de límite de tasa de API desde backup"""
    return import_api_rate_limit_config(backup_name)

def get_api_rate_limit_config_summary():
    """Obtiene resumen de configuración de límite de tasa de API"""
    return {
        "omdb_requests_per_minute": get_omdb_requests_per_minute(),
        "tvmaze_requests_per_minute": get_tvmaze_requests_per_minute(),
        "enable_rate_limiting": is_rate_limiting_enabled()
    }

# Cargar configuración de límite de tasa de API al importar
load_api_rate_limit_config()
