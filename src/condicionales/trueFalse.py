a = True
b = False
c = not b

resultado = a or b and c
print(resultado)  # Imprime True

resultado = (a or b) and c
print(resultado)  # Imprime True

# Este código define tres variables booleanas: 'a' es True, 'b' es False y 'c' es el resultado de la negación de 'b', lo que significa que 'c' es True. Luego, se evalúan dos expresiones lógicas utilizando los operadores 'or' y 'and'. En la primera expresión, 'a or b and c', se evalúa primero 'b and c', que es False, y luego se evalúa 'a or False', lo que da como resultado True. En la segunda expresión, '(a or b) and c', se evalúa primero 'a or b', que es True, y luego se evalúa 'True and c', lo que también da como resultado True. Por lo tanto, ambas expresiones imprimen True.