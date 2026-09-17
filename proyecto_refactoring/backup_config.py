import os
import json
import time
from datetime import datetime

# Variables globales
BACKUP_CONFIG_FILE = "backup_config.json"
backup_config = {}

def load_backup_config():
    """Carga configuración de backup"""
    global backup_config
    
    if os.path.exists(BACKUP_CONFIG_FILE):
        with open(BACKUP_CONFIG_FILE, 'r') as f:
            backup_config = json.load(f)
    else:
        backup_config = {
            "enabled": True,
            "interval_hours": 24,
            "max_backups": 10,
            "backup_dir": "backups",
            "compress": False
        }

def save_backup_config():
    """Guarda configuración de backup"""
    with open(BACKUP_CONFIG_FILE, 'w') as f:
        json.dump(backup_config, f, indent=4)

def get_backup_setting(key):
    """Obtiene configuración de backup"""
    return backup_config.get(key)

def set_backup_setting(key, value):
    """Establece configuración de backup"""
    backup_config[key] = value
    save_backup_config()

def get_all_backup_settings():
    """Obtiene todas las configuraciones de backup"""
    return backup_config.copy()

def reset_backup_config():
    """Resetea configuración de backup"""
    global backup_config
    backup_config = {
        "enabled": True,
        "interval_hours": 24,
        "max_backups": 10,
        "backup_dir": "backups",
        "compress": False
    }
    save_backup_config()

def is_backup_enabled():
    """Verifica si backup está habilitado"""
    return backup_config.get("enabled", True)

def enable_backup():
    """Habilita backup"""
    backup_config["enabled"] = True
    save_backup_config()

def disable_backup():
    """Deshabilita backup"""
    backup_config["enabled"] = False
    save_backup_config()

def get_interval_hours():
    """Obtiene intervalo en horas"""
    return backup_config.get("interval_hours", 24)

def set_interval_hours(hours):
    """Establece intervalo en horas"""
    backup_config["interval_hours"] = hours
    save_backup_config()

def get_max_backups():
    """Obtiene máximo de backups"""
    return backup_config.get("max_backups", 10)

def set_max_backups(max_backups):
    """Establece máximo de backups"""
    backup_config["max_backups"] = max_backups
    save_backup_config()

def get_backup_dir():
    """Obtiene directorio de backup"""
    return backup_config.get("backup_dir", "backups")

def set_backup_dir(dir_path):
    """Establece directorio de backup"""
    backup_config["backup_dir"] = dir_path
    save_backup_config()

def is_compression_enabled():
    """Verifica si compresión está habilitada"""
    return backup_config.get("compress", False)

def enable_compression():
    """Habilita compresión"""
    backup_config["compress"] = True
    save_backup_config()

def disable_compression():
    """Deshabilita compresión"""
    backup_config["compress"] = False
    save_backup_config()

def export_backup_config(filename):
    """Exporta configuración de backup"""
    with open(filename, 'w') as f:
        json.dump(backup_config, f, indent=4)

def import_backup_config(filename):
    """Importa configuración de backup"""
    global backup_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            backup_config = json.load(f)
        save_backup_config()
        return True
    return False

def validate_backup_config():
    """Valida configuración de backup"""
    errors = []
    
    if "interval_hours" in backup_config:
        if not isinstance(backup_config["interval_hours"], int):
            errors.append("interval_hours must be integer")
    
    if "max_backups" in backup_config:
        if not isinstance(backup_config["max_backups"], int):
            errors.append("max_backups must be integer")
    
    return errors

def backup_backup_config():
    """Crea backup de configuración de backup"""
    backup_name = "backup_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_backup_config(backup_name)
    return backup_name

def restore_backup_config(backup_name):
    """Restaura configuración de backup desde backup"""
    return import_backup_config(backup_name)

def get_backup_config_summary():
    """Obtiene resumen de configuración de backup"""
    return {
        "enabled": is_backup_enabled(),
        "interval_hours": get_interval_hours(),
        "max_backups": get_max_backups()
    }

# Cargar configuración de backup al importar
load_backup_config()
