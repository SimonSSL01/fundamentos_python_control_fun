saldo = 300
retiro = 500
if saldo >= retiro:
    saldo -= retiro
    print("Retiro exitoso.")
    print(f"Nuevo saldo: {saldo}")
else:
    print("Fondos insuficientes.")
    print(f"Saldo actual: {saldo}")

# Este código verifica si el saldo es suficiente para realizar un retiro. Si el saldo es mayor o igual al monto del retiro, se realiza el retiro y se muestra el nuevo saldo. De lo contrario, se muestra un mensaje indicando que los fondos son insuficientes y se muestra el saldo actual.