fruta = input("Introduzca una fruta: ")

match fruta:
    case "manzana":
        print("La fruta es una manzana.")
    case "naranja":
        print("La fruta es una naranja.")
    case "plátano":
        print("La fruta es un plátano.")
    case _:
        print("Fruta desconocida.")

# Este código solicita al usuario que introduzca el nombre de una fruta. Luego, utiliza una estructura de control 'match' para comparar la entrada del usuario con diferentes casos: "manzana", "naranja" y "plátano". Si la fruta coincide con alguno de estos casos, se imprime un mensaje indicando qué fruta es. Si la fruta no coincide con ninguno de los casos, se ejecuta el caso por defecto (indicado por '_') y se imprime un mensaje indicando que la fruta es desconocida.