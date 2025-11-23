#Función agregar producto
def agregar_producto(inventario):
    #Se solicita al usuario el nombre del objeto a ingresar en el sistema
    nombre=input("Ingresa el nombre del objeto que se va a registrar en el sistema: ").capitalize()
    #Se solicita al usuario el precio del producto
    #Si el usuario ingresa una información que no es congruente con lo solicitado, se le seguira solicitando
    while True:
        precio=input("Ingresa el costo unitario del objeto antes mencionado: ")
        try:
            precio=float(precio)
            break
        except:
            print("El dato ingresado no corresponde con algun precio, intenta de nuevo.")
            continue
    #Se solicita al usuario el precio del producto
    #Si el usuario ingresa una información que no es congruente con lo solicitado, se le seguira solicitando
    while True:
        cantidad=input("Ingresa la cantidad de unidades del objeto antes mencionado: ")
        try:
            cantidad=int(cantidad)
            break
        except:
            print("El dato ingresado no corresponde con la información solicitada, intenta de nuevo.")
            continue
    #Se crea un diccionario con la información del producto y se agrega a la lista de inventario                        
    producto={"Producto": nombre, "Precio":precio, "Cantidad":cantidad}
    inventario.append(producto)
    return inventario

#Función mostrar inventario
def mostrar_inventario(inventario):
    #Verifica si la lista esta vacia, si es asi devuelve un entero
    if len(inventario)==0:
        print("\n"+"Aún no hay productos registrados en el sistema.")
        return 0
    #Si la lista no esta vacia procede a calcular el subtotal de cada producto y lo muestra en pantalla junto el resto de la datos
    #Que es nombre del producto, cantidad de este y el precio unitario
    else:
        print("\n"+"Los objetos registrados en el sistema, con su información correspondiente son:\n")
        for objeto in inventario:
            subtotal=objeto["Cantidad"]*objeto["Precio"]
            print(f"Producto:{objeto["Producto"]}|Precio:{objeto["Precio"]}|Cantidad:{objeto["Cantidad"]}|Total:{subtotal}")

#Funcion mostrar estadisticas
def mostrar_estadisticas(inventario):
    #Usamos dos sumatorias para hallar la cantidad de unidades totales en la lista y el costo de todas esas unidades respectivamente
    total_precio = sum(objeto["Cantidad"] * objeto["Precio"] for objeto in inventario)
    total_objetos = sum(objeto["Cantidad"] for objeto in inventario)
    #Mostramos en consola los datos calculados en el númeral anterior
    print(f"Total de objetos registrados en el sistema: {len(inventario)} Productos\n"
    f"Total de unidades disponibles en el inventario: {total_objetos} unidades\n"
    f"Costo total del inventario actual: {total_precio}")



#Creamos la lista que va a contener todos los datos
inventario=[]
#Creamos un menú que se repite hasta que el usuario elija salir o si ingresa un dato que no sea congruente con lo solicitado
while True:
    #Se le solicita al usuario que elija una de las opciones del menú, y se le impreme en pantalla las opciones disponibles
    opcion_menu=input(""" 

    |------------------------------------------------|
    |       Bienvenido al sistema de inventario,     |
    |       ¿Qué acción deseas realizar?:            |
    |                                                |
    |       1. Agregar Producto                      |
    |       2. Mostrar inventario                    |
    |       3. Calcular estadísticas                 |
    |       3. Salir                                 |
    |------------------------------------------------|

    Digita la opcion escogida: """)
    #Si se elije la opción 1, se ejecuta la función agregar producto y lo devuelve al menú al finalizar la tarea
    if opcion_menu.lower().strip()=="1" or opcion_menu.lower().strip()=="agregar producto":
        print("\n"+"Haz escogido agregar producto, para hacerlo debes llenar la información que vamos a solicitar a continuación\n" \
        "Lee correctamente las instrucciones.")
        inventario=agregar_producto(inventario)
        print("\n"+f"El producto  ha sido ingresado de manera exitosa al sistema, seras redireccionado al menú principal")

    #Si se elije la opción 2, se ejecuta la función mostrar producto y lo devuelve al menú al finalizar la tarea
    elif opcion_menu.lower().strip()=="2" or opcion_menu.lower().strip()=="mostrar inventario":
        print("\n"+"Haz escogido mostrar inventario, a continuación se mostrara los datos encontrados:")
        if mostrar_inventario(inventario)==0:
            continue
        else:
            mostrar_inventario(inventario)
        print("\n"+"Se ha terminado la acción seleccionada, Seras redirigido al menú principal")

    #Si se elije la opción 3, se ejecuta la función mostrar estadísticas y lo devuelve al menú al finalizar la tarea
    elif opcion_menu.lower().strip()=="3" or opcion_menu.lower().strip()=="calcular estadisticas":
        print("\n"+"Haz escogido calcular estadísticas, a continuacion te mostraremos los datos generales más relevantes:\n")
        mostrar_estadisticas(inventario)
        print("\n"+"Se ha terminado la acción seleccionada, Seras redirigido al menú principal")

    #Si se elije la opción 4, se sale del programa
    elif opcion_menu.lower().strip()=="4" or opcion_menu.lower().strip()=="salir":
        print("\nHaz salido exitosamente de la aplicación vuelva pronto.")
        break
    #Si no se elije ninguna de las opciones anteriores, se le notifica al usuario que el dato ingresado no es correcto y se le solicita de nuevo
    else:
        print("\n"+"El dato ingresado no corresponde con alguna de las opciones del menú, intenta de nuevo.")








#EL objetivo de esta semana era el aprender a crear funciones en python, por lo que se creo un sistema de inventario
#que permite agregar productos, mostrar el inventario y calcular estadísticas del mismo, todo esto a través de funciones.
#con la intención de aprender que es muy util el uso de funciones para organizar mejor el código y hacerlo más legible.
#Ademas, de optimizar el tiempo de desarrollo al reutilizar código ya escrito en lugar de repetirlo.