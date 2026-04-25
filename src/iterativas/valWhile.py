def obtener_numero_en_rango(mensaje, minimo, maximo):
    while True:
        try:
            valor = int(input(mensaje))
            if minimo <= valor <= maximo:
                return valor
            print(f"Error: El número debe estar entre {minimo} y {maximo}.")
        except ValueError:
            print("Error: Debes introducir un número entero.")

edad = obtener_numero_en_rango("Introduce tu edad (0-120): ", 0, 120)
print(f"Edad registrada: {edad} años")

# Este código define una función obtener_numero_en_rango() que solicita al usuario que introduzca un número dentro de un rango específico (definido por los parámetros minimo y maximo). La función utiliza un bucle while para continuar solicitando la entrada del usuario hasta que se reciba un número válido. Si el usuario introduce un valor que no es un número entero, se captura la excepción ValueError y se muestra un mensaje de error. Si el número está fuera del rango permitido, también se muestra un mensaje de error. Una vez que se recibe una entrada válida, la función devuelve el número. En este ejemplo, se solicita al usuario que introduzca su edad, asegurándose de que esté entre 0 y 120 años, y luego se imprime la edad registrada.