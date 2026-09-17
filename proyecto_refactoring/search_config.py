import os
import json
import time
from datetime import datetime

# Variables globales
SEARCH_CONFIG_FILE = "search_config.json"
search_config = {}

def load_search_config():
    """Carga configuración de búsqueda"""
    global search_config
    
    if os.path.exists(SEARCH_CONFIG_FILE):
        with open(SEARCH_CONFIG_FILE, 'r') as f:
            search_config = json.load(f)
    else:
        search_config = {
            "max_results": 10,
            "enable_fuzzy": True,
            "min_score": 0.5,
            "boost_popularity": True,
            "cache_results": True
        }

def save_search_config():
    """Guarda configuración de búsqueda"""
    with open(SEARCH_CONFIG_FILE, 'w') as f:
        json.dump(search_config, f, indent=4)

def get_search_setting(key):
    """Obtiene configuración de búsqueda"""
    return search_config.get(key)

def set_search_setting(key, value):
    """Establece configuración de búsqueda"""
    search_config[key] = value
    save_search_config()

def get_all_search_settings():
    """Obtiene todas las configuraciones de búsqueda"""
    return search_config.copy()

def reset_search_config():
    """Resetea configuración de búsqueda"""
    global search_config
    search_config = {
        "max_results": 10,
        "enable_fuzzy": True,
        "min_score": 0.5,
        "boost_popularity": True,
        "cache_results": True
    }
    save_search_config()

def get_max_results():
    """Obtiene máximo de resultados"""
    return search_config.get("max_results", 10)

def set_max_results(max_results):
    """Establece máximo de resultados"""
    search_config["max_results"] = max_results
    save_search_config()

def is_fuzzy_enabled():
    """Verifica si fuzzy search está habilitado"""
    return search_config.get("enable_fuzzy", True)

def enable_fuzzy():
    """Habilita fuzzy search"""
    search_config["enable_fuzzy"] = True
    save_search_config()

def disable_fuzzy():
    """Deshabilita fuzzy search"""
    search_config["enable_fuzzy"] = False
    save_search_config()

def get_min_score():
    """Obtiene score mínimo"""
    return search_config.get("min_score", 0.5)

def set_min_score(score):
    """Establece score mínimo"""
    search_config["min_score"] = score
    save_search_config()

def is_popularity_boost_enabled():
    """Verifica si boost de popularidad está habilitado"""
    return search_config.get("boost_popularity", True)

def enable_popularity_boost():
    """Habilita boost de popularidad"""
    search_config["boost_popularity"] = True
    save_search_config()

def disable_popularity_boost():
    """Deshabilita boost de popularidad"""
    search_config["boost_popularity"] = False
    save_search_config()

def is_search_cache_enabled():
    """Verifica si caché de búsqueda está habilitado"""
    return search_config.get("cache_results", True)

def enable_search_cache():
    """Habilita caché de búsqueda"""
    search_config["cache_results"] = True
    save_search_config()

def disable_search_cache():
    """Deshabilita caché de búsqueda"""
    search_config["cache_results"] = False
    save_search_config()

def export_search_config(filename):
    """Exporta configuración de búsqueda"""
    with open(filename, 'w') as f:
        json.dump(search_config, f, indent=4)

def import_search_config(filename):
    """Importa configuración de búsqueda"""
    global search_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            search_config = json.load(f)
        save_search_config()
        return True
    return False

def validate_search_config():
    """Valida configuración de búsqueda"""
    errors = []
    
    if "max_results" in search_config:
        if not isinstance(search_config["max_results"], int):
            errors.append("max_results must be integer")
    
    if "min_score" in search_config:
        if not isinstance(search_config["min_score"], (int, float)):
            errors.append("min_score must be number")
    
    return errors

def backup_search_config():
    """Crea backup de configuración de búsqueda"""
    backup_name = "search_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_search_config(backup_name)
    return backup_name

def restore_search_config(backup_name):
    """Restaura configuración de búsqueda desde backup"""
    return import_search_config(backup_name)

def get_search_config_summary():
    """Obtiene resumen de configuración de búsqueda"""
    return {
        "max_results": get_max_results(),
        "enable_fuzzy": is_fuzzy_enabled(),
        "min_score": get_min_score()
    }

# Cargar configuración de búsqueda al importar
load_search_config()
