import os
import json
import time
from datetime import datetime

# Variables globales
API_CACHE_MENTORING_CONFIG_FILE = "api_cache_mentoring_config.json"
api_cache_mentoring_config = {}

def load_api_cache_mentoring_config():
    """Carga configuración de mentoring de caché de API"""
    global api_cache_mentoring_config
    
    if os.path.exists(API_CACHE_MENTORING_CONFIG_FILE):
        with open(API_CACHE_MENTORING_CONFIG_FILE, 'r') as f:
            api_cache_mentoring_config = json.load(f)
    else:
        api_cache_mentoring_config = {
            "enabled": True,
            "peer_review": True,
            "code_review": True,
            "best_practices_sharing": True
        }

def save_api_cache_mentoring_config():
    """Guarda configuración de mentoring de caché de API"""
    with open(API_CACHE_MENTORING_CONFIG_FILE, 'w') as f:
        json.dump(api_cache_mentoring_config, f, indent=4)

def get_api_cache_mentoring_setting(key):
    """Obtiene configuración de mentoring de caché de API"""
    return api_cache_mentoring_config.get(key)

def set_api_cache_mentoring_setting(key, value):
    """Establece configuración de mentoring de caché de API"""
    api_cache_mentoring_config[key] = value
    save_api_cache_mentoring_config()

def get_all_api_cache_mentoring_settings():
    """Obtiene todas las configuraciones de mentoring de caché de API"""
    return api_cache_mentoring_config.copy()

def reset_api_cache_mentoring_config():
    """Resetea configuración de mentoring de caché de API"""
    global api_cache_mentoring_config
    api_cache_mentoring_config = {
        "enabled": True,
        "peer_review": True,
        "code_review": True,
        "best_practices_sharing": True
    }
    save_api_cache_mentoring_config()

def is_cache_mentoring_enabled():
    """Verifica si mentoring de caché está habilitado"""
    return api_cache_mentoring_config.get("enabled", True)

def enable_cache_mentoring():
    """Habilita mentoring de caché"""
    api_cache_mentoring_config["enabled"] = True
    save_api_cache_mentoring_config()

def disable_cache_mentoring():
    """Deshabilita mentoring de caché"""
    api_cache_mentoring_config["enabled"] = False
    save_api_cache_mentoring_config()

def is_peer_review_enabled():
    """Verifica si revisión entre pares está habilitada"""
    return api_cache_mentoring_config.get("peer_review", True)

def enable_peer_review():
    """Habilita revisión entre pares"""
    api_cache_mentoring_config["peer_review"] = True
    save_api_cache_mentoring_config()

def disable_peer_review():
    """Deshabilita revisión entre pares"""
    api_cache_mentoring_config["peer_review"] = False
    save_api_cache_mentoring_config()

def is_code_review_enabled():
    """Verifica si revisión de código está habilitada"""
    return api_cache_mentoring_config.get("code_review", True)

def enable_code_review():
    """Habilita revisión de código"""
    api_cache_mentoring_config["code_review"] = True
    save_api_cache_mentoring_config()

def disable_code_review():
    """Deshabilita revisión de código"""
    api_cache_mentoring_config["code_review"] = False
    save_api_cache_mentoring_config()

def is_best_practices_sharing_enabled():
    """Verifica si compartir mejores prácticas está habilitado"""
    return api_cache_mentoring_config.get("best_practices_sharing", True)

def enable_best_practices_sharing():
    """Habilita compartir mejores prácticas"""
    api_cache_mentoring_config["best_practices_sharing"] = True
    save_api_cache_mentoring_config()

def disable_best_practices_sharing():
    """Deshabilita compartir mejores prácticas"""
    api_cache_mentoring_config["best_practices_sharing"] = False
    save_api_cache_mentoring_config()

def export_api_cache_mentoring_config(filename):
    """Exporta configuración de mentoring de caché de API"""
    with open(filename, 'w') as f:
        json.dump(api_cache_mentoring_config, f, indent=4)

def import_api_cache_mentoring_config(filename):
    """Importa configuración de mentoring de caché de API"""
    global api_cache_mentoring_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            api_cache_mentoring_config = json.load(f)
        save_api_cache_mentoring_config()
        return True
    return False

def validate_api_cache_mentoring_config():
    """Valida configuración de mentoring de caché de API"""
    errors = []
    
    for key in ["enabled", "peer_review", "code_review", "best_practices_sharing"]:
        if key in api_cache_mentoring_config:
            if not isinstance(api_cache_mentoring_config[key], bool):
                errors.append(key + " must be boolean")
    
    return errors

def backup_api_cache_mentoring_config():
    """Crea backup de configuración de mentoring de caché de API"""
    backup_name = "api_cache_mentoring_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_api_cache_mentoring_config(backup_name)
    return backup_name

def restore_api_cache_mentoring_config(backup_name):
    """Restaura configuración de mentoring de caché de API desde backup"""
    return import_api_cache_mentoring_config(backup_name)

def get_api_cache_mentoring_config_summary():
    """Obtiene resumen de configuración de mentoring de caché de API"""
    return {
        "enabled": is_cache_mentoring_enabled(),
        "peer_review": is_peer_review_enabled(),
        "code_review": is_code_review_enabled()
    }

# Cargar configuración de mentoring de caché de API al importar
load_api_cache_mentoring_config()
