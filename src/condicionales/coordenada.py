punto = (0, 0)

match punto:
    case (0, 0):
        print("El punto está en el origen.")
    case (0, y):
        print(f"El punto está en el eje Y en y={y}.")
    case (x, 0):
        print(f"El punto está en el eje X en x={x}.")
    case (x, y):
        print(f"El punto está en coordenadas x={x}, y={y}.")

# Este código define una variable 'punto' que es una tupla con dos valores (0, 0). Luego, utiliza una estructura de control 'match' para comparar la variable 'punto' con diferentes patrones. Dependiendo del patrón que coincida, se imprime un mensaje indicando la ubicación del punto en el plano cartesiano. En este caso, como 'punto' es igual a (0, 0), se imprimirá "El punto está en el origen."