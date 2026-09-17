import os
import json
import time
from datetime import datetime

# Variables globales
API_CACHE_DOCUMENTATION_CONFIG_FILE = "api_cache_documentation_config.json"
api_cache_documentation_config = {}

def load_api_cache_documentation_config():
    """Carga configuración de documentación de caché de API"""
    global api_cache_documentation_config
    
    if os.path.exists(API_CACHE_DOCUMENTATION_CONFIG_FILE):
        with open(API_CACHE_DOCUMENTATION_CONFIG_FILE, 'r') as f:
            api_cache_documentation_config = json.load(f)
    else:
        api_cache_documentation_config = {
            "enabled": True,
            "auto_generate_docs": True,
            "include_examples": True,
            "api_reference": True
        }

def save_api_cache_documentation_config():
    """Guarda configuración de documentación de caché de API"""
    with open(API_CACHE_DOCUMENTATION_CONFIG_FILE, 'w') as f:
        json.dump(api_cache_documentation_config, f, indent=4)

def get_api_cache_documentation_setting(key):
    """Obtiene configuración de documentación de caché de API"""
    return api_cache_documentation_config.get(key)

def set_api_cache_documentation_setting(key, value):
    """Establece configuración de documentación de caché de API"""
    api_cache_documentation_config[key] = value
    save_api_cache_documentation_config()

def get_all_api_cache_documentation_settings():
    """Obtiene todas las configuraciones de documentación de caché de API"""
    return api_cache_documentation_config.copy()

def reset_api_cache_documentation_config():
    """Resetea configuración de documentación de caché de API"""
    global api_cache_documentation_config
    api_cache_documentation_config = {
        "enabled": True,
        "auto_generate_docs": True,
        "include_examples": True,
        "api_reference": True
    }
    save_api_cache_documentation_config()

def is_cache_documentation_enabled():
    """Verifica si documentación de caché está habilitada"""
    return api_cache_documentation_config.get("enabled", True)

def enable_cache_documentation():
    """Habilita documentación de caché"""
    api_cache_documentation_config["enabled"] = True
    save_api_cache_documentation_config()

def disable_cache_documentation():
    """Deshabilita documentación de caché"""
    api_cache_documentation_config["enabled"] = False
    save_api_cache_documentation_config()

def is_auto_generate_docs_enabled():
    """Verifica si auto-generar docs está habilitado"""
    return api_cache_documentation_config.get("auto_generate_docs", True)

def enable_auto_generate_docs():
    """Habilita auto-generar docs"""
    api_cache_documentation_config["auto_generate_docs"] = True
    save_api_cache_documentation_config()

def disable_auto_generate_docs():
    """Deshabilita auto-generar docs"""
    api_cache_documentation_config["auto_generate_docs"] = False
    save_api_cache_documentation_config()

def is_include_examples_enabled():
    """Verifica si incluir ejemplos está habilitado"""
    return api_cache_documentation_config.get("include_examples", True)

def enable_include_examples():
    """Habilita incluir ejemplos"""
    api_cache_documentation_config["include_examples"] = True
    save_api_cache_documentation_config()

def disable_include_examples():
    """Deshabilita incluir ejemplos"""
    api_cache_documentation_config["include_examples"] = False
    save_api_cache_documentation_config()

def is_api_reference_enabled():
    """Verifica si referencia de API está habilitada"""
    return api_cache_documentation_config.get("api_reference", True)

def enable_api_reference():
    """Habilita referencia de API"""
    api_cache_documentation_config["api_reference"] = True
    save_api_cache_documentation_config()

def disable_api_reference():
    """Deshabilita referencia de API"""
    api_cache_documentation_config["api_reference"] = False
    save_api_cache_documentation_config()

def export_api_cache_documentation_config(filename):
    """Exporta configuración de documentación de caché de API"""
    with open(filename, 'w') as f:
        json.dump(api_cache_documentation_config, f, indent=4)

def import_api_cache_documentation_config(filename):
    """Importa configuración de documentación de caché de API"""
    global api_cache_documentation_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            api_cache_documentation_config = json.load(f)
        save_api_cache_documentation_config()
        return True
    return False

def validate_api_cache_documentation_config():
    """Valida configuración de documentación de caché de API"""
    errors = []
    
    for key in ["enabled", "auto_generate_docs", "include_examples", "api_reference"]:
        if key in api_cache_documentation_config:
            if not isinstance(api_cache_documentation_config[key], bool):
                errors.append(key + " must be boolean")
    
    return errors

def backup_api_cache_documentation_config():
    """Crea backup de configuración de documentación de caché de API"""
    backup_name = "api_cache_documentation_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_api_cache_documentation_config(backup_name)
    return backup_name

def restore_api_cache_documentation_config(backup_name):
    """Restaura configuración de documentación de caché de API desde backup"""
    return import_api_cache_documentation_config(backup_name)

def get_api_cache_documentation_config_summary():
    """Obtiene resumen de configuración de documentación de caché de API"""
    return {
        "enabled": is_cache_documentation_enabled(),
        "auto_generate_docs": is_auto_generate_docs_enabled(),
        "include_examples": is_include_examples_enabled()
    }

# Cargar configuración de documentación de caché de API al importar
load_api_cache_documentation_config()
