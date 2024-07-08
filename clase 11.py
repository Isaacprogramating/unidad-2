def main():
    try:
        # Solicitamos al usuario la cantidad de pasajes a vender
        cantidadPasajes = int(input("Ingrese la cantidad de pasajes a vender: "))

        # Variable para acumular el total de ingresos
        totalIngresos = 0

        # Bucle para iterar sobre la cantidad de pasajes
        for i in range(1, cantidadPasajes + 1):
            while True:
                try:
                    # Solicitamos al usuario el precio del pasaje
                    precio = float(input(f"Ingrese el precio del pasaje {i}: "))
                    totalIngresos += precio
                    break  # Salimos del bucle while si se ingresa un valor válido
                except ValueError:
                    print("Error: Debe ingresar un valor numérico para el precio del pasaje.")

        # Mostramos el total de ingresos
        print(f"\nEl total de ingresos por la venta de pasajes es: {totalIngresos}")

    except ValueError:
        print("Error: Debe ingresar un número entero para la cantidad de pasajes.")

if __name__ == "__main__":
    main()
