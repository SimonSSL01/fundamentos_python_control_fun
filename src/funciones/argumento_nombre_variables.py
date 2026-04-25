# Argumentos por nombre variables (**kwargs)

# Permite que una función acepte cualquier 
# número de argumentos por nombre:

def mostrar_informacion(**datos):
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

# Podemos pasar cualquier cantidad de argumentos por nombre
mostrar_informacion(nombre="Python", creador="Guido van Rossum", año=1991)
# Imprime:
# nombre: Python
# creador: Guido van Rossum
# año: 1991

# El parámetro **datos recibe 
# todos los argumentos por nombre como 
# un diccionario.

