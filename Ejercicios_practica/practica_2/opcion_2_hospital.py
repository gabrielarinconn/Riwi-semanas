print("¡Bienvenido al Hospital Buenavista!")

pacientes = []  # Lista donde se guardarán los pacientes


# ---------------------------
# FUNCIONES DEL PROGRAMA
# ---------------------------

def registrar():
    print("\n--- REGISTRO DE PACIENTE ---")
    id = input("Ingrese el ID: ")

    # Validar duplicados
    for p in pacientes:
        if p["id"] == id:
            print("❌ ERROR: Ya existe un paciente con ese ID.")
            return

    nombre = input("Ingrese el Nombre: ")
    edad = input("Ingrese la Edad: ")
    genero = input("Ingrese el Género (F/M): ").upper()
    diag = input("Diagnóstico: ")

    # Crear registro
    paciente = {
        "id": id,
        "nombre": nombre,
        "edad": edad,
        "genero": genero,
        "diagnosticos": diag
    }

    pacientes.append(paciente)
    print("✔ Paciente registrado con éxito.\n")


def buscar():
    print("\n--- BÚSQUEDA DE PACIENTE ---")
    id = input("Ingrese el ID del paciente: ")

    for p in pacientes:
        if p["id"] == id:
            print("Paciente encontrado:")
            print(p)
            return
    
    print("❌ No existe un paciente con ese ID.\n")


def actualizar():
    print("\n--- ACTUALIZAR PACIENTE ---")
    id = input("ID del paciente a actualizar: ")

    for p in pacientes:
        if p["id"] == id:
            print("Paciente encontrado.")
            print("Deje en blanco para no modificar.")

            nuevo_nombre = input(f"Nombre ({p['nombre']}): ")
            nueva_edad = input(f"Edad ({p['edad']}): ")
            nuevo_genero = input(f"Género ({p['genero']}): ")
            
            # Actualizar si se ingresó algo
            if nuevo_nombre:
                p["nombre"] = nuevo_nombre
            if nueva_edad:
                p["edad"] = nueva_edad
            if nuevo_genero:
                p["genero"] = nuevo_genero.upper()

            # Actualizar diagnósticos
            print("¿Desea actualizar los diagnósticos? (s/n)")
            if input().lower() == "s":
                nuevos_diag = []
                print("Ingrese los nuevos diagnósticos ('fin' para terminar):")
                while True:
                    diag = input("Diagnóstico: ")
                    if diag.lower() == "fin":
                        break
                    nuevos_diag.append(diag)
                p["diagnosticos"] = nuevos_diag

            print("✔ Paciente actualizado correctamente.\n")
            return

    print("❌ No se encontró un paciente con ese ID.\n")


def eliminar():
    print("\n--- ELIMINAR PACIENTE ---")
    id = input("Ingrese el ID del paciente a eliminar: ")

    for p in pacientes:
        if p["id"] == id:
            pacientes.remove(p)
            print("✔ Paciente eliminado.\n")
            return
    
    print("❌ No existe un paciente con ese ID.\n")


def reporte():
    print("\n--- REPORTE DE PACIENTES ---")
    if not pacientes:
        print("No hay pacientes registrados.\n")
        return
    
    for p in pacientes:
        print(f"ID: {p['id']} \n| Nombre: {p['nombre']} \n| Edad: {p['edad']} \n| Género: {p['genero']}")
        print(f"Diagnósticos: {p['diagnosticos']}")
        print("-" * 40)


# ---------------------------
# MENÚ PRINCIPAL
# ---------------------------

def menuHospital():
    while True:
        print("\nMENU PRINCIPAL")
        print("1. Registrar paciente")
        print("2. Buscar paciente")
        print("3. Actualizar información")
        print("4. Eliminar usuario")
        print("5. Mostrar reporte")
        print("6. Salir")

        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("❌ Entrada inválida. Debe ser un número.")
            continue

        if opcion == 1:
            registrar()
        elif opcion == 2:
            buscar()
        elif opcion == 3:
            actualizar()
        elif opcion == 4:
            eliminar()
        elif opcion == 5:
            reporte()
        elif opcion == 6:
            print("👋 Saliendo del sistema... ¡Hasta luego!")
            break
        else:
            print("❌ Opción inválida.")


# Ejecutar menú
menuHospital()
