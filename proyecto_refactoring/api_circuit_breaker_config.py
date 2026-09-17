import os
import json
import time
from datetime import datetime

# Variables globales
API_CIRCUIT_BREAKER_CONFIG_FILE = "api_circuit_breaker_config.json"
api_circuit_breaker_config = {}

def load_api_circuit_breaker_config():
    """Carga configuración de circuit breaker de API"""
    global api_circuit_breaker_config
    
    if os.path.exists(API_CIRCUIT_BREAKER_CONFIG_FILE):
        with open(API_CIRCUIT_BREAKER_CONFIG_FILE, 'r') as f:
            api_circuit_breaker_config = json.load(f)
    else:
        api_circuit_breaker_config = {
            "enabled": True,
            "failure_threshold": 5,
            "recovery_timeout": 30,
            "half_open_max_calls": 3
        }

def save_api_circuit_breaker_config():
    """Guarda configuración de circuit breaker de API"""
    with open(API_CIRCUIT_BREAKER_CONFIG_FILE, 'w') as f:
        json.dump(api_circuit_breaker_config, f, indent=4)

def get_api_circuit_breaker_setting(key):
    """Obtiene configuración de circuit breaker de API"""
    return api_circuit_breaker_config.get(key)

def set_api_circuit_breaker_setting(key, value):
    """Establece configuración de circuit breaker de API"""
    api_circuit_breaker_config[key] = value
    save_api_circuit_breaker_config()

def get_all_api_circuit_breaker_settings():
    """Obtiene todas las configuraciones de circuit breaker de API"""
    return api_circuit_breaker_config.copy()

def reset_api_circuit_breaker_config():
    """Resetea configuración de circuit breaker de API"""
    global api_circuit_breaker_config
    api_circuit_breaker_config = {
        "enabled": True,
        "failure_threshold": 5,
        "recovery_timeout": 30,
        "half_open_max_calls": 3
    }
    save_api_circuit_breaker_config()

def is_circuit_breaker_enabled():
    """Verifica si circuit breaker está habilitado"""
    return api_circuit_breaker_config.get("enabled", True)

def enable_circuit_breaker():
    """Habilita circuit breaker"""
    api_circuit_breaker_config["enabled"] = True
    save_api_circuit_breaker_config()

def disable_circuit_breaker():
    """Deshabilita circuit breaker"""
    api_circuit_breaker_config["enabled"] = False
    save_api_circuit_breaker_config()

def get_failure_threshold():
    """Obtiene umbral de fallo"""
    return api_circuit_breaker_config.get("failure_threshold", 5)

def set_failure_threshold(threshold):
    """Establece umbral de fallo"""
    api_circuit_breaker_config["failure_threshold"] = threshold
    save_api_circuit_breaker_config()

def get_recovery_timeout():
    """Obtiene timeout de recuperación"""
    return api_circuit_breaker_config.get("recovery_timeout", 30)

def set_recovery_timeout(timeout):
    """Establece timeout de recuperación"""
    api_circuit_breaker_config["recovery_timeout"] = timeout
    save_api_circuit_breaker_config()

def get_half_open_max_calls():
    """Obtiene máximo de llamadas en half-open"""
    return api_circuit_breaker_config.get("half_open_max_calls", 3)

def set_half_open_max_calls(max_calls):
    """Establece máximo de llamadas en half-open"""
    api_circuit_breaker_config["half_open_max_calls"] = max_calls
    save_api_circuit_breaker_config()

def export_api_circuit_breaker_config(filename):
    """Exporta configuración de circuit breaker de API"""
    with open(filename, 'w') as f:
        json.dump(api_circuit_breaker_config, f, indent=4)

def import_api_circuit_breaker_config(filename):
    """Importa configuración de circuit breaker de API"""
    global api_circuit_breaker_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            api_circuit_breaker_config = json.load(f)
        save_api_circuit_breaker_config()
        return True
    return False

def validate_api_circuit_breaker_config():
    """Valida configuración de circuit breaker de API"""
    errors = []
    
    if "enabled" in api_circuit_breaker_config:
        if not isinstance(api_circuit_breaker_config["enabled"], bool):
            errors.append("enabled must be boolean")
    
    for key in ["failure_threshold", "recovery_timeout", "half_open_max_calls"]:
        if key in api_circuit_breaker_config:
            if not isinstance(api_circuit_breaker_config[key], int):
                errors.append(key + " must be integer")
    
    return errors

def backup_api_circuit_breaker_config():
    """Crea backup de configuración de circuit breaker de API"""
    backup_name = "api_circuit_breaker_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_api_circuit_breaker_config(backup_name)
    return backup_name

def restore_api_circuit_breaker_config(backup_name):
    """Restaura configuración de circuit breaker de API desde backup"""
    return import_api_circuit_breaker_config(backup_name)

def get_api_circuit_breaker_config_summary():
    """Obtiene resumen de configuración de circuit breaker de API"""
    return {
        "enabled": is_circuit_breaker_enabled(),
        "failure_threshold": get_failure_threshold(),
        "recovery_timeout": get_recovery_timeout()
    }

# Cargar configuración de circuit breaker de API al importar
load_api_circuit_breaker_config()
