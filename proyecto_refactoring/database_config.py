import os
import json
import time
from datetime import datetime

# Variables globales
DATABASE_CONFIG_FILE = "database_config.json"
database_config = {}

def load_database_config():
    """Carga configuración de base de datos"""
    global database_config
    
    if os.path.exists(DATABASE_CONFIG_FILE):
        with open(DATABASE_CONFIG_FILE, 'r') as f:
            database_config = json.load(f)
    else:
        database_config = {
            "type": "json",
            "path": "data",
            "backup_enabled": True,
            "max_backups": 10
        }

def save_database_config():
    """Guarda configuración de base de datos"""
    with open(DATABASE_CONFIG_FILE, 'w') as f:
        json.dump(database_config, f, indent=4)

def get_database_setting(key):
    """Obtiene configuración de base de datos"""
    return database_config.get(key)

def set_database_setting(key, value):
    """Establece configuración de base de datos"""
    database_config[key] = value
    save_database_config()

def get_all_database_settings():
    """Obtiene todas las configuraciones de base de datos"""
    return database_config.copy()

def reset_database_config():
    """Resetea configuración de base de datos"""
    global database_config
    database_config = {
        "type": "json",
        "path": "data",
        "backup_enabled": True,
        "max_backups": 10
    }
    save_database_config()

def get_database_type():
    """Obtiene tipo de base de datos"""
    return database_config.get("type", "json")

def set_database_type(db_type):
    """Establece tipo de base de datos"""
    database_config["type"] = db_type
    save_database_config()

def get_database_path():
    """Obtiene ruta de base de datos"""
    return database_config.get("path", "data")

def set_database_path(path):
    """Establece ruta de base de datos"""
    database_config["path"] = path
    save_database_config()

def is_backup_enabled():
    """Verifica si backup está habilitado"""
    return database_config.get("backup_enabled", True)

def enable_backup():
    """Habilita backup"""
    database_config["backup_enabled"] = True
    save_database_config()

def disable_backup():
    """Deshabilita backup"""
    database_config["backup_enabled"] = False
    save_database_config()

def get_max_backups():
    """Obtiene máximo de backups"""
    return database_config.get("max_backups", 10)

def set_max_backups(max_backups):
    """Establece máximo de backups"""
    database_config["max_backups"] = max_backups
    save_database_config()

def export_database_config(filename):
    """Exporta configuración de base de datos"""
    with open(filename, 'w') as f:
        json.dump(database_config, f, indent=4)

def import_database_config(filename):
    """Importa configuración de base de datos"""
    global database_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            database_config = json.load(f)
        save_database_config()
        return True
    return False

def validate_database_config():
    """Valida configuración de base de datos"""
    errors = []
    
    if "type" in database_config:
        if database_config["type"] not in ["json", "csv", "sqlite"]:
            errors.append("Invalid database type")
    
    if "path" in database_config:
        if not database_config["path"]:
            errors.append("Database path cannot be empty")
    
    return errors

def backup_database_config():
    """Crea backup de configuración de base de datos"""
    backup_name = "database_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_database_config(backup_name)
    return backup_name

def restore_database_config(backup_name):
    """Restaura configuración de base de datos desde backup"""
    return import_database_config(backup_name)

def get_database_config_summary():
    """Obtiene resumen de configuración de base de datos"""
    return {
        "type": get_database_type(),
        "path": get_database_path(),
        "backup_enabled": is_backup_enabled()
    }

# Cargar configuración de base de datos al importar
load_database_config()
