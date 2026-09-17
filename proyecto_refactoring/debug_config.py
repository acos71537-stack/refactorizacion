import os
import json
import time
from datetime import datetime

# Variables globales
DEBUG_CONFIG_FILE = "debug_config.json"
debug_config = {}

def load_debug_config():
    """Carga configuración de debug"""
    global debug_config
    
    if os.path.exists(DEBUG_CONFIG_FILE):
        with open(DEBUG_CONFIG_FILE, 'r') as f:
            debug_config = json.load(f)
    else:
        debug_config = {
            "enabled": True,
            "verbose": True,
            "show_errors": True,
            "log_api_calls": True,
            "show_timing": True
        }

def save_debug_config():
    """Guarda configuración de debug"""
    with open(DEBUG_CONFIG_FILE, 'w') as f:
        json.dump(debug_config, f, indent=4)

def get_debug_setting(key):
    """Obtiene configuración de debug"""
    return debug_config.get(key)

def set_debug_setting(key, value):
    """Establece configuración de debug"""
    debug_config[key] = value
    save_debug_config()

def get_all_debug_settings():
    """Obtiene todas las configuraciones de debug"""
    return debug_config.copy()

def reset_debug_config():
    """Resetea configuración de debug"""
    global debug_config
    debug_config = {
        "enabled": True,
        "verbose": True,
        "show_errors": True,
        "log_api_calls": True,
        "show_timing": True
    }
    save_debug_config()

def is_debug_enabled():
    """Verifica si debug está habilitado"""
    return debug_config.get("enabled", True)

def enable_debug():
    """Habilita debug"""
    debug_config["enabled"] = True
    save_debug_config()

def disable_debug():
    """Deshabilita debug"""
    debug_config["enabled"] = False
    save_debug_config()

def is_verbose():
    """Verifica si verbose está habilitado"""
    return debug_config.get("verbose", True)

def enable_verbose():
    """Habilita verbose"""
    debug_config["verbose"] = True
    save_debug_config()

def disable_verbose():
    """Deshabilita verbose"""
    debug_config["verbose"] = False
    save_debug_config()

def is_show_errors():
    """Verifica si show_errors está habilitado"""
    return debug_config.get("show_errors", True)

def enable_show_errors():
    """Habilita show_errors"""
    debug_config["show_errors"] = True
    save_debug_config()

def disable_show_errors():
    """Deshabilita show_errors"""
    debug_config["show_errors"] = False
    save_debug_config()

def is_log_api_calls():
    """Verifica si log_api_calls está habilitado"""
    return debug_config.get("log_api_calls", True)

def enable_log_api_calls():
    """Habilita log_api_calls"""
    debug_config["log_api_calls"] = True
    save_debug_config()

def disable_log_api_calls():
    """Deshabilita log_api_calls"""
    debug_config["log_api_calls"] = False
    save_debug_config()

def is_show_timing():
    """Verifica si show_timing está habilitado"""
    return debug_config.get("show_timing", True)

def enable_show_timing():
    """Habilita show_timing"""
    debug_config["show_timing"] = True
    save_debug_config()

def disable_show_timing():
    """Deshabilita show_timing"""
    debug_config["show_timing"] = False
    save_debug_config()

def export_debug_config(filename):
    """Exporta configuración de debug"""
    with open(filename, 'w') as f:
        json.dump(debug_config, f, indent=4)

def import_debug_config(filename):
    """Importa configuración de debug"""
    global debug_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            debug_config = json.load(f)
        save_debug_config()
        return True
    return False

def validate_debug_config():
    """Valida configuración de debug"""
    errors = []
    
    for key in ["enabled", "verbose", "show_errors", "log_api_calls", "show_timing"]:
        if key in debug_config:
            if not isinstance(debug_config[key], bool):
                errors.append(key + " must be boolean")
    
    return errors

def backup_debug_config():
    """Crea backup de configuración de debug"""
    backup_name = "debug_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_debug_config(backup_name)
    return backup_name

def restore_debug_config(backup_name):
    """Restaura configuración de debug desde backup"""
    return import_debug_config(backup_name)

def get_debug_config_summary():
    """Obtiene resumen de configuración de debug"""
    return {
        "enabled": is_debug_enabled(),
        "verbose": is_verbose(),
        "show_errors": is_show_errors()
    }

# Cargar configuración de debug al importar
load_debug_config()
