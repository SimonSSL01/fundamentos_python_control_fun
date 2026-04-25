numeros = [1, 2, 3, 4]

match numeros:
    case []:
        print("La lista está vacía.")
    case [uno]:
        print(f"Un solo elemento: {uno}.")
    case [uno, dos]:
        print(f"Dos elementos: {uno} y {dos}.")
    case [uno, *resto]:
        print(f"Primer elemento: {uno}, resto de la lista: {resto}.")

# Este código define una lista de números y utiliza una estructura de control 'match' para comparar la lista con diferentes patrones. Dependiendo del patrón que coincida, se imprime un mensaje indicando si la lista está vacía, tiene un solo elemento, tiene dos elementos o tiene más de dos elementos. En este caso, como la lista tiene cuatro elementos, se imprimirá "Primer elemento: 1, resto de la lista: [2, 3, 4]."