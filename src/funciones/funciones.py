# En Python, las funciones son **ciudadanos de primera clase**, lo que significa que pueden ser:

# Asignadas a variables
# Pasadas como argumentos a otras funciones
# Devueltas como resultado de otras funciones

# Asignar una función a una variable
convertir = celsius_a_fahrenheit 
temperatura_f = convertir(25) # Equivalente a celsius_a_fahrenheit(25)
print(f"25°C equivalen a {temperatura_f}°F") # Imprime: 25°C equivalen a 77.0°F

"""Las funciones en Python también pueden tener un ámbito (scope), lo que significa que las variables definidas dentro 
de una función solo existen dentro de esa función,
 a menos que se devuelvan explícitamente."""

def calcular_descuento(precio, porcentaje=10):
    # La variable 'descuento' solo existe dentro de esta función
    descuento = precio * (porcentaje / 100)
    precio_final = precio - descuento
    return precio_final

precio_con_descuento = calcular_descuento(100)
print(f"Precio con descuento: {precio_con_descuento}")  # Imprime: Precio con descuento: 90.0
# print(descuento)  # Esto daría error porque 'descuento' no existe fuera de la función

