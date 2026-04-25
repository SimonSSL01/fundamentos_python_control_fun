def es_primo(n):
    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False  # No es primo, salimos inmediatamente

    return True  # Si llegamos aquí, es primo

# Este código define una función es_primo() que determina si un número entero n es primo o no. La función primero verifica si n es menor que 2, en cuyo caso devuelve False, ya que los números menores que 2 no son primos. Luego, utiliza un bucle for para iterar desde 2 hasta la raíz cuadrada de n (inclusive). Si encuentra algún divisor de n en ese rango (es decir, si n es divisible por i), devuelve False, indicando que n no es primo. Si el bucle termina sin encontrar divisores, la función devuelve True, indicando que n es primo. Este enfoque es eficiente porque reduce el número de iteraciones necesarias para determinar la primalidad de n.