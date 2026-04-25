"""Número variable de argumentos

En ocasiones, 
necesitamos funciones que puedan aceptar 
un número variable de argumentos.  
Python nos ofrece dos sintaxis especiales
 para esto:"""

# Argumentos posicionales variables (*args)

# Permite que una función acepte cualquier
#  número de argumentos posicionales:

def sumar(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total

# Podemos pasar cualquier cantidad de argumentos
print(sumar(1, 2))  # Imprime: 3
print(sumar(1, 2, 3, 4, 5))  # Imprime: 15
print(sumar())  # Imprime: 0

#El parámetro *numeros recibe 
# todos los argumentos posicionales como una tupla.

