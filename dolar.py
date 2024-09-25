def convertir_divisas(monto, moneda_destino):
    tasas_cambio = {
        'dolares': 0.047,  # 1 MXN a USD
        'libras': 0.046,   # 1 MXN a GBP
        'pesos_argentinos': 50.6,  # 1 MXN a ARS
        'bolivares': 19138.12,  # 1 MXN a VES
        'euros': 0.055,     # 1 MXN a EUR
    }

    if moneda_destino in tasas_cambio:
        return monto * tasas_cambio[moneda_destino]
    else:
        return None

def main():
    print("Conversor de Divisas (Pesos Mexicanos)")
    print("Opciones:")
    print("a) Pesos a Dólares")
    print("b) Pesos a Libras Esterlinas")
    print("c) Pesos a Pesos Argentinos")
    print("d) Pesos a Bolívares")
    print("e) Pesos a Euros")
    
    opcion = input("Seleccione una opción (a, b, c, d, e): ").lower()
    monto = float(input("Ingrese el monto en Pesos Mexicanos: "))

    if opcion == 'a':
        resultado = convertir_divisas(monto, 'dolares')
        moneda = "Dólares"
    elif opcion == 'b':
        resultado = convertir_divisas(monto, 'libras')
        moneda = "Libras Esterlinas"
    elif opcion == 'c':
        resultado = convertir_divisas(monto, 'pesos_argentinos')
        moneda = "Pesos Argentinos"
    elif opcion == 'd':
        resultado = convertir_divisas(monto, 'bolivares')
        moneda = "Bolívares"
    elif opcion == 'e':
        resultado = convertir_divisas(monto, 'euros')
        moneda = "Euros"
    else:
        print("Opción no válida.")
        return

    if resultado is not None:
        print(f"{monto} Pesos Mexicanos son {resultado:.2f} {moneda}.")
    else:
        print("Error al convertir la divisa.")

if __name__ == "__main__":
    main()