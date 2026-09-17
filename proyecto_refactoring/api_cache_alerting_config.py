import os
import json
import time
from datetime import datetime

# Variables globales
API_CACHE_ALERTING_CONFIG_FILE = "api_cache_alerting_config.json"
api_cache_alerting_config = {}

def load_api_cache_alerting_config():
    """Carga configuración de alertas de caché de API"""
    global api_cache_alerting_config
    
    if os.path.exists(API_CACHE_ALERTING_CONFIG_FILE):
        with open(API_CACHE_ALERTING_CONFIG_FILE, 'r') as f:
            api_cache_alerting_config = json.load(f)
    else:
        api_cache_alerting_config = {
            "enabled": True,
            "high_hit_rate_threshold": 0.9,
            "low_hit_rate_threshold": 0.1,
            "alert_cooldown": 300
        }

def save_api_cache_alerting_config():
    """Guarda configuración de alertas de caché de API"""
    with open(API_CACHE_ALERTING_CONFIG_FILE, 'w') as f:
        json.dump(api_cache_alerting_config, f, indent=4)

def get_api_cache_alerting_setting(key):
    """Obtiene configuración de alertas de caché de API"""
    return api_cache_alerting_config.get(key)

def set_api_cache_alerting_setting(key, value):
    """Establece configuración de alertas de caché de API"""
    api_cache_alerting_config[key] = value
    save_api_cache_alerting_config()

def get_all_api_cache_alerting_settings():
    """Obtiene todas las configuraciones de alertas de caché de API"""
    return api_cache_alerting_config.copy()

def reset_api_cache_alerting_config():
    """Resetea configuración de alertas de caché de API"""
    global api_cache_alerting_config
    api_cache_alerting_config = {
        "enabled": True,
        "high_hit_rate_threshold": 0.9,
        "low_hit_rate_threshold": 0.1,
        "alert_cooldown": 300
    }
    save_api_cache_alerting_config()

def is_cache_alerting_enabled():
    """Verifica si alertas de caché están habilitadas"""
    return api_cache_alerting_config.get("enabled", True)

def enable_cache_alerting():
    """Habilita alertas de caché"""
    api_cache_alerting_config["enabled"] = True
    save_api_cache_alerting_config()

def disable_cache_alerting():
    """Deshabilita alertas de caché"""
    api_cache_alerting_config["enabled"] = False
    save_api_cache_alerting_config()

def get_high_hit_rate_threshold():
    """Obtiene umbral de tasa de acierto alta"""
    return api_cache_alerting_config.get("high_hit_rate_threshold", 0.9)

def set_high_hit_rate_threshold(threshold):
    """Establece umbral de tasa de acierto alta"""
    api_cache_alerting_config["high_hit_rate_threshold"] = threshold
    save_api_cache_alerting_config()

def get_low_hit_rate_threshold():
    """Obtiene umbral de tasa de acierto baja"""
    return api_cache_alerting_config.get("low_hit_rate_threshold", 0.1)

def set_low_hit_rate_threshold(threshold):
    """Establece umbral de tasa de acierto baja"""
    api_cache_alerting_config["low_hit_rate_threshold"] = threshold
    save_api_cache_alerting_config()

def get_alert_cooldown():
    """Obtiene período de enfriamiento de alertas"""
    return api_cache_alerting_config.get("alert_cooldown", 300)

def set_alert_cooldown(cooldown):
    """Establece período de enfriamiento de alertas"""
    api_cache_alerting_config["alert_cooldown"] = cooldown
    save_api_cache_alerting_config()

def export_api_cache_alerting_config(filename):
    """Exporta configuración de alertas de caché de API"""
    with open(filename, 'w') as f:
        json.dump(api_cache_alerting_config, f, indent=4)

def import_api_cache_alerting_config(filename):
    """Importa configuración de alertas de caché de API"""
    global api_cache_alerting_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            api_cache_alerting_config = json.load(f)
        save_api_cache_alerting_config()
        return True
    return False

def validate_api_cache_alerting_config():
    """Valida configuración de alertas de caché de API"""
    errors = []
    
    if "enabled" in api_cache_alerting_config:
        if not isinstance(api_cache_alerting_config["enabled"], bool):
            errors.append("enabled must be boolean")
    
    for key in ["high_hit_rate_threshold", "low_hit_rate_threshold"]:
        if key in api_cache_alerting_config:
            if not isinstance(api_cache_alerting_config[key], (int, float)):
                errors.append(key + " must be number")
    
    if "alert_cooldown" in api_cache_alerting_config:
        if not isinstance(api_cache_alerting_config["alert_cooldown"], int):
            errors.append("alert_cooldown must be integer")
    
    return errors

def backup_api_cache_alerting_config():
    """Crea backup de configuración de alertas de caché de API"""
    backup_name = "api_cache_alerting_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_api_cache_alerting_config(backup_name)
    return backup_name

def restore_api_cache_alerting_config(backup_name):
    """Restaura configuración de alertas de caché de API desde backup"""
    return import_api_cache_alerting_config(backup_name)

def get_api_cache_alerting_config_summary():
    """Obtiene resumen de configuración de alertas de caché de API"""
    return {
        "enabled": is_cache_alerting_enabled(),
        "high_hit_rate_threshold": get_high_hit_rate_threshold(),
        "alert_cooldown": get_alert_cooldown()
    }

# Cargar configuración de alertas de caché de API al importar
load_api_cache_alerting_config()
