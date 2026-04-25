def calcular_factorial(n):
    resultado = 1
    while n > 0:
        resultado *= n
        n -= 1
    return resultado

numero = 5
print(f"El factorial de {numero} es {calcular_factorial(numero)}")  # 120

# Este código define una función calcular_factorial() que calcula el factorial de un número entero positivo utilizando un bucle while. La función inicializa una variable resultado en 1 y luego multiplica resultado por n, decrementando n en cada iteración hasta que n sea 0. Finalmente, devuelve el resultado del factorial. En este caso, se calcula el factorial de 5, que es 120.