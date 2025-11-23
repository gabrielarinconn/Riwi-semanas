# Script principal y menú
import servicios
import archivos
import os
from typing import List, Dict, Any

# Lista global de inventario (Lista de diccionarios) (TASK 2)
inventario: List[Dict[str, Any]] = []

# ====================================================================
# Funciones de Soporte del Menú (TASK 6)
# ====================================================================

def obtener_valor_numerico(prompt: str, tipo: type, negativo_permitido: bool = False) -> Any | None:
    """
    Función de utilidad para solicitar y validar entradas numéricas.
    """
    while True:
        try:
            valor_str = input(prompt)
            if not valor_str:
                return None # Permite entradas vacías para actualizaciones opcionales
            
            valor = tipo(valor_str)
            if not negativo_permitido and valor < 0:
                print("❌ El valor no puede ser negativo.")
                continue
            return valor
        except ValueError:
            print(f"❌ Entrada inválida. Por favor, ingrese un número ({tipo.__name__}).")

def ejecutar_agregar():
    """Ejecuta la lógica para agregar un producto."""
    print("\n--- AGREGAR PRODUCTO ---")
    nombre = input("▶ Nombre: ").strip()
    if not nombre:
        print("❌ El nombre no puede ser vacío.")
        return
        
    precio = obtener_valor_numerico("▶ Precio: ", float)
    if precio is None: return

    cantidad = obtener_valor_numerico("▶ Cantidad: ", int)
    if cantidad is None: return

    servicios.agregar_producto(inventario, nombre, precio, cantidad)
    print(f"✅ '{nombre.title()}' agregado/actualizado.")


def ejecutar_buscar():
    """Ejecuta la lógica para buscar un producto."""
    print("\n--- BUSCAR PRODUCTO ---")
    nombre = input("▶ Nombre del producto a buscar: ").strip()
    
    producto = servicios.buscar_producto(inventario, nombre)
    if producto:
        print("-" * 30)
        print(f"✅ Producto Encontrado:")
        print(f"   Nombre: {producto['nombre']}")
        print(f"   Precio: ${producto['precio']:.2f}")
        print(f"   Cantidad: {producto['cantidad']}")
        print(f"   Subtotal: ${servicios.subtotal_producto(producto):.2f}")
        print("-" * 30)
    else:
        print(f"❌ Producto '{nombre.title()}' no encontrado en el inventario.")


def ejecutar_actualizar():
    """Ejecuta la lógica para actualizar un producto."""
    print("\n--- ACTUALIZAR PRODUCTO ---")
    nombre = input("▶ Nombre del producto a actualizar: ").strip()
    
    producto_existente = servicios.buscar_producto(inventario, nombre)
    if not producto_existente:
        print(f"❌ Producto '{nombre.title()}' no encontrado. No se puede actualizar.")
        return

    print("Ingrese nuevos valores (deje vacío para mantener el actual):")
    nuevo_precio = obtener_valor_numerico(f"▶ Nuevo Precio (Actual: {producto_existente['precio']:.2f}): ", float)
    nueva_cantidad = obtener_valor_numerico(f"▶ Nueva Cantidad (Actual: {producto_existente['cantidad']}): ", int)

    if nuevo_precio is None and nueva_cantidad is None:
        print("💡 No se ingresaron cambios. Operación cancelada.")
        return

    servicios.actualizar_producto(inventario, nombre, nuevo_precio, nueva_cantidad)
    print(f"✅ Producto '{nombre.title()}' actualizado.")


def ejecutar_eliminar():
    """Ejecuta la lógica para eliminar un producto."""
    print("\n--- ELIMINAR PRODUCTO ---")
    nombre = input("▶ Nombre del producto a eliminar: ").strip()

    if servicios.eliminar_producto(inventario, nombre):
        print(f"✅ Producto '{nombre.title()}' eliminado del inventario.")
    else:
        print(f"❌ Producto '{nombre.title()}' no encontrado. No se pudo eliminar.")

def ejecutar_guardar_csv():
    """Ejecuta la lógica para guardar el inventario en CSV."""
    print("\n--- GUARDAR INVENTARIO CSV ---")
    ruta = input("▶ Ingrese la ruta/nombre del archivo CSV (ej. inventario.csv): ").strip()
    if ruta:
        archivos.guardar_csv(inventario, ruta)
    else:
        print("❌ Ruta inválida.")

def ejecutar_cargar_csv():
    """Ejecuta la lógica para cargar el inventario desde CSV."""
    print("\n--- CARGAR INVENTARIO CSV ---")
    ruta = input("▶ Ingrese la ruta del archivo CSV a cargar: ").strip()
    
    if ruta:
        productos_cargados, filas_invalidas, accion = archivos.cargar_csv(inventario, ruta)
        
        if accion != "Error":
            print("\n" + "=" * 50)
            print("📊 RESUMEN DE CARGA")
            print("-" * 50)
            print(f"Productos Válidos Cargados/Fusionados: **{productos_cargados}**")
            print(f"Filas Inválidas Omitidas: **{filas_invalidas}**")
            print(f"Acción Realizada: **{accion}**")
            print("=" * 50)
    else:
        print("❌ Ruta inválida.")


# ====================================================================
# Menú Principal (TASK 6)
# ====================================================================

def mostrar_menu():
    """Muestra el menú principal de opciones."""
    print("\n" + "=" * 50)
    print("      SISTEMA AVANZADO DE INVENTARIO (SEMANA 3)")
    print("=" * 50)
    print("1. Agregar Producto")
    print("2. Mostrar Inventario")
    print("3. Buscar Producto")
    print("4. Actualizar Producto")
    print("5. Eliminar Producto")
    print("6. Calcular Estadísticas")
    print("-" * 50)
    print("7. Guardar Inventario a CSV")
    print("8. Cargar Inventario desde CSV")
    print("9. Salir")
    print("=" * 50)

def main():
    """Función principal que ejecuta el bucle del menú."""
    while True:
        mostrar_menu()
        
        opcion_str = input("👉 Elige una opción (1-9): ").strip()

        try:
            opcion = int(opcion_str)
        except ValueError:
            opcion = 0 # Opción inválida

        print() # Salto de línea para claridad

        if opcion == 1:
            ejecutar_agregar()
        elif opcion == 2:
            servicios.mostrar_inventario(inventario)
        elif opcion == 3:
            ejecutar_buscar()
        elif opcion == 4:
            ejecutar_actualizar()
        elif opcion == 5:
            ejecutar_eliminar()
        elif opcion == 6:
            servicios.mostrar_estadisticas(inventario)
        elif opcion == 7:
            ejecutar_guardar_csv()
        elif opcion == 8:
            ejecutar_cargar_csv()
        elif opcion == 9:
            print("\n👋 ¡Gracias por usar el sistema! Los datos no guardados se perderán. Hasta pronto.")
            break
        else:
            print("❌ Opción inválida. Por favor, selecciona un número entre 1 y 9.")

# Ejecutar el programa
if __name__ == "__main__":
    main()