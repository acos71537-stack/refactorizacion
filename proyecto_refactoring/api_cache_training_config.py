import os
import json
import time
from datetime import datetime

# Variables globales
API_CACHE_TRAINING_CONFIG_FILE = "api_cache_training_config.json"
api_cache_training_config = {}

def load_api_cache_training_config():
    """Carga configuración de entrenamiento de caché de API"""
    global api_cache_training_config
    
    if os.path.exists(API_CACHE_TRAINING_CONFIG_FILE):
        with open(API_CACHE_TRAINING_CONFIG_FILE, 'r') as f:
            api_cache_training_config = json.load(f)
    else:
        api_cache_training_config = {
            "enabled": True,
            "interactive_mode": True,
            "progress_tracking": True,
            "certification_enabled": False
        }

def save_api_cache_training_config():
    """Guarda configuración de entrenamiento de caché de API"""
    with open(API_CACHE_TRAINING_CONFIG_FILE, 'w') as f:
        json.dump(api_cache_training_config, f, indent=4)

def get_api_cache_training_setting(key):
    """Obtiene configuración de entrenamiento de caché de API"""
    return api_cache_training_config.get(key)

def set_api_cache_training_setting(key, value):
    """Establece configuración de entrenamiento de caché de API"""
    api_cache_training_config[key] = value
    save_api_cache_training_config()

def get_all_api_cache_training_settings():
    """Obtiene todas las configuraciones de entrenamiento de caché de API"""
    return api_cache_training_config.copy()

def reset_api_cache_training_config():
    """Resetea configuración de entrenamiento de caché de API"""
    global api_cache_training_config
    api_cache_training_config = {
        "enabled": True,
        "interactive_mode": True,
        "progress_tracking": True,
        "certification_enabled": False
    }
    save_api_cache_training_config()

def is_cache_training_enabled():
    """Verifica si entrenamiento de caché está habilitado"""
    return api_cache_training_config.get("enabled", True)

def enable_cache_training():
    """Habilita entrenamiento de caché"""
    api_cache_training_config["enabled"] = True
    save_api_cache_training_config()

def disable_cache_training():
    """Deshabilita entrenamiento de caché"""
    api_cache_training_config["enabled"] = False
    save_api_cache_training_config()

def is_interactive_mode_enabled():
    """Verifica si modo interactivo está habilitado"""
    return api_cache_training_config.get("interactive_mode", True)

def enable_interactive_mode():
    """Habilita modo interactivo"""
    api_cache_training_config["interactive_mode"] = True
    save_api_cache_training_config()

def disable_interactive_mode():
    """Deshabilita modo interactivo"""
    api_cache_training_config["interactive_mode"] = False
    save_api_cache_training_config()

def is_progress_tracking_enabled():
    """Verifica si rastreo de progreso está habilitado"""
    return api_cache_training_config.get("progress_tracking", True)

def enable_progress_tracking():
    """Habilita rastreo de progreso"""
    api_cache_training_config["progress_tracking"] = True
    save_api_cache_training_config()

def disable_progress_tracking():
    """Deshabilita rastreo de progreso"""
    api_cache_training_config["progress_tracking"] = False
    save_api_cache_training_config()

def is_certification_enabled():
    """Verifica si certificación está habilitada"""
    return api_cache_training_config.get("certification_enabled", False)

def enable_certification():
    """Habilita certificación"""
    api_cache_training_config["certification_enabled"] = True
    save_api_cache_training_config()

def disable_certification():
    """Deshabilita certificación"""
    api_cache_training_config["certification_enabled"] = False
    save_api_cache_training_config()

def export_api_cache_training_config(filename):
    """Exporta configuración de entrenamiento de caché de API"""
    with open(filename, 'w') as f:
        json.dump(api_cache_training_config, f, indent=4)

def import_api_cache_training_config(filename):
    """Importa configuración de entrenamiento de caché de API"""
    global api_cache_training_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            api_cache_training_config = json.load(f)
        save_api_cache_training_config()
        return True
    return False

def validate_api_cache_training_config():
    """Valida configuración de entrenamiento de caché de API"""
    errors = []
    
    for key in ["enabled", "interactive_mode", "progress_tracking", "certification_enabled"]:
        if key in api_cache_training_config:
            if not isinstance(api_cache_training_config[key], bool):
                errors.append(key + " must be boolean")
    
    return errors

def backup_api_cache_training_config():
    """Crea backup de configuración de entrenamiento de caché de API"""
    backup_name = "api_cache_training_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_api_cache_training_config(backup_name)
    return backup_name

def restore_api_cache_training_config(backup_name):
    """Restaura configuración de entrenamiento de caché de API desde backup"""
    return import_api_cache_training_config(backup_name)

def get_api_cache_training_config_summary():
    """Obtiene resumen de configuración de entrenamiento de caché de API"""
    return {
        "enabled": is_cache_training_enabled(),
        "interactive_mode": is_interactive_mode_enabled(),
        "progress_tracking": is_progress_tracking_enabled()
    }

# Cargar configuración de entrenamiento de caché de API al importar
load_api_cache_training_config()
