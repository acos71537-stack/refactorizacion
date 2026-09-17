import os
import json
import time
from datetime import datetime

# Variables globales
API_CACHE_COLLABORATION_CONFIG_FILE = "api_cache_collaboration_config.json"
api_cache_collaboration_config = {}

def load_api_cache_collaboration_config():
    """Carga configuración de colaboración de caché de API"""
    global api_cache_collaboration_config
    
    if os.path.exists(API_CACHE_COLLABORATION_CONFIG_FILE):
        with open(API_CACHE_COLLABORATION_CONFIG_FILE, 'r') as f:
            api_cache_collaboration_config = json.load(f)
    else:
        api_cache_collaboration_config = {
            "enabled": True,
            "shared_cache": False,
            "cross_team_caching": False,
            "collaborative_optimization": True
        }

def save_api_cache_collaboration_config():
    """Guarda configuración de colaboración de caché de API"""
    with open(API_CACHE_COLLABORATION_CONFIG_FILE, 'w') as f:
        json.dump(api_cache_collaboration_config, f, indent=4)

def get_api_cache_collaboration_setting(key):
    """Obtiene configuración de colaboración de caché de API"""
    return api_cache_collaboration_config.get(key)

def set_api_cache_collaboration_setting(key, value):
    """Establece configuración de colaboración de caché de API"""
    api_cache_collaboration_config[key] = value
    save_api_cache_collaboration_config()

def get_all_api_cache_collaboration_settings():
    """Obtiene todas las configuraciones de colaboración de caché de API"""
    return api_cache_collaboration_config.copy()

def reset_api_cache_collaboration_config():
    """Resetea configuración de colaboración de caché de API"""
    global api_cache_collaboration_config
    api_cache_collaboration_config = {
        "enabled": True,
        "shared_cache": False,
        "cross_team_caching": False,
        "collaborative_optimization": True
    }
    save_api_cache_collaboration_config()

def is_cache_collaboration_enabled():
    """Verifica si colaboración de caché está habilitada"""
    return api_cache_collaboration_config.get("enabled", True)

def enable_cache_collaboration():
    """Habilita colaboración de caché"""
    api_cache_collaboration_config["enabled"] = True
    save_api_cache_collaboration_config()

def disable_cache_collaboration():
    """Deshabilita colaboración de caché"""
    api_cache_collaboration_config["enabled"] = False
    save_api_cache_collaboration_config()

def is_shared_cache_enabled():
    """Verifica si caché compartida está habilitada"""
    return api_cache_collaboration_config.get("shared_cache", False)

def enable_shared_cache():
    """Habilita caché compartida"""
    api_cache_collaboration_config["shared_cache"] = True
    save_api_cache_collaboration_config()

def disable_shared_cache():
    """Deshabilita caché compartida"""
    api_cache_collaboration_config["shared_cache"] = False
    save_api_cache_collaboration_config()

def is_cross_team_caching_enabled():
    """Verifica si caché entre equipos está habilitada"""
    return api_cache_collaboration_config.get("cross_team_caching", False)

def enable_cross_team_caching():
    """Habilita caché entre equipos"""
    api_cache_collaboration_config["cross_team_caching"] = True
    save_api_cache_collaboration_config()

def disable_cross_team_caching():
    """Deshabilita caché entre equipos"""
    api_cache_collaboration_config["cross_team_caching"] = False
    save_api_cache_collaboration_config()

def is_collaborative_optimization_enabled():
    """Verifica si optimización colaborativa está habilitada"""
    return api_cache_collaboration_config.get("collaborative_optimization", True)

def enable_collaborative_optimization():
    """Habilita optimización colaborativa"""
    api_cache_collaboration_config["collaborative_optimization"] = True
    save_api_cache_collaboration_config()

def disable_collaborative_optimization():
    """Deshabilita optimización colaborativa"""
    api_cache_collaboration_config["collaborative_optimization"] = False
    save_api_cache_collaboration_config()

def export_api_cache_collaboration_config(filename):
    """Exporta configuración de colaboración de caché de API"""
    with open(filename, 'w') as f:
        json.dump(api_cache_collaboration_config, f, indent=4)

def import_api_cache_collaboration_config(filename):
    """Importa configuración de colaboración de caché de API"""
    global api_cache_collaboration_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            api_cache_collaboration_config = json.load(f)
        save_api_cache_collaboration_config()
        return True
    return False

def validate_api_cache_collaboration_config():
    """Valida configuración de colaboración de caché de API"""
    errors = []
    
    for key in ["enabled", "shared_cache", "cross_team_caching", "collaborative_optimization"]:
        if key in api_cache_collaboration_config:
            if not isinstance(api_cache_collaboration_config[key], bool):
                errors.append(key + " must be boolean")
    
    return errors

def backup_api_cache_collaboration_config():
    """Crea backup de configuración de colaboración de caché de API"""
    backup_name = "api_cache_collaboration_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_api_cache_collaboration_config(backup_name)
    return backup_name

def restore_api_cache_collaboration_config(backup_name):
    """Restaura configuración de colaboración de caché de API desde backup"""
    return import_api_cache_collaboration_config(backup_name)

def get_api_cache_collaboration_config_summary():
    """Obtiene resumen de configuración de colaboración de caché de API"""
    return {
        "enabled": is_cache_collaboration_enabled(),
        "shared_cache": is_shared_cache_enabled(),
        "collaborative_optimization": is_collaborative_optimization_enabled()
    }

# Cargar configuración de colaboración de caché de API al importar
load_api_cache_collaboration_config()
