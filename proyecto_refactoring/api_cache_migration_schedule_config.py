import os
import json
import time
from datetime import datetime

# Variables globales
API_CACHE_MIGRATION_SCHEDULE_CONFIG_FILE = "api_cache_migration_schedule_config.json"
api_cache_migration_schedule_config = {}

def load_api_cache_migration_schedule_config():
    """Carga configuración de horario de migración de caché de API"""
    global api_cache_migration_schedule_config
    
    if os.path.exists(API_CACHE_MIGRATION_SCHEDULE_CONFIG_FILE):
        with open(API_CACHE_MIGRATION_SCHEDULE_CONFIG_FILE, 'r') as f:
            api_cache_migration_schedule_config = json.load(f)
    else:
        api_cache_migration_schedule_config = {
            "scheduled_migration": False,
            "migration_window": "maintenance-hours",
            "auto_rollback": True,
            "notification_before_migration": True
        }

def save_api_cache_migration_schedule_config():
    """Guarda configuración de horario de migración de caché de API"""
    with open(API_CACHE_MIGRATION_SCHEDULE_CONFIG_FILE, 'w') as f:
        json.dump(api_cache_migration_schedule_config, f, indent=4)

def get_api_cache_migration_schedule_setting(key):
    """Obtiene configuración de horario de migración de caché de API"""
    return api_cache_migration_schedule_config.get(key)

def set_api_cache_migration_schedule_setting(key, value):
    """Establece configuración de horario de migración de caché de API"""
    api_cache_migration_schedule_config[key] = value
    save_api_cache_migration_schedule_config()

def get_all_api_cache_migration_schedule_settings():
    """Obtiene todas las configuraciones de horario de migración de caché de API"""
    return api_cache_migration_schedule_config.copy()

def reset_api_cache_migration_schedule_config():
    """Resetea configuración de horario de migración de caché de API"""
    global api_cache_migration_schedule_config
    api_cache_migration_schedule_config = {
        "scheduled_migration": False,
        "migration_window": "maintenance-hours",
        "auto_rollback": True,
        "notification_before_migration": True
    }
    save_api_cache_migration_schedule_config()

def is_scheduled_migration_enabled():
    """Verifica si migración programada está habilitada"""
    return api_cache_migration_schedule_config.get("scheduled_migration", False)

def enable_scheduled_migration():
    """Habilita migración programada"""
    api_cache_migration_schedule_config["scheduled_migration"] = True
    save_api_cache_migration_schedule_config()

def disable_scheduled_migration():
    """Deshabilita migración programada"""
    api_cache_migration_schedule_config["scheduled_migration"] = False
    save_api_cache_migration_schedule_config()

def get_migration_window():
    """Obtiene ventana de migración"""
    return api_cache_migration_schedule_config.get("migration_window", "maintenance-hours")

def set_migration_window(window):
    """Establece ventana de migración"""
    api_cache_migration_schedule_config["migration_window"] = window
    save_api_cache_migration_schedule_config()

def is_auto_rollback_enabled():
    """Verifica si auto-rollback está habilitado"""
    return api_cache_migration_schedule_config.get("auto_rollback", True)

def enable_auto_rollback():
    """Habilita auto-rollback"""
    api_cache_migration_schedule_config["auto_rollback"] = True
    save_api_cache_migration_schedule_config()

def disable_auto_rollback():
    """Deshabilita auto-rollback"""
    api_cache_migration_schedule_config["auto_rollback"] = False
    save_api_cache_migration_schedule_config()

def is_notification_before_migration_enabled():
    """Verifica si notificación antes de migración está habilitada"""
    return api_cache_migration_schedule_config.get("notification_before_migration", True)

def enable_notification_before_migration():
    """Habilita notificación antes de migración"""
    api_cache_migration_schedule_config["notification_before_migration"] = True
    save_api_cache_migration_schedule_config()

def disable_notification_before_migration():
    """Deshabilita notificación antes de migración"""
    api_cache_migration_schedule_config["notification_before_migration"] = False
    save_api_cache_migration_schedule_config()

def export_api_cache_migration_schedule_config(filename):
    """Exporta configuración de horario de migración de caché de API"""
    with open(filename, 'w') as f:
        json.dump(api_cache_migration_schedule_config, f, indent=4)

def import_api_cache_migration_schedule_config(filename):
    """Importa configuración de horario de migración de caché de API"""
    global api_cache_migration_schedule_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            api_cache_migration_schedule_config = json.load(f)
        save_api_cache_migration_schedule_config()
        return True
    return False

def validate_api_cache_migration_schedule_config():
    """Valida configuración de horario de migración de caché de API"""
    errors = []
    
    for key in ["scheduled_migration", "auto_rollback", "notification_before_migration"]:
        if key in api_cache_migration_schedule_config:
            if not isinstance(api_cache_migration_schedule_config[key], bool):
                errors.append(key + " must be boolean")
    
    return errors

def backup_api_cache_migration_schedule_config():
    """Crea backup de configuración de horario de migración de caché de API"""
    backup_name = "api_cache_migration_schedule_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_api_cache_migration_schedule_config(backup_name)
    return backup_name

def restore_api_cache_migration_schedule_config(backup_name):
    """Restaura configuración de horario de migración de caché de API desde backup"""
    return import_api_cache_migration_schedule_config(backup_name)

def get_api_cache_migration_schedule_config_summary():
    """Obtiene resumen de configuración de horario de migración de caché de API"""
    return {
        "scheduled_migration": is_scheduled_migration_enabled(),
        "migration_window": get_migration_window(),
        "auto_rollback": is_auto_rollback_enabled()
    }

# Cargar configuración de horario de migración de caché de API al importar
load_api_cache_migration_schedule_config()
