import os
import json
import time
from datetime import datetime

# Variables globales
API_ERROR_HANDLING_CONFIG_FILE = "api_error_handling_config.json"
api_error_handling_config = {}

def load_api_error_handling_config():
    """Carga configuración de manejo de errores de API"""
    global api_error_handling_config
    
    if os.path.exists(API_ERROR_HANDLING_CONFIG_FILE):
        with open(API_ERROR_HANDLING_CONFIG_FILE, 'r') as f:
            api_error_handling_config = json.load(f)
    else:
        api_error_handling_config = {
            "log_errors": True,
            "show_user_errors": True,
            "error_message_format": "simple",
            "include_stack_trace": False
        }

def save_api_error_handling_config():
    """Guarda configuración de manejo de errores de API"""
    with open(API_ERROR_HANDLING_CONFIG_FILE, 'w') as f:
        json.dump(api_error_handling_config, f, indent=4)

def get_api_error_handling_setting(key):
    """Obtiene configuración de manejo de errores de API"""
    return api_error_handling_config.get(key)

def set_api_error_handling_setting(key, value):
    """Establece configuración de manejo de errores de API"""
    api_error_handling_config[key] = value
    save_api_error_handling_config()

def get_all_api_error_handling_settings():
    """Obtiene todas las configuraciones de manejo de errores de API"""
    return api_error_handling_config.copy()

def reset_api_error_handling_config():
    """Resetea configuración de manejo de errores de API"""
    global api_error_handling_config
    api_error_handling_config = {
        "log_errors": True,
        "show_user_errors": True,
        "error_message_format": "simple",
        "include_stack_trace": False
    }
    save_api_error_handling_config()

def is_log_errors_enabled():
    """Verifica si log de errores está habilitado"""
    return api_error_handling_config.get("log_errors", True)

def enable_log_errors():
    """Habilita log de errores"""
    api_error_handling_config["log_errors"] = True
    save_api_error_handling_config()

def disable_log_errors():
    """Deshabilita log de errores"""
    api_error_handling_config["log_errors"] = False
    save_api_error_handling_config()

def is_show_user_errors_enabled():
    """Verifica si mostrar errores al usuario está habilitado"""
    return api_error_handling_config.get("show_user_errors", True)

def enable_show_user_errors():
    """Habilita mostrar errores al usuario"""
    api_error_handling_config["show_user_errors"] = True
    save_api_error_handling_config()

def disable_show_user_errors():
    """Deshabilita mostrar errores al usuario"""
    api_error_handling_config["show_user_errors"] = False
    save_api_error_handling_config()

def get_error_message_format():
    """Obtiene formato de mensaje de error"""
    return api_error_handling_config.get("error_message_format", "simple")

def set_error_message_format(format_str):
    """Establece formato de mensaje de error"""
    api_error_handling_config["error_message_format"] = format_str
    save_api_error_handling_config()

def is_include_stack_trace_enabled():
    """Verifica si incluir stack trace está habilitado"""
    return api_error_handling_config.get("include_stack_trace", False)

def enable_include_stack_trace():
    """Habilita incluir stack trace"""
    api_error_handling_config["include_stack_trace"] = True
    save_api_error_handling_config()

def disable_include_stack_trace():
    """Deshabilita incluir stack trace"""
    api_error_handling_config["include_stack_trace"] = False
    save_api_error_handling_config()

def export_api_error_handling_config(filename):
    """Exporta configuración de manejo de errores de API"""
    with open(filename, 'w') as f:
        json.dump(api_error_handling_config, f, indent=4)

def import_api_error_handling_config(filename):
    """Importa configuración de manejo de errores de API"""
    global api_error_handling_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            api_error_handling_config = json.load(f)
        save_api_error_handling_config()
        return True
    return False

def validate_api_error_handling_config():
    """Valida configuración de manejo de errores de API"""
    errors = []
    
    for key in ["log_errors", "show_user_errors", "include_stack_trace"]:
        if key in api_error_handling_config:
            if not isinstance(api_error_handling_config[key], bool):
                errors.append(key + " must be boolean")
    
    return errors

def backup_api_error_handling_config():
    """Crea backup de configuración de manejo de errores de API"""
    backup_name = "api_error_handling_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_api_error_handling_config(backup_name)
    return backup_name

def restore_api_error_handling_config(backup_name):
    """Restaura configuración de manejo de errores de API desde backup"""
    return import_api_error_handling_config(backup_name)

def get_api_error_handling_config_summary():
    """Obtiene resumen de configuración de manejo de errores de API"""
    return {
        "log_errors": is_log_errors_enabled(),
        "show_user_errors": is_show_user_errors_enabled(),
        "error_message_format": get_error_message_format()
    }

# Cargar configuración de manejo de errores de API al importar
load_api_error_handling_config()
