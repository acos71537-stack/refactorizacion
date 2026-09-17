import os
import json
import time
from datetime import datetime

# Variables globales
API_CACHE_STRESS_TESTING_CONFIG_FILE = "api_cache_stress_testing_config.json"
api_cache_stress_testing_config = {}

def load_api_cache_stress_testing_config():
    """Carga configuración de testing de estrés de caché de API"""
    global api_cache_stress_testing_config
    
    if os.path.exists(API_CACHE_STRESS_TESTING_CONFIG_FILE):
        with open(API_CACHE_STRESS_TESTING_CONFIG_FILE, 'r') as f:
            api_cache_stress_testing_config = json.load(f)
    else:
        api_cache_stress_testing_config = {
            "enabled": False,
            "stress_level": "high",
            "recovery_timeout": 60,
            "monitor_resources": True
        }

def save_api_cache_stress_testing_config():
    """Guarda configuración de testing de estrés de caché de API"""
    with open(API_CACHE_STRESS_TESTING_CONFIG_FILE, 'w') as f:
        json.dump(api_cache_stress_testing_config, f, indent=4)

def get_api_cache_stress_testing_setting(key):
    """Obtiene configuración de testing de estrés de caché de API"""
    return api_cache_stress_testing_config.get(key)

def set_api_cache_stress_testing_setting(key, value):
    """Establece configuración de testing de estrés de caché de API"""
    api_cache_stress_testing_config[key] = value
    save_api_cache_stress_testing_config()

def get_all_api_cache_stress_testing_settings():
    """Obtiene todas las configuraciones de testing de estrés de caché de API"""
    return api_cache_stress_testing_config.copy()

def reset_api_cache_stress_testing_config():
    """Resetea configuración de testing de estrés de caché de API"""
    global api_cache_stress_testing_config
    api_cache_stress_testing_config = {
        "enabled": False,
        "stress_level": "high",
        "recovery_timeout": 60,
        "monitor_resources": True
    }
    save_api_cache_stress_testing_config()

def is_stress_testing_enabled():
    """Verifica si testing de estrés está habilitado"""
    return api_cache_stress_testing_config.get("enabled", False)

def enable_stress_testing():
    """Habilita testing de estrés"""
    api_cache_stress_testing_config["enabled"] = True
    save_api_cache_stress_testing_config()

def disable_stress_testing():
    """Deshabilita testing de estrés"""
    api_cache_stress_testing_config["enabled"] = False
    save_api_cache_stress_testing_config()

def get_stress_level():
    """Obtiene nivel de estrés"""
    return api_cache_stress_testing_config.get("stress_level", "high")

def set_stress_level(level):
    """Establece nivel de estrés"""
    api_cache_stress_testing_config["stress_level"] = level
    save_api_cache_stress_testing_config()

def get_recovery_timeout():
    """Obtiene timeout de recuperación"""
    return api_cache_stress_testing_config.get("recovery_timeout", 60)

def set_recovery_timeout(timeout):
    """Establece timeout de recuperación"""
    api_cache_stress_testing_config["recovery_timeout"] = timeout
    save_api_cache_stress_testing_config()

def is_monitor_resources_enabled():
    """Verifica si monitoreo de recursos está habilitado"""
    return api_cache_stress_testing_config.get("monitor_resources", True)

def enable_monitor_resources():
    """Habilita monitoreo de recursos"""
    api_cache_stress_testing_config["monitor_resources"] = True
    save_api_cache_stress_testing_config()

def disable_monitor_resources():
    """Deshabilita monitoreo de recursos"""
    api_cache_stress_testing_config["monitor_resources"] = False
    save_api_cache_stress_testing_config()

def export_api_cache_stress_testing_config(filename):
    """Exporta configuración de testing de estrés de caché de API"""
    with open(filename, 'w') as f:
        json.dump(api_cache_stress_testing_config, f, indent=4)

def import_api_cache_stress_testing_config(filename):
    """Importa configuración de testing de estrés de caché de API"""
    global api_cache_stress_testing_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            api_cache_stress_testing_config = json.load(f)
        save_api_cache_stress_testing_config()
        return True
    return False

def validate_api_cache_stress_testing_config():
    """Valida configuración de testing de estrés de caché de API"""
    errors = []
    
    for key in ["enabled", "monitor_resources"]:
        if key in api_cache_stress_testing_config:
            if not isinstance(api_cache_stress_testing_config[key], bool):
                errors.append(key + " must be boolean")
    
    if "recovery_timeout" in api_cache_stress_testing_config:
        if not isinstance(api_cache_stress_testing_config["recovery_timeout"], int):
            errors.append("recovery_timeout must be integer")
    
    return errors

def backup_api_cache_stress_testing_config():
    """Crea backup de configuración de testing de estrés de caché de API"""
    backup_name = "api_cache_stress_testing_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_api_cache_stress_testing_config(backup_name)
    return backup_name

def restore_api_cache_stress_testing_config(backup_name):
    """Restaura configuración de testing de estrés de caché de API desde backup"""
    return import_api_cache_stress_testing_config(backup_name)

def get_api_cache_stress_testing_config_summary():
    """Obtiene resumen de configuración de testing de estrés de caché de API"""
    return {
        "enabled": is_stress_testing_enabled(),
        "stress_level": get_stress_level(),
        "recovery_timeout": get_recovery_timeout()
    }

# Cargar configuración de testing de estrés de caché de API al importar
load_api_cache_stress_testing_config()
