import os


def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")


def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(_file_)

    opciones = {
        '1': 'Semana 01/Semana 1,ejemplo.py',
        '2': 'Semana 02/SEMANA 2.POO.py',
        '3': 'Semana 03/SEMANA 3 , Utilizando funciones .py',
        '4': 'Semana 04/SEMANA 4.py',
        '5': 'Semana 05/SEMANA 5 .py',
        '6': 'Semana 06/SEMANA 6.py',
        '7': 'Semana 07/SEMANA 7.py',
        # Agrega aquí el resto de las rutas de los scripts
 }

    while True:
        print("\nMenu Principal - Dashboard")
        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")

        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            # Asegura que el path sea absoluto
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


# Ejecutar el dashboard
if __name__ == "_main_":
    mostrar_menu()