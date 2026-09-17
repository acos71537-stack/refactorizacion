import os
import json
import time
from datetime import datetime

# Variables globales
API_CACHE_FAILOVER_CONFIG_FILE = "api_cache_failover_config.json"
api_cache_failover_config = {}

def load_api_cache_failover_config():
    """Carga configuración de failover de caché de API"""
    global api_cache_failover_config
    
    if os.path.exists(API_CACHE_FAILOVER_CONFIG_FILE):
        with open(API_CACHE_FAILOVER_CONFIG_FILE, 'r') as f:
            api_cache_failover_config = json.load(f)
    else:
        api_cache_failover_config = {
            "enabled": True,
            "fallback_to_disk": True,
            "fallback_to_memory": True,
            "auto_recovery": True
        }

def save_api_cache_failover_config():
    """Guarda configuración de failover de caché de API"""
    with open(API_CACHE_FAILOVER_CONFIG_FILE, 'w') as f:
        json.dump(api_cache_failover_config, f, indent=4)

def get_api_cache_failover_setting(key):
    """Obtiene configuración de failover de caché de API"""
    return api_cache_failover_config.get(key)

def set_api_cache_failover_setting(key, value):
    """Establece configuración de failover de caché de API"""
    api_cache_failover_config[key] = value
    save_api_cache_failover_config()

def get_all_api_cache_failover_settings():
    """Obtiene todas las configuraciones de failover de caché de API"""
    return api_cache_failover_config.copy()

def reset_api_cache_failover_config():
    """Resetea configuración de failover de caché de API"""
    global api_cache_failover_config
    api_cache_failover_config = {
        "enabled": True,
        "fallback_to_disk": True,
        "fallback_to_memory": True,
        "auto_recovery": True
    }
    save_api_cache_failover_config()

def is_cache_failover_enabled():
    """Verifica si failover de caché está habilitado"""
    return api_cache_failover_config.get("enabled", True)

def enable_cache_failover():
    """Habilita failover de caché"""
    api_cache_failover_config["enabled"] = True
    save_api_cache_failover_config()

def disable_cache_failover():
    """Deshabilita failover de caché"""
    api_cache_failover_config["enabled"] = False
    save_api_cache_failover_config()

def is_fallback_to_disk_enabled():
    """Verifica si fallback a disco está habilitado"""
    return api_cache_failover_config.get("fallback_to_disk", True)

def enable_fallback_to_disk():
    """Habilita fallback a disco"""
    api_cache_failover_config["fallback_to_disk"] = True
    save_api_cache_failover_config()

def disable_fallback_to_disk():
    """Deshabilita fallback a disco"""
    api_cache_failover_config["fallback_to_disk"] = False
    save_api_cache_failover_config()

def is_fallback_to_memory_enabled():
    """Verifica si fallback a memoria está habilitado"""
    return api_cache_failover_config.get("fallback_to_memory", True)

def enable_fallback_to_memory():
    """Habilita fallback a memoria"""
    api_cache_failover_config["fallback_to_memory"] = True
    save_api_cache_failover_config()

def disable_fallback_to_memory():
    """Deshabilita fallback a memoria"""
    api_cache_failover_config["fallback_to_memory"] = False
    save_api_cache_failover_config()

def is_auto_recovery_enabled():
    """Verifica si recuperación automática está habilitada"""
    return api_cache_failover_config.get("auto_recovery", True)

def enable_auto_recovery():
    """Habilita recuperación automática"""
    api_cache_failover_config["auto_recovery"] = True
    save_api_cache_failover_config()

def disable_auto_recovery():
    """Deshabilita recuperación automática"""
    api_cache_failover_config["auto_recovery"] = False
    save_api_cache_failover_config()

def export_api_cache_failover_config(filename):
    """Exporta configuración de failover de caché de API"""
    with open(filename, 'w') as f:
        json.dump(api_cache_failover_config, f, indent=4)

def import_api_cache_failover_config(filename):
    """Importa configuración de failover de caché de API"""
    global api_cache_failover_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            api_cache_failover_config = json.load(f)
        save_api_cache_failover_config()
        return True
    return False

def validate_api_cache_failover_config():
    """Valida configuración de failover de caché de API"""
    errors = []
    
    for key in ["enabled", "fallback_to_disk", "fallback_to_memory", "auto_recovery"]:
        if key in api_cache_failover_config:
            if not isinstance(api_cache_failover_config[key], bool):
                errors.append(key + " must be boolean")
    
    return errors

def backup_api_cache_failover_config():
    """Crea backup de configuración de failover de caché de API"""
    backup_name = "api_cache_failover_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_api_cache_failover_config(backup_name)
    return backup_name

def restore_api_cache_failover_config(backup_name):
    """Restaura configuración de failover de caché de API desde backup"""
    return import_api_cache_failover_config(backup_name)

def get_api_cache_failover_config_summary():
    """Obtiene resumen de configuración de failover de caché de API"""
    return {
        "enabled": is_cache_failover_enabled(),
        "fallback_to_disk": is_fallback_to_disk_enabled(),
        "auto_recovery": is_auto_recovery_enabled()
    }

# Cargar configuración de failover de caché de API al importar
load_api_cache_failover_config()
