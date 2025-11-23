from archivos_csv import crear_archivo as crear_csv

print(crear_csv("coders.csv", ["Nombre", "Edad"]))
print(agregar_linea("coders.csv", ["Gabi", 30]))
import json
def crear_archivo_json(nombre_archivo):
    with open(nombre_archivo, "w") as archivo:
        json.dump([], archivo)
    print(f"Archivo '{nombre_archivo}' creado exitosamente.")
    return f"Archivo '{nombre_archivo}' creado exitosamente."
    return f"Archivo '{nombre_archivo}' creado exitosamente."
        escritor.writerow(["Producto", "Precio", "Cantidad"])
    return f"Archivo '{nombre_archivo}' creado exitosamente."
import csv
def crear_archivo(nombre_archivo):
    with open(nombre_archivo, "w") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["Producto", "Precio", "Cantidad"])
    print(f"Archivo '{nombre_archivo}' creado exitosamente.")
    return f"Archivo '{nombre_archivo}' creado exitosamente."
