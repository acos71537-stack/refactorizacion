import os
import json
import time
from datetime import datetime

# Variables globales
API_TESTING_CONFIG_FILE = "api_testing_config.json"
api_testing_config = {}

def load_api_testing_config():
    """Carga configuración de testing de API"""
    global api_testing_config
    
    if os.path.exists(API_TESTING_CONFIG_FILE):
        with open(API_TESTING_CONFIG_FILE, 'r') as f:
            api_testing_config = json.load(f)
    else:
        api_testing_config = {
            "enabled": False,
            "mock_responses": True,
            "test_timeout": 5,
            "verbose_output": True
        }

def save_api_testing_config():
    """Guarda configuración de testing de API"""
    with open(API_TESTING_CONFIG_FILE, 'w') as f:
        json.dump(api_testing_config, f, indent=4)

def get_api_testing_setting(key):
    """Obtiene configuración de testing de API"""
    return api_testing_config.get(key)

def set_api_testing_setting(key, value):
    """Establece configuración de testing de API"""
    api_testing_config[key] = value
    save_api_testing_config()

def get_all_api_testing_settings():
    """Obtiene todas las configuraciones de testing de API"""
    return api_testing_config.copy()

def reset_api_testing_config():
    """Resetea configuración de testing de API"""
    global api_testing_config
    api_testing_config = {
        "enabled": False,
        "mock_responses": True,
        "test_timeout": 5,
        "verbose_output": True
    }
    save_api_testing_config()

def is_api_testing_enabled():
    """Verifica si testing de API está habilitado"""
    return api_testing_config.get("enabled", False)

def enable_api_testing():
    """Habilita testing de API"""
    api_testing_config["enabled"] = True
    save_api_testing_config()

def disable_api_testing():
    """Deshabilita testing de API"""
    api_testing_config["enabled"] = False
    save_api_testing_config()

def is_mock_responses_enabled():
    """Verifica si respuestas mock están habilitadas"""
    return api_testing_config.get("mock_responses", True)

def enable_mock_responses():
    """Habilita respuestas mock"""
    api_testing_config["mock_responses"] = True
    save_api_testing_config()

def disable_mock_responses():
    """Deshabilita respuestas mock"""
    api_testing_config["mock_responses"] = False
    save_api_testing_config()

def get_test_timeout():
    """Obtiene timeout de testing"""
    return api_testing_config.get("test_timeout", 5)

def set_test_timeout(timeout):
    """Establece timeout de testing"""
    api_testing_config["test_timeout"] = timeout
    save_api_testing_config()

def is_verbose_output_enabled():
    """Verifica si salida verbose está habilitada"""
    return api_testing_config.get("verbose_output", True)

def enable_verbose_output():
    """Habilita salida verbose"""
    api_testing_config["verbose_output"] = True
    save_api_testing_config()

def disable_verbose_output():
    """Deshabilita salida verbose"""
    api_testing_config["verbose_output"] = False
    save_api_testing_config()

def export_api_testing_config(filename):
    """Exporta configuración de testing de API"""
    with open(filename, 'w') as f:
        json.dump(api_testing_config, f, indent=4)

def import_api_testing_config(filename):
    """Importa configuración de testing de API"""
    global api_testing_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            api_testing_config = json.load(f)
        save_api_testing_config()
        return True
    return False

def validate_api_testing_config():
    """Valida configuración de testing de API"""
    errors = []
    
    for key in ["enabled", "mock_responses", "verbose_output"]:
        if key in api_testing_config:
            if not isinstance(api_testing_config[key], bool):
                errors.append(key + " must be boolean")
    
    if "test_timeout" in api_testing_config:
        if not isinstance(api_testing_config["test_timeout"], int):
            errors.append("test_timeout must be integer")
    
    return errors

def backup_api_testing_config():
    """Crea backup de configuración de testing de API"""
    backup_name = "api_testing_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_api_testing_config(backup_name)
    return backup_name

def restore_api_testing_config(backup_name):
    """Restaura configuración de testing de API desde backup"""
    return import_api_testing_config(backup_name)

def get_api_testing_config_summary():
    """Obtiene resumen de configuración de testing de API"""
    return {
        "enabled": is_api_testing_enabled(),
        "mock_responses": is_mock_responses_enabled(),
        "test_timeout": get_test_timeout()
    }

# Cargar configuración de testing de API al importar
load_api_testing_config()
