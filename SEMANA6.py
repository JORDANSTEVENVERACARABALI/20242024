# Definición de la clase base
class Animal:
    def __init__(self, nombre):
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre

    def hacer_sonido(self):
        pass

# Definición de la clase derivada
class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza

    def hacer_sonido(self):
        return "¡Guau!"

    def presentarse(self):
        return f"Soy {self.get_nombre()}, un perro de raza {self.raza}."

# Función principal
def main():
    # Crear instancia de la clase derivada
    mi_perro = Perro("JACK", "Rottweiler")

    # Acceder a métodos heredados y propios de la clase Perro
    print(mi_perro.presentarse())
    print(mi_perro.hacer_sonido())

if __name__ == "__main__":
    main()
