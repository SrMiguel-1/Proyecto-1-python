from modules.clientes import gestionar_clientes
from modules.instructores import gestionar_intructores
from modules.vehiculos import gestionar_vehiculos
from modules.citas import gestionar_citas

def mostrar_menu_principal():
    print("\n================================")
    print("  ACADEMIA DE CONDUCCIÓN DRIVESAFE")
    print("==================================")
    print("1. Gestionar Clientes")
    print("2. Gestionar Instructores")
    print("3. Gestionar Vehículos")
    print("4. Gestionar Citas y Asistencias")
    print("5. Salir")

def main():
    while True:
        mostrar_menu_principal()
        opcion = input("\nElige una opción (1-5): ")

        if opcion == "1":
            pass
        elif opcion == "2":
            pass
        elif opcion == "3":
            pass
        elif opcion == "4":
            pass
        elif opcion == "5":
            print("\n¡Hasta luego! Nos vemos después.")
            break
        else:
            print("\nOpcion inválida. Intentalo de nuevo con 1-5")

if __name__ == "__main__":
    main()

    





