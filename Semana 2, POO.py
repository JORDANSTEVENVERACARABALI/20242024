class ClimaDiario:
    def __init__(self):
        self.temperaturas = []

    def ingresar_temperatura(self, dia, temperatura):
        """
        Método para ingresar la temperatura de un día específico.
        """
        if 1 <= dia <= 7:
            if len(self.temperaturas) < dia:
                self.temperaturas.extend([None] * (dia - len(self.temperaturas)))
            self.temperaturas[dia - 1] = temperatura
        else:
            print("Día inválido. Por favor ingrese un día entre 1 y 7.")

    def calcular_promedio_semanal(self):
        """
        Método para calcular el promedio semanal de temperaturas.
        """
        if not self.temperaturas or len(self.temperaturas) < 7:
            print("No se han ingresado todas las temperaturas.")
            return None
        return sum(self.temperaturas) / len(self.temperaturas)


# Programa principal
def main():
    clima = ClimaDiario()

    for i in range(7):
        temperatura = float(input(f"Ingrese la temperatura del día {i + 1}: "))
        clima.ingresar_temperatura(i + 1, temperatura)

    promedio = clima.calcular_promedio_semanal()
    if promedio is not None:
        print(f"El promedio semanal de temperaturas es: {promedio:.2f}°C")


if __name__ == "__main__":
    main()
