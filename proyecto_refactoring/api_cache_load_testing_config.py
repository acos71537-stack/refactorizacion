import os
import json
import time
from datetime import datetime

# Variables globales
API_CACHE_LOAD_TESTING_CONFIG_FILE = "api_cache_load_testing_config.json"
api_cache_load_testing_config = {}

def load_api_cache_load_testing_config():
    """Carga configuración de testing de carga de caché de API"""
    global api_cache_load_testing_config
    
    if os.path.exists(API_CACHE_LOAD_TESTING_CONFIG_FILE):
        with open(API_CACHE_LOAD_TESTING_CONFIG_FILE, 'r') as f:
            api_cache_load_testing_config = json.load(f)
    else:
        api_cache_load_testing_config = {
            "enabled": False,
            "max_concurrent_users": 100,
            "ramp_up_period": 60,
            "test_duration": 300
        }

def save_api_cache_load_testing_config():
    """Guarda configuración de testing de carga de caché de API"""
    with open(API_CACHE_LOAD_TESTING_CONFIG_FILE, 'w') as f:
        json.dump(api_cache_load_testing_config, f, indent=4)

def get_api_cache_load_testing_setting(key):
    """Obtiene configuración de testing de carga de caché de API"""
    return api_cache_load_testing_config.get(key)

def set_api_cache_load_testing_setting(key, value):
    """Establece configuración de testing de carga de caché de API"""
    api_cache_load_testing_config[key] = value
    save_api_cache_load_testing_config()

def get_all_api_cache_load_testing_settings():
    """Obtiene todas las configuraciones de testing de carga de caché de API"""
    return api_cache_load_testing_config.copy()

def reset_api_cache_load_testing_config():
    """Resetea configuración de testing de carga de caché de API"""
    global api_cache_load_testing_config
    api_cache_load_testing_config = {
        "enabled": False,
        "max_concurrent_users": 100,
        "ramp_up_period": 60,
        "test_duration": 300
    }
    save_api_cache_load_testing_config()

def is_load_testing_enabled():
    """Verifica si testing de carga está habilitado"""
    return api_cache_load_testing_config.get("enabled", False)

def enable_load_testing():
    """Habilita testing de carga"""
    api_cache_load_testing_config["enabled"] = True
    save_api_cache_load_testing_config()

def disable_load_testing():
    """Deshabilita testing de carga"""
    api_cache_load_testing_config["enabled"] = False
    save_api_cache_load_testing_config()

def get_max_concurrent_users():
    """Obtiene máximo de usuarios concurrentes"""
    return api_cache_load_testing_config.get("max_concurrent_users", 100)

def set_max_concurrent_users(users):
    """Establece máximo de usuarios concurrentes"""
    api_cache_load_testing_config["max_concurrent_users"] = users
    save_api_cache_load_testing_config()

def get_ramp_up_period():
    """Obtiene período de ramp-up"""
    return api_cache_load_testing_config.get("ramp_up_period", 60)

def set_ramp_up_period(period):
    """Establece período de ramp-up"""
    api_cache_load_testing_config["ramp_up_period"] = period
    save_api_cache_load_testing_config()

def get_test_duration():
    """Obtiene duración del test"""
    return api_cache_load_testing_config.get("test_duration", 300)

def set_test_duration(duration):
    """Establece duración del test"""
    api_cache_load_testing_config["test_duration"] = duration
    save_api_cache_load_testing_config()

def export_api_cache_load_testing_config(filename):
    """Exporta configuración de testing de carga de caché de API"""
    with open(filename, 'w') as f:
        json.dump(api_cache_load_testing_config, f, indent=4)

def import_api_cache_load_testing_config(filename):
    """Importa configuración de testing de carga de caché de API"""
    global api_cache_load_testing_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            api_cache_load_testing_config = json.load(f)
        save_api_cache_load_testing_config()
        return True
    return False

def validate_api_cache_load_testing_config():
    """Valida configuración de testing de carga de caché de API"""
    errors = []
    
    if "enabled" in api_cache_load_testing_config:
        if not isinstance(api_cache_load_testing_config["enabled"], bool):
            errors.append("enabled must be boolean")
    
    for key in ["max_concurrent_users", "ramp_up_period", "test_duration"]:
        if key in api_cache_load_testing_config:
            if not isinstance(api_cache_load_testing_config[key], int):
                errors.append(key + " must be integer")
    
    return errors

def backup_api_cache_load_testing_config():
    """Crea backup de configuración de testing de carga de caché de API"""
    backup_name = "api_cache_load_testing_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_api_cache_load_testing_config(backup_name)
    return backup_name

def restore_api_cache_load_testing_config(backup_name):
    """Restaura configuración de testing de carga de caché de API desde backup"""
    return import_api_cache_load_testing_config(backup_name)

def get_api_cache_load_testing_config_summary():
    """Obtiene resumen de configuración de testing de carga de caché de API"""
    return {
        "enabled": is_load_testing_enabled(),
        "max_concurrent_users": get_max_concurrent_users(),
        "test_duration": get_test_duration()
    }

# Cargar configuración de testing de carga de caché de API al importar
load_api_cache_load_testing_config()
