def obtener_temperaturas():
    """
    Función para obtener las temperaturas diarias.
    Retorna una lista de 7 temperaturas.
    """
    temperaturas = []
    for i in range(7):
        temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
        temperaturas.append(temp)
    return temperaturas

def calcular_promedio_semanal(temperaturas):
    """
    Función para calcular el promedio semanal de temperaturas.
    Recibe una lista de temperaturas y retorna el promedio.
    """
    return sum(temperaturas) / len(temperaturas)

# Programa principal
def main():
    temperaturas = obtener_temperaturas()
    promedio = calcular_promedio_semanal(temperaturas)
    print(f"El promedio semanal de temperaturas es: {promedio:.2f}°C")

if __name__ == "__main__":
    main()
