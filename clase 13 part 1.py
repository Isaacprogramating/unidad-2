# Puntos iniciales del usuario
puntos = 100000

# Ciclo principal para el canje de puntos
while True:
    try:
        # Mostrar opciones de canje y solicitar la selección al usuario
        print("Seleccione una opción de canje:")
        print("1. Canje de 10000 puntos")
        print("2. Canje de 25000 puntos")
        print("3. Canje de 30000 puntos")
        print("4. Salir")
        continu = int(input("Ingrese el número de la opción deseada: "))

        # Verificar la selección del usuario
        if continu == 1:
            puntos -= 10000
            print(f"Canje exitoso, le quedan: ${puntos} puntos")
        elif continu == 2:
            puntos -= 25000
            print(f"Canje exitoso, le quedan: ${puntos} puntos")
        elif continu == 3:
            puntos -= 30000
            print(f"Canje exitoso, le quedan: ${puntos} puntos")
        elif continu == 4:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, ingrese una opción válida.")

    except ValueError:
        print("Error: Debe ingresar un número.")

# Finalizar el programa
print("Gracias por usar nuestro sistema de canje de puntos.")
