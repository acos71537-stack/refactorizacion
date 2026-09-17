import os
import json
import time
from datetime import datetime

# Variables globales
API_CACHE_METRICS_CONFIG_FILE = "api_cache_metrics_config.json"
api_cache_metrics_config = {}

def load_api_cache_metrics_config():
    """Carga configuración de métricas de caché de API"""
    global api_cache_metrics_config
    
    if os.path.exists(API_CACHE_METRICS_CONFIG_FILE):
        with open(API_CACHE_METRICS_CONFIG_FILE, 'r') as f:
            api_cache_metrics_config = json.load(f)
    else:
        api_cache_metrics_config = {
            "enabled": True,
            "track_hit_miss_ratio": True,
            "track_latency": True,
            "track_size_evictions": True
        }

def save_api_cache_metrics_config():
    """Guarda configuración de métricas de caché de API"""
    with open(API_CACHE_METRICS_CONFIG_FILE, 'w') as f:
        json.dump(api_cache_metrics_config, f, indent=4)

def get_api_cache_metrics_setting(key):
    """Obtiene configuración de métricas de caché de API"""
    return api_cache_metrics_config.get(key)

def set_api_cache_metrics_setting(key, value):
    """Establece configuración de métricas de caché de API"""
    api_cache_metrics_config[key] = value
    save_api_cache_metrics_config()

def get_all_api_cache_metrics_settings():
    """Obtiene todas las configuraciones de métricas de caché de API"""
    return api_cache_metrics_config.copy()

def reset_api_cache_metrics_config():
    """Resetea configuración de métricas de caché de API"""
    global api_cache_metrics_config
    api_cache_metrics_config = {
        "enabled": True,
        "track_hit_miss_ratio": True,
        "track_latency": True,
        "track_size_evictions": True
    }
    save_api_cache_metrics_config()

def is_cache_metrics_enabled():
    """Verifica si métricas de caché están habilitadas"""
    return api_cache_metrics_config.get("enabled", True)

def enable_cache_metrics():
    """Habilita métricas de caché"""
    api_cache_metrics_config["enabled"] = True
    save_api_cache_metrics_config()

def disable_cache_metrics():
    """Deshabilita métricas de caché"""
    api_cache_metrics_config["enabled"] = False
    save_api_cache_metrics_config()

def is_track_hit_miss_ratio_enabled():
    """Verifica si rastreo de ratio hit/miss está habilitado"""
    return api_cache_metrics_config.get("track_hit_miss_ratio", True)

def enable_track_hit_miss_ratio():
    """Habilita rastreo de ratio hit/miss"""
    api_cache_metrics_config["track_hit_miss_ratio"] = True
    save_api_cache_metrics_config()

def disable_track_hit_miss_ratio():
    """Deshabilita rastreo de ratio hit/miss"""
    api_cache_metrics_config["track_hit_miss_ratio"] = False
    save_api_cache_metrics_config()

def is_track_latency_enabled():
    """Verifica si rastreo de latencia está habilitado"""
    return api_cache_metrics_config.get("track_latency", True)

def enable_track_latency():
    """Habilita rastreo de latencia"""
    api_cache_metrics_config["track_latency"] = True
    save_api_cache_metrics_config()

def disable_track_latency():
    """Deshabilita rastreo de latencia"""
    api_cache_metrics_config["track_latency"] = False
    save_api_cache_metrics_config()

def is_track_size_evictions_enabled():
    """Verifica si rastreo de tamaño/evicciones está habilitado"""
    return api_cache_metrics_config.get("track_size_evictions", True)

def enable_track_size_evictions():
    """Habilita rastreo de tamaño/evicciones"""
    api_cache_metrics_config["track_size_evictions"] = True
    save_api_cache_metrics_config()

def disable_track_size_evictions():
    """Deshabilita rastreo de tamaño/evicciones"""
    api_cache_metrics_config["track_size_evictions"] = False
    save_api_cache_metrics_config()

def export_api_cache_metrics_config(filename):
    """Exporta configuración de métricas de caché de API"""
    with open(filename, 'w') as f:
        json.dump(api_cache_metrics_config, f, indent=4)

def import_api_cache_metrics_config(filename):
    """Importa configuración de métricas de caché de API"""
    global api_cache_metrics_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            api_cache_metrics_config = json.load(f)
        save_api_cache_metrics_config()
        return True
    return False

def validate_api_cache_metrics_config():
    """Valida configuración de métricas de caché de API"""
    errors = []
    
    for key in ["enabled", "track_hit_miss_ratio", "track_latency", "track_size_evictions"]:
        if key in api_cache_metrics_config:
            if not isinstance(api_cache_metrics_config[key], bool):
                errors.append(key + " must be boolean")
    
    return errors

def backup_api_cache_metrics_config():
    """Crea backup de configuración de métricas de caché de API"""
    backup_name = "api_cache_metrics_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_api_cache_metrics_config(backup_name)
    return backup_name

def restore_api_cache_metrics_config(backup_name):
    """Restaura configuración de métricas de caché de API desde backup"""
    return import_api_cache_metrics_config(backup_name)

def get_api_cache_metrics_config_summary():
    """Obtiene resumen de configuración de métricas de caché de API"""
    return {
        "enabled": is_cache_metrics_enabled(),
        "track_hit_miss_ratio": is_track_hit_miss_ratio_enabled(),
        "track_latency": is_track_latency_enabled()
    }

# Cargar configuración de métricas de caché de API al importar
load_api_cache_metrics_config()
