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
        try:
            if sexo.upper() not in ['M', 'F']:
                return 'M'
            return sexo.upper()
        except (AttributeError, TypeError):
            return 'M'

    def calcularIMC(self):
        try:
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
        except (TypeError, ZeroDivisionError, ValueError):
            return -1

    def esMayorDeEdad(self):
        try:
            return self._edad >= 18
        except (TypeError, ValueError):
            return False

    def listarInformacion(self):
        try:
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
        except Exception as e:
            print(f"Error al mostrar información: {e}")

    def setDocumento(self, doc): 
        try:
            doc_str = str(doc).strip()
            if not doc_str:
                print("Error: El documento no puede estar vacío")
                return
            if not doc_str.isdigit():
                print("Error: El documento solo puede contener números")
                return
            self._documento = doc_str
        except (TypeError, ValueError):
            print("Error: Documento inválido")
    
    def setNombre(self, nom): 
        try:
            nom_str = str(nom).strip()
            if not nom_str:
                print("Error: El nombre no puede estar vacío")
                return
            if not nom_str.replace(" ", "").isalpha():
                print("Error: El nombre solo puede contener letras")
                return
            self._nombre = nom_str
        except (TypeError, ValueError):
            print("Error: Nombre inválido")
    
    def setEdad(self, edad): 
        try:
            edad_int = int(edad)
            if edad_int < 0:
                print("Error: La edad no puede ser negativa")
                return
            if edad_int > 150:
                print("Error: La edad no puede ser mayor a 150 años")
                return
            self._edad = edad_int
        except (TypeError, ValueError):
            print("Error: Edad debe ser un número entero")
    
    def setSexo(self, sexo): 
        self._sexo = self._comprobarSexo(sexo)
    
    def setPeso(self, peso): 
        try:
            peso_float = float(peso)
            if peso_float <= 0:
                print("Error: El peso debe ser mayor a 0")
                return
            if peso_float > 1000:
                print("Error: El peso no puede ser mayor a 1000 kg")
                return
            self._peso = peso_float
        except (TypeError, ValueError):
            print("Error: Peso debe ser un número")
    
    def setAltura(self, altura): 
        try:
            altura_float = float(altura)
            if altura_float <= 0:
                print("Error: La altura debe ser mayor a 0")
                return
            if altura_float > 300:
                print("Error: La altura no puede ser mayor a 300 cm")
                return
            self._altura = altura_float
        except (TypeError, ValueError):
            print("Error: Altura debe ser un número")

    def getDocumento(self): return self._documento
    def getNombre(self): return self._nombre
    def getEdad(self): return self._edad
    def getSexo(self): return self._sexo
    def getPeso(self): return self._peso
    def getAltura(self): return self._altura

def validar_documento(documento):
    """Valida que el documento solo contenga números"""
    documento = documento.strip()
    if not documento:
        return False, "El documento no puede estar vacío"
    if not documento.isdigit():
        return False, "El documento solo puede contener números"
    return True, documento

def validar_nombre(nombre):
    """Valida que el nombre solo contenga letras y espacios"""
    nombre = nombre.strip()
    if not nombre:
        return False, "El nombre no puede estar vacío"
    if not nombre.replace(" ", "").isalpha():
        return False, "El nombre solo puede contener letras"
    return True, nombre

def validar_edad(edad_str):
    """Valida que la edad sea un número entero válido"""
    try:
        edad = int(edad_str)
        if edad < 0:
            return False, "La edad no puede ser negativa"
        if edad > 150:
            return False, "La edad no puede ser mayor a 150 años"
        return True, edad
    except ValueError:
        return False, "La edad debe ser un número entero"

def validar_peso(peso_str):
    """Valida que el peso sea un número válido"""
    try:
        peso = float(peso_str)
        if peso <= 0:
            return False, "El peso debe ser mayor a 0"
        if peso > 1000:
            return False, "El peso no puede ser mayor a 1000 kg"
        return True, peso
    except ValueError:
        return False, "El peso debe ser un número"

