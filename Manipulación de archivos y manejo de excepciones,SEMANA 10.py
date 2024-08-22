class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = self.cargar_inventario()

    def cargar_inventario(self):
        try:
            return {linea.split(',')[0]: linea.strip() for linea in open(self.archivo, "r")}
        except FileNotFoundError:
            return {}

    def guardar_inventario(self):
        with open(self.archivo, "w") as f:
            f.writelines(p + "\n" for p in self.productos.values())

    def añadir_o_actualizar(self, codigo, nombre, cantidad, precio):
        self.productos[codigo] = f"{codigo},{nombre},{cantidad},{precio}"
        self.guardar_inventario()
        print(f"Producto {codigo} añadido/actualizado.")

    def eliminar_producto(self, codigo):
        if self.productos.pop(codigo, None):
            self.guardar_inventario()
            print(f"Producto {codigo} eliminado.")

    def mostrar_inventario(self):
        for p in self.productos.values():
            print(p)


# Ejemplo de uso:
if __name__ == "__main__":
    inventario = Inventario()
    inventario.añadir_o_actualizar("001", "Manzana", 50, 0.5)
    inventario.mostrar_inventario()
    inventario.eliminar_producto("001")
    inventario.mostrar_inventario()
