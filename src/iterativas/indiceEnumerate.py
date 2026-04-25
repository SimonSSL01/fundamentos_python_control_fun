nombres = ["Ana", "Carlos", "Elena"]
for indice, nombre in enumerate(nombres):
    print(f"Posición {indice}: {nombre}")

# Este código utiliza la función enumerate() para iterar sobre la lista "nombres" y obtener tanto el índice como el valor de cada elemento. La función enumerate(nombres) devuelve un objeto iterable que produce pares de índice y valor para cada elemento en la lista. En cada iteración del bucle, se imprime la posición (índice) y el nombre correspondiente en esa posición. En este caso, se imprimirá: