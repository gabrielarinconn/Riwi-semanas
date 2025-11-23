⭐  Parámetro extrasaction='ignore' en csv.DictWriter

Esta es una propiedad específica del módulo csv.

    Propósito: La clase DictWriter escribe filas basadas en una lista de diccionarios, usando las claves del diccionario como nombres de columna. El parámetro fieldnames=HEADER le dice qué columnas esperar ("nombre", "precio", "cantidad").

    Acción: extrasaction='ignore' indica al escritor qué hacer si un diccionario en la lista (inventario) tiene claves que NO están definidas en la lista fieldnames (HEADER).

    Efecto: Le dice al escritor: "ignora" cualquier campo extra en el diccionario del producto que no sea nombre, precio o cantidad. Si estuviera configurado como extrasaction='raise' (el valor por defecto), Python generaría un error.


⭐ Funciones lambda

 Las funciones lambda son simplemente una versión acortada, 
 que puedes usar si te da pereza escribir una función

 Ejemplo
 Lo que sería una función que suma dos números como la siguiente.

        def suma(a, b):
            return a+b

Se podría expresar en forma de una función lambda de la siguiente manera.

        lambda a, b : a + b

La primera diferencia es que una función lambda no tiene un nombre, y por lo tanto salvo que sea asignada a una variable, es totalmente inútil. Para ello debemos.

        suma = lambda a, b: a + b

Una vez tenemos la función, es posible llamarla como si de una función normal se tratase.

        suma(2, 4)

Si es una función que solo queremos usar una vez, tal vez no tenga sentido almacenarla en una variable. Es posible declarar la función y llamarla en la misma línea.

        (lambda a, b: a + b)(2, 4)

⭐ Anotación de tipo de retorno

      ->

- Tipo de Retorno,Sintaxis,¿Qué Devuelve?,Ejemplo (Uso)
- Entero,-> int,Un número entero.,def contar(x: list) -> int:
- Cadena,-> str,Un texto.,def formatear(datos: dict) -> str:
- Booleano,-> bool,True o False.,def es_par(num: int) -> bool:
- Flotante,-> float,Un número decimal.,def calcular_promedio(nums: list) -> float:
- Lista,-> list,Una lista de elementos.,def obtener_items() -> list:
- Tupla,-> tuple,Una secuencia inmutable.,def obtener_coordenadas() -> tuple:
- Nada,-> None,"La función no devuelve un valor explícito (devuelve None implícitamente, común en funciones que solo imprimen o modifican).",def imprimir_mensaje() -> None: