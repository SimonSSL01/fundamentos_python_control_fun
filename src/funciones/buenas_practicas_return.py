"Coherencia en los tipos de retorno:"
" Es recomendable que una función devuelva siempre el mismo tipo de datos, o tipos compatibles."

# Enfoque mejorado: siempre devuelve una lista (vacía en caso de error)
def filtrar_positivos(numeros):
    if not isinstance(numeros, list):
        return []  # Lista vacía en caso de error

    return [num for num in numeros if num > 0]

"Documentar el valor de retorno: Es importante que quede claro qué devuelve la función."
def calcular_descuento(precio, porcentaje):
    """
    Calcula el precio con descuento.

    Args:
        precio: El precio original
        porcentaje: El porcentaje de descuento (0-100)

    Returns:
        float: El precio después de aplicar el descuento
    """
    return precio - (precio * porcentaje / 100)

"Evitar efectos secundarios:"
" Las funciones que devuelven valores no deberían, idealmente,"
" modificar el estado global o realizar acciones como imprimir."
# Mejor: separar la obtención del resultado de su presentación
def calcular_promedio(numeros):
    return sum(numeros) / len(numeros)

# Uso
notas = [7, 8, 6, 9]
promedio = calcular_promedio(notas)
print(f"El promedio es: {promedio}")  # La impresión se hace fuera de la función

"Usar return temprano para casos especiales: Esto mejora la legibilidad del código."
def obtener_calificacion(puntuacion):
    if puntuacion < 0 or puntuacion > 100:
        return "Puntuación inválida"

    if puntuacion >= 90:
        return "Sobresaliente"
    if puntuacion >= 70:
        return "Notable"
    if puntuacion >= 60:
        return "Bien"
    if puntuacion >= 50:
        return "Suficiente"

    return "Insuficiente"