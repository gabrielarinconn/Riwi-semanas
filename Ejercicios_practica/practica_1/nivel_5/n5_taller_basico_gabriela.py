#Nivel 5 — Retos (Integración de todo)
#Objetivo: Aplicar todos los conceptos vistos en problemas más completos.

#Sistema de calificaciones.
#SOLUCION
# Pedimos el nombre del estudiante
nombre = input("Nombre del estudiante: ")
#Lista para guaradar las notas
listNotas =[]
# Pedimos las tres notas
for i in range(3):
    #Pedir al usuario las notas
    promedioo = int(input(f"Ingrese su nota del 1 al 3, nota {i+1}: "))
    listNotas.append(promedioo)
# Calculamos el promedio
promedios = promedioo / 3               
# Decidimos el estado según el promedio
if promedios >= 3:                                    
    estado = "Aprobado ecxelente desempeño"           
elif promedios >= 2:                                   
    estado = "Aprobado"                                 
else:                                                  
    estado = "Reprobado"                              
# Mostramos el resultado
print(f"{nombre} sus notas son: {listNotas}- Promedio: {promedios} - {estado}")


#Carrito de compras.
#SOLUCION
#Lista vacía para almacenar los ítems como tuplas (nombre, precio)
carrito = []                                    
#bucle infinito hasta que el usuario decida salir
while True:                                            
    opcion = input("Escribe: Agregar (a), Ver (v), Eliminar (e), Salir (s): ").lower()
    if opcion == "a":                                
        nombre = input("Nombre del producto: ")      
        precio = float(input("Precio: "))             
        carrito.append((nombre, precio))              
    elif opcion == "v":                             
        total = sum(p for _, p in carrito)            
        print("Carrito:")                             
        for i, (n, p) in enumerate(carrito, 1):        
            print(f"{i}. {n} - ${p:.2f}")            
        print(f"Total: ${total:.2f}")                 
    elif opcion == "e":                                
        indice = int(input("Número del producto a eliminar: "))  
        if 1 <= indice <= len(carrito):               
            carrito.pop(indice - 1)                   
            print("Eliminado.")
        else:
            print("Índice inválido.")
    elif opcion == "s":                            
        print("Gracias por su compra.")               
        break                                        
    else:
        print("Opción no reconocida.")            


#Cajero automático.
#SOLUCION
# Saldo inicial (ejemplo)
saldo = 1000.0                                       
while True:                                           
    print("\n1. Consultar saldo\n2. Retirar\n3. Depositar\n4. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":                                 
        print(f"Saldo disponible: ${saldo:.2f}")     
    elif opcion == "2":                                
        monto = float(input("Monto a retirar: "))
        if monto <= 0:
            print("Ingrese un monto válido.")
        elif monto > saldo:                        
            print("Fondos insuficientes.")
        else:
            saldo -= monto                        
            print(f"Retiraste ${monto:.2f}. Nuevo saldo: ${saldo:.2f}")
    elif opcion == "3":                           
        monto = float(input("Monto a depositar: "))
        if monto <= 0:
            print("Ingrese un monto válido.")
        else:
            saldo += monto                            
            print(f"Depositaste ${monto:.2f}. Nuevo saldo: ${saldo:.2f}")
    elif opcion == "4":                        
        print("Gracias. ¡Hasta luego!")
        break
    else:
        print("Opción inválida.")                  


#Gestión de estudiantes (mini base de datos).
#SOLUCION
# Lista de diccionarios: cada diccionario es un estudiante
estudiantes = []                                    
def crear_estudiante():
    id_ = input("ID: ")                          
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    estudiantes.append({"id": id_, "nombre": nombre, "edad": edad})
    print("Estudiante creado.")

def listar_estudiantes():
    for e in estudiantes:
        print(f"{e['id']} - {e['nombre']} - {e['edad']} años")

def buscar_estudiante(id_buscar):
    for e in estudiantes:
        if e["id"] == id_buscar:
            return e
    return None

# Menú principal
while True:
    accion = input("Crear (c), Listar (l), Buscar (b), Eliminar (e), Salir (s): ").lower()
    if accion == "c":
        crear_estudiante()
    elif accion == "l":
        listar_estudiantes()
    elif accion == "b":
        id_b = input("ID a buscar: ")
        resultado = buscar_estudiante(id_b)
        if resultado:
            print("Encontrado:", resultado)
        else:
            print("No encontrado.")
    elif accion == "e":
        id_b = input("ID a eliminar: ")
        est = buscar_estudiante(id_b)
        if est:
            estudiantes.remove(est)            
            print("Eliminado.")
        else:
            print("No encontrado.")
    elif accion == "s":
        break
    else:
        print("Opción inválida.")


#Calculadora avanzada (usar funciones).
#SOLUCION
import math                                        

def sumar(a, b):
    return a + b                                

def restar(a, b):
    return a - b                                   

def multiplicar(a, b):
    return a * b                                

def dividir(a, b):
    if b == 0:
        return None                             
    return a / b

def potencia(a, b):
    return a ** b                             

def factorial(n):
    if n < 0:
        return None
    return math.factorial(n)               

# Interfaz sencilla
while True:
    print("\nOperaciones: + - * / ^ (potencia) ! (factorial) s(salir)")
    oper = input("Operación: ").strip()
    if oper == "s":
        break
    if oper == "!":                                
        n = int(input("Número entero >=0: "))
        res = factorial(n)
        if res is None:
            print("Valor inválido para factorial.")
        else:
            print(f"{n}! = {res}")
    else:
        a = float(input("a: "))
        b = float(input("b: "))
        if oper == "+":
            print("Resultado:", sumar(a, b))
        elif oper == "-":
            print("Resultado:", restar(a, b))
        elif oper == "*":
            print("Resultado:", multiplicar(a, b))
        elif oper == "/":
            r = dividir(a, b)
            print("Resultado:" if r is not None else "Error: división por cero.", r)
        elif oper == "^":
            print("Resultado:", potencia(a, b))
        else:
            print("Operación no reconocida.")


#Agenda de contactos (lista de diccionarios).
#SOLUCION
# Agenda: lista de diccionarios con keys: nombre, telefono, email
agenda = []

def agregar_contacto():
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    email = input("Email: ")
    agenda.append({"nombre": nombre, "telefono": telefono, "email": email})
    print("Contacto agregado.")

def listar_contactos():
    for i, c in enumerate(agenda, 1):
        print(f"{i}. {c['nombre']} - {c['telefono']} - {c['email']}")

def buscar_por_nombre(nombre_buscar):
    resultados = [c for c in agenda if nombre_buscar.lower() in c["nombre"].lower()]
    return resultados

def eliminar_contacto(indice):
    if 1 <= indice <= len(agenda):
        agenda.pop(indice - 1)
        return True
    return False

# Menú
while True:
    accion = input("Agregar (a), Listar (l), Buscar (b), Eliminar (e), Salir (s): ").lower()
    if accion == "a":
        agregar_contacto()
    elif accion == "l":
        listar_contactos()
    elif accion == "b":
        nombre_b = input("Nombre a buscar: ")
        r = buscar_por_nombre(nombre_b)
        print("Resultados:", r if r else "No se encontraron contactos.")
    elif accion == "e":
        listar_contactos()
        idx = int(input("Número del contacto a eliminar: "))
        if eliminar_contacto(idx):
            print("Eliminado.")
        else:
            print("Índice inválido.")
    elif accion == "s":
        break
    else:
        print("Opción inválida.")