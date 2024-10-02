def area_cuadrado(lado):
    return lado ** 2

def area_rectangulo(base, altura):
    return base * altura

def area_triangulo(base, altura):
    return (base * altura) / 2

def area_trapecio(base_mayor, base_menor, altura):
    return ((base_mayor + base_menor) * altura) / 2

def calculadora_geometrica():
    print("Selecciona la figura para calcular el área:")
    print("a. Cuadrado")
    print("b. Rectángulo")
    print("c. Triángulo")
    print("d. Trapecio")

    while True:
        opcion = input("\nIngresa el número de la figura (a-d) o 'q' para salir: ")

        if opcion == 'q':
            print("Saliendo de la calculadora.")
            break

        if opcion == 'a':
            lado = float(input("Ingresa el lado del cuadrado: "))
            print(f"El área del cuadrado es: {area_cuadrado(lado)}")

        elif opcion == 'b':
            base = float(input("Ingresa la base del rectángulo: "))
            altura = float(input("Ingresa la altura del rectángulo: "))
            print(f"El área del rectángulo es: {area_rectangulo(base, altura)}")

        elif opcion == 'c':
            base = float(input("Ingresa la base del triángulo: "))
            altura = float(input("Ingresa la altura del triángulo: "))
            print(f"El área del triángulo es: {area_triangulo(base, altura)}")

        elif opcion == 'd':
            base_mayor = float(input("Ingresa la base mayor del trapecio: "))
            base_menor = float(input("Ingresa la base menor del trapecio: "))
            altura = float(input("Ingresa la altura del trapecio: "))
            print(f"El área del trapecio es: {area_trapecio(base_mayor, base_menor, altura)}")

        else:
            print("Opción no válida. Inténtalo de nuevo.")

calculadora_geometrica()
