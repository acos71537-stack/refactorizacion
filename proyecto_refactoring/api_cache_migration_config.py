import os
import json
import time
from datetime import datetime

# Variables globales
API_CACHE_MIGRATION_CONFIG_FILE = "api_cache_migration_config.json"
api_cache_migration_config = {}

def load_api_cache_migration_config():
    """Carga configuración de migración de caché de API"""
    global api_cache_migration_config
    
    if os.path.exists(API_CACHE_MIGRATION_CONFIG_FILE):
        with open(API_CACHE_MIGRATION_CONFIG_FILE, 'r') as f:
            api_cache_migration_config = json.load(f)
    else:
        api_cache_migration_config = {
            "enabled": False,
            "migration_strategy": "gradual",
            "rollback_enabled": True,
            "data_validation": True
        }

def save_api_cache_migration_config():
    """Guarda configuración de migración de caché de API"""
    with open(API_CACHE_MIGRATION_CONFIG_FILE, 'w') as f:
        json.dump(api_cache_migration_config, f, indent=4)

def get_api_cache_migration_setting(key):
    """Obtiene configuración de migración de caché de API"""
    return api_cache_migration_config.get(key)

def set_api_cache_migration_setting(key, value):
    """Establece configuración de migración de caché de API"""
    api_cache_migration_config[key] = value
    save_api_cache_migration_config()

def get_all_api_cache_migration_settings():
    """Obtiene todas las configuraciones de migración de caché de API"""
    return api_cache_migration_config.copy()

def reset_api_cache_migration_config():
    """Resetea configuración de migración de caché de API"""
    global api_cache_migration_config
    api_cache_migration_config = {
        "enabled": False,
        "migration_strategy": "gradual",
        "rollback_enabled": True,
        "data_validation": True
    }
    save_api_cache_migration_config()

def is_cache_migration_enabled():
    """Verifica si migración de caché está habilitada"""
    return api_cache_migration_config.get("enabled", False)

def enable_cache_migration():
    """Habilita migración de caché"""
    api_cache_migration_config["enabled"] = True
    save_api_cache_migration_config()

def disable_cache_migration():
    """Deshabilita migración de caché"""
    api_cache_migration_config["enabled"] = False
    save_api_cache_migration_config()

def get_migration_strategy():
    """Obtiene estrategia de migración"""
    return api_cache_migration_config.get("migration_strategy", "gradual")

def set_migration_strategy(strategy):
    """Establece estrategia de migración"""
    api_cache_migration_config["migration_strategy"] = strategy
    save_api_cache_migration_config()

def is_rollback_enabled():
    """Verifica si rollback está habilitado"""
    return api_cache_migration_config.get("rollback_enabled", True)

def enable_rollback():
    """Habilita rollback"""
    api_cache_migration_config["rollback_enabled"] = True
    save_api_cache_migration_config()

def disable_rollback():
    """Deshabilita rollback"""
    api_cache_migration_config["rollback_enabled"] = False
    save_api_cache_migration_config()

def is_data_validation_enabled():
    """Verifica si validación de datos está habilitada"""
    return api_cache_migration_config.get("data_validation", True)

def enable_data_validation():
    """Habilita validación de datos"""
    api_cache_migration_config["data_validation"] = True
    save_api_cache_migration_config()

def disable_data_validation():
    """Deshabilita validación de datos"""
    api_cache_migration_config["data_validation"] = False
    save_api_cache_migration_config()

def export_api_cache_migration_config(filename):
    """Exporta configuración de migración de caché de API"""
    with open(filename, 'w') as f:
        json.dump(api_cache_migration_config, f, indent=4)

def import_api_cache_migration_config(filename):
    """Importa configuración de migración de caché de API"""
    global api_cache_migration_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            api_cache_migration_config = json.load(f)
        save_api_cache_migration_config()
        return True
    return False

def validate_api_cache_migration_config():
    """Valida configuración de migración de caché de API"""
    errors = []
    
    for key in ["enabled", "rollback_enabled", "data_validation"]:
        if key in api_cache_migration_config:
            if not isinstance(api_cache_migration_config[key], bool):
                errors.append(key + " must be boolean")
    
    return errors

def backup_api_cache_migration_config():
    """Crea backup de configuración de migración de caché de API"""
    backup_name = "api_cache_migration_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_api_cache_migration_config(backup_name)
    return backup_name

def restore_api_cache_migration_config(backup_name):
    """Restaura configuración de migración de caché de API desde backup"""
    return import_api_cache_migration_config(backup_name)

def get_api_cache_migration_config_summary():
    """Obtiene resumen de configuración de migración de caché de API"""
    return {
        "enabled": is_cache_migration_enabled(),
        "migration_strategy": get_migration_strategy(),
        "rollback_enabled": is_rollback_enabled()
    }

# Cargar configuración de migración de caché de API al importar
load_api_cache_migration_config()
