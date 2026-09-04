from .utils import cargar_datos, guardar_datos

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

    try:
        idx_ins = int(input("Seleccione el número del instructor: ")) -1
        instructor_elegido = instructores_disponibles[idx_ins]
    except (ValueError, IndexError):
        print("Selección de instructor inválida.")
        return

    vehiculos_disponibles = [v for v in vehiculos if v["tipo"] == tipo_clase and v["disponible"]]
    if not vehiculos_disponibles:
        print(f"No hay vehículos de tipo '{tipo_clase}' disponibles en este momento.")
        return
    print("\nVehículos disponibles:")
    for i, v in enumerate(vehiculos_disponibles, 1):
        print(f"{i}. Placa: {v['placa']}")

    try:
        idx_veh = int(input("Seleccione el número del vehículo: ")) -1
        vehiculo_elegido = vehiculos_disponibles[idx_veh]
    except (ValueError, IndexError):
        print("Selección de vehículo inválida.")
        return

    fecha = input("Ingrese la fecha de la cita (YYYY-MM-DD): ").strip()
    nueva_cita = {
        "cliente": cliente_encontrado["documento"],
        "instructor": instructor_elegido["documento"],
        "vehiculo": vehiculo_elegido["placa"],
        "tipo_clase": tipo_clase,
        "fecha": fecha,
        "estado": "Programada"
    }

    for v in vehiculos:
        if v["placa"] == vehiculo_elegido["placa"]:
            v["disponible"] = False

    guardar_datos(ARCHIVO_VEHICULOS, vehiculos)
    citas.append(nueva_cita)
    guardar_datos(ARCHIVO_CITAS, citas)

    print(f"¡Cita programada exitosamente para el cliente {cliente_encontrado['nombre']}!")

def listar_citas():
    citas = cargar_datos(ARCHIVO_CITAS)

    if not citas:
        print("\nNo hay citas programadas en el sistema.")
        return
    print("\n--- LISTA DE CITAS PROGRAMADAS ---")
    for i, c in enumerate(citas, 1):
        print(f"{i}. Fecha: {c['fecha']} | Tipo: {c['tipo_clase'].capitalize()} | Cliente Doc: {c['cliente']} | Vehículo: {c['vehiculo']} | Estado: {c['estado']}")


def gestionar_asistencia_y_citas():
    citas = cargar_datos(ARCHIVO_CITAS)
    
    if not citas:
        print("\nNo hay citas registradas en el sistema.")
        return

    print("\n--- GESTIÓN DE CITAS Y ASISTENCIAS ---")
    print("Citas actuales:")
    for i, c in enumerate(citas, 1):
        estado = c.get("estado", "Pendiente")
        print(f"{i}. Fecha: {c['fecha']} | Cliente: {c['cliente']} | Vehículo: {c['vehiculo']} | Estado: {estado}")

    try:
        seleccion = int(input("\nSelecciona el número de la cita a gestionar (0 para retroceder): "))
        if seleccion == 0:
            return
        if seleccion < 1 or seleccion > len(citas):
            print("Selección no válida.")
            return
        
        cita_elegida = citas[seleccion - 1]
        
        print(f"\nCita seleccionada para el cliente: {cita_elegida['cliente']}")
        print("1. Marcar como completada")
        print("2. Cancelar / Eliminar cita")
        opcion_gestion = input("Elige una acción (1-2): ").strip()

        if opcion_gestion in ["1", "2"]:
            placa_vehiculo = cita_elegida.get("vehiculo") or cita_elegida.get("vehiculo")
            nombre_instructor = cita_elegida.get("instructor")
            
            if placa_vehiculo:
                vehiculos = cargar_datos(ARCHIVO_VEHICULOS)
                for v in vehiculos:
                    if v.get("placa") == placa_vehiculo:
                        v["disponible"] = True
                guardar_datos(ARCHIVO_VEHICULOS, vehiculos)

            if nombre_instructor:
                instructores = cargar_datos(ARCHIVO_INSTRUCTORES)
                for ins in instructores:
                    if ins.get("nombre") == nombre_instructor or ins.get("documento") == nombre_instructor:
                        ins["estado"] = "Disponible"
                guardar_datos(ARCHIVO_INSTRUCTORES, instructores)
        
        if opcion_gestion == "1":
            cita_elegida["estado"] = "Completada"
            guardar_datos(ARCHIVO_CITAS, citas)
            print("¡Cita marcada como completada! El vehículo, instructor y cliente han quedado libres.")
            
        elif opcion_gestion == "2":
            citas.pop(seleccion - 1)
            guardar_datos(ARCHIVO_CITAS, citas)
            print("¡Cita eliminada del sistema con éxito!")
        else:
            print("Opción no válida.")
            
    except ValueError:
        print("Por favor ingresa un número válido.")
        

