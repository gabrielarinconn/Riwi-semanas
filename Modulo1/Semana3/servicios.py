# Lógica de negocio (CRUD y estadísticas)

# ====================================================================
# Módulo de Funciones CRUD y Estadísticas
# ====================================================================

# Subtotal usando una lambda (TASK 3 Opcional)
subtotal_producto = lambda p: p["precio"] * p["cantidad"] #Las funciones lambda son versión acortada, que puedes usar si te da pereza escribir una función

def agregar_producto(inventario: list, nombre: str, precio: float, cantidad: int) -> dict:
    """
    Agrega un nuevo producto (diccionario) a la lista de inventario.
    
    :param inventario: La lista global de productos.
    :param nombre: Nombre del producto (str).
    :param precio: Precio unitario (float).
    :param cantidad: Cantidad en stock (int).
    :return: El diccionario del producto agregado.
    """
    # Se normaliza el nombre para búsquedas
    producto = {"nombre": nombre.strip().title(), "precio": precio, "cantidad": cantidad}
    inventario.append(producto)
    return producto

def mostrar_inventario(inventario: list):
    """
    Muestra todos los productos en el inventario con un formato de tabla claro.
    
    :param inventario: La lista de productos.
    """
    if not inventario:
        print("💡 El inventario está vacío.")
        return

    print("\n" + "=" * 65)
    print(f"| {'Nombre':<20} | {'Precio':<10} | {'Cantidad':<10} | {'Subtotal':<10} |")  #Para que se vea como una tabla
    print("=" * 65)
    
    for item in inventario:
        subtotal = subtotal_producto(item)
        print(
            f"| {item['nombre']:<20} | {item['precio']:<10.2f} | {item['cantidad']:<10} | {subtotal:<10.2f} |"
        )
    print("=" * 65)

def buscar_producto(inventario: list, nombre: str) -> dict | None:
    """
    Busca un producto por nombre (insensible a mayúsculas/espacios).
    
    :param inventario: La lista de productos.
    :param nombre: El nombre del producto a buscar.
    :return: El diccionario del producto si se encuentra, None si no.
    """
    nombre_busqueda = nombre.strip().title()
    for producto in inventario:
        if producto["nombre"] == nombre_busqueda:
            return producto
    return None

def actualizar_producto(inventario: list, nombre: str, nuevo_precio: float | None = None, nueva_cantidad: int | None = None) -> bool:
    """
    Actualiza el precio y/o la cantidad de un producto existente.
    
    :param inventario: La lista de productos.
    :param nombre: El nombre del producto a actualizar.
    :param nuevo_precio: Nuevo precio (opcional).
    :param nueva_cantidad: Nueva cantidad (opcional).
    :return: True si se actualizó, False si no se encontró el producto.
    """
    producto = buscar_producto(inventario, nombre)
    if producto:
        if nuevo_precio is not None:
            producto["precio"] = nuevo_precio
        if nueva_cantidad is not None:
            producto["cantidad"] = nueva_cantidad
        return True
    return False

def eliminar_producto(inventario: list, nombre: str) -> bool:
    """
    Elimina un producto del inventario por su nombre.
    
    :param inventario: La lista de productos.
    :param nombre: El nombre del producto a eliminar.
    :return: True si se eliminó, False si no se encontró.
    """
    nombre_eliminar = nombre.strip().title()
    for i, producto in enumerate(inventario):
        if producto["nombre"] == nombre_eliminar:
            inventario.pop(i)
            return True
    return False

def calcular_estadisticas(inventario: list) -> tuple[int, float, tuple, tuple]:
    """
    Calcula varias métricas estadísticas del inventario. (TASK 3)
    
    :param inventario: La lista de productos.
    :return: Tupla con (unidades_totales, valor_total, producto_mas_caro, producto_mayor_stock).
    """
    if not inventario:
        # Retornar valores por defecto si el inventario está vacío
        return (0, 0.0, ("N/A", 0.0), ("N/A", 0))

    unidades_totales = 0
    valor_total = 0.0
    
    # Inicializar con el primer producto
    mas_caro = inventario[0]
    mayor_stock = inventario[0]

    for producto in inventario:
        # Acumular totales
        unidades_totales += producto["cantidad"]
        valor_total += subtotal_producto(producto)
        
        # Encontrar producto más caro
        if producto["precio"] > mas_caro["precio"]:
            mas_caro = producto

        # Encontrar producto con mayor stock
        if producto["cantidad"] > mayor_stock["cantidad"]:
            mayor_stock = producto

    # Formatear la salida como tuplas para el retorno (TASK 3)
    return (
        unidades_totales, 
        valor_total, 
        (mas_caro["nombre"], mas_caro["precio"]),
        (mayor_stock["nombre"], mayor_stock["cantidad"])
    )

def mostrar_estadisticas(inventario: list):
    """
    Llama a calcular_estadisticas y muestra los resultados de forma legible.
    """
    if not inventario:
        print("\n💡 Inventario vacío. No hay estadísticas para mostrar.")
        return

    ut, vt, pc, ms = calcular_estadisticas(inventario)

    print("\n" + "=" * 40)
    print("📈 ESTADÍSTICAS DEL INVENTARIO")
    print("=" * 40)
    print(f"📦 Unidades Totales en Stock: **{ut:,.0f}**")
    print(f"💰 Valor Total del Inventario: **{vt:,.2f}**")
    print("-" * 40)
    print(f"💎 Producto Más Caro: **{pc[0]}** (${pc[1]:.2f})")
    print(f"📊 Mayor Stock Individual: **{ms[0]}** ({ms[1]} uds.)")
    print("=" * 40)