"""Aunque Python no impone un formato específico para los docstrings,
 existen convenciones ampliamente aceptadas. Un docstring completo suele incluir:

1. Una breve descripción de una línea
2. Una descripción más detallada (opcional)
3. Información sobre los parámetros
4. Información sobre el valor de retorno
5. Ejemplos o notas (opcional)"""

def calcular_promedio(numeros):
    """
    Calcula el promedio de una lista de números.

    Suma todos los números de la lista y divide el resultado
    entre la cantidad de elementos.

    Args:
        numeros: Una lista de valores numéricos

    Returns:
        El promedio como valor flotante

    Ejemplo:
        >>> calcular_promedio([1, 2, 3, 4])
        2.5
    """
    return sum(numeros) / len(numeros)