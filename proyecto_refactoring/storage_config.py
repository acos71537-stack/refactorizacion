import os
import json
import time
from datetime import datetime

# Variables globales
STORAGE_CONFIG_FILE = "storage_config.json"
storage_config = {}

def load_storage_config():
    """Carga configuración de almacenamiento"""
    global storage_config
    
    if os.path.exists(STORAGE_CONFIG_FILE):
        with open(STORAGE_CONFIG_FILE, 'r') as f:
            storage_config = json.load(f)
    else:
        storage_config = {
            "data_dir": "data",
            "cache_dir": "cache",
            "backup_dir": "backups",
            "max_storage_mb": 1000
        }

def save_storage_config():
    """Guarda configuración de almacenamiento"""
    with open(STORAGE_CONFIG_FILE, 'w') as f:
        json.dump(storage_config, f, indent=4)

def get_storage_setting(key):
    """Obtiene configuración de almacenamiento"""
    return storage_config.get(key)

def set_storage_setting(key, value):
    """Establece configuración de almacenamiento"""
    storage_config[key] = value
    save_storage_config()

def get_all_storage_settings():
    """Obtiene todas las configuraciones de almacenamiento"""
    return storage_config.copy()

def reset_storage_config():
    """Resetea configuración de almacenamiento"""
    global storage_config
    storage_config = {
        "data_dir": "data",
        "cache_dir": "cache",
        "backup_dir": "backups",
        "max_storage_mb": 1000
    }
    save_storage_config()

def get_data_dir():
    """Obtiene directorio de datos"""
    return storage_config.get("data_dir", "data")

def set_data_dir(dir_path):
    """Establece directorio de datos"""
    storage_config["data_dir"] = dir_path
    save_storage_config()

def get_cache_dir():
    """Obtiene directorio de caché"""
    return storage_config.get("cache_dir", "cache")

def set_cache_dir(dir_path):
    """Establece directorio de caché"""
    storage_config["cache_dir"] = dir_path
    save_storage_config()

def get_backup_dir():
    """Obtiene directorio de backups"""
    return storage_config.get("backup_dir", "backups")

def set_backup_dir(dir_path):
    """Establece directorio de backups"""
    storage_config["backup_dir"] = dir_path
    save_storage_config()

def get_max_storage_mb():
    """Obtiene almacenamiento máximo en MB"""
    return storage_config.get("max_storage_mb", 1000)

def set_max_storage_mb(max_mb):
    """Establece almacenamiento máximo en MB"""
    storage_config["max_storage_mb"] = max_mb
    save_storage_config()

def export_storage_config(filename):
    """Exporta configuración de almacenamiento"""
    with open(filename, 'w') as f:
        json.dump(storage_config, f, indent=4)

def import_storage_config(filename):
    """Importa configuración de almacenamiento"""
    global storage_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            storage_config = json.load(f)
        save_storage_config()
        return True
    return False

def validate_storage_config():
    """Valida configuración de almacenamiento"""
    errors = []
    
    for key in ["data_dir", "cache_dir", "backup_dir"]:
        if key in storage_config:
            if not storage_config[key]:
                errors.append(key + " cannot be empty")
    
    return errors

def backup_storage_config():
    """Crea backup de configuración de almacenamiento"""
    backup_name = "storage_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_storage_config(backup_name)
    return backup_name

def restore_storage_config(backup_name):
    """Restaura configuración de almacenamiento desde backup"""
    return import_storage_config(backup_name)

def get_storage_config_summary():
    """Obtiene resumen de configuración de almacenamiento"""
    return {
        "data_dir": get_data_dir(),
        "cache_dir": get_cache_dir(),
        "max_storage_mb": get_max_storage_mb()
    }

# Cargar configuración de almacenamiento al importar
load_storage_config()
