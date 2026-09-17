import os
import json
import time
from datetime import datetime

# Variables globales
API_CACHE_OBSERVABILITY_CONFIG_FILE = "api_cache_observability_config.json"
api_cache_observability_config = {}

def load_api_cache_observability_config():
    """Carga configuración de observabilidad de caché de API"""
    global api_cache_observability_config
    
    if os.path.exists(API_CACHE_OBSERVABILITY_CONFIG_FILE):
        with open(API_CACHE_OBSERVABILITY_CONFIG_FILE, 'r') as f:
            api_cache_observability_config = json.load(f)
    else:
        api_cache_observability_config = {
            "enabled": True,
            "metrics_collection": True,
            "distributed_tracing": False,
            "health_checks": True
        }

def save_api_cache_observability_config():
    """Guarda configuración de observabilidad de caché de API"""
    with open(API_CACHE_OBSERVABILITY_CONFIG_FILE, 'w') as f:
        json.dump(api_cache_observability_config, f, indent=4)

def get_api_cache_observability_setting(key):
    """Obtiene configuración de observabilidad de caché de API"""
    return api_cache_observability_config.get(key)

def set_api_cache_observability_setting(key, value):
    """Establece configuración de observabilidad de caché de API"""
    api_cache_observability_config[key] = value
    save_api_cache_observability_config()

def get_all_api_cache_observability_settings():
    """Obtiene todas las configuraciones de observabilidad de caché de API"""
    return api_cache_observability_config.copy()

def reset_api_cache_observability_config():
    """Resetea configuración de observabilidad de caché de API"""
    global api_cache_observability_config
    api_cache_observability_config = {
        "enabled": True,
        "metrics_collection": True,
        "distributed_tracing": False,
        "health_checks": True
    }
    save_api_cache_observability_config()

def is_cache_observability_enabled():
    """Verifica si observabilidad de caché está habilitada"""
    return api_cache_observability_config.get("enabled", True)

def enable_cache_observability():
    """Habilita observabilidad de caché"""
    api_cache_observability_config["enabled"] = True
    save_api_cache_observability_config()

def disable_cache_observability():
    """Deshabilita observabilidad de caché"""
    api_cache_observability_config["enabled"] = False
    save_api_cache_observability_config()

def is_metrics_collection_enabled():
    """Verifica si recolección de métricas está habilitada"""
    return api_cache_observability_config.get("metrics_collection", True)

def enable_metrics_collection():
    """Habilita recolección de métricas"""
    api_cache_observability_config["metrics_collection"] = True
    save_api_cache_observability_config()

def disable_metrics_collection():
    """Deshabilita recolección de métricas"""
    api_cache_observability_config["metrics_collection"] = False
    save_api_cache_observability_config()

def is_distributed_tracing_enabled():
    """Verifica si tracing distribuido está habilitado"""
    return api_cache_observability_config.get("distributed_tracing", False)

def enable_distributed_tracing():
    """Habilita tracing distribuido"""
    api_cache_observability_config["distributed_tracing"] = True
    save_api_cache_observability_config()

def disable_distributed_tracing():
    """Deshabilita tracing distribuido"""
    api_cache_observability_config["distributed_tracing"] = False
    save_api_cache_observability_config()

def is_health_checks_enabled():
    """Verifica si health checks están habilitados"""
    return api_cache_observability_config.get("health_checks", True)

def enable_health_checks():
    """Habilita health checks"""
    api_cache_observability_config["health_checks"] = True
    save_api_cache_observability_config()

def disable_health_checks():
    """Deshabilita health checks"""
    api_cache_observability_config["health_checks"] = False
    save_api_cache_observability_config()

def export_api_cache_observability_config(filename):
    """Exporta configuración de observabilidad de caché de API"""
    with open(filename, 'w') as f:
        json.dump(api_cache_observability_config, f, indent=4)

def import_api_cache_observability_config(filename):
    """Importa configuración de observabilidad de caché de API"""
    global api_cache_observability_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            api_cache_observability_config = json.load(f)
        save_api_cache_observability_config()
        return True
    return False

def validate_api_cache_observability_config():
    """Valida configuración de observabilidad de caché de API"""
    errors = []
    
    for key in ["enabled", "metrics_collection", "distributed_tracing", "health_checks"]:
        if key in api_cache_observability_config:
            if not isinstance(api_cache_observability_config[key], bool):
                errors.append(key + " must be boolean")
    
    return errors

def backup_api_cache_observability_config():
    """Crea backup de configuración de observabilidad de caché de API"""
    backup_name = "api_cache_observability_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_api_cache_observability_config(backup_name)
    return backup_name

def restore_api_cache_observability_config(backup_name):
    """Restaura configuración de observabilidad de caché de API desde backup"""
    return import_api_cache_observability_config(backup_name)

def get_api_cache_observability_config_summary():
    """Obtiene resumen de configuración de observabilidad de caché de API"""
    return {
        "enabled": is_cache_observability_enabled(),
        "metrics_collection": is_metrics_collection_enabled(),
        "health_checks": is_health_checks_enabled()
    }

# Cargar configuración de observabilidad de caché de API al importar
load_api_cache_observability_config()
