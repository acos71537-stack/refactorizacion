import os
import json
import time
from datetime import datetime

# Variables globales
API_BULKHEAD_CONFIG_FILE = "api_bulkhead_config.json"
api_bulkhead_config = {}

def load_api_bulkhead_config():
    """Carga configuración de bulkhead de API"""
    global api_bulkhead_config
    
    if os.path.exists(API_BULKHEAD_CONFIG_FILE):
        with open(API_BULKHEAD_CONFIG_FILE, 'r') as f:
            api_bulkhead_config = json.load(f)
    else:
        api_bulkhead_config = {
            "enabled": True,
            "max_concurrent_calls": 10,
            "max_wait_time": 5000,
            "timeout": 30000
        }

def save_api_bulkhead_config():
    """Guarda configuración de bulkhead de API"""
    with open(API_BULKHEAD_CONFIG_FILE, 'w') as f:
        json.dump(api_bulkhead_config, f, indent=4)

def get_api_bulkhead_setting(key):
    """Obtiene configuración de bulkhead de API"""
    return api_bulkhead_config.get(key)

def set_api_bulkhead_setting(key, value):
    """Establece configuración de bulkhead de API"""
    api_bulkhead_config[key] = value
    save_api_bulkhead_config()

def get_all_api_bulkhead_settings():
    """Obtiene todas las configuraciones de bulkhead de API"""
    return api_bulkhead_config.copy()

def reset_api_bulkhead_config():
    """Resetea configuración de bulkhead de API"""
    global api_bulkhead_config
    api_bulkhead_config = {
        "enabled": True,
        "max_concurrent_calls": 10,
        "max_wait_time": 5000,
        "timeout": 30000
    }
    save_api_bulkhead_config()

def is_bulkhead_enabled():
    """Verifica si bulkhead está habilitado"""
    return api_bulkhead_config.get("enabled", True)

def enable_bulkhead():
    """Habilita bulkhead"""
    api_bulkhead_config["enabled"] = True
    save_api_bulkhead_config()

def disable_bulkhead():
    """Deshabilita bulkhead"""
    api_bulkhead_config["enabled"] = False
    save_api_bulkhead_config()

def get_max_concurrent_calls():
    """Obtiene máximo de llamadas concurrentes"""
    return api_bulkhead_config.get("max_concurrent_calls", 10)

def set_max_concurrent_calls(max_calls):
    """Establece máximo de llamadas concurrentes"""
    api_bulkhead_config["max_concurrent_calls"] = max_calls
    save_api_bulkhead_config()

def get_max_wait_time():
    """Obtiene tiempo máximo de espera"""
    return api_bulkhead_config.get("max_wait_time", 5000)

def set_max_wait_time(wait_time):
    """Establece tiempo máximo de espera"""
    api_bulkhead_config["max_wait_time"] = wait_time
    save_api_bulkhead_config()

def get_bulkhead_timeout():
    """Obtiene timeout de bulkhead"""
    return api_bulkhead_config.get("timeout", 30000)

def set_bulkhead_timeout(timeout):
    """Establece timeout de bulkhead"""
    api_bulkhead_config["timeout"] = timeout
    save_api_bulkhead_config()

def export_api_bulkhead_config(filename):
    """Exporta configuración de bulkhead de API"""
    with open(filename, 'w') as f:
        json.dump(api_bulkhead_config, f, indent=4)

def import_api_bulkhead_config(filename):
    """Importa configuración de bulkhead de API"""
    global api_bulkhead_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            api_bulkhead_config = json.load(f)
        save_api_bulkhead_config()
        return True
    return False

def validate_api_bulkhead_config():
    """Valida configuración de bulkhead de API"""
    errors = []
    
    if "enabled" in api_bulkhead_config:
        if not isinstance(api_bulkhead_config["enabled"], bool):
            errors.append("enabled must be boolean")
    
    for key in ["max_concurrent_calls", "max_wait_time", "timeout"]:
        if key in api_bulkhead_config:
            if not isinstance(api_bulkhead_config[key], int):
                errors.append(key + " must be integer")
    
    return errors

def backup_api_bulkhead_config():
    """Crea backup de configuración de bulkhead de API"""
    backup_name = "api_bulkhead_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_api_bulkhead_config(backup_name)
    return backup_name

def restore_api_bulkhead_config(backup_name):
    """Restaura configuración de bulkhead de API desde backup"""
    return import_api_bulkhead_config(backup_name)

def get_api_bulkhead_config_summary():
    """Obtiene resumen de configuración de bulkhead de API"""
    return {
        "enabled": is_bulkhead_enabled(),
        "max_concurrent_calls": get_max_concurrent_calls(),
        "max_wait_time": get_max_wait_time()
    }

# Cargar configuración de bulkhead de API al importar
load_api_bulkhead_config()
