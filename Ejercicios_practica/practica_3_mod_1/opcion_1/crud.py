#Contiene las funciones básicas del inventario: Crear, Leer, Actualizar, Eliminar (CRUD).


from utils import validar_entrada_entero, validar_entrada_flotante, generar_nuevo_id

def mostrar_inventario(inventario):
    """Muestra el inventario actual en formato tabular."""
    if not inventario:
        print("\n--- El inventario está vacío. ---")
        return

    print("\n" + "="*50)
    print(f"{'ID':<5}{'Nombre':<25}{'Cantidad':>10}{'Precio Unitario':>10}")
    print("="*50)
    
    for producto in inventario:
        print(
            f"{producto['id']:<5}"
            f"{producto['nombre']:<25}"
            f"{producto['cantidad']:>10}"
            f"{producto['precio']:>10.2f}"
        )
    print("="*50)

def agregar_producto(inventario):
    """Agrega un nuevo producto al inventario."""
    print("\n--- Registrar Nuevo Producto ---")
    
    # Genera un ID único usando la función de utils
    nuevo_id = generar_nuevo_id(inventario)
    
    nombre = input("Nombre del Producto: ").strip()
    # Usa funciones de validación para cantidad y precio
    cantidad = validar_entrada_entero("Cantidad Inicial", min_val=0)
    precio = validar_entrada_flotante("Precio Unitario", min_val=0.01)

    nuevo_producto = {
        "id": nuevo_id,
        "nombre": nombre,
        "cantidad": cantidad,
        "precio": precio
    }
    inventario.append(nuevo_producto)
    print(f"✅ Producto '{nombre}' (ID: {nuevo_id}) agregado con éxito.")
    
def editar_producto(inventario):
    """Edita un producto existente por su ID."""
    if not inventario:
        print("\n⚠️ No hay productos para editar.")
        return
        
    mostrar_inventario(inventario)
    
    producto_id = validar_entrada_entero("Ingrese el ID del producto a editar", min_val=1)
    
    # Buscar el producto
    producto_encontrado = next((p for p in inventario if p['id'] == producto_id), None)
    
    if producto_encontrado:
        print(f"\n--- Editando Producto ID: {producto_id} ({producto_encontrado['nombre']}) ---")
        
        # Editar Nombre
        nuevo_nombre = input(f"Nuevo Nombre (actual: {producto_encontrado['nombre']}) [Enter para mantener]: ").strip()
        if nuevo_nombre:
            producto_encontrado['nombre'] = nuevo_nombre
            
        # Editar Cantidad
        nueva_cantidad = validar_entrada_entero(f"Nueva Cantidad (actual: {producto_encontrado['cantidad']}) [Enter para mantener]", min_val=0)
        if nueva_cantidad != producto_encontrado['cantidad']: # Asumiendo que 0 es una entrada válida para la cantidad si el usuario no presiona Enter.
             producto_encontrado['cantidad'] = nueva_cantidad
        
        # Editar Precio
        nuevo_precio = validar_entrada_flotante(f"Nuevo Precio (actual: {producto_encontrado['precio']}) [Enter para mantener]", min_val=0.01)
        if nuevo_precio != producto_encontrado['precio']:
            producto_encontrado['precio'] = nuevo_precio
            
        print(f"✅ Producto ID: {producto_id} actualizado con éxito.")
    else:
        print(f"⚠️ Error: Producto con ID {producto_id} no encontrado.")

def eliminar_producto(inventario):
    """Elimina un producto existente por su ID."""
    if not inventario:
        print("\n⚠️ No hay productos para eliminar.")
        return
        
    mostrar_inventario(inventario)
    
    producto_id = validar_entrada_entero("Ingrese el ID del producto a eliminar", min_val=1)
    
    # Usar una lista de comprensión o filter para eliminar
    inventario[:] = [p for p in inventario if p['id'] != producto_id]
    
    if len(inventario) == len([p for p in inventario if p['id'] != producto_id]):
         print(f"⚠️ Error: Producto con ID {producto_id} no encontrado.")
    else:
        print(f"🗑️ Producto con ID {producto_id} eliminado con éxito.")