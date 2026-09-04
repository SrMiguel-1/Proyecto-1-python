from .utils import cargar_datos, guardar_datos

ARCHIVO_CLIENTES = "data/clientes.json"

def registrar_cliente():
    clientes = cargar_datos(ARCHIVO_CLIENTES)
    
    print("\n--- REGISTRAR NUEVO CLIENTE ---")
    documento = input("Ingrese el documento del cliente: ").strip()
    
    if any(c["documento"] == documento for c in clientes):
        print("Error: Ya existe un cliente con este documento.")
        return

    nombre = input("Ingrese el nombre completo: ").strip()
    telefono = input("Ingrese el teléfono de contacto: ").strip()
    
    nuevo_cliente = {
        "documento": documento,
        "nombre": nombre,
        "telefono": telefono
    }
    
    clientes.append(nuevo_cliente)
    guardar_datos(ARCHIVO_CLIENTES, clientes)
    print(f"¡Cliente {nombre} registrado exitosamente!")

def listar_clientes():
    clientes = cargar_datos(ARCHIVO_CLIENTES)
    
    if not clientes:
        print("\nNo hay clientes registrados en el sistema.")
        return

    print("\n--- LISTA DE CLIENTES REGISTRADOS ---")
    for i, c in enumerate(clientes, 1):
        print(f"{i}. Documento: {c['documento']} | Nombre: {c['nombre']} | Teléfono: {c['telefono']}")
        