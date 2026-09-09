#ACA COMIENZA LO QUE AGREGUE EN ESTA CLASE/PARCIAL

from .utils import guardar_datos, cargar_datos

ARCHIVO_CITAS = "data/citas.json"
ARCHIVO_CLIENTES = "data/clientes.json"
ARCHIVO_INSTRUCTORES = "data/instructores.json"
ARCHIVO_VEHICULOS = "data/vehiculos.json"
ARCHIVO_EVALUACIONES = "data/evaluaciones.json"

def registrar_evaluacion():
    evaluaciones = cargar_datos(ARCHIVO_EVALUACIONES)
    clientes = cargar_datos(ARCHIVO_CLIENTES)
    instructores = cargar_datos(ARCHIVO_INSTRUCTORES)

    print("\nProgramar nueva evaluación")

    if not clientes or not instructores:
        print("Error. Faltan datos (Instructor o cliente)")
        return

    cliente_name = input("Ingrese el nombre del cliente: ").strip()
    alumno = next((a for a in clientes if a["nombre"] == cliente_name ), None)

    if not alumno:
        print("Alumno no encontrado")
        return

    instructor_name = input("Ingrese el nombre del instructor: ").strip()
    instructor = next((ins for ins in instructores if ins["nombre"] == instructor_name), None)

    if not instructor:
        print("Instructor no se encuentra en la base de datos")
        return

    fecha_eva = input("Ingrese la fecha para la evaluación (YYYY-MM-DD): ").strip()
    nueva_evaluacion = {
        "alumno": alumno,
        "instructor": instructor,
        "fecha": fecha_eva,
        "nota": "sin calificar"
    }

    evaluaciones.append(nueva_evaluacion)
    guardar_datos(ARCHIVO_EVALUACIONES, evaluaciones)


def listar_evaluaciones():
    evaluaciones = cargar_datos(ARCHIVO_EVALUACIONES)

    print("\nGestión de evaluaciones")
    estudiantes_name = input("Ingrese el nombre del alumno").strip()
    estudiante_name = next((e for e in evaluaciones if e["alumno"] == estudiantes_name), None)

    if not estudiante_name:
        print("El estudiantes aun no tiene evaluaciones asignadas")
        return

    for i, c in enumerate(evaluaciones, 1):
        print(f"\nEvaluaciones del alumno: {c['alumno']}")
        print(f"{i}. Fecha:{c['fecha']} Instructor:{c['instructor']}")

    try:
        seleccion= input("\nSelecione la evaluación que desea calificar(0 para retroceder)")
        if seleccion == 0:
            return
        if seleccion < 1 or seleccion > len(evaluaciones):
            print("Selección no valida")
            return
        evaluacion_elegida=evaluaciones[seleccion-1]
        print("\nDeseas calificar? ")
        print("1. Calificar")
        print("2. Volver")
        opc_cal= input("Seleccione una opción (1-2)")

        if opc_cal == "1":
            Nota= input("Que nota merece el alumno? ").strip()
            evaluacion_elegida["nota"]=Nota 
            guardar_datos(ARCHIVO_EVALUACIONES, evaluaciones)
            print("Nota de evaluación actualizada!")

        elif opc_cal == "2":
            return
        else:
            print("Opción no válida")

    except ValueError:
        print("Por favor ingresa un número válido")


        

def calcular_promedio():
    evaluaciones = cargar_datos(ARCHIVO_EVALUACIONES)
    promedio=0
    estudiante_name=input("Nombre del estudiante: ").strip()
    nombre_estudiante=next((est for est in evaluaciones if est["alumno"] == estudiante_name), None)

    if not nombre_estudiante:
        print("No se encontro al estudiante")
        return
    
    if nombre_estudiante:
        for notas in evaluaciones["nota"]:
            promedio=promedio+notas/len(notas)
        print(f"El promedio del estudiante {nombre_estudiante} es {promedio}")

#FINAL DE LO AGREGADO EN EL PARCIAL
