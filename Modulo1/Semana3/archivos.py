# Lógica de persistencia (Guardar/Cargar CSV)

import csv
import os
from typing import List, Dict, Any

# Columnas esperadas para el archivo CSV
HEADER = ["nombre", "precio", "cantidad"]

def guardar_csv(inventario: List[Dict[str, Any]], ruta: str, incluir_header: bool = True) -> bool:
    """
    Guarda el inventario actual en un archivo CSV. (TASK 4)
    
    :param inventario: La lista de productos a guardar.
    :param ruta: La ruta del archivo CSV de destino.
    :param incluir_header: Si se incluye la fila de encabezado.
    :return: True si el guardado fue exitoso, False en caso de error.
    """
    if not inventario:
        print("💡 El inventario está vacío. No se ha guardado nada.")
        return False
        
    try:
        with open(ruta, 'w', newline='', encoding='utf-8') as archivo_csv:
            escritor = csv.DictWriter(archivo_csv, fieldnames=HEADER, extrasaction='ignore')
            
            if incluir_header:
                escritor.writeheader()
            
            escritor.writerows(inventario)
            
        print(f"\n✅ Inventario guardado exitosamente en: **{ruta}**")
        return True

    except IOError as e:
        # Manejo de problemas de permisos, disco lleno, o ruta inválida (TASK 4)
        print(f"\n❌ Error de escritura/permisos al guardar: {e}")
        return False
    except Exception as e:
        print(f"\n❌ Error inesperado al guardar el archivo: {e}")
        return False

def cargar_csv(inventario_actual: List[Dict[str, Any]], ruta: str) -> tuple[int, int, str]:
    """
    Carga productos desde un archivo CSV y permite sobrescribir o fusionar. (TASK 5)
    
    :param inventario_actual: La lista de inventario en memoria (para fusión).
    :param ruta: La ruta del archivo CSV a cargar.
    :return: Tupla con (productos_cargados, filas_invalidas, accion_realizada).
    """
    nueva_data = []
    filas_invalidas = 0
    productos_cargados = 0
    
    # --------------------------------------------------------------------
    # Lectura y Validación de Archivo (TASK 5)
    # --------------------------------------------------------------------
    try:
        with open(ruta, 'r', newline='', encoding='utf-8') as archivo_csv:
            lector = csv.DictReader(archivo_csv, fieldnames=HEADER)
            next(lector) # Omitir la primera línea (Encabezado)

            # Validar que el archivo contenga las columnas correctas
            if lector.fieldnames != HEADER:
                # El encabezado no coincide con nombre,precio,cantidad
                raise ValueError("Encabezado de archivo CSV inválido. Debe ser: nombre,precio,cantidad.")

            for i, fila in enumerate(lector, 2): # i comienza en 2 (fila después del header)
                try:
                    # Validar número de columnas
                    if len(fila) != 3:
                         raise ValueError("Fila con número incorrecto de columnas.")
                    
                    # Validar tipos de datos y no negatividad
                    nombre = fila["nombre"].strip().title()
                    precio = float(fila["precio"])
                    cantidad = int(fila["cantidad"])
                    
                    if precio < 0 or cantidad < 0:
                        raise ValueError("Precio o cantidad deben ser no negativos.")

                    nueva_data.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
                    
                except ValueError as ve:
                    # Captura de errores de conversión/validación de fila
                    filas_invalidas += 1
                    print(f"⚠️ Fila {i} inválida omitida: {ve}")
                except Exception as e:
                    filas_invalidas += 1
                    print(f"⚠️ Fila {i} con error inesperado: {e}")
        
    except FileNotFoundError:
        print(f"\n❌ Error: El archivo '{ruta}' no fue encontrado.")
        return (0, 0, "Error")
    except UnicodeDecodeError:
        print(f"\n❌ Error de codificación: No se pudo leer el archivo. Intente con otro formato de texto.")
        return (0, 0, "Error")
    except ValueError as ve:
        # Captura el error de encabezado o validación general
        print(f"\n❌ Error de formato en CSV: {ve}")
        return (0, 0, "Error")
    except Exception as e:
        print(f"\n❌ Error inesperado durante la carga: {e}")
        return (0, 0, "Error")
    
    # Si no hay datos válidos para cargar
    if not nueva_data:
        print("\n💡 El archivo no contiene productos válidos para cargar.")
        return (0, filas_invalidas, "Error")

    # --------------------------------------------------------------------
    # Fusión/Sobreescritura (TASK 5)
    # --------------------------------------------------------------------
    
    print(f"\nSe encontraron {len(nueva_data)} productos válidos y {filas_invalidas} filas inválidas.")
    
    # Preguntar al usuario si sobrescribe o fusiona
    while True:
        opcion = input("¿Sobrescribir inventario actual? (S/N): ").upper()
        if opcion in ['S', 'N']:
            break
        print("Opción inválida. Ingrese 'S' para Sobrescribir o 'N' para Fusionar.")

    accion_realizada = ""

    if opcion == 'S':
        # Sobreescribir (Reemplazar)
        inventario_actual.clear() # Limpia la lista actual
        inventario_actual.extend(nueva_data) # Añade los nuevos datos
        productos_cargados = len(nueva_data)
        accion_realizada = "Reemplazo"
        
    elif opcion == 'N':
        # Fusionar (Política: Sumar cantidad si existe, si precio difiere, usar el nuevo precio)
        for producto_nuevo in nueva_data:
            encontrado = False
            for producto_existente in inventario_actual:
                if producto_existente["nombre"] == producto_nuevo["nombre"]:
                    # Fusión: Actualizar precio y sumar cantidad
                    producto_existente["precio"] = producto_nuevo["precio"] # Sobrescribir precio
                    producto_existente["cantidad"] += producto_nuevo["cantidad"] # Sumar cantidad
                    productos_cargados += 1
                    encontrado = True
                    break
            
            if not encontrado:
                # Agregar producto nuevo
                inventario_actual.append(producto_nuevo)
                productos_cargados += 1
        
        accion_realizada = "Fusión"
    
    return (productos_cargados, filas_invalidas, accion_realizada)