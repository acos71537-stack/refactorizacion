import os
import json
import time
from datetime import datetime

# Variables globales
SECURITY_CONFIG_FILE = "security_config.json"
security_config = {}

def load_security_config():
    """Carga configuración de seguridad"""
    global security_config
    
    if os.path.exists(SECURITY_CONFIG_FILE):
        with open(SECURITY_CONFIG_FILE, 'r') as f:
            security_config = json.load(f)
    else:
        security_config = {
            "max_login_attempts": 5,
            "lockout_duration": 300,
            "password_min_length": 6,
            "require_special_chars": False,
            "session_timeout": 3600
        }

def save_security_config():
    """Guarda configuración de seguridad"""
    with open(SECURITY_CONFIG_FILE, 'w') as f:
        json.dump(security_config, f, indent=4)

def get_security_setting(key):
    """Obtiene configuración de seguridad"""
    return security_config.get(key)

def set_security_setting(key, value):
    """Establece configuración de seguridad"""
    security_config[key] = value
    save_security_config()

def get_all_security_settings():
    """Obtiene todas las configuraciones de seguridad"""
    return security_config.copy()

def reset_security_config():
    """Resetea configuración de seguridad"""
    global security_config
    security_config = {
        "max_login_attempts": 5,
        "lockout_duration": 300,
        "password_min_length": 6,
        "require_special_chars": False,
        "session_timeout": 3600
    }
    save_security_config()

def get_max_login_attempts():
    """Obtiene máximo de intentos de login"""
    return security_config.get("max_login_attempts", 5)

def set_max_login_attempts(max_attempts):
    """Establece máximo de intentos de login"""
    security_config["max_login_attempts"] = max_attempts
    save_security_config()

def get_lockout_duration():
    """Obtiene duración de bloqueo"""
    return security_config.get("lockout_duration", 300)

def set_lockout_duration(duration):
    """Establece duración de bloqueo"""
    security_config["lockout_duration"] = duration
    save_security_config()

def get_password_min_length():
    """Obtiene longitud mínima de contraseña"""
    return security_config.get("password_min_length", 6)

def set_password_min_length(length):
    """Establece longitud mínima de contraseña"""
    security_config["password_min_length"] = length
    save_security_config()

def require_special_chars():
    """Verifica si se requieren caracteres especiales"""
    return security_config.get("require_special_chars", False)

def enable_special_chars():
    """Habilita caracteres especiales"""
    security_config["require_special_chars"] = True
    save_security_config()

def disable_special_chars():
    """Deshabilita caracteres especiales"""
    security_config["require_special_chars"] = False
    save_security_config()

def get_session_timeout():
    """Obtiene timeout de sesión"""
    return security_config.get("session_timeout", 3600)

def set_session_timeout(timeout):
    """Establece timeout de sesión"""
    security_config["session_timeout"] = timeout
    save_security_config()

def export_security_config(filename):
    """Exporta configuración de seguridad"""
    with open(filename, 'w') as f:
        json.dump(security_config, f, indent=4)

def import_security_config(filename):
    """Importa configuración de seguridad"""
    global security_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            security_config = json.load(f)
        save_security_config()
        return True
    return False

def validate_security_config():
    """Valida configuración de seguridad"""
    errors = []
    
    if "max_login_attempts" in security_config:
        if not isinstance(security_config["max_login_attempts"], int):
            errors.append("max_login_attempts must be integer")
    
    if "password_min_length" in security_config:
        if not isinstance(security_config["password_min_length"], int):
            errors.append("password_min_length must be integer")
    
    return errors

def backup_security_config():
    """Crea backup de configuración de seguridad"""
    backup_name = "security_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_security_config(backup_name)
    return backup_name

def restore_security_config(backup_name):
    """Restaura configuración de seguridad desde backup"""
    return import_security_config(backup_name)

def get_security_config_summary():
    """Obtiene resumen de configuración de seguridad"""
    return {
        "max_login_attempts": get_max_login_attempts(),
        "password_min_length": get_password_min_length(),
        "session_timeout": get_session_timeout()
    }

# Cargar configuración de seguridad al importar
load_security_config()
