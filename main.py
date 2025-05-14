from granja import Granja

def main():
    granja = Granja()

    while True:
        print("\n-- Menu --")
        print("1. Agregar cultivo")
        print("2. Agregar animal")
        print("3. Consultar producción total de la granja")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            granja.agregar_cultivo()
        elif opcion == '2':
            granja.agregar_animal()
        elif opcion == '3':
            granja.mostrar_reporte()
        elif opcion == '4':
            break
        else:
            print("Opción no válida")

if _name_ == "_main_":
    main()