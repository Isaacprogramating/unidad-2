def main():
    productos = {
        "Pan ciabatta": 2000,
        "Pie de limón": 3500,
        "Café": 2200,
        "Té": 1600,
        "Alfajor": 1000
    }
    
    # Variables para almacenar las ventas y el total del día
    ventas_diarias = {}
    total_ventas = 0
    
    try:
        # Iteramos sobre cada producto
        for producto, precio in productos.items():
            while True:
                try:
                    # Solicitamos la cantidad vendida del producto
                    cantidad = int(input(f"Ingrese la cantidad vendida de {producto}: "))
                    
                    # Verificamos si la cantidad ingresada es válida
                    if cantidad < 0:
                        raise ValueError("La cantidad no puede ser negativa.")
                    
                    # Calculamos el total por producto y acumulamos al total del día
                    ventas_diarias[producto] = cantidad * precio
                    total_ventas += ventas_diarias[producto]
                    
                    break  # Salimos del bucle while si la entrada es válida
                
                except ValueError:
                    print("Error: Debe ingresar un número entero positivo.")
    
    except Exception as e:
        print(f"Ocurrió un error inesperado: {str(e)}")
    
    else:
        # Mostramos el informe de ventas
        print("\nInforme de Ventas Diarias:")
        for producto, total in ventas_diarias.items():
            print(f"{producto}: ${total}")
        print(f"Total Ventas del Día: ${total_ventas}")
        
        # Guardamos el informe en un archivo de texto
        try:
            with open("informe_ventas.txt", "w") as archivo:
                archivo.write("Informe de Ventas Diarias:\n")
                for producto, total in ventas_diarias.items():
                    archivo.write(f"{producto}: ${total}\n")
                archivo.write(f"Total Ventas del Día: ${total_ventas}\n")
                
                print("\nInforme de ventas guardado correctamente en 'informe_ventas.txt'.")
        
        except Exception as e:
            print(f"Error al intentar guardar el informe: {str(e)}")

if __name__ == "__main__":
    main()
