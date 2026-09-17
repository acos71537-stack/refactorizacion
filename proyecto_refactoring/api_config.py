import os
import json
import time
from datetime import datetime

# Variables globales
API_CONFIG_FILE = "api_config.json"
api_config = {}

def load_api_config():
    """Carga configuración de API"""
    global api_config
    
    if os.path.exists(API_CONFIG_FILE):
        with open(API_CONFIG_FILE, 'r') as f:
            api_config = json.load(f)
    else:
        api_config = {
            "omdb": {
                "url": "http://www.omdbapi.com/",
                "key": "trilogy",
                "timeout": 30
            },
            "tvmaze": {
                "url": "http://api.tvmaze.com",
                "timeout": 30
            }
        }

def save_api_config():
    """Guarda configuración de API"""
    with open(API_CONFIG_FILE, 'w') as f:
        json.dump(api_config, f, indent=4)

def get_api_config(api_name):
    """Obtiene configuración de una API"""
    return api_config.get(api_name)

def set_api_config(api_name, config):
    """Establece configuración de una API"""
    api_config[api_name] = config
    save_api_config()

def get_all_api_configs():
    """Obtiene todas las configuraciones de API"""
    return api_config.copy()

def get_api_url(api_name):
    """Obtiene URL de una API"""
    return api_config.get(api_name, {}).get("url")

def set_api_url(api_name, url):
    """Establece URL de una API"""
    if api_name not in api_config:
        api_config[api_name] = {}
    api_config[api_name]["url"] = url
    save_api_config()

def get_api_key(api_name):
    """Obtiene clave de una API"""
    return api_config.get(api_name, {}).get("key")

def set_api_key(api_name, key):
    """Establece clave de una API"""
    if api_name not in api_config:
        api_config[api_name] = {}
    api_config[api_name]["key"] = key
    save_api_config()

def get_api_timeout(api_name):
    """Obtiene timeout de una API"""
    return api_config.get(api_name, {}).get("timeout", 30)

def set_api_timeout(api_name, timeout):
    """Establece timeout de una API"""
    if api_name not in api_config:
        api_config[api_name] = {}
    api_config[api_name]["timeout"] = timeout
    save_api_config()

def add_api(api_name, config):
    """Agrega una API"""
    api_config[api_name] = config
    save_api_config()

def remove_api(api_name):
    """Elimina una API"""
    if api_name in api_config:
        del api_config[api_name]
        save_api_config()
        return True
    return False

def search_apis(query):
    """Busca APIs"""
    results = {}
    query_lower = query.lower()
    
    for api_name, config in api_config.items():
        if query_lower in api_name.lower():
            results[api_name] = config
    
    return results

def clear_api_configs():
    """Limpia configuraciones de API"""
    global api_config
    api_config = {}
    save_api_config()

def get_api_stats():
    """Obtiene estadísticas de APIs"""
    stats = {
        "total": len(api_config),
        "with_key": 0,
        "without_key": 0
    }
    
    for config in api_config.values():
        if config.get("key"):
            stats["with_key"] += 1
        else:
            stats["without_key"] += 1
    
    return stats

def export_api_config(filename):
    """Exporta configuración de API"""
    with open(filename, 'w') as f:
        json.dump(api_config, f, indent=4)

def import_api_config(filename):
    """Importa configuración de API"""
    global api_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            api_config = json.load(f)
        save_api_config()
        return True
    return False

def validate_api_config():
    """Valida configuración de API"""
    errors = []
    
    for api_name, config in api_config.items():
        if "url" not in config:
            errors.append("API " + api_name + " missing url")
    
    return errors

def backup_api_config():
    """Crea backup de configuración de API"""
    backup_name = "api_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_api_config(backup_name)
    return backup_name

def restore_api_config(backup_name):
    """Restaura configuración de API desde backup"""
    return import_api_config(backup_name)

def get_api_config_summary():
    """Obtiene resumen de configuración de API"""
    return {
        "total": len(api_config),
        "apis": list(api_config.keys())
    }

# Cargar configuración de API al importar
load_api_config()
