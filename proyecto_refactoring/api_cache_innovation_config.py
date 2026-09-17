import os
import json
import time
from datetime import datetime

# Variables globales
API_CACHE_INNOVATION_CONFIG_FILE = "api_cache_innovation_config.json"
api_cache_innovation_config = {}

def load_api_cache_innovation_config():
    """Carga configuración de innovación de caché de API"""
    global api_cache_innovation_config
    
    if os.path.exists(API_CACHE_INNOVATION_CONFIG_FILE):
        with open(API_CACHE_INNOVATION_CONFIG_FILE, 'r') as f:
            api_cache_innovation_config = json.load(f)
    else:
        api_cache_innovation_config = {
            "enabled": True,
            "experimental_features": False,
            "research_mode": False,
            "innovation_pipeline": True
        }

def save_api_cache_innovation_config():
    """Guarda configuración de innovación de caché de API"""
    with open(API_CACHE_INNOVATION_CONFIG_FILE, 'w') as f:
        json.dump(api_cache_innovation_config, f, indent=4)

def get_api_cache_innovation_setting(key):
    """Obtiene configuración de innovación de caché de API"""
    return api_cache_innovation_config.get(key)

def set_api_cache_innovation_setting(key, value):
    """Establece configuración de innovación de caché de API"""
    api_cache_innovation_config[key] = value
    save_api_cache_innovation_config()

def get_all_api_cache_innovation_settings():
    """Obtiene todas las configuraciones de innovación de caché de API"""
    return api_cache_innovation_config.copy()

def reset_api_cache_innovation_config():
    """Resetea configuración de innovación de caché de API"""
    global api_cache_innovation_config
    api_cache_innovation_config = {
        "enabled": True,
        "experimental_features": False,
        "research_mode": False,
        "innovation_pipeline": True
    }
    save_api_cache_innovation_config()

def is_cache_innovation_enabled():
    """Verifica si innovación de caché está habilitada"""
    return api_cache_innovation_config.get("enabled", True)

def enable_cache_innovation():
    """Habilita innovación de caché"""
    api_cache_innovation_config["enabled"] = True
    save_api_cache_innovation_config()

def disable_cache_innovation():
    """Deshabilita innovación de caché"""
    api_cache_innovation_config["enabled"] = False
    save_api_cache_innovation_config()

def is_experimental_features_enabled():
    """Verifica si características experimentales están habilitadas"""
    return api_cache_innovation_config.get("experimental_features", False)

def enable_experimental_features():
    """Habilita características experimentales"""
    api_cache_innovation_config["experimental_features"] = True
    save_api_cache_innovation_config()

def disable_experimental_features():
    """Deshabilita características experimentales"""
    api_cache_innovation_config["experimental_features"] = False
    save_api_cache_innovation_config()

def is_research_mode_enabled():
    """Verifica si modo de investigación está habilitado"""
    return api_cache_innovation_config.get("research_mode", False)

def enable_research_mode():
    """Habilita modo de investigación"""
    api_cache_innovation_config["research_mode"] = True
    save_api_cache_innovation_config()

def disable_research_mode():
    """Deshabilita modo de investigación"""
    api_cache_innovation_config["research_mode"] = False
    save_api_cache_innovation_config()

def is_innovation_pipeline_enabled():
    """Verifica si pipeline de innovación está habilitado"""
    return api_cache_innovation_config.get("innovation_pipeline", True)

def enable_innovation_pipeline():
    """Habilita pipeline de innovación"""
    api_cache_innovation_config["innovation_pipeline"] = True
    save_api_cache_innovation_config()

def disable_innovation_pipeline():
    """Deshabilita pipeline de innovación"""
    api_cache_innovation_config["innovation_pipeline"] = False
    save_api_cache_innovation_config()

def export_api_cache_innovation_config(filename):
    """Exporta configuración de innovación de caché de API"""
    with open(filename, 'w') as f:
        json.dump(api_cache_innovation_config, f, indent=4)

def import_api_cache_innovation_config(filename):
    """Importa configuración de innovación de caché de API"""
    global api_cache_innovation_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            api_cache_innovation_config = json.load(f)
        save_api_cache_innovation_config()
        return True
    return False

def validate_api_cache_innovation_config():
    """Valida configuración de innovación de caché de API"""
    errors = []
    
    for key in ["enabled", "experimental_features", "research_mode", "innovation_pipeline"]:
        if key in api_cache_innovation_config:
            if not isinstance(api_cache_innovation_config[key], bool):
                errors.append(key + " must be boolean")
    
    return errors

def backup_api_cache_innovation_config():
    """Crea backup de configuración de innovación de caché de API"""
    backup_name = "api_cache_innovation_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_api_cache_innovation_config(backup_name)
    return backup_name

def restore_api_cache_innovation_config(backup_name):
    """Restaura configuración de innovación de caché de API desde backup"""
    return import_api_cache_innovation_config(backup_name)

def get_api_cache_innovation_config_summary():
    """Obtiene resumen de configuración de innovación de caché de API"""
    return {
        "enabled": is_cache_innovation_enabled(),
        "experimental_features": is_experimental_features_enabled(),
        "innovation_pipeline": is_innovation_pipeline_enabled()
    }

# Cargar configuración de innovación de caché de API al importar
load_api_cache_innovation_config()
