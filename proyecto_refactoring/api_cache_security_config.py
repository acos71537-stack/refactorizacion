import os
import json
import time
from datetime import datetime

# Variables globales
API_CACHE_SECURITY_CONFIG_FILE = "api_cache_security_config.json"
api_cache_security_config = {}

def load_api_cache_security_config():
    """Carga configuración de seguridad de caché de API"""
    global api_cache_security_config
    
    if os.path.exists(API_CACHE_SECURITY_CONFIG_FILE):
        with open(API_CACHE_SECURITY_CONFIG_FILE, 'r') as f:
            api_cache_security_config = json.load(f)
    else:
        api_cache_security_config = {
            "encrypt_cache": False,
            "validate_integrity": True,
            "secure_deletion": False,
            "access_control": False
        }

def save_api_cache_security_config():
    """Guarda configuración de seguridad de caché de API"""
    with open(API_CACHE_SECURITY_CONFIG_FILE, 'w') as f:
        json.dump(api_cache_security_config, f, indent=4)

def get_api_cache_security_setting(key):
    """Obtiene configuración de seguridad de caché de API"""
    return api_cache_security_config.get(key)

def set_api_cache_security_setting(key, value):
    """Establece configuración de seguridad de caché de API"""
    api_cache_security_config[key] = value
    save_api_cache_security_config()

def get_all_api_cache_security_settings():
    """Obtiene todas las configuraciones de seguridad de caché de API"""
    return api_cache_security_config.copy()

def reset_api_cache_security_config():
    """Resetea configuración de seguridad de caché de API"""
    global api_cache_security_config
    api_cache_security_config = {
        "encrypt_cache": False,
        "validate_integrity": True,
        "secure_deletion": False,
        "access_control": False
    }
    save_api_cache_security_config()

def is_encrypt_cache_enabled():
    """Verifica si encriptación de caché está habilitada"""
    return api_cache_security_config.get("encrypt_cache", False)

def enable_encrypt_cache():
    """Habilita encriptación de caché"""
    api_cache_security_config["encrypt_cache"] = True
    save_api_cache_security_config()

def disable_encrypt_cache():
    """Deshabilita encriptación de caché"""
    api_cache_security_config["encrypt_cache"] = False
    save_api_cache_security_config()

def is_validate_integrity_enabled():
    """Verifica si validación de integridad está habilitada"""
    return api_cache_security_config.get("validate_integrity", True)

def enable_validate_integrity():
    """Habilita validación de integridad"""
    api_cache_security_config["validate_integrity"] = True
    save_api_cache_security_config()

def disable_validate_integrity():
    """Deshabilita validación de integridad"""
    api_cache_security_config["validate_integrity"] = False
    save_api_cache_security_config()

def is_secure_deletion_enabled():
    """Verifica si eliminación segura está habilitada"""
    return api_cache_security_config.get("secure_deletion", False)

def enable_secure_deletion():
    """Habilita eliminación segura"""
    api_cache_security_config["secure_deletion"] = True
    save_api_cache_security_config()

def disable_secure_deletion():
    """Deshabilita eliminación segura"""
    api_cache_security_config["secure_deletion"] = False
    save_api_cache_security_config()

def is_access_control_enabled():
    """Verifica si control de acceso está habilitado"""
    return api_cache_security_config.get("access_control", False)

def enable_access_control():
    """Habilita control de acceso"""
    api_cache_security_config["access_control"] = True
    save_api_cache_security_config()

def disable_access_control():
    """Deshabilita control de acceso"""
    api_cache_security_config["access_control"] = False
    save_api_cache_security_config()

def export_api_cache_security_config(filename):
    """Exporta configuración de seguridad de caché de API"""
    with open(filename, 'w') as f:
        json.dump(api_cache_security_config, f, indent=4)

def import_api_cache_security_config(filename):
    """Importa configuración de seguridad de caché de API"""
    global api_cache_security_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            api_cache_security_config = json.load(f)
        save_api_cache_security_config()
        return True
    return False

def validate_api_cache_security_config():
    """Valida configuración de seguridad de caché de API"""
    errors = []
    
    for key in ["encrypt_cache", "validate_integrity", "secure_deletion", "access_control"]:
        if key in api_cache_security_config:
            if not isinstance(api_cache_security_config[key], bool):
                errors.append(key + " must be boolean")
    
    return errors

def backup_api_cache_security_config():
    """Crea backup de configuración de seguridad de caché de API"""
    backup_name = "api_cache_security_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_api_cache_security_config(backup_name)
    return backup_name

def restore_api_cache_security_config(backup_name):
    """Restaura configuración de seguridad de caché de API desde backup"""
    return import_api_cache_security_config(backup_name)

def get_api_cache_security_config_summary():
    """Obtiene resumen de configuración de seguridad de caché de API"""
    return {
        "encrypt_cache": is_encrypt_cache_enabled(),
        "validate_integrity": is_validate_integrity_enabled(),
        "secure_deletion": is_secure_deletion_enabled()
    }

# Cargar configuración de seguridad de caché de API al importar
load_api_cache_security_config()
