# Programa para calcular el índice de masa corporal (IMC)
# El usuario ingresa peso en kg y altura en metros, luego se calcula el IMC.

def calcular_imc(peso_kg, altura_m):
    """
    Calcula el índice de masa corporal (IMC) dado el peso en kg y la altura en metros.

    Args:
        peso_kg (float): Peso del individuo en kilogramos.
        altura_m (float): Altura del individuo en metros.

    Returns:
        float: Valor del índice de masa corporal calculado.
    """
    imc = peso_kg / (altura_m ** 2)
    return imc

# Solicitar al usuario que ingrese peso y altura
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

# Calcular el IMC utilizando la función definida
indice_masa_corporal = calcular_imc(peso, altura)

# Mostrar el resultado del IMC
print(f"Su índice de masa corporal es: {indice_masa_corporal:.2f}")

# Evaluación del estado de peso
if indice_masa_corporal < 18.5:
    print("Estás bajo peso.")
elif indice_masa_corporal < 25:
    print("Estás en un rango de peso saludable.")
elif indice_masa_corporal < 30:
    print("Tienes sobrepeso.")
else:
    print("Tienes obesidad.")

