# ====================================================================
# Inventario Básico - Tareas 2, 3, 4 y 5
# Programa para registrar un producto y calcular su costo total.
# ====================================================================

# --------------------------------------------------------------------
# TASK 2: Entrada de datos (variables en Python)
# --------------------------------------------------------------------

# Solicitar el nombre del producto (string). No requiere validación numérica.
nombre = input("▶ Ingrese el nombre del producto: ")

# Bucle para solicitar y validar el precio del producto (float).
while True:
    try:
        # Solicita el precio y usa float() para la conversión.
        precio_str = input("▶ Ingrese el precio unitario (ej. 15.50): ")
        precio = float(precio_str)
        # Si la conversión es exitosa, sale del bucle.
        break
    except ValueError:
        # Muestra un mensaje de error si la entrada no es un número válido.
        print("❌ Error: Por favor, ingrese un valor numérico válido para el precio.")

# Bucle para solicitar y validar la cantidad del producto (int).
while True:
    try:
        # Solicita la cantidad y usa int() para la conversión.
        cantidad_str = input("▶ Ingrese la cantidad en stock (número entero): ")
        cantidad = int(cantidad_str)
        # Si la conversión es exitosa, sale del bucle.
        break
    except ValueError:
        # Muestra un mensaje de error si la entrada no es un número entero válido.
        print("❌ Error: Por favor, ingrese una cantidad entera válida.")

# --------------------------------------------------------------------
# TASK 3: Operación matemática (costo total)
# --------------------------------------------------------------------

# Calcular el costo total (precio * cantidad). Se realiza después de la validación.
costo_total = precio * cantidad

# --------------------------------------------------------------------
# TASK 4: Mostrar resultados en consola
# --------------------------------------------------------------------

print("\n" + "="*50)
print("✅ Producto Registrado y Costo Calculado")
print("="*50)

# Mostrar todos los datos en el formato solicitado, usando f-strings para claridad.
# El precio y el costo total se formatean a 2 decimales para un mejor manejo monetario.
print(f"| Producto: **{nombre}** | Precio: **{precio:.2f}** | Cantidad: **{cantidad}** | Total: **{costo_total:.2f}** |")

print("="*50)
print("¡Operación completada exitosamente!")
print("="*50 + "\n")

# --------------------------------------------------------------------
# TASK 5: Documentación del código (Comentario General)
# --------------------------------------------------------------------

# Este programa en Python tiene como objetivo registrar un producto en un inventario básico.
# Solicita al usuario el nombre (string), el precio (float) y la cantidad (int).
# Implementa validación (uso de bloques try-except) para asegurar que el precio y la cantidad sean valores numéricos correctos,
# volviendo a solicitar el dato si hay un error. Una vez validados, calcula el costo total (precio * cantidad)
# y finalmente imprime todos los detalles del producto en un formato claro en la consola.