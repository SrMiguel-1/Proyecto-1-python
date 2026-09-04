from .utils import cargar_datos, guardar_datos

ARCHIVO_INSTRUCTORES = "data/instructores.json"

def registrar_instructor():
    instructores = cargar_datos(ARCHIVO_INSTRUCTORES)
    
    print("\n--- REGISTRAR NUEVO INSTRUCTOR ---")
    documento = input("Ingrese el documento del instructor: ").strip()
    
    if any(i["documento"] == documento for i in instructores):
        print("Error: Ya existe un instructor con este documento.")
        return

    nombre = input("Ingrese el nombre completo: ").strip()
    
    print("Seleccione la especialidad:")
    print("1. Carro")
    print("2. Moto")
    opcion_esp = input("Elija una opción (1-2): ").strip()
    
    if opcion_esp == "1":
        especialidad = "carro"
    elif opcion_esp == "2":
        especialidad = "moto"
    else:
        print("Opción de especialidad no válida. Se cancela el registro.")
        return

    nuevo_instructor = {
        "documento": documento,
        "nombre": nombre,
        "especialidad": especialidad
    }
    
    instructores.append(nuevo_instructor)
    guardar_datos(ARCHIVO_INSTRUCTORES, instructores)
    print(f"¡Instructor {nombre} registrado con especialidad en {especialidad}!")

def listar_instructores():
    instructores = cargar_datos(ARCHIVO_INSTRUCTORES)
    
    if not instructores:
        print("\nNo hay instructores registrados en el sistema.")
        return

    print("\n--- LISTA DE INSTRUCTORES REGISTRADOS ---")
    for i, ins in enumerate(instructores, 1):
        print(f"{i}. Documento: {ins['documento']} | Nombre: {ins['nombre']} | Especialidad: {ins['especialidad'].capitalize()}")
