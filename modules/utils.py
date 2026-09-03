import json
import os

def cargar_datos(nombre_archivo):
    if not os.path.exists(nombre_archivo):
        return []
    try:
        with open(nombre_archivo, "r", encoding= "utf-8") as archivo:
            return json.load(archivo)
    except json.JSONDecodeError:
        return []

def guardar_datos(nombre_archivo, datos):
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)

