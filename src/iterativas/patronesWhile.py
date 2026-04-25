def imprimir_triangulo(altura):
    fila = 1
    while fila <= altura:
        print("*" * fila)
        fila += 1

imprimir_triangulo(5)

# Este código define una función imprimir_triangulo() que toma un argumento altura y utiliza un bucle while para imprimir un triángulo de asteriscos. El bucle comienza con fila igual a 1 y continúa ejecutándose mientras fila sea menor o igual a altura. En cada iteración, se imprime una cadena de asteriscos cuyo número es igual al valor de fila, y luego se incrementa fila en 1. Al llamar a la función con una altura de 5, se imprimirá un triángulo de asteriscos con 5 filas, donde la primera fila tiene 1 asterisco, la segunda tiene 2, y así sucesivamente hasta la quinta fila que tiene 5 asteriscos.