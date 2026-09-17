import os
import json
import time
from datetime import datetime

# Variables globales
API_CACHE_SERIALIZATION_CONFIG_FILE = "api_cache_serialization_config.json"
api_cache_serialization_config = {}

def load_api_cache_serialization_config():
    """Carga configuración de serialización de caché de API"""
    global api_cache_serialization_config
    
    if os.path.exists(API_CACHE_SERIALIZATION_CONFIG_FILE):
        with open(API_CACHE_SERIALIZATION_CONFIG_FILE, 'r') as f:
            api_cache_serialization_config = json.load(f)
    else:
        api_cache_serialization_config = {
            "format": "json",
            "pretty_print": False,
            "include_metadata": True,
            "encoding": "utf-8"
        }

def save_api_cache_serialization_config():
    """Guarda configuración de serialización de caché de API"""
    with open(API_CACHE_SERIALIZATION_CONFIG_FILE, 'w') as f:
        json.dump(api_cache_serialization_config, f, indent=4)

def get_api_cache_serialization_setting(key):
    """Obtiene configuración de serialización de caché de API"""
    return api_cache_serialization_config.get(key)

def set_api_cache_serialization_setting(key, value):
    """Establece configuración de serialización de caché de API"""
    api_cache_serialization_config[key] = value
    save_api_cache_serialization_config()

def get_all_api_cache_serialization_settings():
    """Obtiene todas las configuraciones de serialización de caché de API"""
    return api_cache_serialization_config.copy()

def reset_api_cache_serialization_config():
    """Resetea configuración de serialización de caché de API"""
    global api_cache_serialization_config
    api_cache_serialization_config = {
        "format": "json",
        "pretty_print": False,
        "include_metadata": True,
        "encoding": "utf-8"
    }
    save_api_cache_serialization_config()

def get_serialization_format():
    """Obtiene formato de serialización"""
    return api_cache_serialization_config.get("format", "json")

def set_serialization_format(format_str):
    """Establece formato de serialización"""
    api_cache_serialization_config["format"] = format_str
    save_api_cache_serialization_config()

def is_pretty_print_enabled():
    """Verifica si pretty print está habilitado"""
    return api_cache_serialization_config.get("pretty_print", False)

def enable_pretty_print():
    """Habilita pretty print"""
    api_cache_serialization_config["pretty_print"] = True
    save_api_cache_serialization_config()

def disable_pretty_print():
    """Deshabilita pretty print"""
    api_cache_serialization_config["pretty_print"] = False
    save_api_cache_serialization_config()

def is_include_metadata_enabled():
    """Verifica si incluir metadatos está habilitado"""
    return api_cache_serialization_config.get("include_metadata", True)

def enable_include_metadata():
    """Habilita incluir metadatos"""
    api_cache_serialization_config["include_metadata"] = True
    save_api_cache_serialization_config()

def disable_include_metadata():
    """Deshabilita incluir metadatos"""
    api_cache_serialization_config["include_metadata"] = False
    save_api_cache_serialization_config()

def get_encoding():
    """Obtiene codificación"""
    return api_cache_serialization_config.get("encoding", "utf-8")

def set_encoding(encoding):
    """Establece codificación"""
    api_cache_serialization_config["encoding"] = encoding
    save_api_cache_serialization_config()

def export_api_cache_serialization_config(filename):
    """Exporta configuración de serialización de caché de API"""
    with open(filename, 'w') as f:
        json.dump(api_cache_serialization_config, f, indent=4)

def import_api_cache_serialization_config(filename):
    """Importa configuración de serialización de caché de API"""
    global api_cache_serialization_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            api_cache_serialization_config = json.load(f)
        save_api_cache_serialization_config()
        return True
    return False

def validate_api_cache_serialization_config():
    """Valida configuración de serialización de caché de API"""
    errors = []
    
    for key in ["pretty_print", "include_metadata"]:
        if key in api_cache_serialization_config:
            if not isinstance(api_cache_serialization_config[key], bool):
                errors.append(key + " must be boolean")
    
    return errors

def backup_api_cache_serialization_config():
    """Crea backup de configuración de serialización de caché de API"""
    backup_name = "api_cache_serialization_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_api_cache_serialization_config(backup_name)
    return backup_name

def restore_api_cache_serialization_config(backup_name):
    """Restaura configuración de serialización de caché de API desde backup"""
    return import_api_cache_serialization_config(backup_name)

def get_api_cache_serialization_config_summary():
    """Obtiene resumen de configuración de serialización de caché de API"""
    return {
        "format": get_serialization_format(),
        "pretty_print": is_pretty_print_enabled(),
        "encoding": get_encoding()
    }

# Cargar configuración de serialización de caché de API al importar
load_api_cache_serialization_config()
