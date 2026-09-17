import os
import json
import time
from datetime import datetime

# Variables globales
API_CACHE_ANALYTICS_CONFIG_FILE = "api_cache_analytics_config.json"
api_cache_analytics_config = {}

def load_api_cache_analytics_config():
    """Carga configuración de analíticas de caché de API"""
    global api_cache_analytics_config
    
    if os.path.exists(API_CACHE_ANALYTICS_CONFIG_FILE):
        with open(API_CACHE_ANALYTICS_CONFIG_FILE, 'r') as f:
            api_cache_analytics_config = json.load(f)
    else:
        api_cache_analytics_config = {
            "enabled": True,
            "track_performance": True,
            "track_usage_patterns": True,
            "generate_reports": True
        }

def save_api_cache_analytics_config():
    """Guarda configuración de analíticas de caché de API"""
    with open(API_CACHE_ANALYTICS_CONFIG_FILE, 'w') as f:
        json.dump(api_cache_analytics_config, f, indent=4)

def get_api_cache_analytics_setting(key):
    """Obtiene configuración de analíticas de caché de API"""
    return api_cache_analytics_config.get(key)

def set_api_cache_analytics_setting(key, value):
    """Establece configuración de analíticas de caché de API"""
    api_cache_analytics_config[key] = value
    save_api_cache_analytics_config()

def get_all_api_cache_analytics_settings():
    """Obtiene todas las configuraciones de analíticas de caché de API"""
    return api_cache_analytics_config.copy()

def reset_api_cache_analytics_config():
    """Resetea configuración de analíticas de caché de API"""
    global api_cache_analytics_config
    api_cache_analytics_config = {
        "enabled": True,
        "track_performance": True,
        "track_usage_patterns": True,
        "generate_reports": True
    }
    save_api_cache_analytics_config()

def is_cache_analytics_enabled():
    """Verifica si analíticas de caché están habilitadas"""
    return api_cache_analytics_config.get("enabled", True)

def enable_cache_analytics():
    """Habilita analíticas de caché"""
    api_cache_analytics_config["enabled"] = True
    save_api_cache_analytics_config()

def disable_cache_analytics():
    """Deshabilita analíticas de caché"""
    api_cache_analytics_config["enabled"] = False
    save_api_cache_analytics_config()

def is_track_performance_enabled():
    """Verifica si rastreo de rendimiento está habilitado"""
    return api_cache_analytics_config.get("track_performance", True)

def enable_track_performance():
    """Habilita rastreo de rendimiento"""
    api_cache_analytics_config["track_performance"] = True
    save_api_cache_analytics_config()

def disable_track_performance():
    """Deshabilita rastreo de rendimiento"""
    api_cache_analytics_config["track_performance"] = False
    save_api_cache_analytics_config()

def is_track_usage_patterns_enabled():
    """Verifica si rastreo de patrones de uso está habilitado"""
    return api_cache_analytics_config.get("track_usage_patterns", True)

def enable_track_usage_patterns():
    """Habilita rastreo de patrones de uso"""
    api_cache_analytics_config["track_usage_patterns"] = True
    save_api_cache_analytics_config()

def disable_track_usage_patterns():
    """Deshabilita rastreo de patrones de uso"""
    api_cache_analytics_config["track_usage_patterns"] = False
    save_api_cache_analytics_config()

def is_generate_reports_enabled():
    """Verifica si generar reportes está habilitado"""
    return api_cache_analytics_config.get("generate_reports", True)

def enable_generate_reports():
    """Habilita generar reportes"""
    api_cache_analytics_config["generate_reports"] = True
    save_api_cache_analytics_config()

def disable_generate_reports():
    """Deshabilita generar reportes"""
    api_cache_analytics_config["generate_reports"] = False
    save_api_cache_analytics_config()

def export_api_cache_analytics_config(filename):
    """Exporta configuración de analíticas de caché de API"""
    with open(filename, 'w') as f:
        json.dump(api_cache_analytics_config, f, indent=4)

def import_api_cache_analytics_config(filename):
    """Importa configuración de analíticas de caché de API"""
    global api_cache_analytics_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            api_cache_analytics_config = json.load(f)
        save_api_cache_analytics_config()
        return True
    return False

def validate_api_cache_analytics_config():
    """Valida configuración de analíticas de caché de API"""
    errors = []
    
    for key in ["enabled", "track_performance", "track_usage_patterns", "generate_reports"]:
        if key in api_cache_analytics_config:
            if not isinstance(api_cache_analytics_config[key], bool):
                errors.append(key + " must be boolean")
    
    return errors

def backup_api_cache_analytics_config():
    """Crea backup de configuración de analíticas de caché de API"""
    backup_name = "api_cache_analytics_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_api_cache_analytics_config(backup_name)
    return backup_name

def restore_api_cache_analytics_config(backup_name):
    """Restaura configuración de analíticas de caché de API desde backup"""
    return import_api_cache_analytics_config(backup_name)

def get_api_cache_analytics_config_summary():
    """Obtiene resumen de configuración de analíticas de caché de API"""
    return {
        "enabled": is_cache_analytics_enabled(),
        "track_performance": is_track_performance_enabled(),
        "generate_reports": is_generate_reports_enabled()
    }

# Cargar configuración de analíticas de caché de API al importar
load_api_cache_analytics_config()
