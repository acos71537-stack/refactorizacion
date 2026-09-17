import os
import json
import time
from datetime import datetime

# Variables globales
API_CACHE_DEPRECATION_SCHEDULE_CONFIG_FILE = "api_cache_deprecation_schedule_config.json"
api_cache_deprecation_schedule_config = {}

def load_api_cache_deprecation_schedule_config():
    """Carga configuración de horario de deprecación de caché de API"""
    global api_cache_deprecation_schedule_config
    
    if os.path.exists(API_CACHE_DEPRECATION_SCHEDULE_CONFIG_FILE):
        with open(API_CACHE_DEPRECATION_SCHEDULE_CONFIG_FILE, 'r') as f:
            api_cache_deprecation_schedule_config = json.load(f)
    else:
        api_cache_deprecation_schedule_config = {
            "auto_deprecate": True,
            "deprecation_announcement_days": 30,
            "grace_period_days": 90,
            "auto_remove_after_grace": True
        }

def save_api_cache_deprecation_schedule_config():
    """Guarda configuración de horario de deprecación de caché de API"""
    with open(API_CACHE_DEPRECATION_SCHEDULE_CONFIG_FILE, 'w') as f:
        json.dump(api_cache_deprecation_schedule_config, f, indent=4)

def get_api_cache_deprecation_schedule_setting(key):
    """Obtiene configuración de horario de deprecación de caché de API"""
    return api_cache_deprecation_schedule_config.get(key)

def set_api_cache_deprecation_schedule_setting(key, value):
    """Establece configuración de horario de deprecación de caché de API"""
    api_cache_deprecation_schedule_config[key] = value
    save_api_cache_deprecation_schedule_config()

def get_all_api_cache_deprecation_schedule_settings():
    """Obtiene todas las configuraciones de horario de deprecación de caché de API"""
    return api_cache_deprecation_schedule_config.copy()

def reset_api_cache_deprecation_schedule_config():
    """Resetea configuración de horario de deprecación de caché de API"""
    global api_cache_deprecation_schedule_config
    api_cache_deprecation_schedule_config = {
        "auto_deprecate": True,
        "deprecation_announcement_days": 30,
        "grace_period_days": 90,
        "auto_remove_after_grace": True
    }
    save_api_cache_deprecation_schedule_config()

def is_auto_deprecate_enabled():
    """Verifica si auto-deprecate está habilitado"""
    return api_cache_deprecation_schedule_config.get("auto_deprecate", True)

def enable_auto_deprecate():
    """Habilita auto-deprecate"""
    api_cache_deprecation_schedule_config["auto_deprecate"] = True
    save_api_cache_deprecation_schedule_config()

def disable_auto_deprecate():
    """Deshabilita auto-deprecate"""
    api_cache_deprecation_schedule_config["auto_deprecate"] = False
    save_api_cache_deprecation_schedule_config()

def get_deprecation_announcement_days():
    """Obtiene días de anuncio de deprecación"""
    return api_cache_deprecation_schedule_config.get("deprecation_announcement_days", 30)

def set_deprecation_announcement_days(days):
    """Establece días de anuncio de deprecación"""
    api_cache_deprecation_schedule_config["deprecation_announcement_days"] = days
    save_api_cache_deprecation_schedule_config()

def get_grace_period_days():
    """Obtiene días de período de gracia"""
    return api_cache_deprecation_schedule_config.get("grace_period_days", 90)

def set_grace_period_days(days):
    """Establece días de período de gracia"""
    api_cache_deprecation_schedule_config["grace_period_days"] = days
    save_api_cache_deprecation_schedule_config()

def is_auto_remove_after_grace_enabled():
    """Verifica si auto-remove después de gracia está habilitado"""
    return api_cache_deprecation_schedule_config.get("auto_remove_after_grace", True)

def enable_auto_remove_after_grace():
    """Habilita auto-remove después de gracia"""
    api_cache_deprecation_schedule_config["auto_remove_after_grace"] = True
    save_api_cache_deprecation_schedule_config()

def disable_auto_remove_after_grace():
    """Deshabilita auto-remove después de gracia"""
    api_cache_deprecation_schedule_config["auto_remove_after_grace"] = False
    save_api_cache_deprecation_schedule_config()

def export_api_cache_deprecation_schedule_config(filename):
    """Exporta configuración de horario de deprecación de caché de API"""
    with open(filename, 'w') as f:
        json.dump(api_cache_deprecation_schedule_config, f, indent=4)

def import_api_cache_deprecation_schedule_config(filename):
    """Importa configuración de horario de deprecación de caché de API"""
    global api_cache_deprecation_schedule_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            api_cache_deprecation_schedule_config = json.load(f)
        save_api_cache_deprecation_schedule_config()
        return True
    return False

def validate_api_cache_deprecation_schedule_config():
    """Valida configuración de horario de deprecación de caché de API"""
    errors = []
    
    for key in ["auto_deprecate", "auto_remove_after_grace"]:
        if key in api_cache_deprecation_schedule_config:
            if not isinstance(api_cache_deprecation_schedule_config[key], bool):
                errors.append(key + " must be boolean")
    
    for key in ["deprecation_announcement_days", "grace_period_days"]:
        if key in api_cache_deprecation_schedule_config:
            if not isinstance(api_cache_deprecation_schedule_config[key], int):
                errors.append(key + " must be integer")
    
    return errors

def backup_api_cache_deprecation_schedule_config():
    """Crea backup de configuración de horario de deprecación de caché de API"""
    backup_name = "api_cache_deprecation_schedule_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_api_cache_deprecation_schedule_config(backup_name)
    return backup_name

def restore_api_cache_deprecation_schedule_config(backup_name):
    """Restaura configuración de horario de deprecación de caché de API desde backup"""
    return import_api_cache_deprecation_schedule_config(backup_name)

def get_api_cache_deprecation_schedule_config_summary():
    """Obtiene resumen de configuración de horario de deprecación de caché de API"""
    return {
        "auto_deprecate": is_auto_deprecate_enabled(),
        "deprecation_announcement_days": get_deprecation_announcement_days(),
        "grace_period_days": get_grace_period_days()
    }

# Cargar configuración de horario de deprecación de caché de API al importar
load_api_cache_deprecation_schedule_config()
