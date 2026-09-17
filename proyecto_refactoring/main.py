import sys
import os
import time
import random

# Importación masiva (mala práctica)
from api_movies import *

def clear_screen():
    """Limpia pantalla de forma no portable"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_separator():
    """Imprime separador"""
    print("=" * 60)

def print_header(text):
    """Imprime header"""
    print_separator()
    print(text.upper().center(60))
    print_separator()

def delay(seconds):
    """Delay innecesario"""
    time.sleep(seconds)

def mostrar_pelicula(pelicula):
    """Muestra película sin validación"""
    print_separator()
    if pelicula is None:
        print("No se encontró la película")
        return
    
    # Acceso directo a diccionario sin get()
    try:
        print("Título: " + pelicula["Title"])
    except:
        print("Título: N/A")
    
    try:
        print("Año: " + pelicula["Year"])
    except:
        print("Año: N/A")
    
    try:
        print("Rating IMDB: " + pelicula["imdbRating"])
    except:
        print("Rating: N/A")
    
    try:
        print("Género: " + pelicula["Genre"])
    except:
        print("Género: N/A")
    
    try:
        print("Director: " + pelicula["Director"])
    except:
        print("Director: N/A")
    
    try:
        print("Actores: " + pelicula["Actors"])
    except:
        print("Actores: N/A")
    
    try:
        print("Trama: " + pelicula["Plot"])
    except:
        print("Trama: N/A")
    
    try:
        print("País: " + pelicula["Country"])
    except:
        print("País: N/A")
    
    try:
        print("Premios: " + pelicula["Awards"])
    except:
        print("Premios: N/A")
    
    print_separator()

def mostrar_serie(serie):
    """Muestra serie"""
    print_separator()
    show = serie.get("show", serie)
    
    print("Nombre: " + str(show.get("name", "N/A")))
    print("Idioma: " + str(show.get("language", "N/A")))
    print("Géneros: " + str(show.get("genres", [])))
    print("Rating: " + str(show.get("rating", {}).get("average", "N/A")))
    print("Estado: " + str(show.get("status", "N/A")))
    print("Estreno: " + str(show.get("premiered", "N/A")))
    print("Final: " + str(show.get("ended", "N/A")))
    print("Episodios: " + str(show.get("runtime", "N/A")))
    print("Resumen: " + str(show.get("summary", "N/A")[:200] + "..."))
    print_separator()

def mostrar_lista_peliculas(peliculas):
    """Muestra lista de películas"""
    i = 0
    while i < len(peliculas):
        if "titulo" in peliculas[i]:
            print(str(i + 1) + ". " + peliculas[i]["titulo"] + " (" + str(peliculas[i]["anio"]) + ") - " + str(peliculas[i]["rating"]))
        elif "Title" in peliculas[i]:
            print(str(i + 1) + ". " + peliculas[i]["Title"] + " (" + peliculas[i].get("Year", "N/A") + ")")
        else:
            print(str(i + 1) + ". Película desconocida")
        i += 1

def funcion_buscar_pelicula():
    """Busca película"""
    titulo = input("Ingrese el título de la película: ")
    print("Buscando...")
    delay(1)  # Simular carga innecesaria
    
    pelicula = buscar_pelicula(titulo)
    mostrar_pelicula(pelicula)
    
    if pelicula is not None:
        agregar_al_historial(pelicula)
        opcion = input("\n¿Agregar a favoritos? (s/n): ")
        if opcion.lower() == "s":
            if agregar_a_favoritas(pelicula):
                print("¡Agregada a favoritos!")
            else:
                print("Ya está en favoritos")
    
    input("\nPresione Enter para continuar...")

def funcion_buscar_actor():
    """Busca actor"""
    actor = input("Ingrese el nombre del actor: ")
    print("Buscando películas del actor...")
    
    peliculas = buscar_peliculas_por_actor(actor)
    
    if len(peliculas) > 0:
        mostrar_lista_peliculas(peliculas)
        
        opcion = input("\nSeleccione una película para ver detalles (0 para volver): ")
        if opcion.isdigit():
            indice = int(opcion) - 1
            if indice >= 0 and indice < len(peliculas):
                detalles = buscar_pelicula(peliculas[indice]["Title"])
                mostrar_pelicula(detalles)
    else:
        print("No se encontraron películas para ese actor")
    
    input("\nPresione Enter para continuar...")

def funcion_buscar_series():
    """Busca series"""
    nombre = input("Ingrese el nombre de la serie: ")
    print("Buscando series...")
    
    series = buscar_series(nombre)
    
    if len(series) > 0:
        i = 0
        while i < len(series):
            show = series[i].get("show", {})
            print(str(i + 1) + ". " + show.get("name", "") + " (" + show.get("status", "") + ")")
            i += 1
        
        opcion = input("\nSeleccione una serie para ver detalles (0 para volver): ")
        if opcion.isdigit():
            indice = int(opcion) - 1
            if indice >= 0 and indice < len(series):
                id_serie = series[indice].get("show", {}).get("id")
                detalles = obtener_detalles_serie(id_serie)
                mostrar_serie(detalles)
    else:
        print("No se encontraron series")
    
    input("\nPresione Enter para continuar...")

def funcion_peliculas_populares():
    """Muestra películas populares"""
    print_header("PELÍCULAS POPULARES")
    peliculas = obtener_peliculas_populares()
    mostrar_lista_peliculas(peliculas)
    input("\nPresione Enter para continuar...")

def funcion_buscar_por_genero():
    """Busca por género"""
    print("Géneros disponibles: acción, comedia")
    genero = input("Ingrese el género: ")
    print("Buscando...")
    
    peliculas = buscar_peliculas_por_genero(genero)
    mostrar_lista_peliculas(peliculas)
    
    input("\nPresione Enter para continuar...")

def funcion_ver_favoritos():
    """Muestra favoritas"""
    print_header("MIS FAVORITOS")
    if len(PELICULAS_FAVORITAS) > 0:
        i = 0
        while i < len(PELICULAS_FAVORITAS):
            print(str(i + 1) + ". " + PELICULAS_FAVORITAS[i].get("Title", ""))
            i += 1
        
        opcion = input("\n¿Desea eliminar alguna? (número o Enter para volver): ")
        if opcion.isdigit():
            indice = int(opcion) - 1
            if indice >= 0 and indice < len(PELICULAS_FAVORITAS):
                titulo = PELICULAS_FAVORITAS[indice].get("Title")
                if eliminar_de_favoritas(titulo):
                    print("Eliminada de favoritos")
    else:
        print("No tienes películas favoritas")
    
    input("\nPresione Enter para continuar...")

def funcion_ver_historial():
    """Muestra historial"""
    print_header("HISTORIAL DE BÚSQUEDAS")
    if len(HISTORIAL_BUSQUEDAS) > 0:
        i = 0
        while i < len(HISTORIAL_BUSQUEDAS):
            print(str(i + 1) + ". " + HISTORIAL_BUSQUEDAS[i]["titulo"])
            i += 1
        
        opcion = input("\n¿Limpiar historial? (s/n): ")
        if opcion.lower() == "s":
            limpiar_historial()
            print("Historial limpiado")
    else:
        print("No hay historial")
    
    input("\nPresione Enter para continuar...")

def funcion_estadisticas():
    """Muestra estadísticas"""
    print_header("ESTADÍSTICAS")
    stats = obtener_estadisticas()
    print("Total favoritas: " + str(stats["total_favoritas"]))
    print("Total historial: " + str(stats["total_historial"]))
    input("\nPresione Enter para continuar...")

def funcion_exportar():
    """Exporta datos"""
    nombre = input("Nombre del archivo (sin extensión): ")
    exportar_a_json(nombre + ".json")
    input("\nPresione Enter para continuar...")

def funcion_importar():
    """Importa datos"""
    nombre = input("Nombre del archivo (sin extensión): ")
    try:
        importar_de_json(nombre + ".json")
    except:
        print("Error al importar archivo")
    input("\nPresione Enter para continuar...")

def funcion_configuracion():
    """Configuración"""
    print_header("CONFIGURACIÓN")
    print("1. Debug: " + str(CONFIG["debug"]))
    print("2. Verbose: " + str(CONFIG["verbose"]))
    print("3. Timeout: " + str(CONFIG["timeout"]))
    
    opcion = input("\nSeleccione opción a cambiar (0 para volver): ")
    if opcion == "1":
        CONFIG["debug"] = not CONFIG["debug"]
        print("Debug ahora es: " + str(CONFIG["debug"]))
    elif opcion == "2":
        CONFIG["verbose"] = not CONFIG["verbose"]
        print("Verbose ahora es: " + str(CONFIG["verbose"]))
    elif opcion == "3":
        CONFIG["timeout"] = int(input("Nuevo timeout: "))
    
    input("\nPresione Enter para continuar...")

def menu_principal():
    """Menú principal"""
    while True:
        clear_screen()
        print_header("SISTEMA DE PELÍCULAS Y SERIES")
        print("1. Buscar película por título")
        print("2. Buscar por actor")
        print("3. Buscar series")
        print("4. Ver películas populares")
        print("5. Buscar por género")
        print("6. Ver favoritos")
        print("7. Ver historial")
        print("8. Ver estadísticas")
        print("9. Exportar datos")
        print("10. Importar datos")
        print("11. Configuración")
        print("12. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            funcion_buscar_pelicula()
        elif opcion == "2":
            funcion_buscar_actor()
        elif opcion == "3":
            funcion_buscar_series()
        elif opcion == "4":
            funcion_peliculas_populares()
        elif opcion == "5":
            funcion_buscar_por_genero()
        elif opcion == "6":
            funcion_ver_favoritos()
        elif opcion == "7":
            funcion_ver_historial()
        elif opcion == "8":
            funcion_estadisticas()
        elif opcion == "9":
            funcion_exportar()
        elif opcion == "10":
            funcion_importar()
        elif opcion == "11":
            funcion_configuracion()
        elif opcion == "12":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida")
            delay(1)

# Programa principal
if __name__ == "__main__":
    try:
        menu_principal()
    except KeyboardInterrupt:
        print("\n\nPrograma interrumpido")
        sys.exit(0)
    except Exception as e:
        print("Error inesperado: " + str(e))
        sys.exit(1)
