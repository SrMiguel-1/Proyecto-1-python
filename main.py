from modules.vehiculos import registrar_vehiculos, listar_vehiculos
from modules.citas import programar_cita, listar_citas, gestionar_asistencia_y_citas
from modules.clientes import registrar_cliente, listar_clientes
from modules.instructores import registrar_instructor, listar_instructores

def menu_principal():
    print("\n====================================")
    print("   ACADEMIA DE CONDUCCIÓN DRIVESAFE   ")
    print("======================================")
    print("1. Gestionar Clientes")
    print("2. Gestionar instructores")
    print("3. Gestionar Vehículos")
    print("4. Gestionar Citas y Asistencias")
    print("5. Salir")

def main():
    while True:
        menu_principal()
        opcion = input("\nSeleccione una opcón (1-5):").strip()

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

        elif opcion == "5":
            print("\n¡Nos vemos! Guardando... Cerrando sistema...")
            break
        else:
            print("Opción inválida. Intentalo nuevamente con número del 1 al 5.")

if __name__ == "__main__":
    main()
