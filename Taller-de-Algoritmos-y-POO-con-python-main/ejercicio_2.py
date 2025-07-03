class Cuenta:
    _numeroCuentaActual = 100001  

    def __init__(self, dni="", saldo=0.0, interes_anual=0.0):
        self._numero_cuenta = Cuenta._numeroCuentaActual
        Cuenta._numeroCuentaActual += 1

        self._dni = dni
        self._saldo = saldo
        self._interes_anual = interes_anual

    def actualizarSaldo(self):
        interes_diario = self._interes_anual / 365
        self._saldo += self._saldo * (interes_diario / 100)

    def ingresar(self, cantidad):
        if cantidad > 0:
            self._saldo += cantidad
            print(f"Se ingresaron ${cantidad:.2f} correctamente.")
        else:
            print("La cantidad debe ser positiva.")

    def retirar(self, cantidad):
        if cantidad <= self._saldo:
            self._saldo -= cantidad
            print(f"Se retiraron ${cantidad:.2f} correctamente.")
        else:
            print("Saldo insuficiente.")

    def mostrarDatos(self):
        print("\nDATOS DE LA CUENTA ")
        print(f"Número de cuenta: {self._numero_cuenta}")
        print(f"DNI del cliente: {self._dni}")
        print(f"Saldo actual: ${self._saldo:.2f}")
        print(f"Interés anual: {self._interes_anual:.2f}%")


def crearCuenta():
    dni = input("Ingrese el documento de identidad (DNI): ")
    saldo = float(input("Ingrese el saldo inicial: "))
    interes = float(input("Ingrese el interés anual (%): "))
    cuenta = Cuenta(dni, saldo, interes)
    print("\nCuenta creada correctamente.")
    return cuenta

def menu():
    cuenta = crearCuenta()

    while True:
        print("""
 MENÚ DE CUENTA BANCARIA 
1. Mostrar datos de la cuenta
2. Ingresar dinero
3. Retirar dinero
4. Actualizar saldo con interés diario
5. Salir
""")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            cuenta.mostrarDatos()
        elif opcion == "2":
            cantidad = float(input("Ingrese la cantidad a ingresar: "))
            cuenta.ingresar(cantidad)
        elif opcion == "3":
            cantidad = float(input("Ingrese la cantidad a retirar: "))
            cuenta.retirar(cantidad)
        elif opcion == "4":
            cuenta.actualizarSaldo()
            print("Saldo actualizado con interés diario.")
        elif opcion == "5":
            print("Saliendo del sistema. ¡Gracias!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
