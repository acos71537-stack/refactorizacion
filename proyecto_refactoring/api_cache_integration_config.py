import os
import json
import time
from datetime import datetime

# Variables globales
API_CACHE_INTEGRATION_CONFIG_FILE = "api_cache_integration_config.json"
api_cache_integration_config = {}

def load_api_cache_integration_config():
    """Carga configuración de integración de caché de API"""
    global api_cache_integration_config
    
    if os.path.exists(API_CACHE_INTEGRATION_CONFIG_FILE):
        with open(API_CACHE_INTEGRATION_CONFIG_FILE, 'r') as f:
            api_cache_integration_config = json.load(f)
    else:
        api_cache_integration_config = {
            "enabled": True,
            "integration_points": ["search", "details", "popular"],
            "fallback_strategy": "pass-through",
            "error_handling": "graceful"
        }

def save_api_cache_integration_config():
    """Guarda configuración de integración de caché de API"""
    with open(API_CACHE_INTEGRATION_CONFIG_FILE, 'w') as f:
        json.dump(api_cache_integration_config, f, indent=4)

def get_api_cache_integration_setting(key):
    """Obtiene configuración de integración de caché de API"""
    return api_cache_integration_config.get(key)

def set_api_cache_integration_setting(key, value):
    """Establece configuración de integración de caché de API"""
    api_cache_integration_config[key] = value
    save_api_cache_integration_config()

def get_all_api_cache_integration_settings():
    """Obtiene todas las configuraciones de integración de caché de API"""
    return api_cache_integration_config.copy()

def reset_api_cache_integration_config():
    """Resetea configuración de integración de caché de API"""
    global api_cache_integration_config
    api_cache_integration_config = {
        "enabled": True,
        "integration_points": ["search", "details", "popular"],
        "fallback_strategy": "pass-through",
        "error_handling": "graceful"
    }
    save_api_cache_integration_config()

def is_cache_integration_enabled():
    """Verifica si integración de caché está habilitada"""
    return api_cache_integration_config.get("enabled", True)

def enable_cache_integration():
    """Habilita integración de caché"""
    api_cache_integration_config["enabled"] = True
    save_api_cache_integration_config()

def disable_cache_integration():
    """Deshabilita integración de caché"""
    api_cache_integration_config["enabled"] = False
    save_api_cache_integration_config()

def get_integration_points():
    """Obtiene puntos de integración"""
    return api_cache_integration_config.get("integration_points", [])

def set_integration_points(points):
    """Establece puntos de integración"""
    api_cache_integration_config["integration_points"] = points
    save_api_cache_integration_config()

def add_integration_point(point):
    """Agrega punto de integración"""
    if "integration_points" not in api_cache_integration_config:
        api_cache_integration_config["integration_points"] = []
    
    if point not in api_cache_integration_config["integration_points"]:
        api_cache_integration_config["integration_points"].append(point)
        save_api_cache_integration_config()
        return True
    return False

def remove_integration_point(point):
    """Elimina punto de integración"""
    if "integration_points" in api_cache_integration_config:
        if point in api_cache_integration_config["integration_points"]:
            api_cache_integration_config["integration_points"].remove(point)
            save_api_cache_integration_config()
            return True
    return False

def get_fallback_strategy():
    """Obtiene estrategia de fallback"""
    return api_cache_integration_config.get("fallback_strategy", "pass-through")

def set_fallback_strategy(strategy):
    """Establece estrategia de fallback"""
    api_cache_integration_config["fallback_strategy"] = strategy
    save_api_cache_integration_config()

def get_error_handling():
    """Obtiene manejo de errores"""
    return api_cache_integration_config.get("error_handling", "graceful")

def set_error_handling(handling):
    """Establece manejo de errores"""
    api_cache_integration_config["error_handling"] = handling
    save_api_cache_integration_config()

def export_api_cache_integration_config(filename):
    """Exporta configuración de integración de caché de API"""
    with open(filename, 'w') as f:
        json.dump(api_cache_integration_config, f, indent=4)

def import_api_cache_integration_config(filename):
    """Importa configuración de integración de caché de API"""
    global api_cache_integration_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            api_cache_integration_config = json.load(f)
        save_api_cache_integration_config()
        return True
    return False

def validate_api_cache_integration_config():
    """Valida configuración de integración de caché de API"""
    errors = []
    
    if "enabled" in api_cache_integration_config:
        if not isinstance(api_cache_integration_config["enabled"], bool):
            errors.append("enabled must be boolean")
    
    if "integration_points" in api_cache_integration_config:
        if not isinstance(api_cache_integration_config["integration_points"], list):
            errors.append("integration_points must be list")
    
    return errors

def backup_api_cache_integration_config():
    """Crea backup de configuración de integración de caché de API"""
    backup_name = "api_cache_integration_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_api_cache_integration_config(backup_name)
    return backup_name

def restore_api_cache_integration_config(backup_name):
    """Restaura configuración de integración de caché de API desde backup"""
    return import_api_cache_integration_config(backup_name)

def get_api_cache_integration_config_summary():
    """Obtiene resumen de configuración de integración de caché de API"""
    return {
        "enabled": is_cache_integration_enabled(),
        "integration_points": get_integration_points(),
        "fallback_strategy": get_fallback_strategy()
    }

# Cargar configuración de integración de caché de API al importar
load_api_cache_integration_config()
