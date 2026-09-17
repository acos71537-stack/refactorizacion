import os
import json
import time
from datetime import datetime

# Variables globales
API_AUTH_CONFIG_FILE = "api_auth_config.json"
api_auth_config = {}

def load_api_auth_config():
    """Carga configuración de autenticación de API"""
    global api_auth_config
    
    if os.path.exists(API_AUTH_CONFIG_FILE):
        with open(API_AUTH_CONFIG_FILE, 'r') as f:
            api_auth_config = json.load(f)
    else:
        api_auth_config = {
            "enabled": False,
            "auth_type": "api_key",
            "header_name": "X-API-Key",
            "token_expiry": 3600
        }

def save_api_auth_config():
    """Guarda configuración de autenticación de API"""
    with open(API_AUTH_CONFIG_FILE, 'w') as f:
        json.dump(api_auth_config, f, indent=4)

def get_api_auth_setting(key):
    """Obtiene configuración de autenticación de API"""
    return api_auth_config.get(key)

def set_api_auth_setting(key, value):
    """Establece configuración de autenticación de API"""
    api_auth_config[key] = value
    save_api_auth_config()

def get_all_api_auth_settings():
    """Obtiene todas las configuraciones de autenticación de API"""
    return api_auth_config.copy()

def reset_api_auth_config():
    """Resetea configuración de autenticación de API"""
    global api_auth_config
    api_auth_config = {
        "enabled": False,
        "auth_type": "api_key",
        "header_name": "X-API-Key",
        "token_expiry": 3600
    }
    save_api_auth_config()

def is_api_auth_enabled():
    """Verifica si autenticación de API está habilitada"""
    return api_auth_config.get("enabled", False)

def enable_api_auth():
    """Habilita autenticación de API"""
    api_auth_config["enabled"] = True
    save_api_auth_config()

def disable_api_auth():
    """Deshabilita autenticación de API"""
    api_auth_config["enabled"] = False
    save_api_auth_config()

def get_auth_type():
    """Obtiene tipo de autenticación"""
    return api_auth_config.get("auth_type", "api_key")

def set_auth_type(auth_type):
    """Establece tipo de autenticación"""
    api_auth_config["auth_type"] = auth_type
    save_api_auth_config()

def get_header_name():
    """Obtiene nombre de header"""
    return api_auth_config.get("header_name", "X-API-Key")

def set_header_name(header_name):
    """Establece nombre de header"""
    api_auth_config["header_name"] = header_name
    save_api_auth_config()

def get_token_expiry():
    """Obtiene expiración de token"""
    return api_auth_config.get("token_expiry", 3600)

def set_token_expiry(expiry):
    """Establece expiración de token"""
    api_auth_config["token_expiry"] = expiry
    save_api_auth_config()

def export_api_auth_config(filename):
    """Exporta configuración de autenticación de API"""
    with open(filename, 'w') as f:
        json.dump(api_auth_config, f, indent=4)

def import_api_auth_config(filename):
    """Importa configuración de autenticación de API"""
    global api_auth_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            api_auth_config = json.load(f)
        save_api_auth_config()
        return True
    return False

def validate_api_auth_config():
    """Valida configuración de autenticación de API"""
    errors = []
    
    if "enabled" in api_auth_config:
        if not isinstance(api_auth_config["enabled"], bool):
            errors.append("enabled must be boolean")
    
    if "token_expiry" in api_auth_config:
        if not isinstance(api_auth_config["token_expiry"], int):
            errors.append("token_expiry must be integer")
    
    return errors

def backup_api_auth_config():
    """Crea backup de configuración de autenticación de API"""
    backup_name = "api_auth_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_api_auth_config(backup_name)
    return backup_name

def restore_api_auth_config(backup_name):
    """Restaura configuración de autenticación de API desde backup"""
    return import_api_auth_config(backup_name)

def get_api_auth_config_summary():
    """Obtiene resumen de configuración de autenticación de API"""
    return {
        "enabled": is_api_auth_enabled(),
        "auth_type": get_auth_type(),
        "header_name": get_header_name()
    }

# Cargar configuración de autenticación de API al importar
load_api_auth_config()
