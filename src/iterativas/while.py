entrada = ""
while not entrada.isdigit():
    entrada = input("Introduce un número: ")

print(f"Has introducido el número: {entrada}")

# Este código utiliza un bucle while para solicitar al usuario que introduzca un número. El bucle continúa ejecutándose hasta que el usuario ingresa una cadena que consiste únicamente en dígitos (es decir, un número válido). La función isdigit() se utiliza para verificar si la entrada del usuario es un número. Una vez que se recibe una entrada válida, el programa imprime el número introducido por el usuario.