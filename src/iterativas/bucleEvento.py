import random

objetivo = random.randint(1, 10)
intentos = 0
adivinado = False

while not adivinado and intentos < 3:
    intentos += 1
    numero = int(input(f"Intento {intentos}/3: Adivina un número del 1 al 10: "))

    if numero == objetivo:
        print(f"¡Correcto! Has adivinado en {intentos} intentos.")
        adivinado = True
    else:
        pista = "mayor" if numero < objetivo else "menor"
        print(f"Incorrecto. El número es {pista} que {numero}.")

if not adivinado:
    print(f"Se acabaron los intentos. El número era {objetivo}.")

# Este código implementa un juego de adivinanza de números. El programa genera un número aleatorio entre 1 y 10, y el usuario tiene tres intentos para adivinarlo. En cada intento, el programa proporciona una pista indicando si el número a adivinar es mayor o menor que el número ingresado por el usuario. Si el usuario adivina correctamente dentro de los intentos permitidos, se muestra un mensaje de éxito. Si no, se revela el número correcto al final del juego.