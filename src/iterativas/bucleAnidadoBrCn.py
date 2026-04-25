for i in range(1, 4):
    print(f"Grupo {i}:")

    for j in range(1, 6):
        if j == 3:
            print("  Saltando el elemento 3")
            continue  # Solo afecta al bucle interno

        print(f"  Elemento {j}")

    print("Fin del grupo\n")

# Este código utiliza dos bucles for anidados para imprimir grupos de elementos. El primer bucle (con la variable i) itera sobre los números del 1 al 3, representando cada grupo. Dentro de este bucle, hay un segundo bucle (con la variable j) que itera sobre los números del 1 al 5, representando los elementos dentro de cada grupo. Si el elemento j es igual a 3, se imprime un mensaje indicando que se está saltando ese elemento y se utiliza la declaración continue para saltar a la siguiente iteración del bucle interno, lo que significa que el código debajo de continue no se ejecutará para el elemento 3. Para los demás elementos, se imprime su número. Al final de cada grupo, se imprime un mensaje indicando el fin del grupo. Como resultado, este programa imprimirá los elementos del 1 al 5 para cada grupo, pero omitirá el elemento 3 en cada caso.

encontrado = False

for i in range(5):
    for j in range(5):
        if i * j > 10:
            print(f"Valor encontrado: {i} * {j} = {i*j}")
            encontrado = True
            break  # Sale del bucle interno

    if encontrado:
        break  # Sale del bucle externo

# Este código utiliza dos bucles for anidados para buscar el primer par de números (i, j) cuyo producto sea mayor que 10. El primer bucle itera sobre los números del 0 al 4 para i, y el segundo bucle hace lo mismo para j. Dentro del segundo bucle, se verifica si el producto de i y j es mayor que 10. Si es así, se imprime el valor encontrado, se establece la variable encontrado en True y se utiliza la declaración break para salir del bucle interno. Luego, después del segundo bucle, se verifica si encontrado es True, lo que indica que se ha encontrado un valor que cumple la condición, y si es así, se utiliza otro break para salir del bucle externo. Como resultado, este programa imprimirá el primer par de números (i, j) cuyo producto sea mayor que 10 y luego terminará la búsqueda.