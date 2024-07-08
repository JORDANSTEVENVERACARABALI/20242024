class Archivo:
    def __init__(self, nombre):
        """Abre el archivo al crear el objeto."""
        self.nombre = nombre
        self.archivo = open(nombre, 'w')
        print(f"Archivo '{self.nombre}' abierto.")

    def escribir(self, contenido):
        """Escribe contenido en el archivo."""
        self.archivo.write(contenido)

    def __del__(self):
        """Cierra el archivo al destruir el objeto."""
        self.archivo.close()
        print(f"Archivo '{self.nombre}' cerrado.")


class ConexionBD:
    def __init__(self, db_name):
        """Simula la conexión a la base de datos."""
        self.db_name = db_name
        print(f"Conectado a la base de datos '{self.db_name}'.")

    def __del__(self):
        """Simula la desconexión de la base de datos."""
        print(f"Desconectado de la base de datos '{self.db_name}'.")


# Uso de las clases
if __name__ == "__main__":
    archivo = Archivo("UEA JORDAN")
    archivo.escribir("Hola, mundo!")

    conexion = ConexionBD("UNIVERSIDAD ESTATAL AMAZONICA")
