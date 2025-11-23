#Crear un menu que muestre opciones de registrar, buscar, actualizar, eliminar y muestre reportes
print("¡Bienvenido al Hospital Buenavista!")
print("MENU \n 1. Registrar paciente \n 2. Buscar paciente \n 3. Acfualizar Información \n 4. Eliminar usuario \n 5. Mostrar Reporte \n 6.Salir")


pacientes = []  # lista donde se guardarán los pacientes

def menuHospital():
    while True:
        opcion = int(input("Que desea hacer: "))
        if opcion == 1:
            def registrar():
                #Campos requeridos id,nombre,edad,genero,diagnostico ["consulta general", "control presion arterial"],historial
                #Validar que no hayan duplicados y que se puedan hacer varios registros
                print("¡Bienvenido al modulo Registrar paciente paciente!")
                id = input("Ingrese el Id: ")
                nombre = input("Ingrese el Nombre: ")
                edad= input("Ingrese la Edad: ")
                genero= input("Ingrese el Género (F/M): ").lower()
                #---Ingreso multiple de diagnosticos
                diagnosticos = []
                print ("Ingrese los Diagnosticos (escriba 'fin' para terminar): ")
                while True:
                      diagnosticoN = input("Diagnostico")
                      if diagnosticoN.lower() == "fin": 
                        break
                      diagnosticos.append(diagnosticoN)

                historial= input("Ingrese el Historial (DIA - MES - AÑO): ")

                registrarCampos = {
                    "id": id ,
                    "nombre":nombre,
                    "edad":edad,
                    "genero":genero,
                    "diagnostico": diagnosticos, #diagnostico = ["consulta general","control presion arterial"], en tupla
                    "historial":historial
                }
                print(registrarCampos)
                pacientes.append(registrarCampos)  # guarda el registro en la lista

            registrar()
            
        if opcion == 2:
                print("¡Bienvenido al modulo Buscar paciente!")
        elif opcion == 3:
                print("¡Bienvenido al modulo Actualizar Infromación paciente!")
        elif opcion == 4:
                print("¡Bienvenido al modulo Eliminar Usuario paciente!")
        elif opcion == 5:
                print("¡Bienvenido al modulo Mostrar Reporte paciente!")
        elif opcion == 6:
                print("¡Bienvenido al modulo  paciente!")
        else:
                print("Error, ingrese una opcion del menu: 1, 2, 3, 4, 5, 6")
        break

menuHospital()