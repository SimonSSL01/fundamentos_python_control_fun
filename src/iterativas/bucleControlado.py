while True:
    respuesta = input("¿Quieres continuar? (s/n): ").lower()

    if respuesta == "n":
        print("Programa finalizado.")
        break

    if respuesta == "s":
        print("Continuando...")
    else:
        print("Respuesta no válida. Introduce 's' o 'n'.")

# Este código implementa un bucle controlado por eventos. El programa pregunta al usuario si desea continuar o no. Si el usuario responde "n", el programa imprime un mensaje de finalización y rompe el bucle, terminando la ejecución. Si el usuario responde "s", el programa imprime un mensaje de continuación y el bucle se repite. Si el usuario introduce cualquier otra respuesta, se muestra un mensaje de error indicando que la respuesta no es válida, y el bucle continúa solicitando una respuesta válida.