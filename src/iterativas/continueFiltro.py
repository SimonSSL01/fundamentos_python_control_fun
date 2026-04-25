temperaturas = [22, -5, 28, 31, -15, 19, 26, -8]

print("Temperaturas positivas:")
for temp in temperaturas:
    if temp <= 0:
        continue

    print(f"{temp}°C")

# Este código define una lista de temperaturas que incluye tanto valores positivos como negativos. Luego, utiliza un bucle for para iterar a través de cada temperatura en la lista. Dentro del bucle, se verifica si la temperatura es menor o igual a 0. Si es así, se utiliza la declaración continue para saltar a la siguiente iteración del bucle, lo que significa que el código debajo de continue no se ejecutará para las temperaturas negativas o cero. Si la temperatura es positiva, se imprime en la consola. Como resultado, este programa imprimirá solo las temperaturas positivas de la lista (22°C, 28°C, 31°C, 19°C y 26°C).