numeros = [1, 2, 3, 4, 5]
paridad = ["par" if n % 2 == 0 else "impar" for n in numeros]
print(paridad)  # Salida: ['impar', 'par', 'impar', 'par', 'impar']

# Este código utiliza una comprensión de listas para crear una nueva lista llamada 'paridad' que contiene la cadena "par" si el número 'n' es par (es decir, si el residuo de 'n' dividido por 2 es 0) o "impar" si el número es impar. La comprensión de listas itera sobre cada número en la lista 'numeros' y evalúa la condición para determinar si cada número es par o impar, asignando el resultado correspondiente a la nueva lista 'paridad'. Finalmente, se imprime la lista 'paridad', que muestra si cada número en la lista original es par o impar.