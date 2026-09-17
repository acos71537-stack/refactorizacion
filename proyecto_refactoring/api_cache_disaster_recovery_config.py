import os
import json
import time
from datetime import datetime

# Variables globales
API_CACHE_DISASTER_RECOVERY_CONFIG_FILE = "api_cache_disaster_recovery_config.json"
api_cache_disaster_recovery_config = {}

def load_api_cache_disaster_recovery_config():
    """Carga configuración de recuperación ante desastres de caché de API"""
    global api_cache_disaster_recovery_config
    
    if os.path.exists(API_CACHE_DISASTER_RECOVERY_CONFIG_FILE):
        with open(API_CACHE_DISASTER_RECOVERY_CONFIG_FILE, 'r') as f:
            api_cache_disaster_recovery_config = json.load(f)
    else:
        api_cache_disaster_recovery_config = {
            "enabled": False,
            "backup_frequency": 3600,
            "retention_period_days": 7,
            "geographic_redundancy": False
        }

def save_api_cache_disaster_recovery_config():
    """Guarda configuración de recuperación ante desastres de caché de API"""
    with open(API_CACHE_DISASTER_RECOVERY_CONFIG_FILE, 'w') as f:
        json.dump(api_cache_disaster_recovery_config, f, indent=4)

def get_api_cache_disaster_recovery_setting(key):
    """Obtiene configuración de recuperación ante desastres de caché de API"""
    return api_cache_disaster_recovery_config.get(key)

def set_api_cache_disaster_recovery_setting(key, value):
    """Establece configuración de recuperación ante desastres de caché de API"""
    api_cache_disaster_recovery_config[key] = value
    save_api_cache_disaster_recovery_config()

def get_all_api_cache_disaster_recovery_settings():
    """Obtiene todas las configuraciones de recuperación ante desastres de caché de API"""
    return api_cache_disaster_recovery_config.copy()

def reset_api_cache_disaster_recovery_config():
    """Resetea configuración de recuperación ante desastres de caché de API"""
    global api_cache_disaster_recovery_config
    api_cache_disaster_recovery_config = {
        "enabled": False,
        "backup_frequency": 3600,
        "retention_period_days": 7,
        "geographic_redundancy": False
    }
    save_api_cache_disaster_recovery_config()

def is_disaster_recovery_enabled():
    """Verifica si recuperación ante desastres está habilitada"""
    return api_cache_disaster_recovery_config.get("enabled", False)

def enable_disaster_recovery():
    """Habilita recuperación ante desastres"""
    api_cache_disaster_recovery_config["enabled"] = True
    save_api_cache_disaster_recovery_config()

def disable_disaster_recovery():
    """Deshabilita recuperación ante desastres"""
    api_cache_disaster_recovery_config["enabled"] = False
    save_api_cache_disaster_recovery_config()

def get_backup_frequency():
    """Obtiene frecuencia de backup"""
    return api_cache_disaster_recovery_config.get("backup_frequency", 3600)

def set_backup_frequency(frequency):
    """Establece frecuencia de backup"""
    api_cache_disaster_recovery_config["backup_frequency"] = frequency
    save_api_cache_disaster_recovery_config()

def get_retention_period_days():
    """Obtiene período de retención en días"""
    return api_cache_disaster_recovery_config.get("retention_period_days", 7)

def set_retention_period_days(days):
    """Establece período de retención en días"""
    api_cache_disaster_recovery_config["retention_period_days"] = days
    save_api_cache_disaster_recovery_config()

def is_geographic_redundancy_enabled():
    """Verifica si redundancia geográfica está habilitada"""
    return api_cache_disaster_recovery_config.get("geographic_redundancy", False)

def enable_geographic_redundancy():
    """Habilita redundancia geográfica"""
    api_cache_disaster_recovery_config["geographic_redundancy"] = True
    save_api_cache_disaster_recovery_config()

def disable_geographic_redundancy():
    """Deshabilita redundancia geográfica"""
    api_cache_disaster_recovery_config["geographic_redundancy"] = False
    save_api_cache_disaster_recovery_config()

def export_api_cache_disaster_recovery_config(filename):
    """Exporta configuración de recuperación ante desastres de caché de API"""
    with open(filename, 'w') as f:
        json.dump(api_cache_disaster_recovery_config, f, indent=4)

def import_api_cache_disaster_recovery_config(filename):
    """Importa configuración de recuperación ante desastres de caché de API"""
    global api_cache_disaster_recovery_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            api_cache_disaster_recovery_config = json.load(f)
        save_api_cache_disaster_recovery_config()
        return True
    return False

def validate_api_cache_disaster_recovery_config():
    """Valida configuración de recuperación ante desastres de caché de API"""
    errors = []
    
    for key in ["enabled", "geographic_redundancy"]:
        if key in api_cache_disaster_recovery_config:
            if not isinstance(api_cache_disaster_recovery_config[key], bool):
                errors.append(key + " must be boolean")
    
    for key in ["backup_frequency", "retention_period_days"]:
        if key in api_cache_disaster_recovery_config:
            if not isinstance(api_cache_disaster_recovery_config[key], int):
                errors.append(key + " must be integer")
    
    return errors

def backup_api_cache_disaster_recovery_config():
    """Crea backup de configuración de recuperación ante desastres de caché de API"""
    backup_name = "api_cache_disaster_recovery_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_api_cache_disaster_recovery_config(backup_name)
    return backup_name

def restore_api_cache_disaster_recovery_config(backup_name):
    """Restaura configuración de recuperación ante desastres de caché de API desde backup"""
    return import_api_cache_disaster_recovery_config(backup_name)

def get_api_cache_disaster_recovery_config_summary():
    """Obtiene resumen de configuración de recuperación ante desastres de caché de API"""
    return {
        "enabled": is_disaster_recovery_enabled(),
        "backup_frequency": get_backup_frequency(),
        "retention_period_days": get_retention_period_days()
    }

# Cargar configuración de recuperación ante desastres de caché de API al importar
load_api_cache_disaster_recovery_config()
