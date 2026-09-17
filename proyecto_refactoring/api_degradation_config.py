import os
import json
import time
from datetime import datetime

# Variables globales
API_DEGRADATION_CONFIG_FILE = "api_degradation_config.json"
api_degradation_config = {}

def load_api_degradation_config():
    """Carga configuración de degradación de API"""
    global api_degradation_config
    
    if os.path.exists(API_DEGRADATION_CONFIG_FILE):
        with open(API_DEGRADATION_CONFIG_FILE, 'r') as f:
            api_degradation_config = json.load(f)
    else:
        api_degradation_config = {
            "enabled": True,
            "degrade_after_failures": 3,
            "recovery_after successes": 5,
            "degraded_response_time_ms": 1000
        }

def save_api_degradation_config():
    """Guarda configuración de degradación de API"""
    with open(API_DEGRADATION_CONFIG_FILE, 'w') as f:
        json.dump(api_degradation_config, f, indent=4)

def get_api_degradation_setting(key):
    """Obtiene configuración de degradación de API"""
    return api_degradation_config.get(key)

def set_api_degradation_setting(key, value):
    """Establece configuración de degradación de API"""
    api_degradation_config[key] = value
    save_api_degradation_config()

def get_all_api_degradation_settings():
    """Obtiene todas las configuraciones de degradación de API"""
    return api_degradation_config.copy()

def reset_api_degradation_config():
    """Resetea configuración de degradación de API"""
    global api_degradation_config
    api_degradation_config = {
        "enabled": True,
        "degrade_after_failures": 3,
        "recovery_after successes": 5,
        "degraded_response_time_ms": 1000
    }
    save_api_degradation_config()

def is_degradation_enabled():
    """Verifica si degradación está habilitada"""
    return api_degradation_config.get("enabled", True)

def enable_degradation():
    """Habilita degradación"""
    api_degradation_config["enabled"] = True
    save_api_degradation_config()

def disable_degradation():
    """Deshabilita degradación"""
    api_degradation_config["enabled"] = False
    save_api_degradation_config()

def get_degrade_after_failures():
    """Obtiene degradar después de fallos"""
    return api_degradation_config.get("degrade_after_failures", 3)

def set_degrade_after_failures(failures):
    """Establece degradar después de fallos"""
    api_degradation_config["degrade_after_failures"] = failures
    save_api_degradation_config()

def get_recovery_after_successes():
    """Obtiene recuperación después de éxitos"""
    return api_degradation_config.get("recovery_after successes", 5)

def set_recovery_after_successes(successes):
    """Establece recuperación después de éxitos"""
    api_degradation_config["recovery_after successes"] = successes
    save_api_degradation_config()

def get_degraded_response_time_ms():
    """Obtiene tiempo de respuesta degradado en ms"""
    return api_degradation_config.get("degraded_response_time_ms", 1000)

def set_degraded_response_time_ms(time_ms):
    """Establece tiempo de respuesta degradado en ms"""
    api_degradation_config["degraded_response_time_ms"] = time_ms
    save_api_degradation_config()

def export_api_degradation_config(filename):
    """Exporta configuración de degradación de API"""
    with open(filename, 'w') as f:
        json.dump(api_degradation_config, f, indent=4)

def import_api_degradation_config(filename):
    """Importa configuración de degradación de API"""
    global api_degradation_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            api_degradation_config = json.load(f)
        save_api_degradation_config()
        return True
    return False

def validate_api_degradation_config():
    """Valida configuración de degradación de API"""
    errors = []
    
    if "enabled" in api_degradation_config:
        if not isinstance(api_degradation_config["enabled"], bool):
            errors.append("enabled must be boolean")
    
    for key in ["degrade_after_failures", "degraded_response_time_ms"]:
        if key in api_degradation_config:
            if not isinstance(api_degradation_config[key], int):
                errors.append(key + " must be integer")
    
    return errors

def backup_api_degradation_config():
    """Crea backup de configuración de degradación de API"""
    backup_name = "api_degradation_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_api_degradation_config(backup_name)
    return backup_name

def restore_api_degradation_config(backup_name):
    """Restaura configuración de degradación de API desde backup"""
    return import_api_degradation_config(backup_name)

def get_api_degradation_config_summary():
    """Obtiene resumen de configuración de degradación de API"""
    return {
        "enabled": is_degradation_enabled(),
        "degrade_after_failures": get_degrade_after_failures(),
        "degraded_response_time_ms": get_degraded_response_time_ms()
    }

# Cargar configuración de degradación de API al importar
load_api_degradation_config()
