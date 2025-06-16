class Cuenta:
    _siguiente_numero = 100001
    
    def __init__(self, dni="", saldo=0.0, interes=0.0):
        self.numero_cuenta = Cuenta._siguiente_numero
        Cuenta._siguiente_numero += 1
        self.dni = dni
        self.saldo = saldo
        self.interes_anual = interes
    
    def actualizar_saldo(self):
        interes_diario = (self.interes_anual / 365) / 100
        self.saldo += self.saldo * interes_diario
        return self.saldo
    
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            return True
        raise ValueError("Cantidad debe ser mayor que 0")
    
    def retirar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("Cantidad debe ser mayor que 0")
        if cantidad > self.saldo:
            raise ValueError("Saldo insuficiente")
        self.saldo -= cantidad
        return True
    
    def mostrar_datos(self):
        return f"Cuenta: {self.numero_cuenta} | DNI: {self.dni} | Saldo: €{self.saldo:.2f} | Interés: {self.interes_anual}%"


# Sistema de gestión
cuentas = {}

def crear_cuenta():
    dni = input("DNI: ")
    saldo = float(input("Saldo inicial (€): ") or "0")
    interes = float(input("Interés anual (%): ") or "0")
    cuenta = Cuenta(dni, saldo, interes)
    cuentas[cuenta.numero_cuenta] = cuenta
    print(f"✅ Cuenta {cuenta.numero_cuenta} creada")

def buscar_cuenta():
    num = int(input("Número de cuenta: "))
    if num in cuentas:
        return cuentas[num]
    print("❌ Cuenta no encontrada")
    return None

def main():
    menu = {
        "1": ("Crear cuenta", crear_cuenta),
        "2": ("Mostrar datos", lambda: print(buscar_cuenta().mostrar_datos()) if buscar_cuenta() else None),
        "3": ("Ingresar", lambda: buscar_cuenta().ingresar(float(input("Cantidad: €"))) if buscar_cuenta() else None),
        "4": ("Retirar", lambda: buscar_cuenta().retirar(float(input("Cantidad: €"))) if buscar_cuenta() else None),
        "5": ("Actualizar saldo", lambda: print(f"Nuevo saldo: €{buscar_cuenta().actualizar_saldo():.2f}") if buscar_cuenta() else None),
        "6": ("Listar cuentas", lambda: [print(c.mostrar_datos()) for c in cuentas.values()] or print("Sin cuentas") if not cuentas else None)
    }
    
    while True:
        print("\n🏦 BANCO")
        [print(f"{k}. {v[0]}") for k, v in menu.items()]
        print("7. Salir")
        
        try:
            opcion = input("Opción: ")
            if opcion == "7":
                break
            if opcion in menu:
                menu[opcion][1]()
                print("✅ Operación completada")
            else:
                print("❌ Opción inválida")
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()