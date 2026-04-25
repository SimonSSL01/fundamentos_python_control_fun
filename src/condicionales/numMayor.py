a = 5
b = 10
c = 15

if a > b:
    if a > c:
        print('a es el mayor.')
    else:
        if c > b:
            print('c es el mayor.')
        else:
            print('b es el mayor.')
else:
    if b > c:
        print('b es el mayor.')
    else:
        print('c es el mayor.')

# Este código compara tres números, 'a', 'b' y 'c', para determinar cuál de ellos es el mayor. Primero, se compara 'a' con 'b'. Si 'a' es mayor que 'b', se compara 'a' con 'c' para determinar si 'a' es el mayor. Si 'a' no es mayor que 'c', se compara 'c' con 'b' para determinar si 'c' es el mayor o si 'b' es el mayor. Si 'a' no es mayor que 'b', se compara 'b' con 'c' para determinar si 'b' es el mayor o si 'c' es el mayor. En este caso, como 'c' es el número más grande, se imprimirá "c es el mayor."

mayor = a

if b > mayor:
    mayor = b

if c > mayor:
    mayor = c

print(f'El número mayor es {mayor}.')

# Este código también compara los números 'a', 'b' y 'c' para encontrar el mayor, pero lo hace de una manera más eficiente. Primero, se asigna el valor de 'a' a la variable 'mayor'. Luego, se compara 'b' con 'mayor'. Si 'b' es mayor que 'mayor', se actualiza el valor de 'mayor' a 'b'. Después, se compara 'c' con 'mayor'. Si 'c' es mayor que 'mayor', se actualiza el valor de 'mayor' a 'c'. Finalmente, se imprime el número mayor utilizando una f-string. En este caso, como 'c' es el número más grande, se imprimirá "El número mayor es 15."