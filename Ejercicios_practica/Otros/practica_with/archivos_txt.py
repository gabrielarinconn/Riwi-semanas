import csv

def crear_archivo(nombre_archivo):
    with open(nombre_archivo, "w") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["Producto", "Precio", "Cantidad"])
    |   por favor elige una de las siguientes opciones:|        
    |------------------------------------------------|
    | 1. Agregar un nuevo producto al inventario      |
    | 2. Mostrar inventario completo                  |             
    | 3. Mostrar estadísticas del inventario         |
    | 4. Salir del sistema                            |
    |------------------------------------------------|
    Elige una opción: """)
    print(f"Archivo '{nombre_archivo}' creado exitosamente.")
    