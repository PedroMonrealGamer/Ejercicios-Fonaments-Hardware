def kilos(peso):
    resultado = peso / 1000
    return resultado

def toneladas(peso):
    resultado = peso / 1000000
    return resultado

def miligramos(peso):
    resultado = peso * 1000
    return resultado

def insertar_datos():
    print("Elija una de las siguientes opciones:")
    print("1 = Kilogramos")
    print("2 = Toneladas")
    print("3 = Miligramos")
    modo = int(input("Modo elegido: "))
    return modo

modo = insertar_datos()
peso = float(input("Ingrese el peso en gramos: "))

if modo == 1:
    resultado = kilos(peso)
    print(str(peso) + " gramos equivalen a " + str(resultado) + " kilogramos.")
else:
    if modo == 2:
        resultado = toneladas(peso)
        print(str(peso) + " gramos equivalen a " + str(resultado) + " toneladas.")
    else:
        if modo == 3:
            resultado = miligramos(peso)
            print(str(peso) + " gramos equivalen a " + str(resultado) + " miligramos.")
        else:
            print("Opción no válida. Por favor, elija 1, 2 o 3.")
