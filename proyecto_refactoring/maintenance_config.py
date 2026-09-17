import os
import json
import time
from datetime import datetime

# Variables globales
MAINTENANCE_CONFIG_FILE = "maintenance_config.json"
maintenance_config = {}

def load_maintenance_config():
    """Carga configuración de mantenimiento"""
    global maintenance_config
    
    if os.path.exists(MAINTENANCE_CONFIG_FILE):
        with open(MAINTENANCE_CONFIG_FILE, 'r') as f:
            maintenance_config = json.load(f)
    else:
        maintenance_config = {
            "enabled": False,
            "message": "Sistema en mantenimiento",
            "estimated_time": "1 hora",
            "contact": "admin@example.com"
        }

def save_maintenance_config():
    """Guarda configuración de mantenimiento"""
    with open(MAINTENANCE_CONFIG_FILE, 'w') as f:
        json.dump(maintenance_config, f, indent=4)

def get_maintenance_setting(key):
    """Obtiene configuración de mantenimiento"""
    return maintenance_config.get(key)

def set_maintenance_setting(key, value):
    """Establece configuración de mantenimiento"""
    maintenance_config[key] = value
    save_maintenance_config()

def get_all_maintenance_settings():
    """Obtiene todas las configuraciones de mantenimiento"""
    return maintenance_config.copy()

def reset_maintenance_config():
    """Resetea configuración de mantenimiento"""
    global maintenance_config
    maintenance_config = {
        "enabled": False,
        "message": "Sistema en mantenimiento",
        "estimated_time": "1 hora",
        "contact": "admin@example.com"
    }
    save_maintenance_config()

def is_maintenance_enabled():
    """Verifica si mantenimiento está habilitado"""
    return maintenance_config.get("enabled", False)

def enable_maintenance():
    """Habilita mantenimiento"""
    maintenance_config["enabled"] = True
    save_maintenance_config()

def disable_maintenance():
    """Deshabilita mantenimiento"""
    maintenance_config["enabled"] = False
    save_maintenance_config()

def get_maintenance_message():
    """Obtiene mensaje de mantenimiento"""
    return maintenance_config.get("message", "Sistema en mantenimiento")

def set_maintenance_message(message):
    """Establece mensaje de mantenimiento"""
    maintenance_config["message"] = message
    save_maintenance_config()

def get_estimated_time():
    """Obtiene tiempo estimado"""
    return maintenance_config.get("estimated_time", "1 hora")

def set_estimated_time(time_str):
    """Establece tiempo estimado"""
    maintenance_config["estimated_time"] = time_str
    save_maintenance_config()

def get_contact():
    """Obtiene contacto"""
    return maintenance_config.get("contact", "admin@example.com")

def set_contact(contact):
    """Establece contacto"""
    maintenance_config["contact"] = contact
    save_maintenance_config()

def export_maintenance_config(filename):
    """Exporta configuración de mantenimiento"""
    with open(filename, 'w') as f:
        json.dump(maintenance_config, f, indent=4)

def import_maintenance_config(filename):
    """Importa configuración de mantenimiento"""
    global maintenance_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            maintenance_config = json.load(f)
        save_maintenance_config()
        return True
    return False

def validate_maintenance_config():
    """Valida configuración de mantenimiento"""
    errors = []
    
    if "enabled" in maintenance_config:
        if not isinstance(maintenance_config["enabled"], bool):
            errors.append("enabled must be boolean")
    
    return errors

def backup_maintenance_config():
    """Crea backup de configuración de mantenimiento"""
    backup_name = "maintenance_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_maintenance_config(backup_name)
    return backup_name

def restore_maintenance_config(backup_name):
    """Restaura configuración de mantenimiento desde backup"""
    return import_maintenance_config(backup_name)

def get_maintenance_config_summary():
    """Obtiene resumen de configuración de mantenimiento"""
    return {
        "enabled": is_maintenance_enabled(),
        "message": get_maintenance_message(),
        "estimated_time": get_estimated_time()
    }

# Cargar configuración de mantenimiento al importar
load_maintenance_config()
