class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"

class Inventario:
    def __init__(self):
        self.productos = []

    def añadir_producto(self, producto):
        if any(p.id == producto.id for p in self.productos):
            print("Error: ID duplicado.")
        else:
            self.productos.append(producto)

    def eliminar_producto(self, id):
        self.productos = [p for p in self.productos if p.id != id]

    def actualizar_producto(self, id, cantidad=None, precio=None):
        for p in self.productos:
            if p.id == id:
                if cantidad: p.cantidad = cantidad
                if precio: p.precio = precio

    def buscar_productos_por_nombre(self, nombre):
        encontrados = [p for p in self.productos if nombre.lower() in p.nombre.lower()]
        for p in encontrados: print(p)

    def mostrar_todos(self):
        for p in self.productos: print(p)

def menu():
        inv = Inventario()
        opciones = {
            '1': lambda: inv.añadir_producto(Producto(input("ID: "), input("Nombre: "), int(input("Cantidad: ")), float(input("Precio: ")))),
            '2': lambda: inv.eliminar_producto(input("ID: ")),
            '3': lambda: inv.actualizar_producto(input("ID: "), int(input("Nueva Cantidad: ")), float(input("Nuevo Precio: "))),
            '4': lambda: inv.buscar_productos_por_nombre(input("Nombre: ")),
            '5': inv.mostrar_todos,
        }

        while (opcion := input("\n1. Añadir nuevo producto \n2. Eliminar producto por ID\n3. Actualizar cantidad o precio de un producto por ID\n4. Buscar producto(s) por nombre\n5. Mostrar todos los productos en el inventario\n6. Salir\n")) != '6':
            opciones.get(opcion, lambda: print("Opción no válida"))()

menu()
