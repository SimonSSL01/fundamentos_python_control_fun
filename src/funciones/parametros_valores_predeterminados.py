# Permiten especificar un valor por defecto 
# que se usará si no se proporciona un argumento:

def saludar(nombre, mensaje="¡Bienvenido!"):
    print(f"Hola {nombre}. {mensaje}")

saludar("Carlos")  # Usa el mensaje predeterminado
# Imprime: Hola Carlos. ¡Bienvenido!

saludar("María", "¿Cómo estás hoy?")  # Usa el mensaje personalizado
# Imprime: Hola María. ¿Cómo estás hoy?

"""Los parámetros con valores predeterminados deben aparecer después 
de los parámetros sin valores predeterminados:"""

# Correcto
def crear_perfil(nombre, edad, ciudad="Madrid"):
    return f"Perfil: {nombre}, {edad} años, {ciudad}"# Incorrecto - causaría un error de sintaxis
# def crear_perfil(nombre, ciudad="Madrid", edad):
#     return f"Perfil: {nombre}, {edad} años, {ciudad}"