edad = 20
categoria = "Menor" if edad < 18 else ("Joven Adulto" if edad < 30 else "Adulto")
print(categoria)

# Este código utiliza expresiones condicionales anidadas para clasificar a una persona en una categoría basada en su edad. Primero, se verifica si la edad es menor que 18; si es así, se asigna "Menor" a la variable 'categoria'. Si la edad no es menor que 18, se verifica si es menor que 30; si es así, se asigna "Joven Adulto". Si la edad es 30 o más, se asigna "Adulto". Finalmente, se imprime la categoría correspondiente. En este caso, como la edad es 20, se imprimirá "Joven Adulto".