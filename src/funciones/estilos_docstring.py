"""Estilos de docstrings Existen varios estilos populares para formatear docstrings. 
Los más comunes son:"""

# 1. Estilo Google:
def validar_email(email):
    """
    Verifica si una dirección de correo electrónico tiene formato válido.

    Args:
        email (str): La dirección de correo a validar

    Returns:
        bool: True si el formato es válido, False en caso contrario

    Raises:
        TypeError: Si email no es una cadena de texto
    """
    if not isinstance(email, str):
        raise TypeError("El email debe ser una cadena de texto")
    return "@" in email and "." in email.split("@")[-1]


# Estilo reStructuredText (reST)
def convertir_a_celsius(fahrenheit):
    """
    Convierte una temperatura de Fahrenheit a Celsius.

    :param fahrenheit: Temperatura en grados Fahrenheit
    :type fahrenheit: float
    :return: Temperatura en grados Celsius
    :rtype: float
    """
    return (fahrenheit - 32) * 5/9

#Estilo NumPy/SciPy
def filtrar_pares(lista):
    """
    Filtra los números pares de una lista.

    Parameters
    ----------
    lista : list
        Lista de números enteros

    Returns
    -------
    list
        Nueva lista que contiene solo los números pares
    """
    return [num for num in lista if num % 2 == 0]

"Para proyectos personales o pequeños, puedes elegir el estilo que prefieras. "
"Para proyectos más grandes o equipos, es recomendable seguir un estilo consistente en todo el código."