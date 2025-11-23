# Contiene las funciones para Leer y Guardar el inventario en los diferentes formatos (TXT, JSON, CSV).


import json
import csv
from utils import validar_entrada_entero # Necesario para la opción de formato

# --- Funciones de Lectura (Leer desde el archivo y cargar a la memoria) ---

def leer_inventario_json(nombre_archivo="inventario.json"):
    """Lee el inventario desde un archivo JSON."""
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as f:
            inventario = json.load(f)
            print(f"✅ Inventario cargado desde {nombre_archivo} (JSON).")
            return inventario
    except FileNotFoundError:
        print(f"ℹ️ Archivo {nombre_archivo} no encontrado. Inicializando inventario vacío.")
        return []
    except json.JSONDecodeError:
        print(f"❌ Error al decodificar JSON en {nombre_archivo}. Archivo corrupto.")
        return []
    except Exception as e:
        print(f"❌ Error desconocido al leer JSON: {e}")
        return []

def leer_inventario_csv(nombre_archivo="inventario.csv"):
    """Lee el inventario desde un archivo CSV."""
    inventario = []
    try:
        with open(nombre_archivo, 'r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    # Convertir tipos de datos
                    inventario.append({
                        "id": int(row['id']),
                        "nombre": row['nombre'],
                        "cantidad": int(row['cantidad']),
                        "precio": float(row['precio'])
                    })
                except (ValueError, KeyError) as e:
                    print(f"⚠️ Error de formato en la fila CSV: {e}. Fila ignorada.")
            print(f"✅ Inventario cargado desde {nombre_archivo} (CSV).")
            return inventario
    except FileNotFoundError:
        print(f"ℹ️ Archivo {nombre_archivo} no encontrado. Inicializando inventario vacío.")
        return []
    except Exception as e:
        print(f"❌ Error desconocido al leer CSV: {e}")
        return []

def leer_inventario_txt(nombre_archivo="inventario.txt"):
    """Lee el inventario desde un archivo TXT (formato: id;nombre;cantidad;precio)."""
    inventario = []
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as f:
            for linea in f:
                try:
                    # Eliminar espacios y dividir por el separador ';'
                    partes = linea.strip().split(';')
                    if len(partes) == 4:
                        inventario.append({
                            "id": int(partes[0]),
                            "nombre": partes[1],
                            "cantidad": int(partes[2]),
                            "precio": float(partes[3])
                        })
                except (ValueError, IndexError) as e:
                    print(f"⚠️ Error de formato en la línea TXT: {e}. Línea ignorada.")
            print(f"✅ Inventario cargado desde {nombre_archivo} (TXT).")
            return inventario
    except FileNotFoundError:
        print(f"ℹ️ Archivo {nombre_archivo} no encontrado. Inicializando inventario vacío.")
        return []
    except Exception as e:
        print(f"❌ Error desconocido al leer TXT: {e}")
        return []

# --- Funciones de Guardado (Guardar el inventario de la memoria al archivo) ---

def guardar_inventario_json(inventario, nombre_archivo="inventario.json"):
    """Guarda el inventario en un archivo JSON."""
    try:
        with open(nombre_archivo, 'w', encoding='utf-8') as f:
            # Usa indent=4 para un formato legible
            json.dump(inventario, f, indent=4) 
        print(f"💾 Inventario guardado con éxito en {nombre_archivo} (JSON).")
    except Exception as e:
        print(f"❌ Error al guardar en JSON: {e}")

def guardar_inventario_csv(inventario, nombre_archivo="inventario.csv"):
    """Guarda el inventario en un archivo CSV."""
    if not inventario:
        print("⚠️ No hay datos para guardar en CSV. Archivo no creado.")
        return
        
    # Obtiene los nombres de las cabeceras (keys del primer diccionario)
    fieldnames = ['id', 'nombre', 'cantidad', 'precio']
    
    try:
        with open(nombre_archivo, 'w', newline='', encoding='utf-8') as f:
            # DictWriter facilita escribir diccionarios como filas
            writer = csv.DictWriter(f, fieldnames=fieldnames) 
            writer.writeheader() # Escribe la fila de cabeceras
            writer.writerows(inventario) # Escribe todas las filas de datos
        print(f"💾 Inventario guardado con éxito en {nombre_archivo} (CSV).")
    except Exception as e:
        print(f"❌ Error al guardar en CSV: {e}")

def guardar_inventario_txt(inventario, nombre_archivo="inventario.txt"):
    """Guarda el inventario en un archivo TXT (formato: id;nombre;cantidad;precio)."""
    try:
        with open(nombre_archivo, 'w', encoding='utf-8') as f:
            for p in inventario:
                # Escribe cada producto en una línea con el separador ';'
                linea = f"{p['id']};{p['nombre']};{p['cantidad']};{p['precio']:.2f}\n"
                f.write(linea)
        print(f"💾 Inventario guardado con éxito en {nombre_archivo} (TXT).")
    except Exception as e:
        print(f"❌ Error al guardar en TXT: {e}")

def seleccionar_formato_guardado(inventario):
    """Permite al usuario elegir y guardar en un formato."""
    print("\n--- Seleccionar Formato de Guardado ---")
    print("1. Guardar como JSON")
    print("2. Guardar como CSV")
    print("3. Guardar como TXT")
    
    opcion = validar_entrada_entero("Seleccione una opción", min_val=1, max_val=3)
    
    if opcion == 1:
        guardar_inventario_json(inventario)
    elif opcion == 2:
        guardar_inventario_csv(inventario)
    elif opcion == 3:
        guardar_inventario_txt(inventario)

def seleccionar_formato_carga(inventario):
    """Permite al usuario elegir y cargar un inventario desde un formato."""
    print("\n--- Seleccionar Formato de Carga ---")
    print("¡Advertencia! Esto reemplazará el inventario actual en memoria.")
    print("1. Cargar desde JSON")
    print("2. Cargar desde CSV")
    print("3. Cargar desde TXT")
    
    opcion = validar_entrada_entero("Seleccione una opción", min_val=1, max_val=3)
    
    if opcion == 1:
        return leer_inventario_json()
    elif opcion == 2:
        return leer_inventario_csv()
    elif opcion == 3:
        return leer_inventario_txt()
    
    return inventario # Retorna el inventario sin cambios si la opción es inválida o no se carga nada