import os
import json
import time
from datetime import datetime

# Variables globales
API_CACHE_BEST_PRACTICES_CONFIG_FILE = "api_cache_best_practices_config.json"
api_cache_best_practices_config = {}

def load_api_cache_best_practices_config():
    """Carga configuración de mejores prácticas de caché de API"""
    global api_cache_best_practices_config
    
    if os.path.exists(API_CACHE_BEST_PRACTICES_CONFIG_FILE):
        with open(API_CACHE_BEST_PRACTICES_CONFIG_FILE, 'r') as f:
            api_cache_best_practices_config = json.load(f)
    else:
        api_cache_best_practices_config = {
            "enforce_naming_conventions": True,
            "require_documentation": True,
            "validate_configurations": True,
            "enforce_security_policies": True
        }

def save_api_cache_best_practices_config():
    """Guarda configuración de mejores prácticas de caché de API"""
    with open(API_CACHE_BEST_PRACTICES_CONFIG_FILE, 'w') as f:
        json.dump(api_cache_best_practices_config, f, indent=4)

def get_api_cache_best_practices_setting(key):
    """Obtiene configuración de mejores prácticas de caché de API"""
    return api_cache_best_practices_config.get(key)

def set_api_cache_best_practices_setting(key, value):
    """Establece configuración de mejores prácticas de caché de API"""
    api_cache_best_practices_config[key] = value
    save_api_cache_best_practices_config()

def get_all_api_cache_best_practices_settings():
    """Obtiene todas las configuraciones de mejores prácticas de caché de API"""
    return api_cache_best_practices_config.copy()

def reset_api_cache_best_practices_config():
    """Resetea configuración de mejores prácticas de caché de API"""
    global api_cache_best_practices_config
    api_cache_best_practices_config = {
        "enforce_naming_conventions": True,
        "require_documentation": True,
        "validate_configurations": True,
        "enforce_security_policies": True
    }
    save_api_cache_best_practices_config()

def is_enforce_naming_conventions_enabled():
    """Verifica si imponer convenciones de nombres está habilitado"""
    return api_cache_best_practices_config.get("enforce_naming_conventions", True)

def enable_enforce_naming_conventions():
    """Habilita imponer convenciones de nombres"""
    api_cache_best_practices_config["enforce_naming_conventions"] = True
    save_api_cache_best_practices_config()

def disable_enforce_naming_conventions():
    """Deshabilita imponer convenciones de nombres"""
    api_cache_best_practices_config["enforce_naming_conventions"] = False
    save_api_cache_best_practices_config()

def is_require_documentation_enabled():
    """Verifica si requerir documentación está habilitado"""
    return api_cache_best_practices_config.get("require_documentation", True)

def enable_require_documentation():
    """Habilita requerir documentación"""
    api_cache_best_practices_config["require_documentation"] = True
    save_api_cache_best_practices_config()

def disable_require_documentation():
    """Deshabilita requerir documentación"""
    api_cache_best_practices_config["require_documentation"] = False
    save_api_cache_best_practices_config()

def is_validate_configurations_enabled():
    """Verifica si validar configuraciones está habilitado"""
    return api_cache_best_practices_config.get("validate_configurations", True)

def enable_validate_configurations():
    """Habilita validar configuraciones"""
    api_cache_best_practices_config["validate_configurations"] = True
    save_api_cache_best_practices_config()

def disable_validate_configurations():
    """Deshabilita validar configuraciones"""
    api_cache_best_practices_config["validate_configurations"] = False
    save_api_cache_best_practices_config()

def is_enforce_security_policies_enabled():
    """Verifica si imponer políticas de seguridad está habilitado"""
    return api_cache_best_practices_config.get("enforce_security_policies", True)

def enable_enforce_security_policies():
    """Habilita imponer políticas de seguridad"""
    api_cache_best_practices_config["enforce_security_policies"] = True
    save_api_cache_best_practices_config()

def disable_enforce_security_policies():
    """Deshabilita imponer políticas de seguridad"""
    api_cache_best_practices_config["enforce_security_policies"] = False
    save_api_cache_best_practices_config()

def export_api_cache_best_practices_config(filename):
    """Exporta configuración de mejores prácticas de caché de API"""
    with open(filename, 'w') as f:
        json.dump(api_cache_best_practices_config, f, indent=4)

def import_api_cache_best_practices_config(filename):
    """Importa configuración de mejores prácticas de caché de API"""
    global api_cache_best_practices_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            api_cache_best_practices_config = json.load(f)
        save_api_cache_best_practices_config()
        return True
    return False

def validate_api_cache_best_practices_config():
    """Valida configuración de mejores prácticas de caché de API"""
    errors = []
    
    for key in ["enforce_naming_conventions", "require_documentation", "validate_configurations", "enforce_security_policies"]:
        if key in api_cache_best_practices_config:
            if not isinstance(api_cache_best_practices_config[key], bool):
                errors.append(key + " must be boolean")
    
    return errors

def backup_api_cache_best_practices_config():
    """Crea backup de configuración de mejores prácticas de caché de API"""
    backup_name = "api_cache_best_practices_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_api_cache_best_practices_config(backup_name)
    return backup_name

def restore_api_cache_best_practices_config(backup_name):
    """Restaura configuración de mejores prácticas de caché de API desde backup"""
    return import_api_cache_best_practices_config(backup_name)

def get_api_cache_best_practices_config_summary():
    """Obtiene resumen de configuración de mejores prácticas de caché de API"""
    return {
        "enforce_naming_conventions": is_enforce_naming_conventions_enabled(),
        "require_documentation": is_require_documentation_enabled(),
        "validate_configurations": is_validate_configurations_enabled()
    }

# Cargar configuración de mejores prácticas de caché de API al importar
load_api_cache_best_practices_config()
