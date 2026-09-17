import os
import json
import time
from datetime import datetime

# Variables globales
API_TIMEOUT_CONFIG_FILE = "api_timeout_config.json"
api_timeout_config = {}

def load_api_timeout_config():
    """Carga configuración de timeout de API"""
    global api_timeout_config
    
    if os.path.exists(API_TIMEOUT_CONFIG_FILE):
        with open(API_TIMEOUT_CONFIG_FILE, 'r') as f:
            api_timeout_config = json.load(f)
    else:
        api_timeout_config = {
            "omdb_timeout": 30,
            "tvmaze_timeout": 30,
            "default_timeout": 30,
            "connect_timeout": 10
        }

def save_api_timeout_config():
    """Guarda configuración de timeout de API"""
    with open(API_TIMEOUT_CONFIG_FILE, 'w') as f:
        json.dump(api_timeout_config, f, indent=4)

def get_api_timeout_setting(key):
    """Obtiene configuración de timeout de API"""
    return api_timeout_config.get(key)

def set_api_timeout_setting(key, value):
    """Establece configuración de timeout de API"""
    api_timeout_config[key] = value
    save_api_timeout_config()

def get_all_api_timeout_settings():
    """Obtiene todas las configuraciones de timeout de API"""
    return api_timeout_config.copy()

def reset_api_timeout_config():
    """Resetea configuración de timeout de API"""
    global api_timeout_config
    api_timeout_config = {
        "omdb_timeout": 30,
        "tvmaze_timeout": 30,
        "default_timeout": 30,
        "connect_timeout": 10
    }
    save_api_timeout_config()

def get_omdb_timeout():
    """Obtiene timeout de OMDB"""
    return api_timeout_config.get("omdb_timeout", 30)

def set_omdb_timeout(timeout):
    """Establece timeout de OMDB"""
    api_timeout_config["omdb_timeout"] = timeout
    save_api_timeout_config()

def get_tvmaze_timeout():
    """Obtiene timeout de TVMaze"""
    return api_timeout_config.get("tvmaze_timeout", 30)

def set_tvmaze_timeout(timeout):
    """Establece timeout de TVMaze"""
    api_timeout_config["tvmaze_timeout"] = timeout
    save_api_timeout_config()

def get_default_timeout():
    """Obtiene timeout por defecto"""
    return api_timeout_config.get("default_timeout", 30)

def set_default_timeout(timeout):
    """Establece timeout por defecto"""
    api_timeout_config["default_timeout"] = timeout
    save_api_timeout_config()

def get_connect_timeout():
    """Obtiene timeout de conexión"""
    return api_timeout_config.get("connect_timeout", 10)

def set_connect_timeout(timeout):
    """Establece timeout de conexión"""
    api_timeout_config["connect_timeout"] = timeout
    save_api_timeout_config()

def export_api_timeout_config(filename):
    """Exporta configuración de timeout de API"""
    with open(filename, 'w') as f:
        json.dump(api_timeout_config, f, indent=4)

def import_api_timeout_config(filename):
    """Importa configuración de timeout de API"""
    global api_timeout_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            api_timeout_config = json.load(f)
        save_api_timeout_config()
        return True
    return False

def validate_api_timeout_config():
    """Valida configuración de timeout de API"""
    errors = []
    
    for key in ["omdb_timeout", "tvmaze_timeout", "default_timeout", "connect_timeout"]:
        if key in api_timeout_config:
            if not isinstance(api_timeout_config[key], int):
                errors.append(key + " must be integer")
    
    return errors

def backup_api_timeout_config():
    """Crea backup de configuración de timeout de API"""
    backup_name = "api_timeout_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_api_timeout_config(backup_name)
    return backup_name

def restore_api_timeout_config(backup_name):
    """Restaura configuración de timeout de API desde backup"""
    return import_api_timeout_config(backup_name)

def get_api_timeout_config_summary():
    """Obtiene resumen de configuración de timeout de API"""
    return {
        "omdb_timeout": get_omdb_timeout(),
        "tvmaze_timeout": get_tvmaze_timeout(),
        "default_timeout": get_default_timeout()
    }

# Cargar configuración de timeout de API al importar
load_api_timeout_config()
