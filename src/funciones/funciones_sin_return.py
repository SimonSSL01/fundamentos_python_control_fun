# Si una función no incluye una sentencia 
# return explícita, 
# Python automáticamente devuelve None:

def saludar(nombre):
    print(f"Hola, {nombre}")
    # No hay return explícito

resultado = saludar("Laura")
print(f"La función devolvió: {resultado}")  # Imprime: La función devolvió: None

"""Esto muestra una distinción importante: la función saludar muestra un mensaje pero no devuelve ningún valor utilizable. Esto es adecuado para funciones que realizan acciones (como imprimir o guardar datos) 
pero no necesitan proporcionar un resultado."""