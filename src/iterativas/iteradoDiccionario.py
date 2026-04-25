usuario = {"nombre": "Laura", "edad": 28, "ciudad": "Madrid"}

# Iterando sobre claves
for clave in usuario:
    print(f"Clave: {clave}, Valor: {usuario[clave]}")

# Este código define un diccionario llamado "usuario" con información sobre una persona. Luego, utiliza un bucle for para iterar sobre las claves del diccionario. En cada iteración, se imprime la clave actual y su valor correspondiente utilizando la sintaxis usuario[clave].

# Iterando sobre pares clave-valor
for clave, valor in usuario.items():
    print(f"{clave}: {valor}")

# Iterando solo sobre valores
for valor in usuario.values():
    print(valor)

# Este código muestra diferentes formas de iterar sobre un diccionario en Python. En la primera parte, se itera sobre las claves del diccionario y se accede a los valores utilizando la sintaxis usuario[clave]. En la segunda parte, se utiliza el método items() para obtener tanto las claves como los valores en cada iteración. Finalmente, en la tercera parte, se itera directamente sobre los valores del diccionario utilizando el método values().