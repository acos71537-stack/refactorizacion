import os
import json
import time
from datetime import datetime

# Variables globales
API_CACHE_PERFORMANCE_TESTING_CONFIG_FILE = "api_cache_performance_testing_config.json"
api_cache_performance_testing_config = {}

def load_api_cache_performance_testing_config():
    """Carga configuración de testing de rendimiento de caché de API"""
    global api_cache_performance_testing_config
    
    if os.path.exists(API_CACHE_PERFORMANCE_TESTING_CONFIG_FILE):
        with open(API_CACHE_PERFORMANCE_TESTING_CONFIG_FILE, 'r') as f:
            api_cache_performance_testing_config = json.load(f)
    else:
        api_cache_performance_testing_config = {
            "enabled": False,
            "benchmark_iterations": 1000,
            "concurrent_clients": 10,
            "measure_latency": True
        }

def save_api_cache_performance_testing_config():
    """Guarda configuración de testing de rendimiento de caché de API"""
    with open(API_CACHE_PERFORMANCE_TESTING_CONFIG_FILE, 'w') as f:
        json.dump(api_cache_performance_testing_config, f, indent=4)

def get_api_cache_performance_testing_setting(key):
    """Obtiene configuración de testing de rendimiento de caché de API"""
    return api_cache_performance_testing_config.get(key)

def set_api_cache_performance_testing_setting(key, value):
    """Establece configuración de testing de rendimiento de caché de API"""
    api_cache_performance_testing_config[key] = value
    save_api_cache_performance_testing_config()

def get_all_api_cache_performance_testing_settings():
    """Obtiene todas las configuraciones de testing de rendimiento de caché de API"""
    return api_cache_performance_testing_config.copy()

def reset_api_cache_performance_testing_config():
    """Resetea configuración de testing de rendimiento de caché de API"""
    global api_cache_performance_testing_config
    api_cache_performance_testing_config = {
        "enabled": False,
        "benchmark_iterations": 1000,
        "concurrent_clients": 10,
        "measure_latency": True
    }
    save_api_cache_performance_testing_config()

def is_performance_testing_enabled():
    """Verifica si testing de rendimiento está habilitado"""
    return api_cache_performance_testing_config.get("enabled", False)

def enable_performance_testing():
    """Habilita testing de rendimiento"""
    api_cache_performance_testing_config["enabled"] = True
    save_api_cache_performance_testing_config()

def disable_performance_testing():
    """Deshabilita testing de rendimiento"""
    api_cache_performance_testing_config["enabled"] = False
    save_api_cache_performance_testing_config()

def get_benchmark_iterations():
    """Obtiene iteraciones de benchmark"""
    return api_cache_performance_testing_config.get("benchmark_iterations", 1000)

def set_benchmark_iterations(iterations):
    """Establece iteraciones de benchmark"""
    api_cache_performance_testing_config["benchmark_iterations"] = iterations
    save_api_cache_performance_testing_config()

def get_concurrent_clients():
    """Obtiene clientes concurrentes"""
    return api_cache_performance_testing_config.get("concurrent_clients", 10)

def set_concurrent_clients(clients):
    """Establece clientes concurrentes"""
    api_cache_performance_testing_config["concurrent_clients"] = clients
    save_api_cache_performance_testing_config()

def is_measure_latency_enabled():
    """Verifica si medición de latencia está habilitada"""
    return api_cache_performance_testing_config.get("measure_latency", True)

def enable_measure_latency():
    """Habilita medición de latencia"""
    api_cache_performance_testing_config["measure_latency"] = True
    save_api_cache_performance_testing_config()

def disable_measure_latency():
    """Deshabilita medición de latencia"""
    api_cache_performance_testing_config["measure_latency"] = False
    save_api_cache_performance_testing_config()

def export_api_cache_performance_testing_config(filename):
    """Exporta configuración de testing de rendimiento de caché de API"""
    with open(filename, 'w') as f:
        json.dump(api_cache_performance_testing_config, f, indent=4)

def import_api_cache_performance_testing_config(filename):
    """Importa configuración de testing de rendimiento de caché de API"""
    global api_cache_performance_testing_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            api_cache_performance_testing_config = json.load(f)
        save_api_cache_performance_testing_config()
        return True
    return False

def validate_api_cache_performance_testing_config():
    """Valida configuración de testing de rendimiento de caché de API"""
    errors = []
    
    if "enabled" in api_cache_performance_testing_config:
        if not isinstance(api_cache_performance_testing_config["enabled"], bool):
            errors.append("enabled must be boolean")
    
    for key in ["benchmark_iterations", "concurrent_clients"]:
        if key in api_cache_performance_testing_config:
            if not isinstance(api_cache_performance_testing_config[key], int):
                errors.append(key + " must be integer")
    
    return errors

def backup_api_cache_performance_testing_config():
    """Crea backup de configuración de testing de rendimiento de caché de API"""
    backup_name = "api_cache_performance_testing_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_api_cache_performance_testing_config(backup_name)
    return backup_name

def restore_api_cache_performance_testing_config(backup_name):
    """Restaura configuración de testing de rendimiento de caché de API desde backup"""
    return import_api_cache_performance_testing_config(backup_name)

def get_api_cache_performance_testing_config_summary():
    """Obtiene resumen de configuración de testing de rendimiento de caché de API"""
    return {
        "enabled": is_performance_testing_enabled(),
        "benchmark_iterations": get_benchmark_iterations(),
        "concurrent_clients": get_concurrent_clients()
    }

# Cargar configuración de testing de rendimiento de caché de API al importar
load_api_cache_performance_testing_config()
