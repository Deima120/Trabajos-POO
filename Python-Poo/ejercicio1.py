class Persona:
    _contador_dni = 0
    
    def __init__(self, documento="", nombre="", edad=0, sexo='M', peso=0.0, altura=0.0):
        self.documento = documento
        self.nombre = nombre
        self.edad = edad
        self.sexo = 'M' if sexo.upper() not in ['M', 'F'] else sexo.upper()
        self.peso = peso
        self.altura = altura
        Persona._contador_dni += 1
        self.dni = Persona._contador_dni
    
    def calcular_imc(self):
        """Calcula IMC: -1=Bajo, 0=Normal, 1=Sobrepeso, 2=Obesidad, 3=Extrema"""
        if self.peso <= 0 or self.altura <= 0:
            return 0
        
        imc = self.peso / ((self.altura / 100) ** 2)
        
        if imc < 18.5: return -1
        elif imc <= 24.9: return 0
        elif imc <= 29.9: return 1
        elif imc <= 39.9: return 2
        else: return 3
    
    def es_mayor_de_edad(self):
        return self.edad >= 18
    
    def info(self):
        categorias = {-1: "Bajo peso", 0: "Normal", 1: "Sobrepeso", 2: "Obesidad", 3: "Obesidad extrema"}
        genero = "Masculino" if self.sexo == 'M' else "Femenino"
        
        return (f"👤 {self.nombre} (ID: {self.dni}) | Doc: {self.documento} | "
                f"Edad: {self.edad} | {genero} | {self.peso}kg, {self.altura}cm | "
                f"IMC: {categorias[self.calcular_imc()]} | "
                f"{'✅ Mayor' if self.es_mayor_de_edad() else '❌ Menor'}")


def crear_personas():
    """Crea y muestra 3 personas con diferentes constructores"""
    print("📝 Ingrese datos:")
    doc = input("Documento: ")
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    sexo = input("Sexo (M/F): ")
    peso = float(input("Peso (kg): "))
    altura = float(input("Altura (cm): "))
    
    # 3 formas de crear personas
    personas = [
        Persona(doc, nombre, edad, sexo, peso, altura),  # Completa
        Persona(doc, nombre, edad, sexo),                # Sin peso/altura
        Persona()                                        # Vacía
    ]
    
    # Configurar la tercera persona
    personas[2].documento = doc
    personas[2].nombre = nombre
    personas[2].edad = edad
    personas[2].sexo = sexo
    personas[2].peso = peso
    personas[2].altura = altura
    
    # Mostrar todas
    print(f"\n{'='*80}")
    for i, p in enumerate(personas, 1):
        print(f"{i}. {p.info()}")
    print(f"{'='*80}")


def main():
    print("🧑‍💼 SISTEMA DE PERSONAS")
    
    while True:
        try:
            crear_personas()
            if input("\n¿Otra persona? (s/n): ").lower() != 's':
                break
        except ValueError:
            print("❌ Error: Ingrese números válidos")
        except KeyboardInterrupt:
            print("\n👋 ¡Adiós!")
            break
    
    print("✅ Fin del programa")


if __name__ == "__main__":
    main()