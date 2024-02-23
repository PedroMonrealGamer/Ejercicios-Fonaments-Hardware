import tkinter as tk

def convertir():
    try:
        dinero = float(entry_valor.get())
        modo = int(entry_modo.get())
        resultado.set(realizar_conversion(dinero, modo))
    except ValueError:
        resultado.set("Error")

def realizar_conversion(dinero, modo):
    if modo in modos_conversion:
        conversion_func = modos_conversion[modo]
        cambio = conversion_func(dinero)
        nombre_moneda = {1: "dólares", 2: "yen", 3: "libras"}[modo]
        return f"{dinero} euros son {cambio:.2f} {nombre_moneda}."
    else:
        return "Modo no válido."

# Ventana
ventana = tk.Tk()
ventana.title("Conversión de monedas visual")
ventana.geometry("400x300")

# Variables
valor_var = tk.StringVar()
modo_var = tk.StringVar()
resultado = tk.StringVar()

# Etiquetas y campos de entrada
tk.Label(ventana, text="Cantidad en euros:").pack
entry_valor = tk.Entry(ventana, textvariable=valor_var)
entry_valor.pack()

tk.Label(ventana, text="Modo de conversión").pack()
tk.Label(ventana, text="1: dólares - 1.09").pack()
tk.Label(ventana, text="2: yen - 162.29").pack()
tk.Label(ventana, text="3: libras - 0.88").pack()

entry_modo = tk.Entry(ventana, textvariable=modo_var)
entry_modo.pack(pady=10)  #pady es como padding de css

# Botón de convertir
tk.Button(ventana, text="Convertir", command=convertir).pack()

# Muestra el
tk.Label(ventana, textvariable=resultado).pack(pady=10)

# Modos de conversión
modos_conversion = {
    1: lambda dinero: dinero * 1.09,
    2: lambda dinero: dinero * 162.29,
    3: lambda dinero: dinero * 0.88
}

ventana.mainloop()
