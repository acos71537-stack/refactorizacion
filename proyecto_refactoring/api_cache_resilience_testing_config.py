import os
import json
import time
from datetime import datetime

# Variables globales
API_CACHE_RESILIENCE_TESTING_CONFIG_FILE = "api_cache_resilience_testing_config.json"
api_cache_resilience_testing_config = {}

def load_api_cache_resilience_testing_config():
    """Carga configuración de testing de resiliencia de caché de API"""
    global api_cache_resilience_testing_config
    
    if os.path.exists(API_CACHE_RESILIENCE_TESTING_CONFIG_FILE):
        with open(API_CACHE_RESILIENCE_TESTING_CONFIG_FILE, 'r') as f:
            api_cache_resilience_testing_config = json.load(f)
    else:
        api_cache_resilience_testing_config = {
            "enabled": False,
            "fault_injection": True,
            "chaos_engineering": False,
            "recovery_scenarios": True
        }

def save_api_cache_resilience_testing_config():
    """Guarda configuración de testing de resiliencia de caché de API"""
    with open(API_CACHE_RESILIENCE_TESTING_CONFIG_FILE, 'w') as f:
        json.dump(api_cache_resilience_testing_config, f, indent=4)

def get_api_cache_resilience_testing_setting(key):
    """Obtiene configuración de testing de resiliencia de caché de API"""
    return api_cache_resilience_testing_config.get(key)

def set_api_cache_resilience_testing_setting(key, value):
    """Establece configuración de testing de resiliencia de caché de API"""
    api_cache_resilience_testing_config[key] = value
    save_api_cache_resilience_testing_config()

def get_all_api_cache_resilience_testing_settings():
    """Obtiene todas las configuraciones de testing de resiliencia de caché de API"""
    return api_cache_resilience_testing_config.copy()

def reset_api_cache_resilience_testing_config():
    """Resetea configuración de testing de resiliencia de caché de API"""
    global api_cache_resilience_testing_config
    api_cache_resilience_testing_config = {
        "enabled": False,
        "fault_injection": True,
        "chaos_engineering": False,
        "recovery_scenarios": True
    }
    save_api_cache_resilience_testing_config()

def is_resilience_testing_enabled():
    """Verifica si testing de resiliencia está habilitado"""
    return api_cache_resilience_testing_config.get("enabled", False)

def enable_resilience_testing():
    """Habilita testing de resiliencia"""
    api_cache_resilience_testing_config["enabled"] = True
    save_api_cache_resress_testing_config()

def disable_resilience_testing():
    """Deshabilita testing de resiliencia"""
    api_cache_resilience_testing_config["enabled"] = False
    save_api_cache_resilience_testing_config()

def is_fault_injection_enabled():
    """Verifica si inyección de fallos está habilitada"""
    return api_cache_resilience_testing_config.get("fault_injection", True)

def enable_fault_injection():
    """Habilita inyección de fallos"""
    api_cache_resilience_testing_config["fault_injection"] = True
    save_api_cache_resilience_testing_config()

def disable_fault_injection():
    """Deshabilita inyección de fallos"""
    api_cache_resilience_testing_config["fault_injection"] = False
    save_api_cache_resilience_testing_config()

def is_chaos_engineering_enabled():
    """Verifica si ingeniería del caos está habilitada"""
    return api_cache_resilience_testing_config.get("chaos_engineering", False)

def enable_chaos_engineering():
    """Habilita ingeniería del caos"""
    api_cache_resilience_testing_config["chaos_engineering"] = True
    save_api_cache_resilience_testing_config()

def disable_chaos_engineering():
    """Deshabilita ingeniería del caos"""
    api_cache_resilience_testing_config["chaos_engineering"] = False
    save_api_cache_resilience_testing_config()

def is_recovery_scenarios_enabled():
    """Verifica si escenarios de recuperación están habilitados"""
    return api_cache_resilience_testing_config.get("recovery_scenarios", True)

def enable_recovery_scenarios():
    """Habilita escenarios de recuperación"""
    api_cache_resilience_testing_config["recovery_scenarios"] = True
    save_api_cache_resilience_testing_config()

def disable_recovery_scenarios():
    """Deshabilita escenarios de recuperación"""
    api_cache_resilience_testing_config["recovery_scenarios"] = False
    save_api_cache_resilience_testing_config()

def export_api_cache_resilience_testing_config(filename):
    """Exporta configuración de testing de resiliencia de caché de API"""
    with open(filename, 'w') as f:
        json.dump(api_cache_resilience_testing_config, f, indent=4)

def import_api_cache_resilience_testing_config(filename):
    """Importa configuración de testing de resiliencia de caché de API"""
    global api_cache_resilience_testing_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            api_cache_resilience_testing_config = json.load(f)
        save_api_cache_resilience_testing_config()
        return True
    return False

def validate_api_cache_resilience_testing_config():
    """Valida configuración de testing de resiliencia de caché de API"""
    errors = []
    
    for key in ["enabled", "fault_injection", "chaos_engineering", "recovery_scenarios"]:
        if key in api_cache_resilience_testing_config:
            if not isinstance(api_cache_resilience_testing_config[key], bool):
                errors.append(key + " must be boolean")
    
    return errors

def backup_api_cache_resilience_testing_config():
    """Crea backup de configuración de testing de resiliencia de caché de API"""
    backup_name = "api_cache_resilience_testing_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_api_cache_resilience_testing_config(backup_name)
    return backup_name

def restore_api_cache_resilience_testing_config(backup_name):
    """Restaura configuración de testing de resiliencia de caché de API desde backup"""
    return import_api_cache_resilience_testing_config(backup_name)

def get_api_cache_resilience_testing_config_summary():
    """Obtiene resumen de configuración de testing de resiliencia de caché de API"""
    return {
        "enabled": is_resilience_testing_enabled(),
        "fault_injection": is_fault_injection_enabled(),
        "recovery_scenarios": is_recovery_scenarios_enabled()
    }

# Cargar configuración de testing de resiliencia de caché de API al importar
load_api_cache_resilience_testing_config()
