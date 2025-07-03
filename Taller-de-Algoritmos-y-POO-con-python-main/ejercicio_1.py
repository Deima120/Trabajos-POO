
class Persona:
    _dni_counter = 1  

    def __init__(self, documento="", nombre="", edad=0, sexo='M', peso=0.0, altura=0.0):
        self._documento = documento
        self._nombre = nombre
        self._edad = edad
        self._sexo = self._comprobarSexo(sexo)
        self._peso = peso
        self._altura = altura
        self._dni = self._generaDNI()

    @classmethod
    def crearConDatosBasicos(cls, documento, nombre, edad, sexo):
        return cls(documento, nombre, edad, sexo)

    @classmethod
    def crearPorDefecto(cls):
        return cls()

    def _generaDNI(self):
        dni_generado = Persona._dni_counter
        Persona._dni_counter += 1
        return dni_generado

    def _comprobarSexo(self, sexo):
        if sexo.upper() not in ['M', 'F']:
            return 'M'
        return sexo.upper()

    def calcularIMC(self):
        if self._altura <= 0:
            return -1

        imc = self._peso / ((self._altura / 100) ** 2)
        if imc < 18.5:
            return -1
        elif 18.5 <= imc <= 24.9:
            return 0
        elif 25.0 <= imc <= 29.9:
            return 1
        elif 30.0 <= imc <= 39.9:
            return 2
        else:
            return 3

    def esMayorDeEdad(self):
        return self._edad >= 18

    def listarInformacion(self):
        genero = "Masculino" if self._sexo == 'M' else "Femenino"
        imc_resultado = self.calcularIMC()
        categorias = {
            -1: "Por debajo del peso",
            0: "Normal",
            1: "Con sobrepeso",
            2: "Obesidad",
            3: "Obesidad extrema o de alto riesgo"
        }
        categoria_texto = categorias.get(imc_resultado, "Desconocido")

        print(f"\nHola {self._nombre}, tu código dentro del sistema es {self._dni}.")
        print(f"Tu identificación es {self._documento}. Tu edad es {self._edad} años.")
        print(f"Tu género es {genero}. Tu Peso es {self._peso} kg y tu Altura es {self._altura} cm.")
        print(f"Al calcular tu IMC concluimos que tu peso está: {categoria_texto}.")
        print("Mayor de edad:", "Sí" if self.esMayorDeEdad() else "No")

    def setDocumento(self, doc): self._documento = doc
    def setNombre(self, nom): self._nombre = nom
    def setEdad(self, edad): self._edad = edad
    def setSexo(self, sexo): self._sexo = self._comprobarSexo(sexo)
    def setPeso(self, peso): self._peso = peso
    def setAltura(self, altura): self._altura = altura

    def getDocumento(self): return self._documento
    def getNombre(self): return self._nombre
    def getEdad(self): return self._edad
    def getSexo(self): return self._sexo
    def getPeso(self): return self._peso
    def getAltura(self): return self._altura

def crear_persona_por_teclado():
    documento = input("Documento: ")
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    sexo = input("Sexo (M/F): ")
    peso = float(input("Peso (kg): "))
    altura = float(input("Altura (cm): "))
    return Persona(documento, nombre, edad, sexo, peso, altura)

def main():
    print("\n INGRESA DATOS PARA LA PRIMERA PERSONA ")
    persona1 = crear_persona_por_teclado()

    print("\nSEGUNDA PERSONA")
    doc2 = input("Documento: ")
    nom2 = input("Nombre: ")
    edad2 = int(input("Edad: "))
    sexo2 = input("Sexo (M/F): ")
    persona2 = Persona.crearConDatosBasicos(doc2, nom2, edad2, sexo2)

    print("\n TERCERA PERSONA ")
    persona3 = Persona.crearPorDefecto()
    persona3.setDocumento("123456")
    persona3.setNombre("Emanuel Garcia")
    persona3.setEdad(30)
    persona3.setSexo("M")
    persona3.setPeso(80)
    persona3.setAltura(175)

    for i, persona in enumerate([persona1, persona2, persona3], 1):
        print(f"\n INFORMACIÓN DE LA PERSONA {i}")
        persona.listarInformacion()

    while True:
        opcion = input("\n¿Deseas ingresar otra persona? (S/N): ").upper()
        if opcion == 'S':
            nueva = crear_persona_por_teclado()
            nueva.listarInformacion()
        else:
            print("Fin del programa.")
            break

if __name__ == "__main__":
    main()


