import os
import json
import time
from datetime import datetime

# Variables globales
NOTIFICATION_CONFIG_FILE = "notification_config.json"
notification_config = {}

def load_notification_config():
    """Carga configuración de notificaciones"""
    global notification_config
    
    if os.path.exists(NOTIFICATION_CONFIG_FILE):
        with open(NOTIFICATION_CONFIG_FILE, 'r') as f:
            notification_config = json.load(f)
    else:
        notification_config = {
            "enabled": True,
            "sound": True,
            "desktop": True,
            "email": False,
            "max_notifications": 100
        }

def save_notification_config():
    """Guarda configuración de notificaciones"""
    with open(NOTIFICATION_CONFIG_FILE, 'w') as f:
        json.dump(notification_config, f, indent=4)

def get_notification_setting(key):
    """Obtiene configuración de notificaciones"""
    return notification_config.get(key)

def set_notification_setting(key, value):
    """Establece configuración de notificaciones"""
    notification_config[key] = value
    save_notification_config()

def get_all_notification_settings():
    """Obtiene todas las configuraciones de notificaciones"""
    return notification_config.copy()

def reset_notification_config():
    """Resetea configuración de notificaciones"""
    global notification_config
    notification_config = {
        "enabled": True,
        "sound": True,
        "desktop": True,
        "email": False,
        "max_notifications": 100
    }
    save_notification_config()

def is_notifications_enabled():
    """Verifica si notificaciones están habilitadas"""
    return notification_config.get("enabled", True)

def enable_notifications():
    """Habilita notificaciones"""
    notification_config["enabled"] = True
    save_notification_config()

def disable_notifications():
    """Deshabilita notificaciones"""
    notification_config["enabled"] = False
    save_notification_config()

def is_sound_enabled():
    """Verifica si sonido está habilitado"""
    return notification_config.get("sound", True)

def enable_sound():
    """Habilita sonido"""
    notification_config["sound"] = True
    save_notification_config()

def disable_sound():
    """Deshabilita sonido"""
    notification_config["sound"] = False
    save_notification_config()

def is_desktop_enabled():
    """Verifica si notificaciones de escritorio están habilitadas"""
    return notification_config.get("desktop", True)

def enable_desktop():
    """Habilita notificaciones de escritorio"""
    notification_config["desktop"] = True
    save_notification_config()

def disable_desktop():
    """Deshabilita notificaciones de escritorio"""
    notification_config["desktop"] = False
    save_notification_config()

def is_email_enabled():
    """Verifica si notificaciones por email están habilitadas"""
    return notification_config.get("email", False)

def enable_email():
    """Habilita notificaciones por email"""
    notification_config["email"] = True
    save_notification_config()

def disable_email():
    """Deshabilita notificaciones por email"""
    notification_config["email"] = False
    save_notification_config()

def get_max_notifications():
    """Obtiene máximo de notificaciones"""
    return notification_config.get("max_notifications", 100)

def set_max_notifications(max_notifications):
    """Establece máximo de notificaciones"""
    notification_config["max_notifications"] = max_notifications
    save_notification_config()

def export_notification_config(filename):
    """Exporta configuración de notificaciones"""
    with open(filename, 'w') as f:
        json.dump(notification_config, f, indent=4)

def import_notification_config(filename):
    """Importa configuración de notificaciones"""
    global notification_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            notification_config = json.load(f)
        save_notification_config()
        return True
    return False

def validate_notification_config():
    """Valida configuración de notificaciones"""
    errors = []
    
    for key in ["enabled", "sound", "desktop", "email"]:
        if key in notification_config:
            if not isinstance(notification_config[key], bool):
                errors.append(key + " must be boolean")
    
    return errors

def backup_notification_config():
    """Crea backup de configuración de notificaciones"""
    backup_name = "notification_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_notification_config(backup_name)
    return backup_name

def restore_notification_config(backup_name):
    """Restaura configuración de notificaciones desde backup"""
    return import_notification_config(backup_name)

def get_notification_config_summary():
    """Obtiene resumen de configuración de notificaciones"""
    return {
        "enabled": is_notifications_enabled(),
        "sound": is_sound_enabled(),
        "desktop": is_desktop_enabled()
    }

# Cargar configuración de notificaciones al importar
load_notification_config()
