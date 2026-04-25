edad = 20

match edad:
    case edad if edad < 18:
        print("Eres menor de edad.")
    case edad if edad >= 18 and edad < 65:
        print("Eres adulto.")
    case edad if edad >= 65:
        print("Eres adulto mayor.")

# Este código utiliza una estructura de control 'match' para clasificar a una persona en función de su edad. Dependiendo del valor de la variable 'edad', se imprime un mensaje indicando si la persona es menor de edad, adulto o adulto mayor. En este caso, como 'edad' es igual a 20, se imprimirá "Eres adulto."