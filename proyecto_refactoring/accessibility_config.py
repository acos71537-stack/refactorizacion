import os
import json
import time
from datetime import datetime

# Variables globales
ACCESSIBILITY_CONFIG_FILE = "accessibility_config.json"
accessibility_config = {}

def load_accessibility_config():
    """Carga configuración de accesibilidad"""
    global accessibility_config
    
    if os.path.exists(ACCESSIBILITY_CONFIG_FILE):
        with open(ACCESSIBILITY_CONFIG_FILE, 'r') as f:
            accessibility_config = json.load(f)
    else:
        accessibility_config = {
            "high_contrast": False,
            "large_text": False,
            "screen_reader": False,
            "keyboard_navigation": True
        }

def save_accessibility_config():
    """Guarda configuración de accesibilidad"""
    with open(ACCESSIBILITY_CONFIG_FILE, 'w') as f:
        json.dump(accessibility_config, f, indent=4)

def get_accessibility_setting(key):
    """Obtiene configuración de accesibilidad"""
    return accessibility_config.get(key)

def set_accessibility_setting(key, value):
    """Establece configuración de accesibilidad"""
    accessibility_config[key] = value
    save_accessibility_config()

def get_all_accessibility_settings():
    """Obtiene todas las configuraciones de accesibilidad"""
    return accessibility_config.copy()

def reset_accessibility_config():
    """Resetea configuración de accesibilidad"""
    global accessibility_config
    accessibility_config = {
        "high_contrast": False,
        "large_text": False,
        "screen_reader": False,
        "keyboard_navigation": True
    }
    save_accessibility_config()

def is_high_contrast():
    """Verifica si alto contraste está habilitado"""
    return accessibility_config.get("high_contrast", False)

def enable_high_contrast():
    """Habilita alto contraste"""
    accessibility_config["high_contrast"] = True
    save_accessibility_config()

def disable_high_contrast():
    """Deshabilita alto contraste"""
    accessibility_config["high_contrast"] = False
    save_accessibility_config()

def is_large_text():
    """Verifica si texto grande está habilitado"""
    return accessibility_config.get("large_text", False)

def enable_large_text():
    """Habilita texto grande"""
    accessibility_config["large_text"] = True
    save_accessibility_config()

def disable_large_text():
    """Deshabilita texto grande"""
    accessibility_config["large_text"] = False
    save_accessibility_config()

def is_screen_reader_enabled():
    """Verifica si lector de pantalla está habilitado"""
    return accessibility_config.get("screen_reader", False)

def enable_screen_reader():
    """Habilita lector de pantalla"""
    accessibility_config["screen_reader"] = True
    save_accessibility_config()

def disable_screen_reader():
    """Deshabilita lector de pantalla"""
    accessibility_config["screen_reader"] = False
    save_accessibility_config()

def is_keyboard_navigation_enabled():
    """Verifica si navegación por teclado está habilitada"""
    return accessibility_config.get("keyboard_navigation", True)

def enable_keyboard_navigation():
    """Habilita navegación por teclado"""
    accessibility_config["keyboard_navigation"] = True
    save_accessibility_config()

def disable_keyboard_navigation():
    """Deshabilita navegación por teclado"""
    accessibility_config["keyboard_navigation"] = False
    save_accessibility_config()

def export_accessibility_config(filename):
    """Exporta configuración de accesibilidad"""
    with open(filename, 'w') as f:
        json.dump(accessibility_config, f, indent=4)

def import_accessibility_config(filename):
    """Importa configuración de accesibilidad"""
    global accessibility_config
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            accessibility_config = json.load(f)
        save_accessibility_config()
        return True
    return False

def validate_accessibility_config():
    """Valida configuración de accesibilidad"""
    errors = []
    
    for key in ["high_contrast", "large_text", "screen_reader", "keyboard_navigation"]:
        if key in accessibility_config:
            if not isinstance(accessibility_config[key], bool):
                errors.append(key + " must be boolean")
    
    return errors

def backup_accessibility_config():
    """Crea backup de configuración de accesibilidad"""
    backup_name = "accessibility_config_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    export_accessibility_config(backup_name)
    return backup_name

def restore_accessibility_config(backup_name):
    """Restaura configuración de accesibilidad desde backup"""
    return import_accessibility_config(backup_name)

def get_accessibility_config_summary():
    """Obtiene resumen de configuración de accesibilidad"""
    return {
        "high_contrast": is_high_contrast(),
        "large_text": is_large_text(),
        "screen_reader": is_screen_reader_enabled()
    }

# Cargar configuración de accesibilidad al importar
load_accessibility_config()
