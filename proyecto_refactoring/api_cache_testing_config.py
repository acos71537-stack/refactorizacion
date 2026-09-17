import os
import json
import time
from datetime import datetime

# Variables globales
API_CACHE_TESTING_CONFIG_FILE = "api_cache_testing_config.json"
api_cache_testing_config = {}

def load_api_cache_testing_config():
    """Carga configuración de testing de caché de API"""
    global api_cache_testing_config
    
    if os.path.exists(API_CACHE_TESTING_CONFIG_FILE):
        with open(API_CACHE_TESTING_CONFIG_FILE, 'r') as f:
            api_cache_testing_config = json.load(f)
    else:
        api_cache_testing_config = {
            "enabled": False,
            "mock_cache": True,
            "test_isolation": True,
            "verbose_output": True
        }

def save_api_cache_testing_config():
    """Guarda configuración de testing de caché de API"""
    with open(API_CACHE_TESTING_CONFIG_FILE, 'w') as f:
        json.dump(api_cache_testing_config, f, indent=4)

def get_api_cache_testing_setting(key):
    """Obtiene configuración de testing de caché de API"""
    return api_cache_testing_config.get(key)

def set_api_cache_testing_setting(key, value):
    """Establece configuración de testing de caché de API"""
    api_cache_testing_config[key] = value
    save_api_cache_testing_config()

def get_all_api_cache_testing_settings():
    """Obtiene todas las configuraciones de testing de caché de API"""
    return api_cache_testing_config.copy()

def reset_api_cache_testing_config():
    """Resetea configuración de testing de caché de API"""
    global api_cache_testing_config
    api_cache_testing_config = {
        "enabled": False,
        "mock_cache": True,
        "test_isolation": True,
        "verbose_output": True
    }
    save_api_cache_testing_config()

def is_cache_testing_enabled():
    """Verifica si testing de caché está habilitado"""
    return api_cache_testing_config.get("enabled", False)

def enable_cache_testing():
    """Habilita testing de caché"""
    api_cache_testing_config["enabled"] = True
    save_api_cache_testing_config()

def disable_cache_testing():
    """Deshabilita testing de caché"""
    api_cache_testing_config["enabled"] = False
    save_api_cache_testing_config()

def is_mock_cache_enabled():
    """Verifica si caché mock está habilitado"""
    return api_cache_testing_config.get("mock_cache", True)

def enable_mock_cache():
    """Habilita caché mock"""
    api_cache_testing_config["mock_cache"] = True
    save_api_cache_testing_config()

def disable_mock_cache():
    """Deshabilita caché mock"""
    api_cache_testing_config["mock_cache"] = False
    save_api_cache_testing_config()

def is_test_isolation_enabled():
    """Verifica si aislamiento de tests está habilitado"""
    return api_cache_testing_config.get("test_isolation", True)

def enable_test_isolation():
    """Habilita aislamiento de tests"""
    api_cache_testing_config["test_isolation"] = True
    save_api_cache_testing_config()

def disable_test_isolation():
    """Deshabilita aislamiento de tests"""
    api_cache_testing_config["test_isolation"] = False
    save_api_cache_testing_config()

def is_verbose_output_enabled():
    """Verifica si salida verbose está habilitada"""
    return api_cache_testing_config.get("verbose_output", True)

def enable_verbose_output():
    """Habilita salida verbose"""
    api_cache_testing_config["verbose_output"] = True
    save_api_cache_testing_config()

def disable_verbose_output():
    """Deshabilita salida verbose"""
    api_cache_testing_config["verbose_output"] = False
    save_api_cache_testing_config()

def export_api_cache_testing_config(filename):
    """Exporta configuración de testing de caché de API"""
    with open(filename, 'w') as f:
        json.dump(api_cache_testing_config, f, indent=4)

def import_api_cache_testing_config(filename):
    """Importa configuración de testing de caché de API"""
    global api_cache_testing_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            api_cache_testing_config = json.load(f)
        save_api_cache_testing_config()
        return True
    return False

def validate_api_cache_testing_config():
    """Valida configuración de testing de caché de API"""
    errors = []
    
    for key in ["enabled", "mock_cache", "test_isolation", "verbose_output"]:
        if key in api_cache_testing_config:
            if not isinstance(api_cache_testing_config[key], bool):
                errors.append(key + " must be boolean")
    
    return errors

def backup_api_cache_testing_config():
    """Crea backup de configuración de testing de caché de API"""
    backup_name = "api_cache_testing_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_api_cache_testing_config(backup_name)
    return backup_name

def restore_api_cache_testing_config(backup_name):
    """Restaura configuración de testing de caché de API desde backup"""
    return import_api_cache_testing_config(backup_name)

def get_api_cache_testing_config_summary():
    """Obtiene resumen de configuración de testing de caché de API"""
    return {
        "enabled": is_cache_testing_enabled(),
        "mock_cache": is_mock_cache_enabled(),
        "test_isolation": is_test_isolation_enabled()
    }

# Cargar configuración de testing de caché de API al importar
load_api_cache_testing_config()
