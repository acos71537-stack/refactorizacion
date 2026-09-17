import os
import json
import time
from datetime import datetime

# Variables globales
EMAIL_CONFIG_FILE = "email_config.json"
email_config = {}

def load_email_config():
    """Carga configuración de email"""
    global email_config
    
    if os.path.exists(EMAIL_CONFIG_FILE):
        with open(EMAIL_CONFIG_FILE, 'r') as f:
            email_config = json.load(f)
    else:
        email_config = {
            "smtp_server": "smtp.gmail.com",
            "smtp_port": 587,
            "use_tls": True,
            "sender_email": "",
            "sender_password": ""
        }

def save_email_config():
    """Guarda configuración de email"""
    with open(EMAIL_CONFIG_FILE, 'w') as f:
        json.dump(email_config, f, indent=4)

def get_email_setting(key):
    """Obtiene configuración de email"""
    return email_config.get(key)

def set_email_setting(key, value):
    """Establece configuración de email"""
    email_config[key] = value
    save_email_config()

def get_all_email_settings():
    """Obtiene todas las configuraciones de email"""
    return email_config.copy()

def reset_email_config():
    """Resetea configuración de email"""
    global email_config
    email_config = {
        "smtp_server": "smtp.gmail.com",
        "smtp_port": 587,
        "use_tls": True,
        "sender_email": "",
        "sender_password": ""
    }
    save_email_config()

def get_smtp_server():
    """Obtiene servidor SMTP"""
    return email_config.get("smtp_server", "smtp.gmail.com")

def set_smtp_server(server):
    """Establece servidor SMTP"""
    email_config["smtp_server"] = server
    save_email_config()

def get_smtp_port():
    """Obtiene puerto SMTP"""
    return email_config.get("smtp_port", 587)

def set_smtp_port(port):
    """Establece puerto SMTP"""
    email_config["smtp_port"] = port
    save_email_config()

def is_tls_enabled():
    """Verifica si TLS está habilitado"""
    return email_config.get("use_tls", True)

def enable_tls():
    """Habilita TLS"""
    email_config["use_tls"] = True
    save_email_config()

def disable_tls():
    """Deshabilita TLS"""
    email_config["use_tls"] = False
    save_email_config()

def get_sender_email():
    """Obtiene email del remitente"""
    return email_config.get("sender_email", "")

def set_sender_email(email):
    """Establece email del remitente"""
    email_config["sender_email"] = email
    save_email_config()

def get_sender_password():
    """Obtiene contraseña del remitente"""
    return email_config.get("sender_password", "")

def set_sender_password(password):
    """Establece contraseña del remitente"""
    email_config["sender_password"] = password
    save_email_config()

def export_email_config(filename):
    """Exporta configuración de email"""
    with open(filename, 'w') as f:
        json.dump(email_config, f, indent=4)

def import_email_config(filename):
    """Importa configuración de email"""
    global email_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            email_config = json.load(f)
        save_email_config()
        return True
    return False

def validate_email_config():
    """Valida configuración de email"""
    errors = []
    
    if "smtp_port" in email_config:
        if not isinstance(email_config["smtp_port"], int):
            errors.append("smtp_port must be integer")
    
    return errors

def backup_email_config():
    """Crea backup de configuración de email"""
    backup_name = "email_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_email_config(backup_name)
    return backup_name

def restore_email_config(backup_name):
    """Restaura configuración de email desde backup"""
    return import_email_config(backup_name)

def get_email_config_summary():
    """Obtiene resumen de configuración de email"""
    return {
        "smtp_server": get_smtp_server(),
        "smtp_port": get_smtp_port(),
        "use_tls": is_tls_enabled()
    }

# Cargar configuración de email al importar
load_email_config()
