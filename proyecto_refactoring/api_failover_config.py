import os
import json
import time
from datetime import datetime

# Variables globales
API_FAILOVER_CONFIG_FILE = "api_failover_config.json"
api_failover_config = {}

def load_api_failover_config():
    """Carga configuración de failover de API"""
    global api_failover_config
    
    if os.path.exists(API_FAILOVER_CONFIG_FILE):
        with open(API_FAILOVER_CONFIG_FILE, 'r') as f:
            api_failover_config = json.load(f)
    else:
        api_failover_config = {
            "enabled": True,
            "fallback_url": "",
            "health_check_interval": 60,
            "auto_switch": True
        }

def save_api_failover_config():
    """Guarda configuración de failover de API"""
    with open(API_FAILOVER_CONFIG_FILE, 'w') as f:
        json.dump(api_failover_config, f, indent=4)

def get_api_failover_setting(key):
    """Obtiene configuración de failover de API"""
    return api_failover_config.get(key)

def set_api_failover_setting(key, value):
    """Establece configuración de failover de API"""
    api_failover_config[key] = value
    save_api_failover_config()

def get_all_api_failover_settings():
    """Obtiene todas las configuraciones de failover de API"""
    return api_failover_config.copy()

def reset_api_failover_config():
    """Resetea configuración de failover de API"""
    global api_failover_config
    api_failover_config = {
        "enabled": True,
        "fallback_url": "",
        "health_check_interval": 60,
        "auto_switch": True
    }
    save_api_failover_config()

def is_api_failover_enabled():
    """Verifica si failover de API está habilitado"""
    return api_failover_config.get("enabled", True)

def enable_api_failover():
    """Habilita failover de API"""
    api_failover_config["enabled"] = True
    save_api_failover_config()

def disable_api_failover():
    """Deshabilita failover de API"""
    api_failover_config["enabled"] = False
    save_api_failover_config()

def get_fallback_url():
    """Obtiene URL de respaldo"""
    return api_failover_config.get("fallback_url", "")

def set_fallback_url(url):
    """Establece URL de respaldo"""
    api_failover_config["fallback_url"] = url
    save_api_failover_config()

def get_health_check_interval():
    """Obtiene intervalo de health check"""
    return api_failover_config.get("health_check_interval", 60)

def set_health_check_interval(interval):
    """Establece intervalo de health check"""
    api_failover_config["health_check_interval"] = interval
    save_api_failover_config()

def is_auto_switch_enabled():
    """Verifica si auto-switch está habilitado"""
    return api_failover_config.get("auto_switch", True)

def enable_auto_switch():
    """Habilita auto-switch"""
    api_failover_config["auto_switch"] = True
    save_api_failover_config()

def disable_auto_switch():
    """Deshabilita auto-switch"""
    api_failover_config["auto_switch"] = False
    save_api_failover_config()

def export_api_failover_config(filename):
    """Exporta configuración de failover de API"""
    with open(filename, 'w') as f:
        json.dump(api_failover_config, f, indent=4)

def import_api_failover_config(filename):
    """Importa configuración de failover de API"""
    global api_failover_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            api_failover_config = json.load(f)
        save_api_failover_config()
        return True
    return False

def validate_api_failover_config():
    """Valida configuración de failover de API"""
    errors = []
    
    for key in ["enabled", "auto_switch"]:
        if key in api_failover_config:
            if not isinstance(api_failover_config[key], bool):
                errors.append(key + " must be boolean")
    
    if "health_check_interval" in api_failover_config:
        if not isinstance(api_failover_config["health_check_interval"], int):
            errors.append("health_check_interval must be integer")
    
    return errors

def backup_api_failover_config():
    """Crea backup de configuración de failover de API"""
    backup_name = "api_failover_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_api_failover_config(backup_name)
    return backup_name

def restore_api_failover_config(backup_name):
    """Restaura configuración de failover de API desde backup"""
    return import_api_failover_config(backup_name)

def get_api_failover_config_summary():
    """Obtiene resumen de configuración de failover de API"""
    return {
        "enabled": is_api_failover_enabled(),
        "fallback_url": get_fallback_url(),
        "auto_switch": is_auto_switch_enabled()
    }

# Cargar configuración de failover de API al importar
load_api_failover_config()
