"""En este ejemplo, `calcular_area_rectangulo` es 
una función que:

1. Recibe dos valores (base y altura)
2. Realiza un cálculo con ellos
3. Devuelve el resultado"""

def calcular_area_rectangulo(base, altura):
    area = base * altura
    return area

# Uso de la función
resultado = calcular_area_rectangulo(5, 3)
print(f"El área del rectángulo es: {resultado}")  # Imprime: El área del rectángulo es: 15

"""Las funciones pueden ser tan simples o complejas como necesites, pero una buena práctica es que cada función realice una única tarea específica. 
Esto hace que tu código 
sea más fácil de entender, probar y mantener."""

# Función que verifica si un número es par
def es_par(numero):
    return numero % 2 == 0

# Función que convierte temperatura de Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32