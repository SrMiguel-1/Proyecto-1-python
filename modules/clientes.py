from .utils import cargar_datos, guardar_datos

ARCHIVO_CLIENTES = "data/clientes.json"
from .utils import cargar_datos, guardar_datos

ARCHIVO_CLIENTES = "data/clientes.json"


def registrar_cliente():
	clientes = cargar_datos(ARCHIVO_CLIENTES)
	print("\n--- REGISTRAR CLIENTE ---")
	documento = input("Documento: ").strip()
	if not documento:
		print("El documento es obligatorio.")
		return
	if any(cliente["documento"] == documento for cliente in clientes):
		print("Ya existe un cliente con ese documento.")
		return
	nombre = input("Nombre completo: ").strip()
	telefono = input("Teléfono: ").strip()
	if not nombre:
		print("El nombre es obligatorio.")
		return
	clientes.append({"documento": documento, "nombre": nombre, "telefono": telefono})
	guardar_datos(ARCHIVO_CLIENTES, clientes)
	print("Cliente registrado exitosamente.")


def listar_clientes():
	clientes = cargar_datos(ARCHIVO_CLIENTES)
	print("\n--- LISTA DE CLIENTES ---")
	if not clientes:
		print("No hay clientes registrados.")
		return
	for numero, cliente in enumerate(clientes, 1):
		print(f"{numero}. {cliente['nombre']} | Documento: {cliente['documento']} | Teléfono: {cliente['telefono']}")


def gestionar_clientes():
	while True:
		print("\n1. Registrar cliente\n2. Listar clientes\n3. Volver")
		opcion = input("Seleccione una opción: ").strip()
		if opcion == "1":
			registrar_cliente()
		elif opcion == "2":
			listar_clientes()
		elif opcion == "3":
			return
		else:
			print("Opción inválida.")
