class Cafetera:
    def __init__(self, capacidadMaxima=1000, cantidadActual=0):
        self.capacidadMaxima = capacidadMaxima
        if cantidadActual > capacidadMaxima:
            self.cantidadActual = capacidadMaxima
        else:
            self.cantidadActual = cantidadActual

    def llenarCafetera(self):
        self.cantidadActual = self.capacidadMaxima
        print("La cafetera se llenó completamente.")

    def servirTaza(self, tamanoTaza):
        if self.cantidadActual >= tamanoTaza:
            self.cantidadActual -= tamanoTaza
            print(f"Taza de {tamanoTaza} c.c. servida completamente.")
        else:
            print(f"No hay suficiente café. Solo se sirvieron {self.cantidadActual} c.c.")
            self.cantidadActual = 0

    def vaciarCafetera(self):
        self.cantidadActual = 0
        print("La cafetera se ha vaciado.")

    def agregarCafe(self, cantidad):
        if cantidad <= 0:
            print("No se puede agregar una cantidad negativa o cero.")
            return

        if self.cantidadActual + cantidad > self.capacidadMaxima:
            print(f"La cafetera se llenó. Se desperdiciaron {self.cantidadActual + cantidad - self.capacidadMaxima} c.c.")
            self.cantidadActual = self.capacidadMaxima
        else:
            self.cantidadActual += cantidad
            print(f"Se agregaron {cantidad} c.c. de café a la cafetera.")

    def mostrarEstado(self):
        print(f"\nCapacidad máxima: {self.capacidadMaxima} c.c.")
        print(f"Cantidad actual: {self.cantidadActual} c.c.\n")


def main():
    print("Inicializando cafetera...")
    cafetera = Cafetera() 

    while True:
        print("""
--- MENÚ DE CAFETERA ---
1. Llenar cafetera
2. Servir taza
3. Vaciar cafetera
4. Agregar café
5. Mostrar estado
6. Salir
""")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            cafetera.llenarCafetera()
        elif opcion == "2":
            taza = int(input("Tamaño de la taza en c.c.: "))
            cafetera.servirTaza(taza)
        elif opcion == "3":
            cafetera.vaciarCafetera()
        elif opcion == "4":
            cantidad = int(input("Cantidad de café a agregar: "))
            cafetera.agregarCafe(cantidad)
        elif opcion == "5":
            cafetera.mostrarEstado()
        elif opcion == "6":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
