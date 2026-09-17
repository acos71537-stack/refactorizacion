import os
import json
import time
from datetime import datetime

# Variables globales
API_TIMEOUT_RETRY_CONFIG_FILE = "api_timeout_retry_config.json"
api_timeout_retry_config = {}

def load_api_timeout_retry_config():
    """Carga configuración de timeout y retry de API"""
    global api_timeout_retry_config
    
    if os.path.exists(API_TIMEOUT_RETRY_CONFIG_FILE):
        with open(API_TIMEOUT_RETRY_CONFIG_FILE, 'r') as f:
            api_timeout_retry_config = json.load(f)
    else:
        api_timeout_retry_config = {
            "connect_timeout": 10,
            "read_timeout": 30,
            "write_timeout": 30,
            "retry_on_timeout": True
        }

def save_api_timeout_retry_config():
    """Guarda configuración de timeout y retry de API"""
    with open(API_TIMEOUT_RETRY_CONFIG_FILE, 'w') as f:
        json.dump(api_timeout_retry_config, f, indent=4)

def get_api_timeout_retry_setting(key):
    """Obtiene configuración de timeout y retry de API"""
    return api_timeout_retry_config.get(key)

def set_api_timeout_retry_setting(key, value):
    """Establece configuración de timeout y retry de API"""
    api_timeout_retry_config[key] = value
    save_api_timeout_retry_config()

def get_all_api_timeout_retry_settings():
    """Obtiene todas las configuraciones de timeout y retry de API"""
    return api_timeout_retry_config.copy()

def reset_api_timeout_retry_config():
    """Resetea configuración de timeout y retry de API"""
    global api_timeout_retry_config
    api_timeout_retry_config = {
        "connect_timeout": 10,
        "read_timeout": 30,
        "write_timeout": 30,
        "retry_on_timeout": True
    }
    save_api_timeout_retry_config()

def get_connect_timeout():
    """Obtiene timeout de conexión"""
    return api_timeout_retry_config.get("connect_timeout", 10)

def set_connect_timeout(timeout):
    """Establece timeout de conexión"""
    api_timeout_retry_config["connect_timeout"] = timeout
    save_api_timeout_retry_config()

def get_read_timeout():
    """Obtiene timeout de lectura"""
    return api_timeout_retry_config.get("read_timeout", 30)

def set_read_timeout(timeout):
    """Establece timeout de lectura"""
    api_timeout_retry_config["read_timeout"] = timeout
    save_api_timeout_retry_config()

def get_write_timeout():
    """Obtiene timeout de escritura"""
    return api_timeout_retry_config.get("write_timeout", 30)

def set_write_timeout(timeout):
    """Establece timeout de escritura"""
    api_timeout_retry_config["write_timeout"] = timeout
    save_api_timeout_retry_config()

def is_retry_on_timeout_enabled():
    """Verifica si retry en timeout está habilitado"""
    return api_timeout_retry_config.get("retry_on_timeout", True)

def enable_retry_on_timeout():
    """Habilita retry en timeout"""
    api_timeout_retry_config["retry_on_timeout"] = True
    save_api_timeout_retry_config()

def disable_retry_on_timeout():
    """Deshabilita retry en timeout"""
    api_timeout_retry_config["retry_on_timeout"] = False
    save_api_timeout_retry_config()

def export_api_timeout_retry_config(filename):
    """Exporta configuración de timeout y retry de API"""
    with open(filename, 'w') as f:
        json.dump(api_timeout_retry_config, f, indent=4)

def import_api_timeout_retry_config(filename):
    """Importa configuración de timeout y retry de API"""
    global api_timeout_retry_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            api_timeout_retry_config = json.load(f)
        save_api_timeout_retry_config()
        return True
    return False

def validate_api_timeout_retry_config():
    """Valida configuración de timeout y retry de API"""
    errors = []
    
    if "retry_on_timeout" in api_timeout_retry_config:
        if not isinstance(api_timeout_retry_config["retry_on_timeout"], bool):
            errors.append("retry_on_timeout must be boolean")
    
    for key in ["connect_timeout", "read_timeout", "write_timeout"]:
        if key in api_timeout_retry_config:
            if not isinstance(api_timeout_retry_config[key], int):
                errors.append(key + " must be integer")
    
    return errors

def backup_api_timeout_retry_config():
    """Crea backup de configuración de timeout y retry de API"""
    backup_name = "api_timeout_retry_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_api_timeout_retry_config(backup_name)
    return backup_name

def restore_api_timeout_retry_config(backup_name):
    """Restaura configuración de timeout y retry de API desde backup"""
    return import_api_timeout_retry_config(backup_name)

def get_api_timeout_retry_config_summary():
    """Obtiene resumen de configuración de timeout y retry de API"""
    return {
        "connect_timeout": get_connect_timeout(),
        "read_timeout": get_read_timeout(),
        "retry_on_timeout": is_retry_on_timeout_enabled()
    }

# Cargar configuración de timeout y retry de API al importar
load_api_timeout_retry_config()
