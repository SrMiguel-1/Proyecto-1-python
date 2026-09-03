from modules.utils import cargar_datos,guardar_datos
ARCHIVO_INSTRUCTORES= "data/instructores.json"

def registrar_instructor():
    "Registra un instructor exigiendo especialidad obligatoria (moto o carro)."
    instructores=cargar_datos(ARCHIVO_INSTRUCTORES)

    print("\n--- REGISTRAR NUEVO INSTRUCTOR ---")
    documento = input("Ingrese el documento del instructor: ").strip()

    for ins in instructores:
        if ins["documento"] == documento:
            print("ERROR:Ya existe un instructor registrado con este documento.")
            return

    nombre=input("Ingrese el nombre completo del instructor:").strip().title()

    especialidad=input("Ingrese la especialidad del instructor(moto/carro):").strip().lower()
    while especialidad not in ["moto","carro"]:
        print("Especialidad invalidad.Debe ser exactamente 'moto'o 'carro'.")
        especialidad=input("Ingrese la especialidad del instructor(moto/carro):").strip().lower()

        nuevo_instructor={
            "documento": documento,
            "nombre":nombre,
            "especialidad":especialidad
        }

        instructores.append(nuevo_instructor)
        guardar_datos(ARCHIVO_INSTRUCTORES, instructores)
        print(f"¡Instructor{nombre}registrado con especialidad en {especialidad}exitosamente!")

        def listar_instructores():
            "Muestra en consola todos los instructores registrados."
            instructores=cargar_datos(ARCHIVO_INSTRUCTORES)

        if not instructores:
            print("\n---LISTA DE INSTRUCTORES---")
            for i,ins in enumerate(instructores,1):
                print(f"{i}Documento:{ins['documento']}---Nombre:{ins['nombre']}---Especialidad: {ins['especialidad'].capitalize()}")