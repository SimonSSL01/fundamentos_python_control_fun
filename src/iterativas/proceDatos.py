temperaturas = [22, 19, 24, 25, 21, 23, 20]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Encontrar el día más caluroso
max_temp = max(temperaturas)
indice_max = temperaturas.index(max_temp)
print(f"El día más caluroso fue {dias[indice_max]} con {max_temp}°C")

# Calcular la temperatura promedio
promedio = sum(temperaturas) / len(temperaturas)
print(f"Temperatura promedio: {promedio:.1f}°C")

# Días con temperatura superior al promedio
for i in range(len(dias)):
    if temperaturas[i] > promedio:
        print(f"{dias[i]}: {temperaturas[i]}°C (por encima del promedio)")

# Este código procesa una lista de temperaturas diarias y una lista de días correspondientes. Primero, encuentra la temperatura máxima y su índice para determinar qué día fue el más caluroso. Luego, calcula la temperatura promedio y finalmente itera sobre las listas para identificar y mostrar los días que tuvieron una temperatura superior al promedio.