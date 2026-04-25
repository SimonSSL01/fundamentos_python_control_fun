numeros = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
limite = 50
suma = 0

for num in numeros:
    # Ignoramos múltiplos de 3
    if num % 3 == 0:
        print(f"Omitiendo {num} (múltiplo de 3)")
        continue

    # Sumamos el número
    suma += num
    print(f"Añadiendo {num}: suma = {suma}")

    # Si la suma supera el límite, terminamos
    if suma > limite:
        print(f"Límite de {limite} superado")
        break

# Este código define una lista de números impares del 1 al 19 y un límite de suma de 50. Luego, utiliza un bucle for para iterar a través de cada número en la lista. Dentro del bucle, se verifica si el número es un múltiplo de 3. Si es así, se imprime un mensaje indicando que se está omitiendo ese número y se utiliza la declaración continue para saltar a la siguiente iteración del bucle, lo que significa que el código debajo de continue no se ejecutará para los múltiplos de 3. Si el número no es un múltiplo de 3, se suma a la variable suma y se imprime el nuevo valor de la suma. Luego, se verifica si la suma ha superado el límite establecido. Si es así, se imprime un mensaje indicando que el límite ha sido superado y se utiliza la declaración break para salir del bucle inmediatamente. Como resultado, este programa sumará los números impares del 1 al 19, omitiendo los múltiplos de 3, hasta que la suma supere el límite de 50.