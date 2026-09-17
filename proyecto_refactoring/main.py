import os
import sys
import time
from typing import Any

import api_movies as api


def clear_screen() -> None:
    """Limpia pantalla de forma no portable"""
    os.system("cls" if os.name == "nt" else "clear")


def print_separator() -> None:
    """Imprime separador"""
    print("=" * 60)


def print_header(text: str) -> None:
    """Imprime header"""
    print_separator()
    print(text.upper().center(60))
    print_separator()


def delay(seconds: float) -> None:
    """Delay innecesario"""
    time.sleep(seconds)


def mostrar_pelicula(pelicula: dict[str, Any] | None) -> None:
    """Muestra película sin validación"""
    print_separator()
    if pelicula is None:
        print("No se encontró la película")
        return

    # Acceso directo a diccionario sin get()
    try:
        print(f"Título: {pelicula['Title']}")
    except:
        print("Título: N/A")

    try:
        print(f"Año: {pelicula['Year']}")
    except:
        print("Año: N/A")

    try:
        print(f"Rating IMDB: {pelicula['imdbRating']}")
    except:
        print("Rating: N/A")

    try:
        print(f"Género: {pelicula['Genre']}")
    except:
        print("Género: N/A")

    try:
        print(f"Director: {pelicula['Director']}")
    except:
        print("Director: N/A")

    try:
        print(f"Actores: {pelicula['Actors']}")
    except:
        print("Actores: N/A")

    try:
        print(f"Trama: {pelicula['Plot']}")
    except:
        print("Trama: N/A")

    try:
        print(f"País: {pelicula['Country']}")
    except:
        print("País: N/A")

    try:
        print(f"Premios: {pelicula['Awards']}")
    except:
        print("Premios: N/A")

    print_separator()


def mostrar_serie(serie: dict[str, Any]) -> None:
    """Muestra serie"""
    print_separator()
    show = serie.get("show", serie)

    print(f"Nombre: {show.get('name', 'N/A')}")
    print(f"Idioma: {show.get('language', 'N/A')}")
    print(f"Géneros: {show.get('genres', [])}")
    print(f"Rating: {show.get('rating', {}).get('average', 'N/A')}")
    print(f"Estado: {show.get('status', 'N/A')}")
    print(f"Estreno: {show.get('premiered', 'N/A')}")
    print(f"Final: {show.get('ended', 'N/A')}")
    print(f"Episodios: {show.get('runtime', 'N/A')}")
    print(f"Resumen: {str(show.get('summary', 'N/A'))[:200]}...")
    print_separator()


def mostrar_lista_peliculas(peliculas: list[dict[str, Any]]) -> None:
    """Muestra lista de películas"""
    i = 0
    while i < len(peliculas):
        if "titulo" in peliculas[i]:
            print(
                f"{i + 1}. {peliculas[i]['titulo']} ({peliculas[i]['anio']}) - {peliculas[i]['rating']}"
            )
        elif "Title" in peliculas[i]:
            print(f"{i + 1}. {peliculas[i]['Title']} ({peliculas[i].get('Year', 'N/A')})")
        else:
            print(f"{i + 1}. Película desconocida")
        i += 1


def funcion_buscar_pelicula() -> None:
    """Busca película"""
    titulo = input("Ingrese el título de la película: ")
    print("Buscando...")
    delay(1)  # Simular carga innecesaria

    pelicula = api.buscar_pelicula(titulo)
    mostrar_pelicula(pelicula)

    if pelicula is not None:
        api.agregar_al_historial(pelicula)
        opcion = input("\n¿Agregar a favoritos? (s/n): ")
        if opcion.lower() == "s":
            if api.agregar_a_favoritas(pelicula):
                print("¡Agregada a favoritos!")
            else:
                print("Ya está en favoritos")

    input("\nPresione Enter para continuar...")


def funcion_buscar_actor() -> None:
    """Busca actor"""
    actor = input("Ingrese el nombre del actor: ")
    print("Buscando películas del actor...")

    peliculas = api.buscar_peliculas_por_actor(actor)

    if len(peliculas) > 0:
        mostrar_lista_peliculas(peliculas)

        opcion = input("\nSeleccione una película para ver detalles (0 para volver): ")
        if opcion.isdigit():
            indice = int(opcion) - 1
            if indice >= 0 and indice < len(peliculas):
                detalles = api.buscar_pelicula(peliculas[indice]["Title"])
                mostrar_pelicula(detalles)
    else:
        print("No se encontraron películas para ese actor")

    input("\nPresione Enter para continuar...")


