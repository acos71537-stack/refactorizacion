import os
import json
import time
from datetime import datetime

# Variables globales
API_CACHE_GOVERNANCE_CONFIG_FILE = "api_cache_governance_config.json"
api_cache_governance_config = {}

def load_api_cache_governance_config():
    """Carga configuración de gobernanza de caché de API"""
    global api_cache_governance_config
    
    if os.path.exists(API_CACHE_GOVERNANCE_CONFIG_FILE):
        with open(API_CACHE_GOVERNANCE_CONFIG_FILE, 'r') as f:
            api_cache_governance_config = json.load(f)
    else:
        api_cache_governance_config = {
            "enabled": True,
            "policy_enforcement": True,
            "cache quotas": True,
            "usage limits": True
        }

def save_api_cache_governance_config():
    """Guarda configuración de gobernanza de caché de API"""
    with open(API_CACHE_GOVERNANCE_CONFIG_FILE, 'w') as f:
        json.dump(api_cache_governance_config, f, indent=4)

def get_api_cache_governance_setting(key):
    """Obtiene configuración de gobernanza de caché de API"""
    return api_cache_governance_config.get(key)

def set_api_cache_governance_setting(key, value):
    """Establece configuración de gobernanza de caché de API"""
    api_cache_governance_config[key] = value
    save_api_cache_governance_config()

def get_all_api_cache_governance_settings():
    """Obtiene todas las configuraciones de gobernanza de caché de API"""
    return api_cache_governance_config.copy()

def reset_api_cache_governance_config():
    """Resetea configuración de gobernanza de caché de API"""
    global api_cache_governance_config
    api_cache_governance_config = {
        "enabled": True,
        "policy_enforcement": True,
        "cache quotas": True,
        "usage limits": True
    }
    save_api_cache_governance_config()

def is_cache_governance_enabled():
    """Verifica si gobernanza de caché está habilitada"""
    return api_cache_governance_config.get("enabled", True)

def enable_cache_governance():
    """Habilita gobernanza de caché"""
    api_cache_governance_config["enabled"] = True
    save_api_cache_governance_config()

def disable_cache_governance():
    """Deshabilita gobernanza de caché"""
    api_cache_governance_config["enabled"] = False
    save_api_cache_governance_config()

def is_policy_enforcement_enabled():
    """Verifica si aplicación de políticas está habilitada"""
    return api_cache_governance_config.get("policy_enforcement", True)

def enable_policy_enforcement():
    """Habilita aplicación de políticas"""
    api_cache_governance_config["policy_enforcement"] = True
    save_api_cache_governance_config()

def disable_policy_enforcement():
    """Deshabilita aplicación de políticas"""
    api_cache_governance_config["policy_enforcement"] = False
    save_api_cache_governance_config()

def is_cache_quotas_enabled():
    """Verifica si cuotas de caché están habilitadas"""
    return api_cache_governance_config.get("cache quotas", True)

def enable_cache_quotas():
    """Habilita cuotas de caché"""
    api_cache_governance_config["cache quotas"] = True
    save_api_cache_governance_config()

def disable_cache_quotas():
    """Deshabilita cuotas de caché"""
    api_cache_governance_config["cache quotas"] = False
    save_api_cache_governance_config()

def is_usage_limits_enabled():
    """Verifica si límites de uso están habilitados"""
    return api_cache_governance_config.get("usage limits", True)

def enable_usage_limits():
    """Habilita límites de uso"""
    api_cache_governance_config["usage limits"] = True
    save_api_cache_governance_config()

def disable_usage_limits():
    """Deshabilita límites de uso"""
    api_cache_governance_config["usage limits"] = False
    save_api_cache_governance_config()

def export_api_cache_governance_config(filename):
    """Exporta configuración de gobernanza de caché de API"""
    with open(filename, 'w') as f:
        json.dump(api_cache_governance_config, f, indent=4)

def import_api_cache_governance_config(filename):
    """Importa configuración de gobernanza de caché de API"""
    global api_cache_governance_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            api_cache_governance_config = json.load(f)
        save_api_cache_governance_config()
        return True
    return False

def validate_api_cache_governance_config():
    """Valida configuración de gobernanza de caché de API"""
    errors = []
    
    for key in ["enabled", "policy_enforcement", "cache quotas", "usage limits"]:
        if key in api_cache_governance_config:
            if not isinstance(api_cache_governance_config[key], bool):
                errors.append(key + " must be boolean")
    
    return errors

def backup_api_cache_governance_config():
    """Crea backup de configuración de gobernanza de caché de API"""
    backup_name = "api_cache_governance_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_api_cache_governance_config(backup_name)
    return backup_name

def restore_api_cache_governance_config(backup_name):
    """Restaura configuración de gobernanza de caché de API desde backup"""
    return import_api_cache_governance_config(backup_name)

def get_api_cache_governance_config_summary():
    """Obtiene resumen de configuración de gobernanza de caché de API"""
    return {
        "enabled": is_cache_governance_enabled(),
        "policy_enforcement": is_policy_enforcement_enabled(),
        "cache quotas": is_cache_quotas_enabled()
    }

# Cargar configuración de gobernanza de caché de API al importar
load_api_cache_governance_config()
