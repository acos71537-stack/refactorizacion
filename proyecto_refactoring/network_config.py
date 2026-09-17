import os
import json
import time
from datetime import datetime

# Variables globales
NETWORK_CONFIG_FILE = "network_config.json"
network_config = {}

def load_network_config():
    """Carga configuración de red"""
    global network_config
    
    if os.path.exists(NETWORK_CONFIG_FILE):
        with open(NETWORK_CONFIG_FILE, 'r') as f:
            network_config = json.load(f)
    else:
        network_config = {
            "timeout": 30,
            "max_retries": 3,
            "retry_delay": 1,
            "verify_ssl": True,
            "user_agent": "MovieExplorer/1.0"
        }

def save_network_config():
    """Guarda configuración de red"""
    with open(NETWORK_CONFIG_FILE, 'w') as f:
        json.dump(network_config, f, indent=4)

def get_network_setting(key):
    """Obtiene configuración de red"""
    return network_config.get(key)

def set_network_setting(key, value):
    """Establece configuración de red"""
    network_config[key] = value
    save_network_config()

def get_all_network_settings():
    """Obtiene todas las configuraciones de red"""
    return network_config.copy()

def reset_network_config():
    """Resetea configuración de red"""
    global network_config
    network_config = {
        "timeout": 30,
        "max_retries": 3,
        "retry_delay": 1,
        "verify_ssl": True,
        "user_agent": "MovieExplorer/1.0"
    }
    save_network_config()

def get_timeout():
    """Obtiene timeout"""
    return network_config.get("timeout", 30)

def set_timeout(timeout):
    """Establece timeout"""
    network_config["timeout"] = timeout
    save_network_config()

def get_max_retries():
    """Obtiene máximo de reintentos"""
    return network_config.get("max_retries", 3)

def set_max_retries(max_retries):
    """Establece máximo de reintentos"""
    network_config["max_retries"] = max_retries
    save_network_config()

def get_retry_delay():
    """Obtiene delay de reintentos"""
    return network_config.get("retry_delay", 1)

def set_retry_delay(delay):
    """Establece delay de reintentos"""
    network_config["retry_delay"] = delay
    save_network_config()

def is_ssl_verification_enabled():
    """Verifica si verificación SSL está habilitada"""
    return network_config.get("verify_ssl", True)

def enable_ssl_verification():
    """Habilita verificación SSL"""
    network_config["verify_ssl"] = True
    save_network_config()

def disable_ssl_verification():
    """Deshabilita verificación SSL"""
    network_config["verify_ssl"] = False
    save_network_config()

def get_user_agent():
    """Obtiene user agent"""
    return network_config.get("user_agent", "MovieExplorer/1.0")

def set_user_agent(user_agent):
    """Establece user agent"""
    network_config["user_agent"] = user_agent
    save_network_config()

def export_network_config(filename):
    """Exporta configuración de red"""
    with open(filename, 'w') as f:
        json.dump(network_config, f, indent=4)

def import_network_config(filename):
    """Importa configuración de red"""
    global network_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            network_config = json.load(f)
        save_network_config()
        return True
    return False

def validate_network_config():
    """Valida configuración de red"""
    errors = []
    
    if "timeout" in network_config:
        if not isinstance(network_config["timeout"], int):
            errors.append("timeout must be integer")
    
    if "max_retries" in network_config:
        if not isinstance(network_config["max_retries"], int):
            errors.append("max_retries must be integer")
    
    return errors

def backup_network_config():
    """Crea backup de configuración de red"""
    backup_name = "network_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_network_config(backup_name)
    return backup_name

def restore_network_config(backup_name):
    """Restaura configuración de red desde backup"""
    return import_network_config(backup_name)

def get_network_config_summary():
    """Obtiene resumen de configuración de red"""
    return {
        "timeout": get_timeout(),
        "max_retries": get_max_retries(),
        "verify_ssl": is_ssl_verification_enabled()
    }

# Cargar configuración de red al importar
load_network_config()
