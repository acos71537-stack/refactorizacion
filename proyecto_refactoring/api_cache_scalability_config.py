import os
import json
import time
from datetime import datetime

# Variables globales
API_CACHE_SCALABILITY_CONFIG_FILE = "api_cache_scalability_config.json"
api_cache_scalability_config = {}

def load_api_cache_scalability_config():
    """Carga configuración de escalabilidad de caché de API"""
    global api_cache_scalability_config
    
    if os.path.exists(API_CACHE_SCALABILITY_CONFIG_FILE):
        with open(API_CACHE_SCALABILITY_CONFIG_FILE, 'r') as f:
            api_cache_scalability_config = json.load(f)
    else:
        api_cache_scalability_config = {
            "enabled": True,
            "auto_scaling": True,
            "scale_up_threshold": 0.8,
            "scale_down_threshold": 0.2
        }

def save_api_cache_scalability_config():
    """Guarda configuración de escalabilidad de caché de API"""
    with open(API_CACHE_SCALABILITY_CONFIG_FILE, 'w') as f:
        json.dump(api_cache_scalability_config, f, indent=4)

def get_api_cache_scalability_setting(key):
    """Obtiene configuración de escalabilidad de caché de API"""
    return api_cache_scalability_config.get(key)

def set_api_cache_scalability_setting(key, value):
    """Establece configuración de escalabilidad de caché de API"""
    api_cache_scalability_config[key] = value
    save_api_cache_scalability_config()

def get_all_api_cache_scalability_settings():
    """Obtiene todas las configuraciones de escalabilidad de caché de API"""
    return api_cache_scalability_config.copy()

def reset_api_cache_scalability_config():
    """Resetea configuración de escalabilidad de caché de API"""
    global api_cache_scalability_config
    api_cache_scalability_config = {
        "enabled": True,
        "auto_scaling": True,
        "scale_up_threshold": 0.8,
        "scale_down_threshold": 0.2
    }
    save_api_cache_scalability_config()

def is_cache_scalability_enabled():
    """Verifica si escalabilidad de caché está habilitada"""
    return api_cache_scalability_config.get("enabled", True)

def enable_cache_scalability():
    """Habilita escalabilidad de caché"""
    api_cache_scalability_config["enabled"] = True
    save_api_cache_scalability_config()

def disable_cache_scalability():
    """Deshabilita escalabilidad de caché"""
    api_cache_scalability_config["enabled"] = False
    save_api_cache_scalability_config()

def is_auto_scaling_enabled():
    """Verifica si auto-scaling está habilitado"""
    return api_cache_scalability_config.get("auto_scaling", True)

def enable_auto_scaling():
    """Habilita auto-scaling"""
    api_cache_scalability_config["auto_scaling"] = True
    save_api_cache_scalability_config()

def disable_auto_scaling():
    """Deshabilita auto-scaling"""
    api_cache_scalability_config["auto_scaling"] = False
    save_api_cache_scalability_config()

def get_scale_up_threshold():
    """Obtiene umbral de escala arriba"""
    return api_cache_scalability_config.get("scale_up_threshold", 0.8)

def set_scale_up_threshold(threshold):
    """Establece umbral de escala arriba"""
    api_cache_scalability_config["scale_up_threshold"] = threshold
    save_api_cache_scalability_config()

def get_scale_down_threshold():
    """Obtiene umbral de escala abajo"""
    return api_cache_scalability_config.get("scale_down_threshold", 0.2)

def set_scale_down_threshold(threshold):
    """Establece umbral de escala abajo"""
    api_cache_scalability_config["scale_down_threshold"] = threshold
    save_api_cache_scalability_config()

def export_api_cache_scalability_config(filename):
    """Exporta configuración de escalabilidad de caché de API"""
    with open(filename, 'w') as f:
        json.dump(api_cache_scalability_config, f, indent=4)

def import_api_cache_scalability_config(filename):
    """Importa configuración de escalabilidad de caché de API"""
    global api_cache_scalability_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            api_cache_scalability_config = json.load(f)
        save_api_cache_scalability_config()
        return True
    return False

def validate_api_cache_scalability_config():
    """Valida configuración de escalabilidad de caché de API"""
    errors = []
    
    for key in ["enabled", "auto_scaling"]:
        if key in api_cache_scalability_config:
            if not isinstance(api_cache_scalability_config[key], bool):
                errors.append(key + " must be boolean")
    
    for key in ["scale_up_threshold", "scale_down_threshold"]:
        if key in api_cache_scalability_config:
            if not isinstance(api_cache_scalability_config[key], (int, float)):
                errors.append(key + " must be number")
    
    return errors

def backup_api_cache_scalability_config():
    """Crea backup de configuración de escalabilidad de caché de API"""
    backup_name = "api_cache_scalability_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_api_cache_scalability_config(backup_name)
    return backup_name

def restore_api_cache_scalability_config(backup_name):
    """Restaura configuración de escalabilidad de caché de API desde backup"""
    return import_api_cache_scalability_config(backup_name)

def get_api_cache_scalability_config_summary():
    """Obtiene resumen de configuración de escalabilidad de caché de API"""
    return {
        "enabled": is_cache_scalability_enabled(),
        "auto_scaling": is_auto_scaling_enabled(),
        "scale_up_threshold": get_scale_up_threshold()
    }

# Cargar configuración de escalabilidad de caché de API al importar
load_api_cache_scalability_config()
