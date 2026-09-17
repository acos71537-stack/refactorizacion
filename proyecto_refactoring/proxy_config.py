import os
import json
import time
from datetime import datetime

# Variables globales
PROXY_CONFIG_FILE = "proxy_config.json"
proxy_config = {}

def load_proxy_config():
    """Carga configuración de proxy"""
    global proxy_config
    
    if os.path.exists(PROXY_CONFIG_FILE):
        with open(PROXY_CONFIG_FILE, 'r') as f:
            proxy_config = json.load(f)
    else:
        proxy_config = {
            "enabled": False,
            "host": "",
            "port": 8080,
            "username": "",
            "password": ""
        }

def save_proxy_config():
    """Guarda configuración de proxy"""
    with open(PROXY_CONFIG_FILE, 'w') as f:
        json.dump(proxy_config, f, indent=4)

def get_proxy_setting(key):
    """Obtiene configuración de proxy"""
    return proxy_config.get(key)

def set_proxy_setting(key, value):
    """Establece configuración de proxy"""
    proxy_config[key] = value
    save_proxy_config()

def get_all_proxy_settings():
    """Obtiene todas las configuraciones de proxy"""
    return proxy_config.copy()

def reset_proxy_config():
    """Resetea configuración de proxy"""
    global proxy_config
    proxy_config = {
        "enabled": False,
        "host": "",
        "port": 8080,
        "username": "",
        "password": ""
    }
    save_proxy_config()

def is_proxy_enabled():
    """Verifica si proxy está habilitado"""
    return proxy_config.get("enabled", False)

def enable_proxy():
    """Habilita proxy"""
    proxy_config["enabled"] = True
    save_proxy_config()

def disable_proxy():
    """Deshabilita proxy"""
    proxy_config["enabled"] = False
    save_proxy_config()

def get_proxy_host():
    """Obtiene host de proxy"""
    return proxy_config.get("host", "")

def set_proxy_host(host):
    """Establece host de proxy"""
    proxy_config["host"] = host
    save_proxy_config()

def get_proxy_port():
    """Obtiene puerto de proxy"""
    return proxy_config.get("port", 8080)

def set_proxy_port(port):
    """Establece puerto de proxy"""
    proxy_config["port"] = port
    save_proxy_config()

def get_proxy_username():
    """Obtiene usuario de proxy"""
    return proxy_config.get("username", "")

def set_proxy_username(username):
    """Establece usuario de proxy"""
    proxy_config["username"] = username
    save_proxy_config()

def get_proxy_password():
    """Obtiene contraseña de proxy"""
    return proxy_config.get("password", "")

def set_proxy_password(password):
    """Establece contraseña de proxy"""
    proxy_config["password"] = password
    save_proxy_config()

def export_proxy_config(filename):
    """Exporta configuración de proxy"""
    with open(filename, 'w') as f:
        json.dump(proxy_config, f, indent=4)

def import_proxy_config(filename):
    """Importa configuración de proxy"""
    global proxy_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            proxy_config = json.load(f)
        save_proxy_config()
        return True
    return False

def validate_proxy_config():
    """Valida configuración de proxy"""
    errors = []
    
    if "port" in proxy_config:
        if not isinstance(proxy_config["port"], int):
            errors.append("port must be integer")
    
    return errors

def backup_proxy_config():
    """Crea backup de configuración de proxy"""
    backup_name = "proxy_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_proxy_config(backup_name)
    return backup_name

def restore_proxy_config(backup_name):
    """Restaura configuración de proxy desde backup"""
    return import_proxy_config(backup_name)

def get_proxy_config_summary():
    """Obtiene resumen de configuración de proxy"""
    return {
        "enabled": is_proxy_enabled(),
        "host": get_proxy_host(),
        "port": get_proxy_port()
    }

# Cargar configuración de proxy al importar
load_proxy_config()
