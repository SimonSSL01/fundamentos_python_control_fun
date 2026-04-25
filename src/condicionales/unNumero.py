numeros = [0, 0, 1, 0]

if any(numeros):
    print("Al menos un número es no cero.")

# Este código utiliza la función 'any()' para verificar si al menos uno de los elementos en la lista 'numeros' es diferente de cero. La función 'any()' devuelve True si al menos un elemento de la lista es verdadero (en este caso, cualquier número diferente de cero se considera verdadero). Si 'any(numeros)' devuelve True, se imprime el mensaje "Al menos un número es no cero." En este caso, como hay un número 1 en la lista, se imprimirá "Al menos un número es no cero."