saldo = 1000
while saldo > 0:
    print(f"Saldo actual: {saldo}€")
    gasto = float(input("Introduce la cantidad a gastar (0 para salir): "))

    if gasto == 0:
        break  # Salimos del bucle inmediatamente

    if gasto > saldo:
        print("No tienes suficiente saldo.")
        continue  # Volvemos al inicio del bucle

    saldo -= gasto

print(f"Saldo final: {saldo}€")

# Este código simula un sistema de control de gastos. El usuario tiene un saldo inicial de 1000€. El programa utiliza un bucle while que continúa ejecutándose mientras el saldo sea mayor que 0. En cada iteración, se muestra el saldo actual y se solicita al usuario que introduzca una cantidad a gastar. Si el usuario introduce 0, el bucle se rompe y el programa termina. Si el gasto es mayor que el saldo disponible, se muestra un mensaje de error y se vuelve al inicio del bucle para solicitar una nueva cantidad. Si el gasto es válido, se resta del saldo. Al final, se muestra el saldo final después de las operaciones realizadas.