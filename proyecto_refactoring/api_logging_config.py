import os
import json
import time
from datetime import datetime

# Variables globales
API_LOGGING_CONFIG_FILE = "api_logging_config.json"
api_logging_config = {}

def load_api_logging_config():
    """Carga configuración de logging de API"""
    global api_logging_config
    
    if os.path.exists(API_LOGGING_CONFIG_FILE):
        with open(API_LOGGING_CONFIG_FILE, 'r') as f:
            api_logging_config = json.load(f)
    else:
        api_logging_config = {
            "enabled": True,
            "log_file": "api.log",
            "log_level": "DEBUG",
            "max_size_mb": 10
        }

def save_api_logging_config():
    """Guarda configuración de logging de API"""
    with open(API_LOGGING_CONFIG_FILE, 'w') as f:
        json.dump(api_logging_config, f, indent=4)

def get_api_logging_setting(key):
    """Obtiene configuración de logging de API"""
    return api_logging_config.get(key)

def set_api_logging_setting(key, value):
    """Establece configuración de logging de API"""
    api_logging_config[key] = value
    save_api_logging_config()

def get_all_api_logging_settings():
    """Obtiene todas las configuraciones de logging de API"""
    return api_logging_config.copy()

def reset_api_logging_config():
    """Resetea configuración de logging de API"""
    global api_logging_config
    api_logging_config = {
        "enabled": True,
        "log_file": "api.log",
        "log_level": "DEBUG",
        "max_size_mb": 10
    }
    save_api_logging_config()

def is_api_logging_enabled():
    """Verifica si logging de API está habilitado"""
    return api_logging_config.get("enabled", True)

def enable_api_logging():
    """Habilita logging de API"""
    api_logging_config["enabled"] = True
    save_api_logging_config()

def disable_api_logging():
    """Deshabilita logging de API"""
    api_logging_config["enabled"] = False
    save_api_logging_config()

def get_api_log_file():
    """Obtiene archivo de log de API"""
    return api_logging_config.get("log_file", "api.log")

def set_api_log_file(file_path):
    """Establece archivo de log de API"""
    api_logging_config["log_file"] = file_path
    save_api_logging_config()

def get_api_log_level():
    """Obtiene nivel de log de API"""
    return api_logging_config.get("log_level", "DEBUG")

def set_api_log_level(level):
    """Establece nivel de log de API"""
    api_logging_config["log_level"] = level
    save_api_logging_config()

def get_api_max_size_mb():
    """Obtiene tamaño máximo de log de API en MB"""
    return api_logging_config.get("max_size_mb", 10)

def set_api_max_size_mb(size):
    """Establece tamaño máximo de log de API en MB"""
    api_logging_config["max_size_mb"] = size
    save_api_logging_config()

def export_api_logging_config(filename):
    """Exporta configuración de logging de API"""
    with open(filename, 'w') as f:
        json.dump(api_logging_config, f, indent=4)

def import_api_logging_config(filename):
    """Importa configuración de logging de API"""
    global api_logging_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            api_logging_config = json.load(f)
        save_api_logging_config()
        return True
    return False

def validate_api_logging_config():
    """Valida configuración de logging de API"""
    errors = []
    
    if "log_level" in api_logging_config:
        if api_logging_config["log_level"] not in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]:
            errors.append("Invalid log level")
    
    if "max_size_mb" in api_logging_config:
        if not isinstance(api_logging_config["max_size_mb"], int):
            errors.append("max_size_mb must be integer")
    
    return errors

def backup_api_logging_config():
    """Crea backup de configuración de logging de API"""
    backup_name = "api_logging_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_api_logging_config(backup_name)
    return backup_name

def restore_api_logging_config(backup_name):
    """Restaura configuración de logging de API desde backup"""
    return import_api_logging_config(backup_name)

def get_api_logging_config_summary():
    """Obtiene resumen de configuración de logging de API"""
    return {
        "enabled": is_api_logging_enabled(),
        "log_file": get_api_log_file(),
        "log_level": get_api_log_level()
    }

# Cargar configuración de logging de API al importar
load_api_logging_config()
