"Sé conciso pero completo: Incluye toda la información necesaria sin ser excesivamente detallado."

def generar_contraseña(longitud=8):
    """
    Genera una contraseña aleatoria.

    Args:
        longitud: Número de caracteres de la contraseña (predeterminado: 8)

    Returns:
        Una cadena con la contraseña generada
    """
    import random
    import string
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(longitud))

" Usa verbos en presente: Describe lo que la función hace, no lo que hará o hizo" 

# Bien
def validar_usuario(nombre):
    """Verifica si el nombre de usuario cumple con los requisitos."""

# Evitar
def validar_usuario(nombre):
    """Esta función verificará si el nombre de usuario cumple con los requisitos."""


"Documenta los tipos de datos: Especifica qué tipos de datos espera la función y qué tipo devuelve"

def contar_palabras(texto):
    """
    Cuenta el número de palabras en un texto.

    Args:
        texto (str): El texto a analizar

    Returns:
        int: El número de palabras encontradas
    """
    return len(texto.split())

"Incluye ejemplos prácticos: Los ejemplos ayudan a entender rápidamente cómo usar la función."

def formatear_nombre(nombre, apellido):
    """
    Formatea un nombre completo en formato "Apellido, Nombre".

    Args:
        nombre: Nombre de la persona
        apellido: Apellido de la persona

    Returns:
        Cadena formateada como "Apellido, Nombre"

    Ejemplo:
        >>> formatear_nombre("Juan", "Pérez")
        'Pérez, Juan'
    """
    return f"{apellido}, {nombre}"

"Documenta excepciones: Si tu función puede lanzar excepciones, indícalo en el docstring."

def obtener_elemento(lista, indice):
    """
    Obtiene un elemento de una lista por su índice.

    Args:
        lista: La lista de elementos
        indice: Posición del elemento a obtener (comienza en 0)

    Returns:
        El elemento en la posición especificada

    Raises:
        IndexError: Si el índice está fuera del rango de la lista
    """
    return lista[indice]