def funcion_buscar_series() -> None:
    """Busca series"""
    nombre = input("Ingrese el nombre de la serie: ")
    print("Buscando series...")

    series = api.buscar_series(nombre)

    if len(series) > 0:
        i = 0
        while i < len(series):
            show = series[i].get("show", {})
            print(f"{i + 1}. {show.get('name', '')} ({show.get('status', '')})")
            i += 1

        opcion = input("\nSeleccione una serie para ver detalles (0 para volver): ")
        if opcion.isdigit():
            indice = int(opcion) - 1
            if indice >= 0 and indice < len(series):
                id_serie = series[indice].get("show", {}).get("id")
                detalles = api.obtener_detalles_serie(id_serie)
                mostrar_serie(detalles)
    else:
        print("No se encontraron series")

    input("\nPresione Enter para continuar...")


def funcion_peliculas_populares() -> None:
    """Muestra películas populares"""
    print_header("PELÍCULAS POPULARES")
    peliculas = api.obtener_peliculas_populares()
    mostrar_lista_peliculas(peliculas)
    input("\nPresione Enter para continuar...")


def funcion_buscar_por_genero() -> None:
    """Busca por género"""
    print("Géneros disponibles: acción, comedia")
    genero = input("Ingrese el género: ")
    print("Buscando...")

    peliculas = api.buscar_peliculas_por_genero(genero)
    mostrar_lista_peliculas(peliculas)

    input("\nPresione Enter para continuar...")


def funcion_ver_favoritos() -> None:
    """Muestra favoritas"""
    print_header("MIS FAVORITOS")
    if len(api.PELICULAS_FAVORITAS) > 0:
        i = 0
        while i < len(api.PELICULAS_FAVORITAS):
            print(f"{i + 1}. {api.PELICULAS_FAVORITAS[i].get('Title', '')}")
            i += 1

        opcion = input("\n¿Desea eliminar alguna? (número o Enter para volver): ")
        if opcion.isdigit():
            indice = int(opcion) - 1
            if indice >= 0 and indice < len(api.PELICULAS_FAVORITAS):
                titulo = api.PELICULAS_FAVORITAS[indice].get("Title")
                if api.eliminar_de_favoritas(titulo):
                    print("Eliminada de favoritos")
    else:
        print("No tienes películas favoritas")

    input("\nPresione Enter para continuar...")


def funcion_ver_historial() -> None:
    """Muestra historial"""
    print_header("HISTORIAL DE BÚSQUEDAS")
    if len(api.HISTORIAL_BUSQUEDAS) > 0:
        i = 0
        while i < len(api.HISTORIAL_BUSQUEDAS):
            print(f"{i + 1}. {api.HISTORIAL_BUSQUEDAS[i]['titulo']}")
            i += 1

        opcion = input("\n¿Limpiar historial? (s/n): ")
        if opcion.lower() == "s":
            api.limpiar_historial()
            print("Historial limpiado")
    else:
        print("No hay historial")

    input("\nPresione Enter para continuar...")


def funcion_estadisticas() -> None:
    """Muestra estadísticas"""
    print_header("ESTADÍSTICAS")
    stats = api.obtener_estadisticas()
    print(f"Total favoritas: {stats['total_favoritas']}")
    print(f"Total historial: {stats['total_historial']}")
    input("\nPresione Enter para continuar...")


def funcion_exportar() -> None:
    """Exporta datos"""
    nombre = input("Nombre del archivo (sin extensión): ")
    api.exportar_a_json(f"{nombre}.json")
    input("\nPresione Enter para continuar...")


def funcion_importar() -> None:
    """Importa datos"""
    nombre = input("Nombre del archivo (sin extensión): ")
    try:
        api.importar_de_json(f"{nombre}.json")
    except:
        print("Error al importar archivo")
    input("\nPresione Enter para continuar...")


def funcion_configuracion() -> None:
    """Configuración"""
    print_header("CONFIGURACIÓN")
    print(f"1. Debug: {api.CONFIG['debug']}")
    print(f"2. Verbose: {api.CONFIG['verbose']}")
    print(f"3. Timeout: {api.CONFIG['timeout']}")

    opcion = input("\nSeleccione opción a cambiar (0 para volver): ")
    if opcion == "1":
        api.CONFIG["debug"] = not api.CONFIG["debug"]
        print(f"Debug ahora es: {api.CONFIG['debug']}")
    elif opcion == "2":
        api.CONFIG["verbose"] = not api.CONFIG["verbose"]
        print(f"Verbose ahora es: {api.CONFIG['verbose']}")
    elif opcion == "3":
        api.CONFIG["timeout"] = int(input("Nuevo timeout: "))

    input("\nPresione Enter para continuar...")


def menu_principal() -> None:
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
        print(f"Error inesperado: {e}")
        sys.exit(1)
