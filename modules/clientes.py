from .utils import cargar_datos, guardar_datos

ARCHIVO_CLIENTES = "data/clientes.json"

def registrar_cliente():
    "Registra un nuevo cliente validando que el documento no se repita."
    clientes = cargar_datos(ARCHIVO_CLIENTES)

    print("\n---REGISTRAR NUEVO CLIENTE---")
    documento = input("Ingrese el numero de documento del cliente:").strip()

    for c in clientes:
        if c["documentos"]==documento:
            print("ERROR: Ya existe un cliente registrado con este documento.")
            return

    nombre=input("Ingrese el nombre completo del cliente:").strip().title()
    telefono=input("Ingrese el telefono de contacto:").strip()

    nuevo_cliente={
        "documento":documento,
        "nombre":nombre,
        "telefono":telefono
    }

    clientes.append(nuevo_cliente)
    guardar_datos(ARCHIVO_CLIENTES,clientes)
    print(f"¡Cliente{nombre}registrado exitosamente!")

def listar_clientes():
    "Muestra en consola todos los clientes registrados."
    clientes=cargar_datos(ARCHIVO_CLIENTES)

    if not clientes:
        print("\nNo hay clientes registrados en el sistema.")
        return

    print("\n---LISTA DE CLIENTES---")
    for i, c in enumerate(clientes, 1):
        print(f"{i}.Documento:{c['dodumento']}Nombre:{c['nombre']}Telefono:{c['telefono']}")


