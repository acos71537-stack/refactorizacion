import os
import json
import time
from datetime import datetime

# Variables globales
API_CACHE_INTELLIGENCE_CONFIG_FILE = "api_cache_intelligence_config.json"
api_cache_intelligence_config = {}

def load_api_cache_intelligence_config():
    """Carga configuración de inteligencia de caché de API"""
    global api_cache_intelligence_config
    
    if os.path.exists(API_CACHE_INTELLIGENCE_CONFIG_FILE):
        with open(API_CACHE_INTELLIGENCE_CONFIG_FILE, 'r') as f:
            api_cache_intelligence_config = json.load(f)
    else:
        api_cache_intelligence_config = {
            "enabled": True,
            "predictive_caching": False,
            "adaptive_ttl": False,
            "machine_learning": False
        }

def save_api_cache_intelligence_config():
    """Guarda configuración de inteligencia de caché de API"""
    with open(API_CACHE_INTELLIGENCE_CONFIG_FILE, 'w') as f:
        json.dump(api_cache_intelligence_config, f, indent=4)

def get_api_cache_intelligence_setting(key):
    """Obtiene configuración de inteligencia de caché de API"""
    return api_cache_intelligence_config.get(key)

def set_api_cache_intelligence_setting(key, value):
    """Establece configuración de inteligencia de caché de API"""
    api_cache_intelligence_config[key] = value
    save_api_cache_intelligence_config()

def get_all_api_cache_intelligence_settings():
    """Obtiene todas las configuraciones de inteligencia de caché de API"""
    return api_cache_intelligence_config.copy()

def reset_api_cache_intelligence_config():
    """Resetea configuración de inteligencia de caché de API"""
    global api_cache_intelligence_config
    api_cache_intelligence_config = {
        "enabled": True,
        "predictive_caching": False,
        "adaptive_ttl": False,
        "machine_learning": False
    }
    save_api_cache_intelligence_config()

def is_cache_intelligence_enabled():
    """Verifica si inteligencia de caché está habilitada"""
    return api_cache_intelligence_config.get("enabled", True)

def enable_cache_intelligence():
    """Habilita inteligencia de caché"""
    api_cache_intelligence_config["enabled"] = True
    save_api_cache_intelligence_config()

def disable_cache_intelligence():
    """Deshabilita inteligencia de caché"""
    api_cache_intelligence_config["enabled"] = False
    save_api_cache_intelligence_config()

def is_predictive_caching_enabled():
    """Verifica si caché predictivo está habilitado"""
    return api_cache_intelligence_config.get("predictive_caching", False)

def enable_predictive_caching():
    """Habilita caché predictivo"""
    api_cache_intelligence_config["predictive_caching"] = True
    save_api_cache_intelligence_config()

def disable_predictive_caching():
    """Deshabilita caché predictivo"""
    api_cache_intelligence_config["predictive_caching"] = False
    save_api_cache_intelligence_config()

def is_adaptive_ttl_enabled():
    """Verifica si TTL adaptativo está habilitado"""
    return api_cache_intelligence_config.get("adaptive_ttl", False)

def enable_adaptive_ttl():
    """Habilita TTL adaptativo"""
    api_cache_intelligence_config["adaptive_ttl"] = True
    save_api_cache_intelligence_config()

def disable_adaptive_ttl():
    """Deshabilita TTL adaptativo"""
    api_cache_intelligence_config["adaptive_ttl"] = False
    save_api_cache_intelligence_config()

def is_machine_learning_enabled():
    """Verifica si machine learning está habilitado"""
    return api_cache_intelligence_config.get("machine_learning", False)

def enable_machine_learning():
    """Habilita machine learning"""
    api_cache_intelligence_config["machine_learning"] = True
    save_api_cache_intelligence_config()

def disable_machine_learning():
    """Deshabilita machine learning"""
    api_cache_intelligence_config["machine_learning"] = False
    save_api_cache_intelligence_config()

def export_api_cache_intelligence_config(filename):
    """Exporta configuración de inteligencia de caché de API"""
    with open(filename, 'w') as f:
        json.dump(api_cache_intelligence_config, f, indent=4)

def import_api_cache_intelligence_config(filename):
    """Importa configuración de inteligencia de caché de API"""
    global api_cache_intelligence_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            api_cache_intelligence_config = json.load(f)
        save_api_cache_intelligence_config()
        return True
    return False

def validate_api_cache_intelligence_config():
    """Valida configuración de inteligencia de caché de API"""
    errors = []
    
    for key in ["enabled", "predictive_caching", "adaptive_ttl", "machine_learning"]:
        if key in api_cache_intelligence_config:
            if not isinstance(api_cache_intelligence_config[key], bool):
                errors.append(key + " must be boolean")
    
    return errors

def backup_api_cache_intelligence_config():
    """Crea backup de configuración de inteligencia de caché de API"""
    backup_name = "api_cache_intelligence_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_api_cache_intelligence_config(backup_name)
    return backup_name

def restore_api_cache_intelligence_config(backup_name):
    """Restaura configuración de inteligencia de caché de API desde backup"""
    return import_api_cache_intelligence_config(backup_name)

def get_api_cache_intelligence_config_summary():
    """Obtiene resumen de configuración de inteligencia de caché de API"""
    return {
        "enabled": is_cache_intelligence_enabled(),
        "predictive_caching": is_predictive_caching_enabled(),
        "adaptive_ttl": is_adaptive_ttl_enabled()
    }

# Cargar configuración de inteligencia de caché de API al importar
load_api_cache_intelligence_config()
