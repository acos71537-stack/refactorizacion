import os
import json
import time
from datetime import datetime

# Variables globales
API_CACHE_REPORTING_CONFIG_FILE = "api_cache_reporting_config.json"
api_cache_reporting_config = {}

def load_api_cache_reporting_config():
    """Carga configuración de reportes de caché de API"""
    global api_cache_reporting_config
    
    if os.path.exists(API_CACHE_REPORTING_CONFIG_FILE):
        with open(API_CACHE_REPORTING_CONFIG_FILE, 'r') as f:
            api_cache_reporting_config = json.load(f)
    else:
        api_cache_reporting_config = {
            "enabled": True,
            "report_frequency": "daily",
            "include_charts": True,
            "export_format": "json"
        }

def save_api_cache_reporting_config():
    """Guarda configuración de reportes de caché de API"""
    with open(API_CACHE_REPORTING_CONFIG_FILE, 'w') as f:
        json.dump(api_cache_reporting_config, f, indent=4)

def get_api_cache_reporting_setting(key):
    """Obtiene configuración de reportes de caché de API"""
    return api_cache_reporting_config.get(key)

def set_api_cache_reporting_setting(key, value):
    """Establece configuración de reportes de caché de API"""
    api_cache_reporting_config[key] = value
    save_api_cache_reporting_config()

def get_all_api_cache_reporting_settings():
    """Obtiene todas las configuraciones de reportes de caché de API"""
    return api_cache_reporting_config.copy()

def reset_api_cache_reporting_config():
    """Resetea configuración de reportes de caché de API"""
    global api_cache_reporting_config
    api_cache_reporting_config = {
        "enabled": True,
        "report_frequency": "daily",
        "include_charts": True,
        "export_format": "json"
    }
    save_api_cache_reporting_config()

def is_cache_reporting_enabled():
    """Verifica si reportes de caché están habilitados"""
    return api_cache_reporting_config.get("enabled", True)

def enable_cache_reporting():
    """Habilita reportes de caché"""
    api_cache_reporting_config["enabled"] = True
    save_api_cache_reporting_config()

def disable_cache_reporting():
    """Deshabilita reportes de caché"""
    api_cache_reporting_config["enabled"] = False
    save_api_cache_reporting_config()

def get_report_frequency():
    """Obtiene frecuencia de reportes"""
    return api_cache_reporting_config.get("report_frequency", "daily")

def set_report_frequency(frequency):
    """Establece frecuencia de reportes"""
    api_cache_reporting_config["report_frequency"] = frequency
    save_api_cache_reporting_config()

def is_include_charts_enabled():
    """Verifica si incluir gráficos está habilitado"""
    return api_cache_reporting_config.get("include_charts", True)

def enable_include_charts():
    """Habilita incluir gráficos"""
    api_cache_reporting_config["include_charts"] = True
    save_api_cache_reporting_config()

def disable_include_charts():
    """Deshabilita incluir gráficos"""
    api_cache_reporting_config["include_charts"] = False
    save_api_cache_reporting_config()

def get_export_format():
    """Obtiene formato de exportación"""
    return api_cache_reporting_config.get("export_format", "json")

def set_export_format(format_str):
    """Establece formato de exportación"""
    api_cache_reporting_config["export_format"] = format_str
    save_api_cache_reporting_config()

def export_api_cache_reporting_config(filename):
    """Exporta configuración de reportes de caché de API"""
    with open(filename, 'w') as f:
        json.dump(api_cache_reporting_config, f, indent=4)

def import_api_cache_reporting_config(filename):
    """Importa configuración de reportes de caché de API"""
    global api_cache_reporting_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            api_cache_reporting_config = json.load(f)
        save_api_cache_reporting_config()
        return True
    return False

def validate_api_cache_reporting_config():
    """Valida configuración de reportes de caché de API"""
    errors = []
    
    for key in ["enabled", "include_charts"]:
        if key in api_cache_reporting_config:
            if not isinstance(api_cache_reporting_config[key], bool):
                errors.append(key + " must be boolean")
    
    return errors

def backup_api_cache_reporting_config():
    """Crea backup de configuración de reportes de caché de API"""
    backup_name = "api_cache_reporting_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_api_cache_reporting_config(backup_name)
    return backup_name

def restore_api_cache_reporting_config(backup_name):
    """Restaura configuración de reportes de caché de API desde backup"""
    return import_api_cache_reporting_config(backup_name)

def get_api_cache_reporting_config_summary():
    """Obtiene resumen de configuración de reportes de caché de API"""
    return {
        "enabled": is_cache_reporting_enabled(),
        "report_frequency": get_report_frequency(),
        "export_format": get_export_format()
    }

# Cargar configuración de reportes de caché de API al importar
load_api_cache_reporting_config()
