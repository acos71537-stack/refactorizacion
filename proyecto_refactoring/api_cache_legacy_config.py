import os
import json
import time
from datetime import datetime

# Variables globales
API_CACHE_LEGACY_CONFIG_FILE = "api_cache_legacy_config.json"
api_cache_legacy_config = {}

def load_api_cache_legacy_config():
    """Carga configuración legacy de caché de API"""
    global api_cache_legacy_config
    
    if os.path.exists(API_CACHE_LEGACY_CONFIG_FILE):
        with open(API_CACHE_LEGACY_CONFIG_FILE, 'r') as f:
            api_cache_legacy_config = json.load(f)
    else:
        api_cache_legacy_config = {
            "legacy_mode": True,
            "backward_compatibility": True,
            "deprecated_features": ["old-cache-format", "v1-api-support"],
            "migration_required": False
        }

def save_api_cache_legacy_config():
    """Guarda configuración legacy de caché de API"""
    with open(API_CACHE_LEGACY_CONFIG_FILE, 'w') as f:
        json.dump(api_cache_legacy_config, f, indent=4)

def get_api_cache_legacy_setting(key):
    """Obtiene configuración legacy de caché de API"""
    return api_cache_legacy_config.get(key)

def set_api_cache_legacy_setting(key, value):
    """Establece configuración legacy de caché de API"""
    api_cache_legacy_config[key] = value
    save_api_cache_legacy_config()

def get_all_api_cache_legacy_settings():
    """Obtiene todas las configuraciones legacy de caché de API"""
    return api_cache_legacy_config.copy()

def reset_api_cache_legacy_config():
    """Resetea configuración legacy de caché de API"""
    global api_cache_legacy_config
    api_cache_legacy_config = {
        "legacy_mode": True,
        "backward_compatibility": True,
        "deprecated_features": ["old-cache-format", "v1-api-support"],
        "migration_required": False
    }
    save_api_cache_legacy_config()

def is_legacy_mode_enabled():
    """Verifica si modo legacy está habilitado"""
    return api_cache_legacy_config.get("legacy_mode", True)

def enable_legacy_mode():
    """Habilita modo legacy"""
    api_cache_legacy_config["legacy_mode"] = True
    save_api_cache_legacy_config()

def disable_legacy_mode():
    """Deshabilita modo legacy"""
    api_cache_legacy_config["legacy_mode"] = False
    save_api_cache_legacy_config()

def is_backward_compatibility_enabled():
    """Verifica si compatibilidad hacia atrás está habilitada"""
    return api_cache_legacy_config.get("backward_compatibility", True)

def enable_backward_compatibility():
    """Habilita compatibilidad hacia atrás"""
    api_cache_legacy_config["backward_compatibility"] = True
    save_api_cache_legacy_config()

def disable_backward_compatibility():
    """Deshabilita compatibilidad hacia atrás"""
    api_cache_legacy_config["backward_compatibility"] = False
    save_api_cache_legacy_config()

def get_deprecated_features():
    """Obtiene características deprecadas"""
    return api_cache_legacy_config.get("deprecated_features", [])

def set_deprecated_features(features):
    """Establece características deprecadas"""
    api_cache_legacy_config["deprecated_features"] = features
    save_api_cache_legacy_config()

def add_deprecated_feature(feature):
    """Agrega característica deprecada"""
    if "deprecated_features" not in api_cache_legacy_config:
        api_cache_legacy_config["deprecated_features"] = []
    
    if feature not in api_cache_legacy_config["deprecated_features"]:
        api_cache_legacy_config["deprecated_features"].append(feature)
        save_api_cache_legacy_config()
        return True
    return False

def remove_deprecated_feature(feature):
    """Elimina característica deprecada"""
    if "deprecated_features" in api_cache_legacy_config:
        if feature in api_cache_legacy_config["deprecated_features"]:
            api_cache_legacy_config["deprecated_features"].remove(feature)
            save_api_cache_legacy_config()
            return True
    return False

def is_migration_required():
    """Verifica si migración es requerida"""
    return api_cache_legacy_config.get("migration_required", False)

def enable_migration_required():
    """Habilita migración requerida"""
    api_cache_legacy_config["migration_required"] = True
    save_api_cache_legacy_config()

def disable_migration_required():
    """Deshabilita migración requerida"""
    api_cache_legacy_config["migration_required"] = False
    save_api_cache_legacy_config()

def export_api_cache_legacy_config(filename):
    """Exporta configuración legacy de caché de API"""
    with open(filename, 'w') as f:
        json.dump(api_cache_legacy_config, f, indent=4)

def import_api_cache_legacy_config(filename):
    """Importa configuración legacy de caché de API"""
    global api_cache_legacy_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            api_cache_legacy_config = json.load(f)
        save_api_cache_legacy_config()
        return True
    return False

def validate_api_cache_legacy_config():
    """Valida configuración legacy de caché de API"""
    errors = []
    
    for key in ["legacy_mode", "backward_compatibility", "migration_required"]:
        if key in api_cache_legacy_config:
            if not isinstance(api_cache_legacy_config[key], bool):
                errors.append(key + " must be boolean")
    
    if "deprecated_features" in api_cache_legacy_config:
        if not isinstance(api_cache_legacy_config["deprecated_features"], list):
            errors.append("deprecated_features must be list")
    
    return errors

def backup_api_cache_legacy_config():
    """Crea backup de configuración legacy de caché de API"""
    backup_name = "api_cache_legacy_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_api_cache_legacy_config(backup_name)
    return backup_name

def restore_api_cache_legacy_config(backup_name):
    """Restaura configuración legacy de caché de API desde backup"""
    return import_api_cache_legacy_config(backup_name)

def get_api_cache_legacy_config_summary():
    """Obtiene resumen de configuración legacy de caché de API"""
    return {
        "legacy_mode": is_legacy_mode_enabled(),
        "backward_compatibility": is_backward_compatibility_enabled(),
        "deprecated_features_count": len(get_deprecated_features())
    }

# Cargar configuración legacy de caché de API al importar
load_api_cache_legacy_config()
