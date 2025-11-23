#Nivel 4 — Listas y Colecciones
#Objetivo: Crear, recorrer, modificar y eliminar elementos en listas.

#Lista de frutas.
#SOLUCION
frutas = ["manzana", "pera", "uva", "naranja"]
#Mostrar lista
print (frutas)

#Agregar y eliminar frutas.
#SOLUCION
#Agregar elemnto a la lista
frutas.append(str(input("Ingresa el nombre de una fruta: ")))
print (frutas)
#Eliminar elemento a la lista
frutas.remove(str(input("Ingresa el nombre de la fruta que deseas eliminar: ")))
print (frutas)

#Buscar un elemento en la lista.
#SOLUCION
#Pedir al usuario si la fruta que busca esta en la lista
needFrut = str(input("Valida si la fruta que quieres esta en la lista, escribe la fruta: "))
#Condicional para validar si en la lista esta la fruta que buscas

if needFrut in frutas:
    print(f"Sí, {needFrut} está en la lista.")
else:
    print(f"No, {needFrut} no está en la lista.")

#Lista de números y promedio.
#SOLUCION
#Crear lista vacia para almacenar nuemros ingresados por el usuario
listN = []
#Pedir al usuario los numeros
cant = int(input("¿Cuantos números quieres agregar? "))
#Pedir los nuemeros y sacar promedios
for i in range(cant):
    #Pedir al usuario los numeros
    promedioN = int(input(f"Ingrese número {i+1}: "))
    listN.append(promedioN)
#calcular el promedio
promedio = sum(listN) / len(listN)
#ostrar resultados
print(f"Lista de números:{listN} ")
print(f"El promedio es:{promedioN} ")


#Números pares: guardar solo los pares.
#SOLUCION
#crear una lista vacía para guardar los números pares
paress = []
#pedir al usuario cuántos números quiere ingresar
cuantos = int(input("¿Cuántos números deseas ingresar? "))
#leer los números uno por uno
for leer in range(cuantos):
    numX = int(input(f"Ingrese el número {leer+1}: "))
    # Verificar si el número es par
    if numX % 2 == 0:
        paress.append(numX)  # Guardar solo los pares
#mostrar los resultados
print(f"Números pares guardados:{paress}")


#Eliminar duplicados
#SOLUCION
#Crear una lista
notas = [1,4,5,7,4]
#Mostrar lista
print(notas)
#lista para guardar elementos 
repetido = []
nuevaLista =[]
#Revisar que en la lista si hay numeros duplicados
for l in notas:
    if l in nuevaLista not in repetido:
        repetido.append(l)  
    else:
        nuevaLista.append(l)  
#Si estan duplicados decir cual esta duplicado 
print(f"Los nuemros duplicados son: {repetido}")
#Eliminar numero duplicado y mostar lista sin el numero duplicado
print(f"La nueva lista sin los nuemros duplicados es:{nuevaLista}")