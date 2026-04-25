usuarios = [
    {"nombre": "Ana", "rol": "admin"},
    {"nombre": "Luis", "rol": "usuario"},
    {"nombre": "Marta", "rol": "moderador"}
]

for usuario in usuarios:
    match usuario:
        case {"rol": "admin"}:
            print(f"{usuario['nombre']} tiene permisos de administrador.")
        case {"rol": "moderador"}:
            print(f"{usuario['nombre']} puede moderar contenidos.")
        case {"rol": "usuario"}:
            print(f"{usuario['nombre']} es un usuario regular.")
        case _:
            print(f"Rol de {usuario['nombre']} desconocido.")

# Este código define una lista de diccionarios, donde cada diccionario representa a un usuario con su nombre y rol. Luego, utiliza un bucle 'for' para iterar sobre cada usuario y una estructura de control 'match' para determinar el rol de cada usuario. Dependiendo del rol, se imprime un mensaje indicando los permisos o características del usuario. Si el rol no coincide con ninguno de los casos definidos, se imprime un mensaje indicando que el rol es desconocido.