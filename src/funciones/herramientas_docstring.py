"Herramientas para trabajar con docstrings"

"Python incluye varias herramientas que aprovechan los docstrings:"
" help()**: Muestra la documentación de un objeto" 
" pydoc**: Módulo que genera documentación a partir de docstrings"
"doctest**: Permite ejecutar ejemplos incluidos en los docstrings como pruebas"

def area_triangulo(base, altura):
    """
    Calcula el área de un triángulo.

    Args:
        base: Longitud de la base del triángulo
        altura: Altura del triángulo

    Returns:
        El área del triángulo

    Ejemplos:
        >>> area_triangulo(4, 3)
        6.0
        >>> area_triangulo(5, 8)
        20.0
    """
    return (base * altura) / 2

"Estos ejemplos"
" no solo documentan cómo usar la función, sino que también pueden ejecutarse como pruebas automáticas con el módulo doctest:"

import doctest
doctest.testmod()  # Ejecuta todos los ejemplos en los docstrings como pruebas