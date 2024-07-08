def main():
    # Inicialización de la variable sw (1 para indicar sistema activo)
    sw = 1
    
    # Bucle principal del programa
    while sw == 1:
        try:
            # Mostrar menú principal al usuario
            print("\nMENU PRINCIPAL:")
            print("1. Ver mi Saldo")
            print("2. Retirar Dinero")
            print("3. Salir")
            
            # Solicitar al usuario que seleccione una opción
            opcion = int(input("Seleccione una opción (1-3): "))
            
            # Validar la opción ingresada
            if opcion < 1 or opcion > 3:
                raise ValueError("Debe ingresar un número entre 1 y 3.")
            
            # Acciones según la opción seleccionada
            if opcion == 1:
                print("Tiene un saldo de $500000.")
                confirmacion_usuario()
            
            elif opcion == 2:
                print("Transferencia realizada.")
                confirmacion_usuario()
            
            elif opcion == 3:
                print("Cierre de sesión exitoso, adiós.")
                sw = 0  # Salir del bucle principal
            
        except ValueError as ve:
            print(f"Error: {str(ve)}. Por favor, ingrese una opción válida (1-3).")

def confirmacion_usuario():
    # Solicitar confirmación al usuario para volver atrás o salir
    while True:
        try:
            opcion = int(input("Presione 1 para volver atrás o 2 para salir: "))
            if opcion == 1:
                break  # Volver al menú principal
            elif opcion == 2:
                print("Cierre de sesión exitoso, adiós.")
                exit()  # Salir del programa completamente
            else:
                raise ValueError("Debe ingresar 1 o 2.")
        
        except ValueError as ve:
            print(f"Error: {str(ve)}. Por favor, ingrese 1 o 2.")

if __name__ == "__main__":
    main()
