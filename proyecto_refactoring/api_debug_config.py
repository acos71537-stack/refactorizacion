import os
import json
import time
from datetime import datetime

# Variables globales
API_DEBUG_CONFIG_FILE = "api_debug_config.json"
api_debug_config = {}

def load_api_debug_config():
    """Carga configuración de debug de API"""
    global api_debug_config
    
    if os.path.exists(API_DEBUG_CONFIG_FILE):
        with open(API_DEBUG_CONFIG_FILE, 'r') as f:
            api_debug_config = json.load(f)
    else:
        api_debug_config = {
            "log_api_requests": True,
            "log_api_responses": True,
            "log_api_errors": True,
            "show_api_timing": True
        }

def save_api_debug_config():
    """Guarda configuración de debug de API"""
    with open(API_DEBUG_CONFIG_FILE, 'w') as f:
        json.dump(api_debug_config, f, indent=4)

def get_api_debug_setting(key):
    """Obtiene configuración de debug de API"""
    return api_debug_config.get(key)

def set_api_debug_setting(key, value):
    """Establece configuración de debug de API"""
    api_debug_config[key] = value
    save_api_debug_config()

def get_all_api_debug_settings():
    """Obtiene todas las configuraciones de debug de API"""
    return api_debug_config.copy()

def reset_api_debug_config():
    """Resetea configuración de debug de API"""
    global api_debug_config
    api_debug_config = {
        "log_api_requests": True,
        "log_api_responses": True,
        "log_api_errors": True,
        "show_api_timing": True
    }
    save_api_debug_config()

def is_log_api_requests_enabled():
    """Verifica si log de requests de API está habilitado"""
    return api_debug_config.get("log_api_requests", True)

def enable_log_api_requests():
    """Habilita log de requests de API"""
    api_debug_config["log_api_requests"] = True
    save_api_debug_config()

def disable_log_api_requests():
    """Deshabilita log de requests de API"""
    api_debug_config["log_api_requests"] = False
    save_api_debug_config()

def is_log_api_responses_enabled():
    """Verifica si log de respuestas de API está habilitado"""
    return api_debug_config.get("log_api_responses", True)

def enable_log_api_responses():
    """Habilita log de respuestas de API"""
    api_debug_config["log_api_responses"] = True
    save_api_debug_config()

def disable_log_api_responses():
    """Deshabilita log de respuestas de API"""
    api_debug_config["log_api_responses"] = False
    save_api_debug_config()

def is_log_api_errors_enabled():
    """Verifica si log de errores de API está habilitado"""
    return api_debug_config.get("log_api_errors", True)

def enable_log_api_errors():
    """Habilita log de errores de API"""
    api_debug_config["log_api_errors"] = True
    save_api_debug_config()

def disable_log_api_errors():
    """Deshabilita log de errores de API"""
    api_debug_config["log_api_errors"] = False
    save_api_debug_config()

def is_show_api_timing_enabled():
    """Verifica si mostrar timing de API está habilitado"""
    return api_debug_config.get("show_api_timing", True)

def enable_show_api_timing():
    """Habilita mostrar timing de API"""
    api_debug_config["show_api_timing"] = True
    save_api_debug_config()

def disable_show_api_timing():
    """Deshabilita mostrar timing de API"""
    api_debug_config["show_api_timing"] = False
    save_api_debug_config()

def export_api_debug_config(filename):
    """Exporta configuración de debug de API"""
    with open(filename, 'w') as f:
        json.dump(api_debug_config, f, indent=4)

def import_api_debug_config(filename):
    """Importa configuración de debug de API"""
    global api_debug_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            api_debug_config = json.load(f)
        save_api_debug_config()
        return True
    return False

def validate_api_debug_config():
    """Valida configuración de debug de API"""
    errors = []
    
    for key in ["log_api_requests", "log_api_responses", "log_api_errors", "show_api_timing"]:
        if key in api_debug_config:
            if not isinstance(api_debug_config[key], bool):
                errors.append(key + " must be boolean")
    
    return errors

def backup_api_debug_config():
    """Crea backup de configuración de debug de API"""
    backup_name = "api_debug_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_api_debug_config(backup_name)
    return backup_name

def restore_api_debug_config(backup_name):
    """Restaura configuración de debug de API desde backup"""
    return import_api_debug_config(backup_name)

def get_api_debug_config_summary():
    """Obtiene resumen de configuración de debug de API"""
    return {
        "log_api_requests": is_log_api_requests_enabled(),
        "log_api_responses": is_log_api_responses_enabled(),
        "show_api_timing": is_show_api_timing_enabled()
    }

# Cargar configuración de debug de API al importar
load_api_debug_config()
