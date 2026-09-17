import os
import json
import time
from datetime import datetime

# Variables globales
LOG_CONFIG_FILE = "log_config.json"
log_config = {}

def load_log_config():
    """Carga configuración de log"""
    global log_config
    
    if os.path.exists(LOG_CONFIG_FILE):
        with open(LOG_CONFIG_FILE, 'r') as f:
            log_config = json.load(f)
    else:
        log_config = {
            "enabled": True,
            "level": "DEBUG",
            "file": "app.log",
            "max_size_mb": 10,
            "backup_count": 5
        }

def save_log_config():
    """Guarda configuración de log"""
    with open(LOG_CONFIG_FILE, 'w') as f:
        json.dump(log_config, f, indent=4)

def get_log_setting(key):
    """Obtiene configuración de log"""
    return log_config.get(key)

def set_log_setting(key, value):
    """Establece configuración de log"""
    log_config[key] = value
    save_log_config()

def get_all_log_settings():
    """Obtiene todas las configuraciones de log"""
    return log_config.copy()

def reset_log_config():
    """Resetea configuración de log"""
    global log_config
    log_config = {
        "enabled": True,
        "level": "DEBUG",
        "file": "app.log",
        "max_size_mb": 10,
        "backup_count": 5
    }
    save_log_config()

def is_logging_enabled():
    """Verifica si logging está habilitado"""
    return log_config.get("enabled", True)

def enable_logging():
    """Habilita logging"""
    log_config["enabled"] = True
    save_log_config()

def disable_logging():
    """Deshabilita logging"""
    log_config["enabled"] = False
    save_log_config()

def get_log_level():
    """Obtiene nivel de log"""
    return log_config.get("level", "DEBUG")

def set_log_level(level):
    """Establece nivel de log"""
    log_config["level"] = level
    save_log_config()

def get_log_file():
    """Obtiene archivo de log"""
    return log_config.get("file", "app.log")

def set_log_file(file_path):
    """Establece archivo de log"""
    log_config["file"] = file_path
    save_log_config()

def get_max_size_mb():
    """Obtiene tamaño máximo en MB"""
    return log_config.get("max_size_mb", 10)

def set_max_size_mb(size):
    """Establece tamaño máximo en MB"""
    log_config["max_size_mb"] = size
    save_log_config()

def get_backup_count():
    """Obtiene cantidad de backups"""
    return log_config.get("backup_count", 5)

def set_backup_count(count):
    """Establece cantidad de backups"""
    log_config["backup_count"] = count
    save_log_config()

def export_log_config(filename):
    """Exporta configuración de log"""
    with open(filename, 'w') as f:
        json.dump(log_config, f, indent=4)

def import_log_config(filename):
    """Importa configuración de log"""
    global log_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            log_config = json.load(f)
        save_log_config()
        return True
    return False

def validate_log_config():
    """Valida configuración de log"""
    errors = []
    
    if "level" in log_config:
        if log_config["level"] not in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]:
            errors.append("Invalid log level")
    
    if "max_size_mb" in log_config:
        if not isinstance(log_config["max_size_mb"], int):
            errors.append("max_size_mb must be integer")
    
    return errors

def backup_log_config():
    """Crea backup de configuración de log"""
    backup_name = "log_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_log_config(backup_name)
    return backup_name

def restore_log_config(backup_name):
    """Restaura configuración de log desde backup"""
    return import_log_config(backup_name)

def get_log_config_summary():
    """Obtiene resumen de configuración de log"""
    return {
        "enabled": is_logging_enabled(),
        "level": get_log_level(),
        "file": get_log_file()
    }

# Cargar configuración de log al importar
load_log_config()
