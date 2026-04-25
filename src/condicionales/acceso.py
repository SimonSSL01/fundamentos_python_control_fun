acceso_registrado = True

acceso_permitido = False

if acceso_permitido or acceso_registrado:
    print("Acceso concedido.")

# Este código define dos variables booleanas, 'acceso_registrado' y 'acceso_permitido', con los valores True y False respectivamente. Luego, utiliza una estructura de control 'if' para verificar si al menos una de las condiciones es verdadera (es decir, si 'acceso_permitido' es True o 'acceso_registrado' es True). En este caso, como 'acceso_registrado' es True, la condición se cumple y se imprimirá "Acceso concedido."

if acceso_permitido:
    print("Acceso concedido.")
else:
    if acceso_registrado:
        print("Acceso concedido.")

# Este código utiliza una estructura de control 'if-else' anidada para verificar las condiciones de acceso. Primero, se verifica si 'acceso_permitido' es True; si es así, se imprime "Acceso concedido." Si 'acceso_permitido' es False, se entra en el bloque 'else', donde se verifica si 'acceso_registrado' es True. Si 'acceso_registrado' es True, también se imprime "Acceso concedido." En este caso, como 'acceso_permitido' es False pero 'acceso_registrado' es True, se imprimirá "Acceso concedido."

if acceso_permitido or (acceso_registrado and True):
    print("Acceso concedido.")

# Este código utiliza una estructura de control 'if' para verificar si se cumple al menos una de las siguientes condiciones: 'acceso_permitido' es True, o 'acceso_registrado' es True y la condición adicional (que es simplemente True) también se cumple. En este caso, como 'acceso_registrado' es True, la condición dentro del paréntesis se evalúa como True, lo que hace que toda la expresión sea True. Por lo tanto, se imprimirá "Acceso concedido."