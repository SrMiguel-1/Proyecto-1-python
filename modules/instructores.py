from .utils import cargar_datos, guardar_datos

ARCHIVO_INSTRUCTORES = "data/instructores.json"
from .utils import cargar_datos, guardar_datos

ARCHIVO_INSTRUCTORES = "data/instructores.json"


def registrar_instructor():
	instructores = cargar_datos(ARCHIVO_INSTRUCTORES)
	print("\n--- REGISTRAR INSTRUCTOR ---")
	documento = input("Documento: ").strip()
	if not documento:
		print("El documento es obligatorio.")
		return
	if any(instructor["documento"] == documento for instructor in instructores):
		print("Ya existe un instructor con ese documento.")
		return
	nombre = input("Nombre completo: ").strip()
	especialidad = input("Especialidad (moto/carro): ").strip().lower()
	if especialidad not in ("moto", "carro"):
		print("La especialidad debe ser 'moto' o 'carro'.")
		return
	instructores.append({"documento": documento, "nombre": nombre, "especialidad": especialidad})
	guardar_datos(ARCHIVO_INSTRUCTORES, instructores)
	print("Instructor registrado exitosamente.")


def listar_instructores():
	instructores = cargar_datos(ARCHIVO_INSTRUCTORES)
	print("\n--- LISTA DE INSTRUCTORES ---")
	if not instructores:
		print("No hay instructores registrados.")
		return
	for numero, instructor in enumerate(instructores, 1):
		print(f"{numero}. {instructor['nombre']} | Documento: {instructor['documento']} | Especialidad: {instructor['especialidad'].capitalize()}")


def gestionar_instructores():
	while True:
		print("\n1. Registrar instructor\n2. Listar instructores\n3. Volver")
		opcion = input("Seleccione una opción: ").strip()
		if opcion == "1":
			registrar_instructor()
		elif opcion == "2":
			listar_instructores()
		elif opcion == "3":
			return
		else:
			print("Opción inválida.")
