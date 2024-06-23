class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            return True
        else:
            return False

    def devolver(self):
        self.disponible = True


class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros_prestados = []

    def prestar_libro(self, libro):
        if libro.prestar():
            self.libros_prestados.append(libro)
            return True
        else:
            return False

    def devolver_libro(self, libro):
        libro.devolver()
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)


# Ejemplo de uso:

# Crear algunos libros
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez")
libro2 = Libro("1984", "George Orwell")

# Crear algunos usuarios
usuario1 = Usuario("Jordan")
usuario2 = Usuario("María")

# Usuario 1 presta un libro
usuario1.prestar_libro(libro1)

# Mostrar información de los libros prestados por usuario1
print(f"Libros prestados a {usuario1.nombre}:")
for libro in usuario1.libros_prestados:
    print(libro.titulo)


