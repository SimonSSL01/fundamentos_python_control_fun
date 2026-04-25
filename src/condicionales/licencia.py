edad = 17
permiso_parental = True

if (edad >= 18) or (edad >= 16 and permiso_parental):
    print("Puedes obtener la licencia de conducir.")
else:
    print("No cumples los requisitos para la licencia.")

# Este código verifica si una persona cumple con los requisitos para obtener una licencia de conducir. La persona puede obtener la licencia si tiene 18 años o más, o si tiene al menos 16 años y cuenta con permiso parental. Si alguna de estas condiciones se cumple, se imprime un mensaje indicando que la persona puede obtener la licencia de conducir. De lo contrario, se imprime un mensaje indicando que no cumple con los requisitos para la licencia. En este caso, como 'edad' es igual a 17 y 'permiso_parental' es True, se imprimirá "Puedes obtener la licencia de conducir."