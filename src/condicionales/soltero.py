edad = 30
estado_civil = 'soltero'

if edad >= 18:
    if estado_civil == 'casado':
        print('Eres un adulto casado.')
    else:
        print('Eres un adulto soltero.')
else:
    print('Eres menor de edad.')

# Este código verifica la edad y el estado civil de una persona para determinar su categoría. Primero, se verifica si la edad es mayor o igual a 18 años. Si es así, se verifica el estado civil. Si el estado civil es 'casado', se imprime "Eres un adulto casado". Si el estado civil no es 'casado', se asume que es 'soltero' y se imprime "Eres un adulto soltero". Si la edad es menor de 18 años, se imprime "Eres menor de edad". En este caso, como la edad es 30 y el estado civil es 'soltero', se imprimirá "Eres un adulto soltero."