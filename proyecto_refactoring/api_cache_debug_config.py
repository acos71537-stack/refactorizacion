import os
import json
import time
from datetime import datetime

# Variables globales
API_CACHE_DEBUG_CONFIG_FILE = "api_cache_debug_config.json"
api_cache_debug_config = {}

def load_api_cache_debug_config():
    """Carga configuración de debug de caché de API"""
    global api_cache_debug_config
    
    if os.path.exists(API_CACHE_DEBUG_CONFIG_FILE):
        with open(API_CACHE_DEBUG_CONFIG_FILE, 'r') as f:
            api_cache_debug_config = json.load(f)
    else:
        api_cache_debug_config = {
            "enabled": False,
            "verbose_logging": True,
            "trace_requests": True,
            "dump_cache_state": False
        }

def save_api_cache_debug_config():
    """Guarda configuración de debug de caché de API"""
    with open(API_CACHE_DEBUG_CONFIG_FILE, 'w') as f:
        json.dump(api_cache_debug_config, f, indent=4)

def get_api_cache_debug_setting(key):
    """Obtiene configuración de debug de caché de API"""
    return api_cache_debug_config.get(key)

def set_api_cache_debug_setting(key, value):
    """Establece configuración de debug de caché de API"""
    api_cache_debug_config[key] = value
    save_api_cache_debug_config()

def get_all_api_cache_debug_settings():
    """Obtiene todas las configuraciones de debug de caché de API"""
    return api_cache_debug_config.copy()

def reset_api_cache_debug_config():
    """Resetea configuración de debug de caché de API"""
    global api_cache_debug_config
    api_cache_debug_config = {
        "enabled": False,
        "verbose_logging": True,
        "trace_requests": True,
        "dump_cache_state": False
    }
    save_api_cache_debug_config()

def is_cache_debug_enabled():
    """Verifica si debug de caché está habilitado"""
    return api_cache_debug_config.get("enabled", False)

def enable_cache_debug():
    """Habilita debug de caché"""
    api_cache_debug_config["enabled"] = True
    save_api_cache_debug_config()

def disable_cache_debug():
    """Deshabilita debug de caché"""
    api_cache_debug_config["enabled"] = False
    save_api_cache_debug_config()

def is_verbose_logging_enabled():
    """Verifica si logging verbose está habilitado"""
    return api_cache_debug_config.get("verbose_logging", True)

def enable_verbose_logging():
    """Habilita logging verbose"""
    api_cache_debug_config["verbose_logging"] = True
    save_api_cache_debug_config()

def disable_verbose_logging():
    """Deshabilita logging verbose"""
    api_cache_debug_config["verbose_logging"] = False
    save_api_cache_debug_config()

def is_trace_requests_enabled():
    """Verifica si trazado de requests está habilitado"""
    return api_cache_debug_config.get("trace_requests", True)

def enable_trace_requests():
    """Habilita trazado de requests"""
    api_cache_debug_config["trace_requests"] = True
    save_api_cache_debug_config()

def disable_trace_requests():
    """Deshabilita trazado de requests"""
    api_cache_debug_config["trace_requests"] = False
    save_api_cache_debug_config()

def is_dump_cache_state_enabled():
    """Verifica si volcar estado de caché está habilitado"""
    return api_cache_debug_config.get("dump_cache_state", False)

def enable_dump_cache_state():
    """Habilita volcar estado de caché"""
    api_cache_debug_config["dump_cache_state"] = True
    save_api_cache_debug_config()

def disable_dump_cache_state():
    """Deshabilita volcar estado de caché"""
    api_cache_debug_config["dump_cache_state"] = False
    save_api_cache_debug_config()

def export_api_cache_debug_config(filename):
    """Exporta configuración de debug de caché de API"""
    with open(filename, 'w') as f:
        json.dump(api_cache_debug_config, f, indent=4)

def import_api_cache_debug_config(filename):
    """Importa configuración de debug de caché de API"""
    global api_cache_debug_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            api_cache_debug_config = json.load(f)
        save_api_cache_debug_config()
        return True
    return False

def validate_api_cache_debug_config():
    """Valida configuración de debug de caché de API"""
    errors = []
    
    for key in ["enabled", "verbose_logging", "trace_requests", "dump_cache_state"]:
        if key in api_cache_debug_config:
            if not isinstance(api_cache_debug_config[key], bool):
                errors.append(key + " must be boolean")
    
    return errors

def backup_api_cache_debug_config():
    """Crea backup de configuración de debug de caché de API"""
    backup_name = "api_cache_debug_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_api_cache_debug_config(backup_name)
    return backup_name

def restore_api_cache_debug_config(backup_name):
    """Restaura configuración de debug de caché de API desde backup"""
    return import_api_cache_debug_config(backup_name)

def get_api_cache_debug_config_summary():
    """Obtiene resumen de configuración de debug de caché de API"""
    return {
        "enabled": is_cache_debug_enabled(),
        "verbose_logging": is_verbose_logging_enabled(),
        "trace_requests": is_trace_requests_enabled()
    }

# Cargar configuración de debug de caché de API al importar
load_api_cache_debug_config()
