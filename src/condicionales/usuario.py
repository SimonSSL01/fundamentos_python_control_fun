usuario = "admin"
contrasena = "1234"

if usuario == "admin":
    if contrasena == "1234":
        print("Acceso concedido.")

if usuario == "admin" and contrasena == "1234":
    print("Acceso concedido.")

# Este código define dos variables, 'usuario' y 'contrasena', con los valores "admin" y "1234" respectivamente. Luego, utiliza dos estructuras de control 'if' para verificar si el usuario es "admin" y si la contraseña es "1234". En la primera estructura, se verifica primero si el usuario es "admin" y luego, dentro de ese bloque, se verifica si la contraseña es "1234". Si ambas condiciones se cumplen, se imprime "Acceso concedido." En la segunda estructura, se verifica ambas condiciones en una sola línea utilizando el operador 'and'. Si ambas condiciones se cumplen, también se imprime "Acceso concedido." En este caso, como el usuario es "admin" y la contraseña es "1234", ambas estructuras imprimirán "Acceso concedido."