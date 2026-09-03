from modules.utils import cargar_datos, guardar_datos

ARCHIVO_VEHICULOS = "data/vehiculos.json"

def registrar_vehiculos():
    vehiculos = cargar_datos(ARCHIVO_VEHICULOS)

    print("\n--- REGISTRAR NUEVO VEHÍCULOS ---")
    placa = input("Ingrese la placa del vehículo (Ej: ABC123): ").strip().upper()

    for v in vehiculos: 
        if v["placa"] == placa:
            print("Error: Ya existe un vehículo registrado con esa placa.")
            return

    tipo = input("Ingrese el tipo de vehículo (carro/moto): ").strip().lower()
    while tipo not in ["moto", "carro"]:
        print("Tipo inválido. Debe ser 'moto' o 'carro'.")
        tipo = input("Ingrese el tipo de vehículo (moto/carro): ").strip().lower()

    nuevo_vehiculo = {
        "placa" : placa,
        "tipo" : tipo,
        "disponible" : True
    }

    vehiculos.append(nuevo_vehiculo)
    guardar_datos(ARCHIVO_VEHICULOS, vehiculos)
    print(f"¡Vehículo con placa {placa} registrado con exito!")


def listar_vehiculos():
    vehiculos = cargar_datos(ARCHIVO_VEHICULOS)

    if not vehiculos:
        print("\nNo hay vehiculos registrados en el sistema.")
        return

    print("\n--- LISTA DE VEHÍCULOS ---")
    for i, v in enumerate(vehiculos, 1):
        estado = "Disponible" if v["disponible"] else "Ocupado/En clase"
        print(f"{i}. Placa: {v['placa']} | Tipo: {v['tipo'].capitalize()} | Estado: {estado}")