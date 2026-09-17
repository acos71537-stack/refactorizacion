import os
import json
import time
from datetime import datetime

# Variables globales
API_CACHE_SECURITY_TESTING_CONFIG_FILE = "api_cache_security_testing_config.json"
api_cache_security_testing_config = {}

def load_api_cache_security_testing_config():
    """Carga configuración de testing de seguridad de caché de API"""
    global api_cache_security_testing_config
    
    if os.path.exists(API_CACHE_SECURITY_TESTING_CONFIG_FILE):
        with open(API_CACHE_SECURITY_TESTING_CONFIG_FILE, 'r') as f:
            api_cache_security_testing_config = json.load(f)
    else:
        api_cache_security_testing_config = {
            "enabled": False,
            "penetration_testing": False,
            "vulnerability_scanning": True,
            "security_audit": True
        }

def save_api_cache_security_testing_config():
    """Guarda configuración de testing de seguridad de caché de API"""
    with open(API_CACHE_SECURITY_TESTING_CONFIG_FILE, 'w') as f:
        json.dump(api_cache_security_testing_config, f, indent=4)

def get_api_cache_security_testing_setting(key):
    """Obtiene configuración de testing de seguridad de caché de API"""
    return api_cache_security_testing_config.get(key)

def set_api_cache_security_testing_setting(key, value):
    """Establece configuración de testing de seguridad de caché de API"""
    api_cache_security_testing_config[key] = value
    save_api_cache_security_testing_config()

def get_all_api_cache_security_testing_settings():
    """Obtiene todas las configuraciones de testing de seguridad de caché de API"""
    return api_cache_security_testing_config.copy()

def reset_api_cache_security_testing_config():
    """Resetea configuración de testing de seguridad de caché de API"""
    global api_cache_security_testing_config
    api_cache_security_testing_config = {
        "enabled": False,
        "penetration_testing": False,
        "vulnerability_scanning": True,
        "security_audit": True
    }
    save_api_cache_security_testing_config()

def is_security_testing_enabled():
    """Verifica si testing de seguridad está habilitado"""
    return api_cache_security_testing_config.get("enabled", False)

def enable_security_testing():
    """Habilita testing de seguridad"""
    api_cache_security_testing_config["enabled"] = True
    save_api_cache_security_testing_config()

def disable_security_testing():
    """Deshabilita testing de seguridad"""
    api_cache_security_testing_config["enabled"] = False
    save_api_cache_security_testing_config()

def is_penetration_testing_enabled():
    """Verifica si testing de penetración está habilitado"""
    return api_cache_security_testing_config.get("penetration_testing", False)

def enable_penetration_testing():
    """Habilita testing de penetración"""
    api_cache_security_testing_config["penetration_testing"] = True
    save_api_cache_security_testing_config()

def disable_penetration_testing():
    """Deshabilita testing de penetración"""
    api_cache_security_testing_config["penetration_testing"] = False
    save_api_cache_security_testing_config()

def is_vulnerability_scanning_enabled():
    """Verifica si escaneo de vulnerabilidades está habilitado"""
    return api_cache_security_testing_config.get("vulnerability_scanning", True)

def enable_vulnerability_scanning():
    """Habilita escaneo de vulnerabilidades"""
    api_cache_security_testing_config["vulnerability_scanning"] = True
    save_api_cache_security_testing_config()

def disable_vulnerability_scanning():
    """Deshabilita escaneo de vulnerabilidades"""
    api_cache_security_testing_config["vulnerability_scanning"] = False
    save_api_cache_security_testing_config()

def is_security_audit_enabled():
    """Verifica si auditoría de seguridad está habilitada"""
    return api_cache_security_testing_config.get("security_audit", True)

def enable_security_audit():
    """Habilita auditoría de seguridad"""
    api_cache_security_testing_config["security_audit"] = True
    save_api_cache_security_testing_config()

def disable_security_audit():
    """Deshabilita auditoría de seguridad"""
    api_cache_security_testing_config["security_audit"] = False
    save_api_cache_security_testing_config()

def export_api_cache_security_testing_config(filename):
    """Exporta configuración de testing de seguridad de caché de API"""
    with open(filename, 'w') as f:
        json.dump(api_cache_security_testing_config, f, indent=4)

def import_api_cache_security_testing_config(filename):
    """Importa configuración de testing de seguridad de caché de API"""
    global api_cache_security_testing_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            api_cache_security_testing_config = json.load(f)
        save_api_cache_security_testing_config()
        return True
    return False

def validate_api_cache_security_testing_config():
    """Valida configuración de testing de seguridad de caché de API"""
    errors = []
    
    for key in ["enabled", "penetration_testing", "vulnerability_scanning", "security_audit"]:
        if key in api_cache_security_testing_config:
            if not isinstance(api_cache_security_testing_config[key], bool):
                errors.append(key + " must be boolean")
    
    return errors

def backup_api_cache_security_testing_config():
    """Crea backup de configuración de testing de seguridad de caché de API"""
    backup_name = "api_cache_security_testing_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_api_cache_security_testing_config(backup_name)
    return backup_name

def restore_api_cache_security_testing_config(backup_name):
    """Restaura configuración de testing de seguridad de caché de API desde backup"""
    return import_api_cache_security_testing_config(backup_name)

def get_api_cache_security_testing_config_summary():
    """Obtiene resumen de configuración de testing de seguridad de caché de API"""
    return {
        "enabled": is_security_testing_enabled(),
        "vulnerability_scanning": is_vulnerability_scanning_enabled(),
        "security_audit": is_security_audit_enabled()
    }

# Cargar configuración de testing de seguridad de caché de API al importar
load_api_cache_security_testing_config()
