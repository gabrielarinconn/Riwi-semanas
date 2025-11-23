#Validación de datos con condicionales:

#    Crea un menú que pregunte al usuario qué acción desea realizar:
#        Agregar producto
#        Mostrar inventario
#        Calcular estadísticas
#        Salir
#    Usa condicionales if, elif y else para procesar la opción elegida.
#    Si el usuario ingresa una opción inválida, muestra un mensaje de error y pide nuevamente la entrada.

lista = ()

while True:
    print("Bienvenido a Fruver Mafia, aquí la frescura es ley y cada producto tiene su propia reputación")
    print("Mafiosos con descuento: Don Manzelo 🍎, Capo Banano 🍌 y Tomatone 🍅")
    opcionMenu = int(input("Que acción deseas realizar: \n1. Agregar producto \n2. Mostrar inventario \n3. Calcular estadísticas \n4.Salir Digita un número \nElige una opción: "))

    if opcionMenu == 1:

        print("formula agregar producto")
    if opcionMenu == 2:
        print("mostrar inventario")
    if opcionMenu == 3:
        print("calcular estadistica")
    if opcionMenu == 4:
        print("salir")
    else:
        print("Ingrese alguna opción válida: 1 , 2 , 3 o 4")
        break