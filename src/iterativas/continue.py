for numero in range(1, 11):
    if numero % 2 == 0:  # Si el número es par
        continue  # Saltamos a la siguiente iteración

    print(f"Número impar: {numero}")

# Este código utiliza un bucle for para iterar a través de los números del 1 al 10. Dentro del bucle, se verifica si el número actual es par (es decir, si el residuo de dividirlo por 2 es 0). Si el número es par, se utiliza la declaración continue para saltar a la siguiente iteración del bucle, lo que significa que el código debajo de continue no se ejecutará para los números pares. Si el número no es par (es decir, es impar), se imprime un mensaje indicando que es un número impar. Como resultado, este programa imprimirá solo los números impares del 1 al 10 (1, 3, 5, 7 y 9).