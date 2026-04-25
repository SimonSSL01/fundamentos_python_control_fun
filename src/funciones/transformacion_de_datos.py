"Las funciones que "
"transforman datos de un formato a otro son muy comunes:"

def formato_nombre(nombre, apellido):
    return f"{apellido.upper()}, {nombre.capitalize()}"

print(formato_nombre("ana", "garcía"))  # Imprime: GARCÍA, Ana