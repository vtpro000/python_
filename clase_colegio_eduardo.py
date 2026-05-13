#clase colegio. el primer paso es eliminar el diccionario "curso" suelto 

class Alumno:
    def __init__(self, rut, nombre, apellido, curso,contraseña):
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.curso = curso
        self.contraseña = contraseña

class Colegio:
    def __init__(self):
        self.registro_global = {
            "1Ro": {},
            "2Do": {},
            "3Ro": {},
            "4To": {},
            "5To": {},
            "6To": {},
            "7Mo": {},
            "8Vo": {},
            "1medio": {},
            "2medio": {},
            "3medio": {},
            "4medio": {},
        }

    def agregar_nuevo_alumno(self, rut, nombre, apellido, curso, contraseña=None):
        if curso not in self.registro_global:
            print("Curso no encontrado.")
            return False
        if self.buscar_alumno_por_rut(rut) is not None:
            print("El RUT ya existe.")
            return False
        alumno = Alumno(rut, nombre, apellido, curso, contraseña)
        self.registro_global[curso][rut] = alumno
        print(f"Alumno {nombre} {apellido} registrado correctamente en el curso {curso}.")
        return True

    def buscar_alumno_por_rut(self, rut):
        for curso, alumnos in self.registro_global.items():
            if rut in alumnos:
                return alumnos[rut]
        return None

colegio = Colegio()

def registrar_alumno():
    rut = input("ingrese su RUT: ")
    if len(rut) >= 9 and len(rut) <= 10:
        nombre = input("ingrese el nombre del alumno: ").capitalize()
        apellido = input("ingrese su apellido: ").capitalize()

        print("cursos disponibles:", list(colegio.registro_global.keys()))
        curso = input("ingrese un curso: ")
        contraseña = input("ingrese una contraseña: ")

        confirm_contraseña = input("confirme su contraseña: ")
        if confirm_contraseña == contraseña:
            print("contraseña verificada.")
            colegio.agregar_nuevo_alumno(rut, nombre, apellido, curso, contraseña)
        else:
            print("las contraseñas no coinciden.")
    else: print("Los caracteres del RUT no coinciden.")

def mostrar_alumnos():
   rut = input("ingrese su RUT: ")
   contra_entrada = input("ingrese su contraseña: ")

   alumnos = colegio.buscar_alumno_por_rut(rut)

   if alumnos:
       if contra_entrada == alumnos.contraseña:
           print("--datos del Alumnos--")
           print("____________________________________")
           print(f"nombre:  {alumnos.nombre} {alumnos.apellido}")
           print(f"curso:   {alumnos.curso}")
           print(f"RUT:     {alumnos.rut}")
       else:
           print("contraseña incorrecta")
   else:
       print("no se encontro el RUT.")

        
           

def crear_ficha():
    buscar_rut = input("ingrese su rut: ")
    contra_entrada = input("ingrese su contraseña: ")
    
    alumno = colegio.buscar_alumno_por_rut(buscar_rut)

    if alumno:
        if contra_entrada == alumno.contraseña:
            print("_______________________________________")
            print("--ficha del alumno--")
            print(f"nombre:  {alumno.nombre} {alumno.apellido}")
            print(f"curso:   {alumno.curso}")
            print(f"RUT:     {alumno.rut}")
        else:
            print("contraseña incorrecta.")
    else: 
        print("no se encontro el RUT.")

     
def certificado_de_alumno():
    print("hola")
    

def menu():
    while True:
        print("\n--- MENÚ ---")
        print("1. Registrar alumno")
        print("2. Mostrar alumnos")
        print("3. Salir")
        print("4. ver ficha")
        print("5. ver certificado del alumnofe")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_alumno()
        elif opcion == "2":
            mostrar_alumnos()
        elif opcion == "3":
            print("Saliendo.")
            break
        elif opcion == "4":
            crear_ficha()
        elif opcion == "5":
            print("ni idea")
            certificado_de_alumno()
        else:
            print("opcion incorrecta")

menu()

#contraseña
#validacion de contraseña
#ficha
#certificado de alumno
