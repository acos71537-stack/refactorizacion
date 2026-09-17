import os
import json
import time
from datetime import datetime

# Variables globales
API_SECURITY_CONFIG_FILE = "api_security_config.json"
api_security_config = {}

def load_api_security_config():
    """Carga configuración de seguridad de API"""
    global api_security_config
    
    if os.path.exists(API_SECURITY_CONFIG_FILE):
        with open(API_SECURITY_CONFIG_FILE, 'r') as f:
            api_security_config = json.load(f)
    else:
        api_security_config = {
            "verify_ssl": True,
            "allow_redirects": True,
            "max_redirects": 5,
            "user_agent": "MovieExplorer/1.0"
        }

def save_api_security_config():
    """Guarda configuración de seguridad de API"""
    with open(API_SECURITY_CONFIG_FILE, 'w') as f:
        json.dump(api_security_config, f, indent=4)

def get_api_security_setting(key):
    """Obtiene configuración de seguridad de API"""
    return api_security_config.get(key)

def set_api_security_setting(key, value):
    """Establece configuración de seguridad de API"""
    api_security_config[key] = value
    save_api_security_config()

def get_all_api_security_settings():
    """Obtiene todas las configuraciones de seguridad de API"""
    return api_security_config.copy()

def reset_api_security_config():
    """Resetea configuración de seguridad de API"""
    global api_security_config
    api_security_config = {
        "verify_ssl": True,
        "allow_redirects": True,
        "max_redirects": 5,
        "user_agent": "MovieExplorer/1.0"
    }
    save_api_security_config()

def is_ssl_verification_enabled():
    """Verifica si verificación SSL está habilitada"""
    return api_security_config.get("verify_ssl", True)

def enable_ssl_verification():
    """Habilita verificación SSL"""
    api_security_config["verify_ssl"] = True
    save_api_security_config()

def disable_ssl_verification():
    """Deshabilita verificación SSL"""
    api_security_config["verify_ssl"] = False
    save_api_security_config()

def is_allow_redirects_enabled():
    """Verifica si permitir redirecciones está habilitado"""
    return api_security_config.get("allow_redirects", True)

def enable_allow_redirects():
    """Habilita permitir redirecciones"""
    api_security_config["allow_redirects"] = True
    save_api_security_config()

def disable_allow_redirects():
    """Deshabilita permitir redirecciones"""
    api_security_config["allow_redirects"] = False
    save_api_security_config()

def get_max_redirects():
    """Obtiene máximo de redirecciones"""
    return api_security_config.get("max_redirects", 5)

def set_max_redirects(max_redirects):
    """Establece máximo de redirecciones"""
    api_security_config["max_redirects"] = max_redirects
    save_api_security_config()

def get_user_agent():
    """Obtiene user agent"""
    return api_security_config.get("user_agent", "MovieExplorer/1.0")

def set_user_agent(user_agent):
    """Establece user agent"""
    api_security_config["user_agent"] = user_agent
    save_api_security_config()

def export_api_security_config(filename):
    """Exporta configuración de seguridad de API"""
    with open(filename, 'w') as f:
        json.dump(api_security_config, f, indent=4)

def import_api_security_config(filename):
    """Importa configuración de seguridad de API"""
    global api_security_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            api_security_config = json.load(f)
        save_api_security_config()
        return True
    return False

def validate_api_security_config():
    """Valida configuración de seguridad de API"""
    errors = []
    
    for key in ["verify_ssl", "allow_redirects"]:
        if key in api_security_config:
            if not isinstance(api_security_config[key], bool):
                errors.append(key + " must be boolean")
    
    if "max_redirects" in api_security_config:
        if not isinstance(api_security_config["max_redirects"], int):
            errors.append("max_redirects must be integer")
    
    return errors

def backup_api_security_config():
    """Crea backup de configuración de seguridad de API"""
    backup_name = "api_security_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_api_security_config(backup_name)
    return backup_name

def restore_api_security_config(backup_name):
    """Restaura configuración de seguridad de API desde backup"""
    return import_api_security_config(backup_name)

def get_api_security_config_summary():
    """Obtiene resumen de configuración de seguridad de API"""
    return {
        "verify_ssl": is_ssl_verification_enabled(),
        "allow_redirects": is_allow_redirects_enabled(),
        "max_redirects": get_max_redirects()
    }

# Cargar configuración de seguridad de API al importar
load_api_security_config()
