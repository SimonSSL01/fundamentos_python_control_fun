# Usando while
suma = 0
i = 1
while i <= 10:
    suma += i
    i += 1
print(f"Suma (while): {suma}")

# Equivalente con for
suma = 0
for i in range(1, 11):
    suma += i
print(f"Suma (for): {suma}")

# Este código muestra dos formas de calcular la suma de los primeros 10 números enteros. La primera parte utiliza un bucle while, donde se inicializa una variable suma en 0 y un contador i en 1. El bucle continúa ejecutándose mientras i sea menor o igual a 10, sumando i a la variable suma y luego incrementando i en cada iteración. La segunda parte hace lo mismo pero utilizando un bucle for con la función range(), que genera una secuencia de números del 1 al 10. Al final, ambos métodos imprimen el resultado de la suma, que es 55.