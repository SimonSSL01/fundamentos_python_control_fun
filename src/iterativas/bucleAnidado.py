# Crear una matriz de multiplicación 3x3
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} × {j} = {i*j}", end="\t")
    print()  # Salto de línea después de cada fila

# Este código utiliza dos bucles for anidados para crear una matriz de multiplicación de 3x3. El primer bucle (con la variable i) itera sobre los números del 1 al 3, y el segundo bucle (con la variable j) también itera sobre los números del 1 al 3. Dentro del segundo bucle, se imprime el resultado de multiplicar i por j, formateado como una tabla. Después de completar cada fila (cuando el segundo bucle termina), se imprime un salto de línea para separar las filas de la matriz.