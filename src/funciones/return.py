"""La sentencia `return` cumple dos propósitos 
fundamentales:

1. Devolver un valor como resultado de la función
2. Finalizar la ejecución de la función inmediatamente"""

def calcular_cuadrado(numero):
    resultado = numero * numero
    return resultado  # Devuelve el valor y termina la función

area = calcular_cuadrado(4)
print(area)  # Imprime: 16

"""En este ejemplo, la función calcular_cuadrado 
recibe un número, calcula su cuadrado 
y lo devuelve mediante return. 
El valor devuelto se puede asignar a 
una variable (area) para usarlo posteriormente."""

