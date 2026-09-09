from modules.vehiculos import registrar_vehiculos, listar_vehiculos
from modules.citas import programar_cita, listar_citas, gestionar_asistencia_y_citas
from modules.clientes import registrar_cliente, listar_clientes
from modules.instructores import registrar_instructor, listar_instructores
from modules.sistema_evalucion import registrar_evaluacion, listar_evaluaciones, calcular_promedio



def menu_principal():
    print("\n====================================")
    print("   ACADEMIA DE CONDUCCIÓN DRIVESAFE   ")
    print("======================================")
    print("1. Gestionar Clientes")
    print("2. Gestionar instructores")
    print("3. Gestionar Vehículos")
    print("4. Gestionar Citas y Asistencias")
    print("5. Sistema de evaluaciones") #LÍNEA NUEVA PARA EL PARCIAL
    print("6. salir")


def main():
    while True:
        menu_principal()
        opcion = input("\nSeleccione una opcón (1-6):").strip()

        if opcion == "1":
            print("\n--- GESTIÓN DE CLIENTES ---")
            print("1. Registrar cliente")
            print("2. Listar clientes")
            print("3. Volver")
            sub = input("Elige una opción: ").strip()
            if sub == "1":
                registrar_cliente()
            elif sub == "2":
                listar_clientes()
            elif sub == "3":
                break
            else:
                print("Opción no válida. (1-3)")

        elif opcion == "2":
            while True:
                print("\n--- GESTIÓN DE INSTRUCTORES ---")
                print("1. Registrar instructor")
                print("2. Listar instructores")
                print("3. Volver")
                sub = input("Elige una opción: ").strip()

                if sub == "1":
                    registrar_instructor()
                elif sub == "2":
                    listar_instructores()
                elif sub == "3":
                    break
                else:
                    print("Opción no válida. (1-3)")

        elif opcion == "3":
            while True:
                print("\n--- GESTIÓN DE VEHÍCULOS ---")
                print("1. Registrar vehículo")
                print("2. Listar vehículos")
                print("3. Volver")
                sub = input("Elige una opción: ").strip()

                if sub == "1":
                    registrar_vehiculos()
                elif sub == "2":
                    listar_vehiculos()
                elif sub == "3":
                    break
                else:
                    print("Opción no válida. (1-3)")

        elif opcion == "4":
            while True:
                print("\n--- GESTIÓN DE CITAS ---")
                print("1. Programar cita")
                print("2. Listar citas")
                print("3. Gestionar asistencia")
                print("4. Volver")
                sub = input("Elige una opción: ").strip()

                if sub == "1":
                    programar_cita()
                elif sub == "2":
                    listar_citas()
                elif sub == "3":
                    gestionar_asistencia_y_citas()
                elif sub == "4":
                    break
                else:
                    print("Opción inválida. (1-4)")


       #NUEVA FUNCIÓN DESDE ACA Y MÁS EN EL MODULO SISTEMA_EVALUACIÓN

        elif opcion == "5":
            while True:
                print("\n--- SISTEMA DE EVALUCIÓN") #NUEVO CONJUNTO DE CÓDIGO
                print("1. Registrar nueva evaluación")
                print("2. Consultar evaluacines ")
                print("3. Calcular promedio")
                print("4. Volver")
                sub = input("Elige una opción (1-4) ").strip()

                if sub == "1":
                    registrar_evaluacion()
                elif sub == "2":
                    listar_evaluaciones()
                elif sub == "3":
                    calcular_promedio()
                elif sub == "4":
                    break
                else:
                    print("Opción inválida. (1-4)")
        #HASTA ACA LO NUEVO DEL PARCIAL
                
        elif opcion == "6":
            print("\n¡Nos vemos! Guardando... Cerrando sistema...")
            break

        else:
            print("Opción inválida. Intentalo nuevamente con número del 1 al 5.")

if __name__ == "__main__":
    main()
