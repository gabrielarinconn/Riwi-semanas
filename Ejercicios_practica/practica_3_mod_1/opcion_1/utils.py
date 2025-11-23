# Contiene funciones de ayuda, como validación de entrada y manejo de errores comunes.



def validar_entrada_entero(mensaje, min_val=None, max_val=None):
    """
    Pide un entero al usuario y maneja errores de valor.
    
    Args:
        mensaje (str): El mensaje a mostrar al usuario.
        min_val (int, optional): Valor mínimo permitido.
        max_val (int, optional): Valor máximo permitido.
        
    Returns:
        int: El valor entero validado.
    """
    while True:
        try:
            entrada = input(f"{mensaje}: ")
            valor = int(entrada)
            
            if min_val is not None and valor < min_val:
                print(f"⚠️ Error: El valor debe ser mayor o igual a {min_val}.")
                continue
            
            if max_val is not None and valor > max_val:
                print(f"⚠️ Error: El valor debe ser menor o igual a {max_val}.")
                continue
                
            return valor
        except ValueError:
            print("⚠️ Error: Entrada inválida. Por favor, ingrese un número entero.")

def validar_entrada_flotante(mensaje, min_val=0.0):
    """
    Pide un número flotante al usuario y maneja errores de valor.
    
    Args:
        mensaje (str): El mensaje a mostrar al usuario.
        min_val (float, optional): Valor mínimo permitido (por defecto 0.0).
        
    Returns:
        float: El valor flotante validado.
    """
    while True:
        try:
            entrada = input(f"{mensaje}: ")
            valor = float(entrada)
            
            if valor < min_val:
                print(f"⚠️ Error: El valor debe ser mayor o igual a {min_val}.")
                continue
                
            return valor
        except ValueError:
            print("⚠️ Error: Entrada inválida. Por favor, ingrese un número decimal o entero.")

def generar_nuevo_id(inventario):
    """
    Genera un ID único para un nuevo producto.
    """
    if not inventario:
        return 1
    return max(producto['id'] for producto in inventario) + 1