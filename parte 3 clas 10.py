def main():
    try:
        # Capturamos el valor ingresado por el usuario
        num1 = float(input("Ingrese un número: "))
        num2 = float(input("Ingrese otro número: "))

        # Realizamos la división
        resultado = num1 / num2

        # Imprimimos el resultado
        print(f"El resultado de la división {num1} / {num2} es: {resultado}")

    except ValueError:
        print("Error: Se esperaba un valor numérico.")
    except ZeroDivisionError:
        print("Error: División por cero no permitida.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {str(e)}")

if __name__ == "__main__":
    main()
