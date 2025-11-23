Historia de usuario - Semana 1
Fundamentos y operaciones básicas del inventario

Objetivo de la Historia de usuario

    Registrar productos con su nombre, precio y cantidad en un programa simple.
    Calcular operaciones básicas como total de unidades y costo aproximado.
    Aplicar fundamentos de programación: entrada de datos, variables, operaciones matemáticas y salidas en consola.

 
Descripción de las tareas
TASK 1
1. Diagrama de flujo inicial:

    Diseña un diagrama de flujo que represente el proceso de registrar un producto en el inventario.
    Debe incluir los pasos: Inicio → Leer nombre, precio y cantidad → Calcular costo total → Mostrar resultado → Fin.
    Realízalo en draw.io y guarda la evidencia como imagen o PDF.

TASK 2
2. Entrada de datos (variables en Python):

    Crea un archivo inventario.py.
    Declara variables para nombre (string), precio (float) y cantidad (int).
    Solicita al usuario estos datos con la función input().
    Asegúrate de que el precio y la cantidad se conviertan correctamente a sus tipos numéricos usando float() e int().
    Si el usuario ingresa un valor inválido, muestra un mensaje y vuelve a pedirlo.

TASK 3
3. Operación matemática (costo total):

    Crea una variable llamada costo_total.
    Almacena en ella el resultado de multiplicar el precio por la cantidad (precio * cantidad).
    Asegúrate de que la operación se realice después de validar los datos de entrada.

TASK 4
4. Mostrar resultados en consola:

    Usa la función print() para mostrar un mensaje con:
        Nombre del producto
        Precio unitario
        Cantidad
        Costo total calculado
    El formato del mensaje debe ser claro, por ejemplo: "Producto: Lápiz | Precio: 500 | Cantidad: 3 | Total: 1500"

TASK 5
4. Documentación del código:

    Incluye comentarios (#) antes de cada bloque de código explicando qué hace.
        Ejemplo: # Solicitar datos al usuario
        nombre = input("Ingrese el nombre del producto: ")
    Al final del archivo, escribe un comentario general explicando qué hace el programa completo.

 
Criterios de aceptación

    El programa debe solicitar tres datos obligatorios: nombre, precio y cantidad.
    Si el usuario ingresa un valor inválido en precio o cantidad, el sistema debe mostrar un mensaje de error y pedir nuevamente el dato.
    El cálculo del costo total debe realizarse correctamente y mostrarse de forma clara.
    El código debe estar estructurado, comentado y sin errores de sintaxis.
    El diagrama de flujo debe reflejar las tres fases: entrada, procesamiento y salida.

