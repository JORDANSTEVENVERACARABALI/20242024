class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn

    def __repr__(self):
        return f"{self.titulo} por {self.autor} (ISBN: {self.isbn})"


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def __repr__(self):
        return f"Usuario: {self.nombre} (ID: {self.id_usuario})"

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)


class Biblioteca:
    def __init__(self):
        self.libros_disponibles = {}  # {ISBN: Libro}
        self.usuarios_registrados = {}  # {ID de Usuario: Usuario}
        self.prestamos = {}  # {ISBN: Usuario}

    def añadir_libro(self, libro):
        if libro.isbn not in self.libros_disponibles:
            self.libros_disponibles[libro.isbn] = libro
        else:
            print(f"El libro con ISBN {libro.isbn} ya está en la biblioteca.")

    def quitar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            del self.libros_disponibles[isbn]
        else:
            print(f"El libro con ISBN {isbn} no está en la biblioteca.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.usuarios_registrados:
            self.usuarios_registrados[usuario.id_usuario] = usuario
        else:
            print(f"El usuario con ID {usuario.id_usuario} ya está registrado.")

    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios_registrados:
            del self.usuarios_registrados[id_usuario]
        else:
            print(f"El usuario con ID {id_usuario} no está registrado.")

    def prestar_libro(self, isbn, id_usuario):
        if isbn in self.libros_disponibles and id_usuario in self.usuarios_registrados:
            libro = self.libros_disponibles[isbn]
            usuario = self.usuarios_registrados[id_usuario]
            usuario.prestar_libro(libro)
            self.prestamos[isbn] = usuario
            del self.libros_disponibles[isbn]
        else:
            print(f"El libro con ISBN {isbn} no está disponible o el usuario no está registrado.")

    def devolver_libro(self, isbn):
        if isbn in self.prestamos:
            usuario = self.prestamos[isbn]
            libro = self.prestamos.pop(isbn)
            usuario.devolver_libro(libro)
            self.libros_disponibles[isbn] = libro
        else:
            print(f"El libro con ISBN {isbn} no está prestado actualmente.")

    def buscar_libro(self, criterio, valor):
        resultados = []
        for libro in self.libros_disponibles.values():
            if (criterio == 'titulo' and valor.lower() in libro.titulo.lower()) or \
               (criterio == 'autor' and valor.lower() in libro.autor.lower()) or \
               (criterio == 'categoria' and valor.lower() in libro.categoria.lower()):
                resultados.append(libro)
        return resultados

    def listar_libros_prestados(self, id_usuario):
        if id_usuario in self.usuarios_registrados:
            usuario = self.usuarios_registrados[id_usuario]
            return usuario.libros_prestados
        else:
            print(f"El usuario con ID {id_usuario} no está registrado.")
            return []

# Ejemplo de uso
if __name__ == "__main__":
    biblioteca = Biblioteca()

    # Crear usuarios
    usuario1 = Usuario("Ana Pérez", "001")
    usuario2 = Usuario("Luis Gómez", "002")

    # Registrar usuarios
    biblioteca.registrar_usuario(usuario1)
    biblioteca.registrar_usuario(usuario2)

    # Crear libros
    libro1 = Libro("La Espada de Bolivar", "Patricia Lara", "Historia", "978-3-16-148410-0")
    libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", "Ficción", "978-3-16-148410-1")

    # Añadir libros
    biblioteca.añadir_libro(libro1)
    biblioteca.añadir_libro(libro2)

    # Prestar libro
    biblioteca.prestar_libro("978-3-16-148410-0", "001")

    # Buscar libro
    resultados = biblioteca.buscar_libro('titulo', 'La Espada de Bolivar')
    print("Resultados de búsqueda:", resultados)

    # Listar libros prestados
    print("Libros prestados por Jordan Vera:", biblioteca.listar_libros_prestados("001"))

    # Devolver libro
    biblioteca.devolver_libro("978-3-16-148410-0")

    # Limpiar datos para prueba
    biblioteca.quitar_libro("978-3-16-148410-0")
    biblioteca.dar_baja_usuario("001")
