"""Un parámetro es una variable que se define en la declaración de una función. 
Actúa como un espacio reservado 
para los datos que la función necesita
 para realizar su tarea. Por otro lado, 
 un argumento es el 
 valor real que pasamos a la función 
 cuando la llamamos."""

def saludar_persona(nombre):  # 'nombre' es un parámetro
    print(f"Hola, {nombre}!")

saludar_persona("Ana")  # "Ana" es un argumento

# En este ejemplo, 
# nombre es el parámetro
#  (la variable que espera recibir la función) 
# y "Ana" es el argumento (el valor concreto que le pasamos).

