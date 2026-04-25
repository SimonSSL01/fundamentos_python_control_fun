def buscar_elemento(lista, objetivo):
    for indice, elemento in enumerate(lista):
        if elemento == objetivo:
            return indice

    return -1  # Si llegamos aquí, el elemento no está en la lista

numeros = [4, 7, 2, 9, 1, 5]
posicion = buscar_elemento(numeros, 9)
print(f"El elemento se encuentra en la posición: {posicion}")

# Este código define una función buscar_elemento() que toma una lista y un objetivo como argumentos. La función utiliza un bucle for junto con la función enumerate() para iterar sobre la lista, obteniendo tanto el índice como el elemento en cada iteración. Si el elemento coincide con el objetivo, se devuelve el índice correspondiente. Si el bucle termina sin encontrar el objetivo, se devuelve -1 para indicar que el elemento no está presente en la lista. En este ejemplo, se busca el número 9 en la lista de números, y se imprime la posición donde se encuentra (en este caso, la posición 3).