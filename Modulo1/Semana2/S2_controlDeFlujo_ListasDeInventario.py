# ====================================================================
# Inventario con Control de Flujo y Listas - Semana 2
# Objetivo: Gestión de inventario mediante un menú interactivo usando
# listas, diccionarios, bucles (while/for) y condicionales (if/elif/else).
# ====================================================================

# Lista global para almacenar los productos.
# Cada producto será un diccionario: {"nombre": str, "precio": float, "cantidad": int}
inventario = []

# ====================================================================
# TASK 5: Estructura el código en funciones simples
# ====================================================================

def agregar_producto():
    """
    Función para solicitar datos del producto (nombre, precio, cantidad)
    y almacenarlo como un diccionario en la lista 'inventario'.
    Incluye validación para el precio y la cantidad.
    """
    print("\n--- 1. AGREGAR PRODUCTO ---")

    # Solicitar el nombre del producto
    nombre = input("▶ Ingrese el nombre del producto: ").strip()
    if not nombre:
        print("❌ El nombre del producto no puede estar vacío.")
        return

    # Bucle para validar el precio (float)
    while True:
        try:
            precio = float(input("▶ Ingrese el precio unitario: "))
            if precio <= 0:
                print("❌ El precio debe ser un valor positivo.")
                continue
            break
        except ValueError:
            print("❌ Error: Por favor, ingrese un valor numérico válido para el precio.")

    # Bucle para validar la cantidad (int)
    while True:
        try:
            cantidad = int(input("▶ Ingrese la cantidad en stock: "))
            if cantidad < 0:
                print("❌ La cantidad no puede ser negativa.")
                continue
            break
        except ValueError:
            print("❌ Error: Por favor, ingrese una cantidad entera válida.")

    # Crear el diccionario del producto y agregarlo a la lista
    producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    inventario.append(producto)
    print(f"\n✅ Producto '{nombre}' agregado al inventario.")


def mostrar_inventario():
    """
    Función para recorrer y mostrar todos los productos en la lista 'inventario'.
    (TASK 3)
    """
    print("\n--- 2. INVENTARIO ACTUAL ---")

    # Condicional: Verifica si la lista está vacía (Criterio de Aceptación)
    if not inventario:
        print("💡 El inventario está vacío. Agregue productos primero.")
        return

    # Bucle for para recorrer la lista de diccionarios (TASK 3)
    print("=" * 60)
    print(f"{'No.':<4} | {'Producto':<20} | {'Precio':<10} | {'Cantidad':<10} | {'Subtotal':<10}")
    print("=" * 60)
    
    for i, item in enumerate(inventario, 1):
        subtotal = item["precio"] * item["cantidad"]
        # Mostrar en un formato claro (TASK 3)
        print(
            f"{i:<4} | {item['nombre']:<20} | {item['precio']:<10.2f} | {item['cantidad']:<10} | {subtotal:<10.2f}"
        )
    print("=" * 60)


def calcular_estadisticas():
    """
    Función para calcular y mostrar el valor total del inventario y el total
    de productos registrados. (TASK 4)
    """
    print("\n--- 3. ESTADÍSTICAS DEL INVENTARIO ---")

    if not inventario:
        print("💡 No hay productos para calcular estadísticas.")
        return

    valor_total_inventario = 0.0
    cantidad_total_unidades = 0

    # Bucle for para calcular las sumatorias (TASK 4)
    for item in inventario:
        # Acumular el valor total (precio * cantidad)
        valor_total_inventario += item["precio"] * item["cantidad"]
        # Acumular la cantidad total de unidades
        cantidad_total_unidades += item["cantidad"]

    # Mostrar los resultados de forma clara (TASK 4)
    print(f"💰 Valor total del inventario: **{valor_total_inventario:,.2f}**")
    print(f"📦 Cantidad total de unidades: **{cantidad_total_unidades:,}**")
    print(f"🔢 Total de productos registrados: **{len(inventario)}**")


def mostrar_menu():
    """Muestra el menú de opciones."""
    print("\n" + "=" * 40)
    print("    SISTEMA BÁSICO DE INVENTARIO")
    print("=" * 40)
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Calcular estadísticas")
    print("4. Salir")
    print("=" * 40)

# ====================================================================
# TASK 1 y TASK 2: Control de flujo (Bucle while y condicionales)
# ====================================================================

# Bucle while principal que se ejecuta hasta que el usuario elija Salir (TASK 2)
def main():
    while True:
        # Mostrar el menú (TASK 1)
        mostrar_menu()
        
        # Pedir la opción y usar try-except para manejar entradas no numéricas
        opcion_str = input("👉 Elige una opción (1-4): ")

        # Usar condicionales if/elif/else para procesar la opción (TASK 1)
        if opcion_str == '1':
            agregar_producto()
        elif opcion_str == '2':
            mostrar_inventario()
        elif opcion_str == '3':
            calcular_estadisticas()
        elif opcion_str == '4':
            print("\n👋 ¡Hasta pronto! Saliendo del sistema de inventario.")
            break  # Rompe el bucle while
        else:
            # Mensaje de error para opción inválida (TASK 1 - Criterio de Aceptación)
            print("❌ Opción inválida. Por favor, selecciona un número entre 1 y 4.")

# Ejecutar el programa principal
if __name__ == "__main__":
    main()

# ====================================================================
# TASK 5: Comentario final resumiendo el objetivo de la semana
# ====================================================================

# **Comentario Final (Semana 2)**
# Este programa implementa un sistema básico de gestión de inventario.
# Se utilizaron estructuras de control de flujo (`while` para el menú continuo e `if/elif/else` para la selección de opciones)
# y estructuras de datos compuestas (una `lista` de `diccionarios`) para almacenar registros de productos.
# Las funcionalidades principales (agregar, mostrar, calcular) fueron encapsuladas en `funciones` para modularizar y mejorar la legibilidad del código.