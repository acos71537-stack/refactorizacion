import os
import json
import time
from datetime import datetime

# Variables globales
API_CACHE_COMPLIANCE_CONFIG_FILE = "api_cache_compliance_config.json"
api_cache_compliance_config = {}

def load_api_cache_compliance_config():
    """Carga configuración de cumplimiento de caché de API"""
    global api_cache_compliance_config
    
    if os.path.exists(API_CACHE_COMPLIANCE_CONFIG_FILE):
        with open(API_CACHE_COMPLIANCE_CONFIG_FILE, 'r') as f:
            api_cache_compliance_config = json.load(f)
    else:
        api_cache_compliance_config = {
            "gdpr_compliance": True,
            "data_retention_policy": "standard",
            "audit_logging": True,
            "data_anonymization": False
        }

def save_api_cache_compliance_config():
    """Guarda configuración de cumplimiento de caché de API"""
    with open(API_CACHE_COMPLIANCE_CONFIG_FILE, 'w') as f:
        json.dump(api_cache_compliance_config, f, indent=4)

def get_api_cache_compliance_setting(key):
    """Obtiene configuración de cumplimiento de caché de API"""
    return api_cache_compliance_config.get(key)

def set_api_cache_compliance_setting(key, value):
    """Establece configuración de cumplimiento de caché de API"""
    api_cache_compliance_config[key] = value
    save_api_cache_compliance_config()

def get_all_api_cache_compliance_settings():
    """Obtiene todas las configuraciones de cumplimiento de caché de API"""
    return api_cache_compliance_config.copy()

def reset_api_cache_compliance_config():
    """Resetea configuración de cumplimiento de caché de API"""
    global api_cache_compliance_config
    api_cache_compliance_config = {
        "gdpr_compliance": True,
        "data_retention_policy": "standard",
        "audit_logging": True,
        "data_anonymization": False
    }
    save_api_cache_compliance_config()

def is_gdpr_compliance_enabled():
    """Verifica si cumplimiento GDPR está habilitado"""
    return api_cache_compliance_config.get("gdpr_compliance", True)

def enable_gdpr_compliance():
    """Habilita cumplimiento GDPR"""
    api_cache_compliance_config["gdpr_compliance"] = True
    save_api_cache_compliance_config()

def disable_gdpr_compliance():
    """Deshabilita cumplimiento GDPR"""
    api_cache_compliance_config["gdpr_compliance"] = False
    save_api_cache_compliance_config()

def get_data_retention_policy():
    """Obtiene política de retención de datos"""
    return api_cache_compliance_config.get("data_retention_policy", "standard")

def set_data_retention_policy(policy):
    """Establece política de retención de datos"""
    api_cache_compliance_config["data_retention_policy"] = policy
    save_api_cache_compliance_config()

def is_audit_logging_enabled():
    """Verifica si logging de auditoría está habilitado"""
    return api_cache_compliance_config.get("audit_logging", True)

def enable_audit_logging():
    """Habilita logging de auditoría"""
    api_cache_compliance_config["audit_logging"] = True
    save_api_cache_compliance_config()

def disable_audit_logging():
    """Deshabilita logging de auditoría"""
    api_cache_compliance_config["audit_logging"] = False
    save_api_cache_compliance_config()

def is_data_anonymization_enabled():
    """Verifica si anonimización de datos está habilitada"""
    return api_cache_compliance_config.get("data_anonymization", False)

def enable_data_anonymization():
    """Habilita anonimización de datos"""
    api_cache_compliance_config["data_anonymization"] = True
    save_api_cache_compliance_config()

def disable_data_anonymization():
    """Deshabilita anonimización de datos"""
    api_cache_compliance_config["data_anonymization"] = False
    save_api_cache_compliance_config()

def export_api_cache_compliance_config(filename):
    """Exporta configuración de cumplimiento de caché de API"""
    with open(filename, 'w') as f:
        json.dump(api_cache_compliance_config, f, indent=4)

def import_api_cache_compliance_config(filename):
    """Importa configuración de cumplimiento de caché de API"""
    global api_cache_compliance_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            api_cache_compliance_config = json.load(f)
        save_api_cache_compliance_config()
        return True
    return False

def validate_api_cache_compliance_config():
    """Valida configuración de cumplimiento de caché de API"""
    errors = []
    
    for key in ["gdpr_compliance", "audit_logging", "data_anonymization"]:
        if key in api_cache_compliance_config:
            if not isinstance(api_cache_compliance_config[key], bool):
                errors.append(key + " must be boolean")
    
    return errors

def backup_api_cache_compliance_config():
    """Crea backup de configuración de cumplimiento de caché de API"""
    backup_name = "api_cache_compliance_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_api_cache_compliance_config(backup_name)
    return backup_name

def restore_api_cache_compliance_config(backup_name):
    """Restaura configuración de cumplimiento de caché de API desde backup"""
    return import_api_cache_compliance_config(backup_name)

def get_api_cache_compliance_config_summary():
    """Obtiene resumen de configuración de cumplimiento de caché de API"""
    return {
        "gdpr_compliance": is_gdpr_compliance_enabled(),
        "data_retention_policy": get_data_retention_policy(),
        "audit_logging": is_audit_logging_enabled()
    }

# Cargar configuración de cumplimiento de caché de API al importar
load_api_cache_compliance_config()
