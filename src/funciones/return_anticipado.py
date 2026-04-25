""" La sentencia return finaliza inmediatamente la ejecución de la función. 
Esto es útil para crear 
salidas anticipadas cuando se cumplen ciertas condiciones:"""

def dividir_seguro(a, b):
    # Verificación de seguridad
    if b == 0:
        print("Error: División por cero")
        return None  # Salida anticipada

    # Este código solo se ejecuta si b no es cero
    resultado = a / b
    return resultado

print(dividir_seguro(10, 2))   # Imprime: 5.0
print(dividir_seguro(10, 0))   # Imprime: Error: División por cero y luego None

"""Esta técnica de retorno 
anticipado es muy útil para 
validaciones y manejo de casos especiales, 
ya que evita el anidamiento 
excesivo de bloques condicionales."""

