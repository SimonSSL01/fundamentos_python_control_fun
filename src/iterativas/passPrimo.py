numeros = [4, 6, 7, 8, 10]  # Ahora incluimos el 7

for num in numeros:
    if num % 2 != 0 and num % 3 != 0:
        print(f"¡Encontrado un primo: {num}!")
        break
else:
    print("No se encontró ningún número primo en la lista")

# Este código define una lista de números y utiliza un bucle for para iterar a través de cada número en la lista. Dentro del bucle, se verifica si el número es primo comprobando si no es divisible por 2 ni por 3 (lo cual es una forma rápida de filtrar algunos números no primos). Si se encuentra un número que cumple con esta condición, se imprime un mensaje indicando que se ha encontrado un número primo y se utiliza la declaración break para salir del bucle inmediatamente. Si el bucle termina sin encontrar ningún número primo, se ejecuta el bloque else asociado al for, que imprime un mensaje indicando que no se encontró ningún número primo en la lista. En este caso, como el número 7 es primo, el resultado será "¡Encontrado un primo