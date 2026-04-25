def analizar_datos(valores, umbral):
    tiene_advertencias = False

    for valor in valores:
        if valor > umbral:
            tiene_advertencias = True
            print(f"Advertencia: valor {valor} excede el umbral {umbral}")
        else:
            pass  # Explícitamente no hacemos nada con valores normales
    else:
        if not tiene_advertencias:
            print("Análisis completo: todos los valores están dentro del rango normal")
            return "OK"

    return "ADVERTENCIA"

# Probamos con diferentes conjuntos de datos
analizar_datos([10, 15, 20, 25], 30)  # Todos dentro del umbral
analizar_datos([10, 35, 20, 25], 30)  # Uno excede el umbral

# Este código define una función analizar_datos() que toma una lista de valores y un umbral como argumentos. La función utiliza un bucle for para iterar a través de cada valor en la lista. Si un valor excede el umbral, se establece una bandera tiene_advertencias en True y se imprime una advertencia indicando qué valor ha excedido el umbral. Si un valor no excede el umbral, se utiliza la declaración pass para indicar explícitamente que no se realiza ninguna acción para esos valores normales. Al finalizar el bucle, si no se han encontrado valores que excedan el umbral (es decir, si tiene_advertencias sigue siendo False), se ejecuta el bloque else asociado al for, que imprime un mensaje indicando que todos los valores están dentro del rango normal y devuelve "OK". Si se encontraron valores que exceden el umbral, la función devuelve "ADVERTENCIA". Luego, se prueban dos conjuntos de datos: uno donde todos los valores están dentro del umbral y otro donde uno de los valores excede el umbral para demostrar el funcionamiento de la función.