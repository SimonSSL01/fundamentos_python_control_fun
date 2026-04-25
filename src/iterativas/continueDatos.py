datos = ["25", "error", "42", "texto", "17"]

suma = 0
for valor in datos:
    if not valor.isdigit():
        print(f"Valor no numérico ignorado: '{valor}'")
        continue

    suma += int(valor)

print(f"La suma de los valores válidos es: {suma}")

# Este código define una lista de datos que contiene tanto valores numéricos como no numéricos. Luego, utiliza un bucle for para iterar a través de cada valor en la lista. Dentro del bucle, se verifica si el valor es un dígito utilizando el método isdigit(). Si el valor no es un dígito (es decir, no es un número), se imprime un mensaje indicando que se ha ignorado ese valor y se utiliza la declaración continue para saltar a la siguiente iteración del bucle. Si el valor es un dígito, se convierte a entero y se suma a la variable suma. Al final, se imprime la suma total de los valores numéricos válidos en la lista. En este caso, la salida será: