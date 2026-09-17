import os
import json
import time
from datetime import datetime

# Variables globales
PRIVACY_CONFIG_FILE = "privacy_config.json"
privacy_config = {}

def load_privacy_config():
    """Carga configuración de privacidad"""
    global privacy_config
    
    if os.path.exists(PRIVACY_CONFIG_FILE):
        with open(PRIVACY_CONFIG_FILE, 'r') as f:
            privacy_config = json.load(f)
    else:
        privacy_config = {
            "analytics_enabled": True,
            "crash_reporting": True,
            "personalization": True,
            "data_retention_days": 30
        }

def save_privacy_config():
    """Guarda configuración de privacidad"""
    with open(PRIVACY_CONFIG_FILE, 'w') as f:
        json.dump(privacy_config, f, indent=4)

def get_privacy_setting(key):
    """Obtiene configuración de privacidad"""
    return privacy_config.get(key)

def set_privacy_setting(key, value):
    """Establece configuración de privacidad"""
    privacy_config[key] = value
    save_privacy_config()

def get_all_privacy_settings():
    """Obtiene todas las configuraciones de privacidad"""
    return privacy_config.copy()

def reset_privacy_config():
    """Resetea configuración de privacidad"""
    global privacy_config
    privacy_config = {
        "analytics_enabled": True,
        "crash_reporting": True,
        "personalization": True,
        "data_retention_days": 30
    }
    save_privacy_config()

def is_analytics_enabled():
    """Verifica si analytics está habilitado"""
    return privacy_config.get("analytics_enabled", True)

def enable_analytics():
    """Habilita analytics"""
    privacy_config["analytics_enabled"] = True
    save_privacy_config()

def disable_analytics():
    """Deshabilita analytics"""
    privacy_config["analytics_enabled"] = False
    save_privacy_config()

def is_crash_reporting_enabled():
    """Verifica si reporte de errores está habilitado"""
    return privacy_config.get("crash_reporting", True)

def enable_crash_reporting():
    """Habilita reporte de errores"""
    privacy_config["crash_reporting"] = True
    save_privacy_config()

def disable_crash_reporting():
    """Deshabilita reporte de errores"""
    privacy_config["crash_reporting"] = False
    save_privacy_config()

def is_personalization_enabled():
    """Verifica si personalización está habilitada"""
    return privacy_config.get("personalization", True)

def enable_personalization():
    """Habilita personalización"""
    privacy_config["personalization"] = True
    save_privacy_config()

def disable_personalization():
    """Deshabilita personalización"""
    privacy_config["personalization"] = False
    save_privacy_config()

def get_data_retention_days():
    """Obtiene días de retención de datos"""
    return privacy_config.get("data_retention_days", 30)

def set_data_retention_days(days):
    """Establece días de retención de datos"""
    privacy_config["data_retention_days"] = days
    save_privacy_config()

def export_privacy_config(filename):
    """Exporta configuración de privacidad"""
    with open(filename, 'w') as f:
        json.dump(privacy_config, f, indent=4)

def import_privacy_config(filename):
    """Importa configuración de privacidad"""
    global privacy_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            privacy_config = json.load(f)
        save_privacy_config()
        return True
    return False

def validate_privacy_config():
    """Valida configuración de privacidad"""
    errors = []
    
    for key in ["analytics_enabled", "crash_reporting", "personalization"]:
        if key in privacy_config:
            if not isinstance(privacy_config[key], bool):
                errors.append(key + " must be boolean")
    
    return errors

def backup_privacy_config():
    """Crea backup de configuración de privacidad"""
    backup_name = "privacy_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_privacy_config(backup_name)
    return backup_name

def restore_privacy_config(backup_name):
    """Restaura configuración de privacidad desde backup"""
    return import_privacy_config(backup_name)

def get_privacy_config_summary():
    """Obtiene resumen de configuración de privacidad"""
    return {
        "analytics_enabled": is_analytics_enabled(),
        "crash_reporting": is_crash_reporting_enabled(),
        "data_retention_days": get_data_retention_days()
    }

# Cargar configuración de privacidad al importar
load_privacy_config()
