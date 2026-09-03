from utils import cargar_datos, guardar_datos

ARCHIVO_CITAS = "data/citas.json"
ARCHIVO_CLIENTES = "data/clientes.json"
ARCHIVO_INSTRUCTORES = "data/instructores.json"
ARCHIVO_VEHICULOS = "data/vehiculos.json"

def programar_cita():
    clientes = cargar_datos(ARCHIVO_CLIENTES)
    instructores = cargar_datos(ARCHIVO_INSTRUCTORES)
    vehiculos = cargar_datos(ARCHIVO_VEHICULOS)
    citas = cargar_datos(ARCHIVO_CITAS)

    print("\n--- PROGRAMAR NUEVA CITA ---")

    if not clientes or not instructores or not vehiculos:
        print("Error: Falta base de datos (debe haber clientes, instructores y vehículos registrados primero).")
        return

    doc_cliente = input("Ingrese el documento del cliente: ").strip()
    cliente_encontrado = next((c for c in clientes if c["documento"] == doc_cliente), None)
    if not cliente_encontrado:
        print("Error: Cliente no encontrado.")
        return

    tipo_clase = input("Ingrese el tipo de clase (moto/carro): ").strip().lower()
    while tipo_clase not in ["moto", "carro"]:
        print("Tipo inválido. Debe ser 'moto' o 'carro'.")
        tipo_clase = input("Ingrese el tipo de clase (moto/carro): ").strip().lower()

    instructores_disponibles = [ins for ins in instructores if ins["especialidad"] == tipo_clase]
    if not instructores_disponibles:
        print(f"No hay instructores con especialidad en '{tipo_clase}'.")
        return
    print(f"\nInstructores disponibles para {tipo_clase}:")
    for i, ins in enumerate(instructores_disponibles, 1):
        print(f"{i}. {ins['nombre']} (Doc: {ins['documento']})")
        


