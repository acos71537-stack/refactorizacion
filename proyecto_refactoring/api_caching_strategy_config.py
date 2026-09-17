import os
import json
import time
from datetime import datetime

# Variables globales
API_CACHING_STRATEGY_CONFIG_FILE = "api_caching_strategy_config.json"
api_caching_strategy_config = {}

def load_api_caching_strategy_config():
    """Carga configuración de estrategia de caché de API"""
    global api_caching_strategy_config
    
    if os.path.exists(API_CACHING_STRATEGY_CONFIG_FILE):
        with open(API_CACHING_STRATEGY_CONFIG_FILE, 'r') as f:
            api_caching_strategy_config = json.load(f)
    else:
        api_caching_strategy_config = {
            "strategy": "time-based",
            "invalidate_on_error": True,
            "pre_fetch": False,
            "cache_warming": False
        }

def save_api_caching_strategy_config():
    """Guarda configuración de estrategia de caché de API"""
    with open(API_CACHING_STRATEGY_CONFIG_FILE, 'w') as f:
        json.dump(api_caching_strategy_config, f, indent=4)

def get_api_caching_strategy_setting(key):
    """Obtiene configuración de estrategia de caché de API"""
    return api_caching_strategy_config.get(key)

def set_api_caching_strategy_setting(key, value):
    """Establece configuración de estrategia de caché de API"""
    api_caching_strategy_config[key] = value
    save_api_caching_strategy_config()

def get_all_api_caching_strategy_settings():
    """Obtiene todas las configuraciones de estrategia de caché de API"""
    return api_caching_strategy_config.copy()

def reset_api_caching_strategy_config():
    """Resetea configuración de estrategia de caché de API"""
    global api_caching_strategy_config
    api_caching_strategy_config = {
        "strategy": "time-based",
        "invalidate_on_error": True,
        "pre_fetch": False,
        "cache_warming": False
    }
    save_api_caching_strategy_config()

def get_caching_strategy():
    """Obtiene estrategia de caché"""
    return api_caching_strategy_config.get("strategy", "time-based")

def set_caching_strategy(strategy):
    """Establece estrategia de caché"""
    api_caching_strategy_config["strategy"] = strategy
    save_api_caching_strategy_config()

def is_invalidate_on_error_enabled():
    """Verifica si invalidar en error está habilitado"""
    return api_caching_strategy_config.get("invalidate_on_error", True)

def enable_invalidate_on_error():
    """Habilita invalidar en error"""
    api_caching_strategy_config["invalidate_on_error"] = True
    save_api_caching_strategy_config()

def disable_invalidate_on_error():
    """Deshabilita invalidar en error"""
    api_caching_strategy_config["invalidate_on_error"] = False
    save_api_caching_strategy_config()

def is_pre_fetch_enabled():
    """Verifica si pre-fetch está habilitado"""
    return api_caching_strategy_config.get("pre_fetch", False)

def enable_pre_fetch():
    """Habilita pre-fetch"""
    api_caching_strategy_config["pre_fetch"] = True
    save_api_caching_strategy_config()

def disable_pre_fetch():
    """Deshabilita pre-fetch"""
    api_caching_strategy_config["pre_fetch"] = False
    save_api_caching_strategy_config()

def is_cache_warming_enabled():
    """Verifica si cache warming está habilitado"""
    return api_caching_strategy_config.get("cache_warming", False)

def enable_cache_warming():
    """Habilita cache warming"""
    api_caching_strategy_config["cache_warming"] = True
    save_api_caching_strategy_config()

def disable_cache_warming():
    """Deshabilita cache warming"""
    api_caching_strategy_config["cache_warming"] = False
    save_api_caching_strategy_config()

def export_api_caching_strategy_config(filename):
    """Exporta configuración de estrategia de caché de API"""
    with open(filename, 'w') as f:
        json.dump(api_caching_strategy_config, f, indent=4)

def import_api_caching_strategy_config(filename):
    """Importa configuración de estrategia de caché de API"""
    global api_caching_strategy_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            api_caching_strategy_config = json.load(f)
        save_api_caching_strategy_config()
        return True
    return False

def validate_api_caching_strategy_config():
    """Valida configuración de estrategia de caché de API"""
    errors = []
    
    for key in ["invalidate_on_error", "pre_fetch", "cache_warming"]:
        if key in api_caching_strategy_config:
            if not isinstance(api_caching_strategy_config[key], bool):
                errors.append(key + " must be boolean")
    
    return errors

def backup_api_caching_strategy_config():
    """Crea backup de configuración de estrategia de caché de API"""
    backup_name = "api_caching_strategy_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_api_caching_strategy_config(backup_name)
    return backup_name

def restore_api_caching_strategy_config(backup_name):
    """Restaura configuración de estrategia de caché de API desde backup"""
    return import_api_caching_strategy_config(backup_name)

def get_api_caching_strategy_config_summary():
    """Obtiene resumen de configuración de estrategia de caché de API"""
    return {
        "strategy": get_caching_strategy(),
        "invalidate_on_error": is_invalidate_on_error_enabled(),
        "pre_fetch": is_pre_fetch_enabled()
    }

# Cargar configuración de estrategia de caché de API al importar
load_api_caching_strategy_config()
