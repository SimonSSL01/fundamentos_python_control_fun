usuario = 'admin'
contrasena = '1234'

if usuario == 'admin':
    if contrasena == '1234':
        print('Acceso concedido.')
    else:
        print('Contraseña incorrecta.')
else:
    print('Usuario no reconocido.')

# Este código define dos variables, 'usuario' y 'contrasena', con los valores "admin" y "1234" respectivamente. Luego, utiliza una estructura de control 'if' para verificar si el usuario es "admin". Si es así, se verifica si la contraseña es "1234". Si ambas condiciones se cumplen, se imprime "Acceso concedido." Si el usuario es "admin" pero la contraseña no es "1234", se imprime "Contraseña incorrecta." Si el usuario no es "admin", se imprime "Usuario no reconocido." En este caso, como el usuario es "admin" y la contraseña es "1234", se imprimirá "Acceso concedido."