import os
import json
import time
from datetime import datetime

# Variables globales
API_CACHE_RECOMMENDATIONS_CONFIG_FILE = "api_cache_recommendations_config.json"
api_cache_recommendations_config = {}

def load_api_cache_recommendations_config():
    """Carga configuración de recomendaciones de caché de API"""
    global api_cache_recommendations_config
    
    if os.path.exists(API_CACHE_RECOMMENDATIONS_CONFIG_FILE):
        with open(API_CACHE_RECOMMENDATIONS_CONFIG_FILE, 'r') as f:
            api_cache_recommendations_config = json.load(f)
    else:
        api_cache_recommendations_config = {
            "enabled": True,
            "auto_optimize": False,
            "suggest_ttl_adjustments": True,
            "suggest_cache_size": True
        }

def save_api_cache_recommendations_config():
    """Guarda configuración de recomendaciones de caché de API"""
    with open(API_CACHE_RECOMMENDATIONS_CONFIG_FILE, 'w') as f:
        json.dump(api_cache_recommendations_config, f, indent=4)

def get_api_cache_recommendations_setting(key):
    """Obtiene configuración de recomendaciones de caché de API"""
    return api_cache_recommendations_config.get(key)

def set_api_cache_recommendations_setting(key, value):
    """Establece configuración de recomendaciones de caché de API"""
    api_cache_recommendations_config[key] = value
    save_api_cache_recommendations_config()

def get_all_api_cache_recommendations_settings():
    """Obtiene todas las configuraciones de recomendaciones de caché de API"""
    return api_cache_recommendations_config.copy()

def reset_api_cache_recommendations_config():
    """Resetea configuración de recomendaciones de caché de API"""
    global api_cache_recommendations_config
    api_cache_recommendations_config = {
        "enabled": True,
        "auto_optimize": False,
        "suggest_ttl_adjustments": True,
        "suggest_cache_size": True
    }
    save_api_cache_recommendations_config()

def is_cache_recommendations_enabled():
    """Verifica si recomendaciones de caché están habilitadas"""
    return api_cache_recommendations_config.get("enabled", True)

def enable_cache_recommendations():
    """Habilita recomendaciones de caché"""
    api_cache_recommendations_config["enabled"] = True
    save_api_cache_recommendations_config()

def disable_cache_recommendations():
    """Deshabilita recomendaciones de caché"""
    api_cache_recommendations_config["enabled"] = False
    save_api_cache_recommendations_config()

def is_auto_optimize_enabled():
    """Verifica si auto-optimización está habilitada"""
    return api_cache_recommendations_config.get("auto_optimize", False)

def enable_auto_optimize():
    """Habilita auto-optimización"""
    api_cache_recommendations_config["auto_optimize"] = True
    save_api_cache_recommendations_config()

def disable_auto_optimize():
    """Deshabilita auto-optimización"""
    api_cache_recommendations_config["auto_optimize"] = False
    save_api_cache_recommendations_config()

def is_suggest_ttl_adjustments_enabled():
    """Verifica si sugerir ajustes de TTL está habilitado"""
    return api_cache_recommendations_config.get("suggest_ttl_adjustments", True)

def enable_suggest_ttl_adjustments():
    """Habilita sugerir ajustes de TTL"""
    api_cache_recommendations_config["suggest_ttl_adjustments"] = True
    save_api_cache_recommendations_config()

def disable_suggest_ttl_adjustments():
    """Deshabilita sugerir ajustes de TTL"""
    api_cache_recommendations_config["suggest_ttl_adjustments"] = False
    save_api_cache_recommendations_config()

def is_suggest_cache_size_enabled():
    """Verifica si sugerir tamaño de caché está habilitado"""
    return api_cache_recommendations_config.get("suggest_cache_size", True)

def enable_suggest_cache_size():
    """Habilita sugerir tamaño de caché"""
    api_cache_recommendations_config["suggest_cache_size"] = True
    save_api_cache_recommendations_config()

def disable_suggest_cache_size():
    """Deshabilita sugerir tamaño de caché"""
    api_cache_recommendations_config["suggest_cache_size"] = False
    save_api_cache_recommendations_config()

def export_api_cache_recommendations_config(filename):
    """Exporta configuración de recomendaciones de caché de API"""
    with open(filename, 'w') as f:
        json.dump(api_cache_recommendations_config, f, indent=4)

def import_api_cache_recommendations_config(filename):
    """Importa configuración de recomendaciones de caché de API"""
    global api_cache_recommendations_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            api_cache_recommendations_config = json.load(f)
        save_api_cache_recommendations_config()
        return True
    return False

def validate_api_cache_recommendations_config():
    """Valida configuración de recomendaciones de caché de API"""
    errors = []
    
    for key in ["enabled", "auto_optimize", "suggest_ttl_adjustments", "suggest_cache_size"]:
        if key in api_cache_recommendations_config:
            if not isinstance(api_cache_recommendations_config[key], bool):
                errors.append(key + " must be boolean")
    
    return errors

def backup_api_cache_recommendations_config():
    """Crea backup de configuración de recomendaciones de caché de API"""
    backup_name = "api_cache_recommendations_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_api_cache_recommendations_config(backup_name)
    return backup_name

def restore_api_cache_recommendations_config(backup_name):
    """Restaura configuración de recomendaciones de caché de API desde backup"""
    return import_api_cache_recommendations_config(backup_name)

def get_api_cache_recommendations_config_summary():
    """Obtiene resumen de configuración de recomendaciones de caché de API"""
    return {
        "enabled": is_cache_recommendations_enabled(),
        "auto_optimize": is_auto_optimize_enabled(),
        "suggest_ttl_adjustments": is_suggest_ttl_adjustments_enabled()
    }

# Cargar configuración de recomendaciones de caché de API al importar
load_api_cache_recommendations_config()
