# Contiene el menú principal y la lógica de la aplicación. Importa las funciones de los otros módulos.



import crud
import file_manager
from utils import validar_entrada_entero

def mostrar_menu():
    """Muestra el menú principal de la aplicación."""
    print("\n" + "*"*40)
    print("  GESTIÓN DE INVENTARIO MULTIFORMATO")
    print("*"*40)
    print("--- Operaciones CRUD ---")
    print("1. Agregar Producto")
    print("2. Mostrar Inventario")
    print("3. Editar Producto")
    print("4. Eliminar Producto")
    print("--- Operaciones de Archivo ---")
    print("5. 📥 Cargar Inventario (Reemplaza el actual)")
    print("6. 💾 Guardar Inventario")
    print("--- Sistema ---")
    print("0. Salir")
    print("*"*40)

def main():
    """Función principal de la aplicación."""
    
    # Inicializa el inventario como una lista vacía
    inventario = []

    # Por defecto, intenta cargar desde un formato (ej. JSON) al inicio
    # Puedes modificar esto para que pregunte al usuario si quiere cargar
    # inventario = file_manager.leer_inventario_json()

    while True:
        mostrar_menu()
        
        # Usa la función de validación de utils para obtener la opción
        opcion = validar_entrada_entero("Ingrese el número de la opción", min_val=0, max_val=6)
        
        # Lógica principal del menú
        if opcion == 1:
            crud.agregar_producto(inventario)
        
        elif opcion == 2:
            crud.mostrar_inventario(inventario)
            
        elif opcion == 3:
            crud.editar_producto(inventario)
            
        elif opcion == 4:
            crud.eliminar_producto(inventario)
            
        elif opcion == 5:
            # Llama a la función que maneja la selección de formato de carga
            nuevo_inventario = file_manager.seleccionar_formato_carga(inventario)
            if nuevo_inventario is not None:
                inventario = nuevo_inventario
                
        elif opcion == 6:
            # Llama a la función que maneja la selección de formato de guardado
            file_manager.seleccionar_formato_guardado(inventario)
            
        elif opcion == 0:
            print("👋 Saliendo del Gestor de Inventario. ¡Hasta pronto!")
            break
            
        else:
            print("⚠️ Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()