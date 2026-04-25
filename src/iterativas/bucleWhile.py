def encontrar_raiz(numero, max_iteraciones=10):
    aproximacion = numero / 2
    iteracion = 0

    while abs(aproximacion**2 - numero) > 0.001 and iteracion < max_iteraciones:
        aproximacion = (aproximacion + numero/aproximacion) / 2
        iteracion += 1
        print(f"Iteración {iteracion}: {aproximacion:.6f}")
    else:
        if iteracion < max_iteraciones:
            print(f"Convergencia alcanzada en {iteracion} iteraciones")
            return aproximacion

    print("No se alcanzó convergencia en el número máximo de iteraciones")
    return aproximacion

encontrar_raiz(25)  # Debería converger rápidamente
encontrar_raiz(612, 5)  # Probablemente no converja en 5 iteraciones

# Este código define una función encontrar_raiz() que utiliza el método de aproximación de Newton para encontrar la raíz cuadrada de un número dado. La función toma un número y un número máximo de iteraciones como argumentos. Dentro de la función, se inicializa una aproximación inicial y se utiliza un bucle while para iterar hasta que la aproximación sea suficientemente precisa o se alcance el número máximo de iteraciones. Si se alcanza la convergencia antes de agotar las iteraciones, se imprime un mensaje indicando que se ha alcanzado la convergencia y se devuelve la aproximación. Si no se alcanza la convergencia dentro del límite de iteraciones, se imprime un mensaje indicando que no se alcanzó la convergencia y se devuelve la última aproximación calculada. Luego, se prueban dos casos: uno con el número 25, que debería converger rápidamente, y otro con el número 612 con un límite de 5 iteraciones, que probablemente no converja en ese tiempo.