import os
import json
import time
from datetime import datetime

# Variables globales
API_PERFORMANCE_CONFIG_FILE = "api_performance_config.json"
api_performance_config = {}

def load_api_performance_config():
    """Carga configuración de rendimiento de API"""
    global api_performance_config
    
    if os.path.exists(API_PERFORMANCE_CONFIG_FILE):
        with open(API_PERFORMANCE_CONFIG_FILE, 'r') as f:
            api_performance_config = json.load(f)
    else:
        api_performance_config = {
            "enable_compression": True,
            "enable_keep_alive": True,
            "connection_pool_size": 10,
            "max_connections": 100
        }

def save_api_performance_config():
    """Guarda configuración de rendimiento de API"""
    with open(API_PERFORMANCE_CONFIG_FILE, 'w') as f:
        json.dump(api_performance_config, f, indent=4)

def get_api_performance_setting(key):
    """Obtiene configuración de rendimiento de API"""
    return api_performance_config.get(key)

def set_api_performance_setting(key, value):
    """Establece configuración de rendimiento de API"""
    api_performance_config[key] = value
    save_api_performance_config()

def get_all_api_performance_settings():
    """Obtiene todas las configuraciones de rendimiento de API"""
    return api_performance_config.copy()

def reset_api_performance_config():
    """Resetea configuración de rendimiento de API"""
    global api_performance_config
    api_performance_config = {
        "enable_compression": True,
        "enable_keep_alive": True,
        "connection_pool_size": 10,
        "max_connections": 100
    }
    save_api_performance_config()

def is_compression_enabled():
    """Verifica si compresión está habilitada"""
    return api_performance_config.get("enable_compression", True)

def enable_compression():
    """Habilita compresión"""
    api_performance_config["enable_compression"] = True
    save_api_performance_config()

def disable_compression():
    """Deshabilita compresión"""
    api_performance_config["enable_compression"] = False
    save_api_performance_config()

def is_keep_alive_enabled():
    """Verifica si keep-alive está habilitado"""
    return api_performance_config.get("enable_keep_alive", True)

def enable_keep_alive():
    """Habilita keep-alive"""
    api_performance_config["enable_keep_alive"] = True
    save_api_performance_config()

def disable_keep_alive():
    """Deshabilita keep-alive"""
    api_performance_config["enable_keep_alive"] = False
    save_api_performance_config()

def get_connection_pool_size():
    """Obtiene tamaño de pool de conexiones"""
    return api_performance_config.get("connection_pool_size", 10)

def set_connection_pool_size(size):
    """Establece tamaño de pool de conexiones"""
    api_performance_config["connection_pool_size"] = size
    save_api_performance_config()

def get_max_connections():
    """Obtiene máximo de conexiones"""
    return api_performance_config.get("max_connections", 100)

def set_max_connections(max_connections):
    """Establece máximo de conexiones"""
    api_performance_config["max_connections"] = max_connections
    save_api_performance_config()

def export_api_performance_config(filename):
    """Exporta configuración de rendimiento de API"""
    with open(filename, 'w') as f:
        json.dump(api_performance_config, f, indent=4)

def import_api_performance_config(filename):
    """Importa configuración de rendimiento de API"""
    global api_performance_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            api_performance_config = json.load(f)
        save_api_performance_config()
        return True
    return False

def validate_api_performance_config():
    """Valida configuración de rendimiento de API"""
    errors = []
    
    for key in ["connection_pool_size", "max_connections"]:
        if key in api_performance_config:
            if not isinstance(api_performance_config[key], int):
                errors.append(key + " must be integer")
    
    return errors

def backup_api_performance_config():
    """Crea backup de configuración de rendimiento de API"""
    backup_name = "api_performance_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_api_performance_config(backup_name)
    return backup_name

def restore_api_performance_config(backup_name):
    """Restaura configuración de rendimiento de API desde backup"""
    return import_api_performance_config(backup_name)

def get_api_performance_config_summary():
    """Obtiene resumen de configuración de rendimiento de API"""
    return {
        "enable_compression": is_compression_enabled(),
        "enable_keep_alive": is_keep_alive_enabled(),
        "connection_pool_size": get_connection_pool_size()
    }

# Cargar configuración de rendimiento de API al importar
load_api_performance_config()
