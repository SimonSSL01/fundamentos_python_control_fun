numeros = [1, 2, 0, 4, 0, 6, 7]

for num in numeros:
    if num == 0:
        print("Omitiendo división por cero")
        continue

    resultado = 10 / num
    print(f"10 / {num} = {resultado}")

# Este código define una lista de números que incluye algunos ceros. Luego, utiliza un bucle for para iterar a través de cada número en la lista. Dentro del bucle, se verifica si el número es igual a 0. Si es así, se imprime un mensaje indicando que se está omitiendo la división por cero y se utiliza la declaración continue para saltar a la siguiente iteración del bucle, lo que significa que el código debajo de continue no se ejecutará para los números cero. Si el número no es cero, se realiza la división de 10 entre ese número y se imprime el resultado. Como resultado, este programa imprimirá los resultados de dividir 10 por cada número en la lista, excepto cuando el número sea 0, donde se imprimirá un mensaje de advertencia.