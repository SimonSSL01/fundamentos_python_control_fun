condiciones = [True, True, False, True]

if all(condiciones):
    print("Todas las condiciones son verdaderas.")
else:
    print("Al menos una condición es falsa.")

# Este código utiliza la función 'all()' para verificar si todas las condiciones en la lista 'condiciones' son verdaderas. La función 'all()' devuelve True si todos los elementos de la lista son verdaderos, y False si al menos uno de ellos es falso. En este caso, como hay una condición que es False, 'all(condiciones)' devolverá False, por lo que se imprimirá "Al menos una condición es falsa."