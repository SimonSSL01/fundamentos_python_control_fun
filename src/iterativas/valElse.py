def validar_edades(lista_edades):
    for edad in lista_edades:
        if not isinstance(edad, int) or edad < 0:
            print(f"Edad inválida encontrada: {edad}")
            break
    else:
        print("Todas las edades son válidas")
        return True

    return False

# Probamos con diferentes listas
validar_edades([25, 17, 30, 42])  # Todas válidas
validar_edades([25, -3, 30, 42])  # Una inválida

# Este código define una función validar_edades() que toma una lista de edades como argumento. La función utiliza un bucle for para iterar a través de cada edad en la lista. Dentro del bucle, se verifica si la edad no es un entero o si es menor que 0. Si se encuentra una edad inválida, se imprime un mensaje indicando cuál es la edad inválida y se utiliza la declaración break para salir del bucle inmediatamente. Si el bucle termina sin encontrar ninguna edad inválida, se ejecuta el bloque else asociado al for, que imprime un mensaje indicando que todas las edades son válidas y devuelve True. Si se encontró una edad inválida, la función devuelve False. Luego, se prueban dos listas de edades: una con todas las edades válidas y otra con una edad inválida para demostrar el funcionamiento de la función.