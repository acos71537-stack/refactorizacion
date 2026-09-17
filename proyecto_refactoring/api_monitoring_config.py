import os
import json
import time
from datetime import datetime

# Variables globales
API_MONITORING_CONFIG_FILE = "api_monitoring_config.json"
api_monitoring_config = {}

def load_api_monitoring_config():
    """Carga configuración de monitoreo de API"""
    global api_monitoring_config
    
    if os.path.exists(API_MONITORING_CONFIG_FILE):
        with open(API_MONITORING_CONFIG_FILE, 'r') as f:
            api_monitoring_config = json.load(f)
    else:
        api_monitoring_config = {
            "enabled": True,
            "track_response_times": True,
            "track_error_rates": True,
            "alert_threshold_ms": 5000
        }

def save_api_monitoring_config():
    """Guarda configuración de monitoreo de API"""
    with open(API_MONITORING_CONFIG_FILE, 'w') as f:
        json.dump(api_monitoring_config, f, indent=4)

def get_api_monitoring_setting(key):
    """Obtiene configuración de monitoreo de API"""
    return api_monitoring_config.get(key)

def set_api_monitoring_setting(key, value):
    """Establece configuración de monitoreo de API"""
    api_monitoring_config[key] = value
    save_api_monitoring_config()

def get_all_api_monitoring_settings():
    """Obtiene todas las configuraciones de monitoreo de API"""
    return api_monitoring_config.copy()

def reset_api_monitoring_config():
    """Resetea configuración de monitoreo de API"""
    global api_monitoring_config
    api_monitoring_config = {
        "enabled": True,
        "track_response_times": True,
        "track_error_rates": True,
        "alert_threshold_ms": 5000
    }
    save_api_monitoring_config()

def is_api_monitoring_enabled():
    """Verifica si monitoreo de API está habilitado"""
    return api_monitoring_config.get("enabled", True)

def enable_api_monitoring():
    """Habilita monitoreo de API"""
    api_monitoring_config["enabled"] = True
    save_api_monitoring_config()

def disable_api_monitoring():
    """Deshabilita monitoreo de API"""
    api_monitoring_config["enabled"] = False
    save_api_monitoring_config()

def is_track_response_times_enabled():
    """Verifica si rastreo de tiempos de respuesta está habilitado"""
    return api_monitoring_config.get("track_response_times", True)

def enable_track_response_times():
    """Habilita rastreo de tiempos de respuesta"""
    api_monitoring_config["track_response_times"] = True
    save_api_monitoring_config()

def disable_track_response_times():
    """Deshabilita rastreo de tiempos de respuesta"""
    api_monitoring_config["track_response_times"] = False
    save_api_monitoring_config()

def is_track_error_rates_enabled():
    """Verifica si rastreo de tasas de error está habilitado"""
    return api_monitoring_config.get("track_error_rates", True)

def enable_track_error_rates():
    """Habilita rastreo de tasas de error"""
    api_monitoring_config["track_error_rates"] = True
    save_api_monitoring_config()

def disable_track_error_rates():
    """Deshabilita rastreo de tasas de error"""
    api_monitoring_config["track_error_rates"] = False
    save_api_monitoring_config()

def get_alert_threshold_ms():
    """Obtiene umbral de alerta en ms"""
    return api_monitoring_config.get("alert_threshold_ms", 5000)

def set_alert_threshold_ms(threshold):
    """Establece umbral de alerta en ms"""
    api_monitoring_config["alert_threshold_ms"] = threshold
    save_api_monitoring_config()

def export_api_monitoring_config(filename):
    """Exporta configuración de monitoreo de API"""
    with open(filename, 'w') as f:
        json.dump(api_monitoring_config, f, indent=4)

def import_api_monitoring_config(filename):
    """Importa configuración de monitoreo de API"""
    global api_monitoring_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            api_monitoring_config = json.load(f)
        save_api_monitoring_config()
        return True
    return False

def validate_api_monitoring_config():
    """Valida configuración de monitoreo de API"""
    errors = []
    
    for key in ["enabled", "track_response_times", "track_error_rates"]:
        if key in api_monitoring_config:
            if not isinstance(api_monitoring_config[key], bool):
                errors.append(key + " must be boolean")
    
    if "alert_threshold_ms" in api_monitoring_config:
        if not isinstance(api_monitoring_config["alert_threshold_ms"], int):
            errors.append("alert_threshold_ms must be integer")
    
    return errors

def backup_api_monitoring_config():
    """Crea backup de configuración de monitoreo de API"""
    backup_name = "api_monitoring_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_api_monitoring_config(backup_name)
    return backup_name

def restore_api_monitoring_config(backup_name):
    """Restaura configuración de monitoreo de API desde backup"""
    return import_api_monitoring_config(backup_name)

def get_api_monitoring_config_summary():
    """Obtiene resumen de configuración de monitoreo de API"""
    return {
        "enabled": is_api_monitoring_enabled(),
        "track_response_times": is_track_response_times_enabled(),
        "alert_threshold_ms": get_alert_threshold_ms()
    }

# Cargar configuración de monitoreo de API al importar
load_api_monitoring_config()