def validar_altura(altura_str):
    """Valida que la altura sea un número válido"""
    try:
        altura = float(altura_str)
        if altura <= 0:
            return False, "La altura debe ser mayor a 0"
        if altura > 300:
            return False, "La altura no puede ser mayor a 300 cm"
        return True, altura
    except ValueError:
        return False, "La altura debe ser un número"

def crear_persona_por_teclado():
    while True:
        try:
            # Validar documento
            while True:
                documento_input = input("Documento: ")
                valido, resultado = validar_documento(documento_input)
                if valido:
                    documento = resultado
                    break
                else:
                    print(f"Error: {resultado}")
            
            # Validar nombre
            while True:
                nombre_input = input("Nombre: ")
                valido, resultado = validar_nombre(nombre_input)
                if valido:
                    nombre = resultado
                    break
                else:
                    print(f"Error: {resultado}")
            
            # Validar edad
            while True:
                edad_input = input("Edad: ")
                valido, resultado = validar_edad(edad_input)
                if valido:
                    edad = resultado
                    break
                else:
                    print(f"Error: {resultado}")
            
            # Validar sexo
            while True:
                sexo = input("Sexo (M/F): ").upper().strip()
                if sexo in ['M', 'F']:
                    break
                else:
                    print("Error: Por favor ingresa 'M' para Masculino o 'F' para Femenino")
            
            # Validar peso
            while True:
                peso_input = input("Peso (kg): ")
                valido, resultado = validar_peso(peso_input)
                if valido:
                    peso = resultado
                    break
                else:
                    print(f"Error: {resultado}")
            
            # Validar altura
            while True:
                altura_input = input("Altura (cm): ")
                valido, resultado = validar_altura(altura_input)
                if valido:
                    altura = resultado
                    break
                else:
                    print(f"Error: {resultado}")
            
            return Persona(documento, nombre, edad, sexo, peso, altura)
            
        except KeyboardInterrupt:
            print("\nOperación cancelada por el usuario")
            return None
        except Exception as e:
            print(f"Error inesperado: {e}")
            print("Intenta nuevamente")

def main():
    try:
        print("\n INGRESA DATOS PARA LA PRIMERA PERSONA ")
        persona1 = crear_persona_por_teclado()
        
        if persona1 is None:
            print("No se pudo crear la primera persona")
            return

        print("\nSEGUNDA PERSONA")
        
        # Validar documento de la segunda persona
        while True:
            doc2_input = input("Documento: ")
            valido, resultado = validar_documento(doc2_input)
            if valido:
                doc2 = resultado
                break
            else:
                print(f"Error: {resultado}")
        
        # Validar nombre de la segunda persona
        while True:
            nom2_input = input("Nombre: ")
            valido, resultado = validar_nombre(nom2_input)
            if valido:
                nom2 = resultado
                break
            else:
                print(f"Error: {resultado}")
        
        # Validar edad de la segunda persona
        while True:
            edad2_input = input("Edad: ")
            valido, resultado = validar_edad(edad2_input)
            if valido:
                edad2 = resultado
                break
            else:
                print(f"Error: {resultado}")
        
        # Validar sexo de la segunda persona
        while True:
            sexo2 = input("Sexo (M/F): ").upper().strip()
            if sexo2 in ['M', 'F']:
                break
            else:
                print("Error: Por favor ingresa 'M' para Masculino o 'F' para Femenino")
        
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
            try:
                opcion = input("\n¿Deseas ingresar otra persona? (S/N): ").upper()
                if opcion == 'S':
                    nueva = crear_persona_por_teclado()
                    if nueva is not None:
                        nueva.listarInformacion()
                elif opcion == 'N':
                    print("Fin del programa.")
                    break
                else:
                    print("Por favor ingresa 'S' para Sí o 'N' para No")
            except KeyboardInterrupt:
                print("\nPrograma terminado por el usuario")
                break
            except Exception as e:
                print(f"Error: {e}")
                print("Intenta nuevamente")

    except Exception as e:
        print(f"Error crítico en el programa: {e}")
    finally:
        print("Programa finalizado")

if __name__ == "__main__":
    main()