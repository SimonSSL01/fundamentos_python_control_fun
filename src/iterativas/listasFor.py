# Crear una lista con los cuadrados de los números del 1 al 5
cuadrados = [x**2 for x in range(1, 6)]
print(cuadrados)  # [1, 4, 9, 16, 25]

# Filtrar elementos usando una condición
pares = [x for x in range(10) if x % 2 == 0]
print(pares)  # [0, 2, 4, 6, 8]

# Este código muestra cómo usar las listas por comprensión para crear nuevas listas de manera concisa. En el primer ejemplo, se genera una lista de los cuadrados de los números del 1 al 5. En el segundo ejemplo, se crea una lista de números pares del 0 al 9 utilizando una condición dentro de la comprensión de listas.