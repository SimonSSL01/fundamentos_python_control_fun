while True:
    entrada = input("Escribe algo (o 'salir' para terminar): ")

    if entrada.lower() == 'salir':
        print("Programa terminado.")
        break

    print(f"Has escrito: {entrada}")

# Este código implementa un bucle infinito que solicita al usuario que escriba algo. Si el usuario escribe "salir" (en cualquier combinación de mayúsculas y minúsculas), el programa imprime un mensaje de finalización y utiliza la declaración break para salir del bucle, terminando la ejecución. Si el usuario escribe cualquier otra cosa, el programa imprime lo que ha escrito y continúa solicitando más entradas hasta que se escriba "salir".