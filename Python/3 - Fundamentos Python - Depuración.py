def insertar_valor():
    dinero = float(input("Inserta la cantidad que quieres convertir: "))
    return dinero

def insertar_modo():
    print("MODOS:")
    print("1 = Dólar USD")
    print("2 = Yen JPY")
    print("3 = Libra esterlina GBP")
    modo = int(input("Inserte el número correspondiente al modo de conversión: "))
    return modo

def dolar(dinero):
    return dinero * 1.09

def yen(dinero):
    return dinero * 162.29

def libra(dinero):
    return dinero * 0.88

modos_conversion = {
    1: dolar,
    2: yen,
    3: libra
}

modo = insertar_modo()
dinero = insertar_valor()

if modo in modos_conversion:
    conversion_func = modos_conversion[modo]
    cambio = conversion_func(dinero)
    nombre_moneda = {1: "dólares", 2: "yen", 3: "libras"}[modo]
    print(f"{dinero} euros son {cambio} {nombre_moneda}.")
else:
    print("Modo no válido.")
