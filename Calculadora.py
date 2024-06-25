import tkinter as tk
from tkinter import messagebox

def agregar_texto(valor):
    contenido_actual = cuadro_texto.get()
    cuadro_texto.delete(0, tk.END)
    cuadro_texto.insert(tk.END, contenido_actual + str(valor))

def limpiar_texto():
    cuadro_texto.delete(0, tk.END)

def borrar_uno():
    contenido_actual = cuadro_texto.get()
    cuadro_texto.delete(0, tk.END)
    cuadro_texto.insert(tk.END, contenido_actual[:-1])

def calcular_resultado():
    try:
        resultado = eval(cuadro_texto.get())
        cuadro_texto.delete(0, tk.END)
        cuadro_texto.insert(tk.END, str(resultado))
    except Exception as e:
        messagebox.showerror("Error", "Entrada inválida")
        limpiar_texto()

def calcular_porcentaje():
    try:
        contenido_actual = cuadro_texto.get()
        resultado = eval(contenido_actual) / 100
        cuadro_texto.delete(0, tk.END)
        cuadro_texto.insert(tk.END, str(resultado))
    except Exception as e:
        messagebox.showerror("Error", "Entrada inválida")
        limpiar_texto()

ventana = tk.Tk()
ventana.geometry("322x350")
ventana.title("Calculadora")
ventana.configure(bg="black")

cuadro_texto = tk.Entry(ventana, width=50, bg="black", fg="white", font=("Arial", 12))
cuadro_texto.place(x=2, y=20, width=316, height=50)

# Función para crear botones
def crear_boton(ventana, text, x, y, command):
    return tk.Button(ventana, text=text, bg="black", fg="white", font=("Arial", 12), relief="flat", command=command).place(x=x, y=y, width=78, height=50)

# Botones adicionales
crear_boton(ventana, "C", 2, 88, limpiar_texto)          #Botón para limpiar todo
crear_boton(ventana, "/", 82, 88, lambda: agregar_texto('/'))   # Botón de división
crear_boton(ventana, "%", 162, 88, calcular_porcentaje)   # Botón de porcentaje
crear_boton(ventana, "←", 242, 88, borrar_uno)           # Botón para borrar un carácter

# Botones Número Izquierda
crear_boton(ventana, "7", 2, 140, lambda: agregar_texto(7))
crear_boton(ventana, "4", 2, 192, lambda: agregar_texto(4))
crear_boton(ventana, "1", 2, 244, lambda: agregar_texto(1))
crear_boton(ventana, "00", 2, 296, lambda: agregar_texto('00'))

# Botones Número Medio
crear_boton(ventana, "8", 82, 140, lambda: agregar_texto(8))
crear_boton(ventana, "5", 82, 192, lambda: agregar_texto(5))
crear_boton(ventana, "2", 82, 244, lambda: agregar_texto(2))
crear_boton(ventana, "0", 82, 296, lambda: agregar_texto(0))

# Botones Número Derecha
crear_boton(ventana, "9", 162, 140, lambda: agregar_texto(9))
crear_boton(ventana, "6", 162, 192, lambda: agregar_texto(6))
crear_boton(ventana, "3", 162, 244, lambda: agregar_texto(3))
crear_boton(ventana, ".", 162, 296, lambda: agregar_texto('.'))

# Botones Acciones
crear_boton(ventana, "*", 242, 140, lambda: agregar_texto('*'))
crear_boton(ventana, "-", 242, 192, lambda: agregar_texto('-'))
crear_boton(ventana, "+", 242, 244, lambda: agregar_texto('+'))
crear_boton(ventana, "=", 242, 296, calcular_resultado)

ventana.mainloop()
