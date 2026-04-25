"""Podemos especificar explícitamente 
qué valor corresponde a cada parámetro,
 independientemente del orden:"""

def dividir(dividendo, divisor):
    return dividendo / divisor

# Usando argumentos posicionales
resultado1 = dividir(10, 2)  # resultado1 = 5.0

# Usando argumentos por nombre
resultado2 = dividir(divisor=2, dividendo=10)  # resultado2 = 5.0

"""Los argumentos por nombre son especialmente 
útiles cuando una función tiene muchos parámetros o cuando 
queremos hacer que nuestro código sea más legible:"""

def crear_usuario(nombre, apellido, edad, email, activo=True):
    return {
        "nombre_completo": f"{nombre} {apellido}",
        "edad": edad,
        "email": email,
        "activo": activo
    }

# Más fácil de leer con argumentos por nombre
usuario = crear_usuario(
    nombre="Juan",
    apellido="Pérez",
    edad=28,
    email="juan@ejemplo.com",
    activo=False
)