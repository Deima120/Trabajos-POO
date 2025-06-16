class Cafetera:
    def __init__(self, capacidad_maxima=1000, cantidad_actual=0):
        self.capacidad_maxima = capacidad_maxima
        self.cantidad_actual = min(cantidad_actual, capacidad_maxima)
    
    def llenar_cafetera(self):
        self.cantidad_actual = self.capacidad_maxima
    
    def servir_taza(self, capacidad_taza):
        servido = min(self.cantidad_actual, capacidad_taza)
        self.cantidad_actual -= servido
        return servido
    
    def vaciar_cafetera(self):
        self.cantidad_actual = 0
    
    def agregar_cafe(self, cantidad):
        self.cantidad_actual = min(self.cantidad_actual + cantidad, self.capacidad_maxima)
    
    def __str__(self):
        return f"☕ {self.cantidad_actual}/{self.capacidad_maxima}cc"


def main():
    cafetera = Cafetera()
    
    menu = {
        "1": ("Llenar", lambda: cafetera.llenar_cafetera()),
        "2": ("Servir", lambda: print(f"Servido: {cafetera.servir_taza(int(input('Capacidad taza: ')))}cc")),
        "3": ("Vaciar", lambda: cafetera.vaciar_cafetera()),
        "4": ("Agregar", lambda: cafetera.agregar_cafe(int(input("Cantidad: ")))),
        "5": ("Estado", lambda: print(cafetera))
    }
    
    while True:
        print(f"\n☕ CAFETERA: {cafetera}")
        [print(f"{k}. {v[0]}") for k, v in menu.items()]
        print("6. Salir")
        
        try:
            op = input("Opción: ")
            if op == "6": break
            if op in menu:
                menu[op][1]()
                print("✅ Hecho")
        except Exception as e:
            print(f"❌ {e}")


if __name__ == "__main__":
    # Demo rápida
    c = Cafetera(500, 100)
    print(f"Inicial: {c}")
    c.llenar_cafetera()
    print(f"Llena: {c}")
    print(f"Servido: {c.servir_taza(200)}cc -> {c}")
    c.agregar_cafe(100)
    print(f"Agregado: {c}")
    c.vaciar_cafetera()
    print(f"Vacía: {c}")
    
    print("\n" + "="*30)
    main()