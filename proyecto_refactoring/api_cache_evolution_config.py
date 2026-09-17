import os
import json
import time
from datetime import datetime

# Variables globales
API_CACHE_EVOLUTION_CONFIG_FILE = "api_cache_evolution_config.json"
api_cache_evolution_config = {}

def load_api_cache_evolution_config():
    """Carga configuración de evolución de caché de API"""
    global api_cache_evolution_config
    
    if os.path.exists(API_CACHE_EVOLUTION_CONFIG_FILE):
        with open(API_CACHE_EVOLUTION_CONFIG_FILE, 'r') as f:
            api_cache_evolution_config = json.load(f)
    else:
        api_cache_evolution_config = {
            "version": "1.0.0",
            "migration_strategy": "backward-compatible",
            "deprecation_policy": "grace-period",
            "compatibility_mode": True
        }

def save_api_cache_evolution_config():
    """Guarda configuración de evolución de caché de API"""
    with open(API_CACHE_EVOLUTION_CONFIG_FILE, 'w') as f:
        json.dump(api_cache_evolution_config, f, indent=4)

def get_api_cache_evolution_setting(key):
    """Obtiene configuración de evolución de caché de API"""
    return api_cache_evolution_config.get(key)

def set_api_cache_evolution_setting(key, value):
    """Establece configuración de evolución de caché de API"""
    api_cache_evolution_config[key] = value
    save_api_cache_evolution_config()

def get_all_api_cache_evolution_settings():
    """Obtiene todas las configuraciones de evolución de caché de API"""
    return api_cache_evolution_config.copy()

def reset_api_cache_evolution_config():
    """Resetea configuración de evolución de caché de API"""
    global api_cache_evolution_config
    api_cache_evolution_config = {
        "version": "1.0.0",
        "migration_strategy": "backward-compatible",
        "deprecation_policy": "grace-period",
        "compatibility_mode": True
    }
    save_api_cache_evolution_config()

def get_cache_version():
    """Obtiene versión de caché"""
    return api_cache_evolution_config.get("version", "1.0.0")

def set_cache_version(version):
    """Establece versión de caché"""
    api_cache_evolution_config["version"] = version
    save_api_cache_evolution_config()

def get_migration_strategy():
    """Obtiene estrategia de migración"""
    return api_cache_evolution_config.get("migration_strategy", "backward-compatible")

def set_migration_strategy(strategy):
    """Establece estrategia de migración"""
    api_cache_evolution_config["migration_strategy"] = strategy
    save_api_cache_evolution_config()

def get_deprecation_policy():
    """Obtiene política de deprecación"""
    return api_cache_evolution_config.get("deprecation_policy", "grace-period")

def set_deprecation_policy(policy):
    """Establece política de deprecación"""
    api_cache_evolution_config["deprecation_policy"] = policy
    save_api_cache_evolution_config()

def is_compatibility_mode_enabled():
    """Verifica si modo de compatibilidad está habilitado"""
    return api_cache_evolution_config.get("compatibility_mode", True)

def enable_compatibility_mode():
    """Habilita modo de compatibilidad"""
    api_cache_evolution_config["compatibility_mode"] = True
    save_api_cache_evolution_config()

def disable_compatibility_mode():
    """Deshabilita modo de compatibilidad"""
    api_cache_evolution_config["compatibility_mode"] = False
    save_api_cache_evolution_config()

def export_api_cache_evolution_config(filename):
    """Exporta configuración de evolución de caché de API"""
    with open(filename, 'w') as f:
        json.dump(api_cache_evolution_config, f, indent=4)

def import_api_cache_evolution_config(filename):
    """Importa configuración de evolución de caché de API"""
    global api_cache_evolution_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            api_cache_evolution_config = json.load(f)
        save_api_cache_evolution_config()
        return True
    return False

def validate_api_cache_evolution_config():
    """Valida configuración de evolución de caché de API"""
    errors = []
    
    if "compatibility_mode" in api_cache_evolution_config:
        if not isinstance(api_cache_evolution_config["compatibility_mode"], bool):
            errors.append("compatibility_mode must be boolean")
    
    return errors

def backup_api_cache_evolution_config():
    """Crea backup de configuración de evolución de caché de API"""
    backup_name = "api_cache_evolution_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_api_cache_evolution_config(backup_name)
    return backup_name

def restore_api_cache_evolution_config(backup_name):
    """Restaura configuración de evolución de caché de API desde backup"""
    return import_api_cache_evolution_config(backup_name)

def get_api_cache_evolution_config_summary():
    """Obtiene resumen de configuración de evolución de caché de API"""
    return {
        "version": get_cache_version(),
        "migration_strategy": get_migration_strategy(),
        "compatibility_mode": is_compatibility_mode_enabled()
    }

# Cargar configuración de evolución de caché de API al importar
load_api_cache_evolution_config()
