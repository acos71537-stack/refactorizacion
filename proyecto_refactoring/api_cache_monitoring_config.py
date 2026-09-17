import os
import json
import time
from datetime import datetime

# Variables globales
API_CACHE_MONITORING_CONFIG_FILE = "api_cache_monitoring_config.json"
api_cache_monitoring_config = {}

def load_api_cache_monitoring_config():
    """Carga configuración de monitoreo de caché de API"""
    global api_cache_monitoring_config
    
    if os.path.exists(API_CACHE_MONITORING_CONFIG_FILE):
        with open(API_CACHE_MONITORING_CONFIG_FILE, 'r') as f:
            api_cache_monitoring_config = json.load(f)
    else:
        api_cache_monitoring_config = {
            "enabled": True,
            "track_hit_rate": True,
            "track_size": True,
            "alert_on_high_usage": True
        }

def save_api_cache_monitoring_config():
    """Guarda configuración de monitoreo de caché de API"""
    with open(API_CACHE_MONITORING_CONFIG_FILE, 'w') as f:
        json.dump(api_cache_monitoring_config, f, indent=4)

def get_api_cache_monitoring_setting(key):
    """Obtiene configuración de monitoreo de caché de API"""
    return api_cache_monitoring_config.get(key)

def set_api_cache_monitoring_setting(key, value):
    """Establece configuración de monitoreo de caché de API"""
    api_cache_monitoring_config[key] = value
    save_api_cache_monitoring_config()

def get_all_api_cache_monitoring_settings():
    """Obtiene todas las configuraciones de monitoreo de caché de API"""
    return api_cache_monitoring_config.copy()

def reset_api_cache_monitoring_config():
    """Resetea configuración de monitoreo de caché de API"""
    global api_cache_monitoring_config
    api_cache_monitoring_config = {
        "enabled": True,
        "track_hit_rate": True,
        "track_size": True,
        "alert_on_high_usage": True
    }
    save_api_cache_monitoring_config()

def is_cache_monitoring_enabled():
    """Verifica si monitoreo de caché está habilitado"""
    return api_cache_monitoring_config.get("enabled", True)

def enable_cache_monitoring():
    """Habilita monitoreo de caché"""
    api_cache_monitoring_config["enabled"] = True
    save_api_cache_monitoring_config()

def disable_cache_monitoring():
    """Deshabilita monitoreo de caché"""
    api_cache_monitoring_config["enabled"] = False
    save_api_cache_monitoring_config()

def is_track_hit_rate_enabled():
    """Verifica si rastreo de tasa de acierto está habilitado"""
    return api_cache_monitoring_config.get("track_hit_rate", True)

def enable_track_hit_rate():
    """Habilita rastreo de tasa de acierto"""
    api_cache_monitoring_config["track_hit_rate"] = True
    save_api_cache_monitoring_config()

def disable_track_hit_rate():
    """Deshabilita rastreo de tasa de acierto"""
    api_cache_monitoring_config["track_hit_rate"] = False
    save_api_cache_monitoring_config()

def is_track_size_enabled():
    """Verifica si rastreo de tamaño está habilitado"""
    return api_cache_monitoring_config.get("track_size", True)

def enable_track_size():
    """Habilita rastreo de tamaño"""
    api_cache_monitoring_config["track_size"] = True
    save_api_cache_monitoring_config()

def disable_track_size():
    """Deshabilita rastreo de tamaño"""
    api_cache_monitoring_config["track_size"] = False
    save_api_cache_monitoring_config()

def is_alert_on_high_usage_enabled():
    """Verifica si alerta en uso alto está habilitada"""
    return api_cache_monitoring_config.get("alert_on_high_usage", True)

def enable_alert_on_high_usage():
    """Habilita alerta en uso alto"""
    api_cache_monitoring_config["alert_on_high_usage"] = True
    save_api_cache_monitoring_config()

def disable_alert_on_high_usage():
    """Deshabilita alerta en uso alto"""
    api_cache_monitoring_config["alert_on_high_usage"] = False
    save_api_cache_monitoring_config()

def export_api_cache_monitoring_config(filename):
    """Exporta configuración de monitoreo de caché de API"""
    with open(filename, 'w') as f:
        json.dump(api_cache_monitoring_config, f, indent=4)

def import_api_cache_monitoring_config(filename):
    """Importa configuración de monitoreo de caché de API"""
    global api_cache_monitoring_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            api_cache_monitoring_config = json.load(f)
        save_api_cache_monitoring_config()
        return True
    return False

def validate_api_cache_monitoring_config():
    """Valida configuración de monitoreo de caché de API"""
    errors = []
    
    for key in ["enabled", "track_hit_rate", "track_size", "alert_on_high_usage"]:
        if key in api_cache_monitoring_config:
            if not isinstance(api_cache_monitoring_config[key], bool):
                errors.append(key + " must be boolean")
    
    return errors

def backup_api_cache_monitoring_config():
    """Crea backup de configuración de monitoreo de caché de API"""
    backup_name = "api_cache_monitoring_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_api_cache_monitoring_config(backup_name)
    return backup_name

def restore_api_cache_monitoring_config(backup_name):
    """Restaura configuración de monitoreo de caché de API desde backup"""
    return import_api_cache_monitoring_config(backup_name)

def get_api_cache_monitoring_config_summary():
    """Obtiene resumen de configuración de monitoreo de caché de API"""
    return {
        "enabled": is_cache_monitoring_enabled(),
        "track_hit_rate": is_track_hit_rate_enabled(),
        "alert_on_high_usage": is_alert_on_high_usage_enabled()
    }

# Cargar configuración de monitoreo de caché de API al importar
load_api_cache_monitoring_config()
