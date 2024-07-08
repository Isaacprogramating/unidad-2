# Definición de variables iniciales (estado de las luces)
luces = {
    "Sala": "apagada",
    "Cocina": "apagada",
    "Dormitorio": "apagada"
}

# Función para mostrar el estado actual de las luces
def mostrar_estado_luces():
    print("\nEstado actual de las luces:")
    for habitacion, estado in luces.items():
        print(f"{habitacion}: {estado}")

# Función para cambiar el estado de una luz (encender o apagar)
def cambiar_estado_luz(habitacion):
    if luces[habitacion] == "apagada":
        luces[habitacion] = "encendida"
        print(f"Luz de {habitacion} encendida.")
    else:
        luces[habitacion] = "apagada"
        print(f"Luz de {habitacion} apagada.")

# Función principal del programa
def main():
    while True:
        # Mostrar el menú de opciones
        print("\nMenú de control de luces:")
        print("1. Encender/Apagar luz de la Sala")
        print("2. Encender/Apagar luz de la Cocina")
        print("3. Encender/Apagar luz del Dormitorio")
        print("4. Mostrar estado de todas las luces")
        print("5. Salir")

        try:
            opcion = int(input("Seleccione una opción (1-5): "))
            
            if opcion == 1:
                cambiar_estado_luz("Sala")
            elif opcion == 2:
                cambiar_estado_luz("Cocina")
            elif opcion == 3:
                cambiar_estado_luz("Dormitorio")
            elif opcion == 4:
                mostrar_estado_luces()
            elif opcion == 5:
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")
        
        except ValueError:
            print("Error: Debe ingresar un número.")
        except KeyError:
            print("Error: Opción no válida.")

if __name__ == "__main__":
    main()
