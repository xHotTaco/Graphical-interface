
'''
El widget Entry se crea utilizando la clase Entry de Tkinter. Puedes personalizar su apariencia y comportamiento utilizando diversos parámetros y opciones. Algunos de los parámetros comunes son:

width: Especifica el ancho del cuadro de texto en caracteres.
show: Permite ocultar el texto ingresado, como para ingresar contraseñas (puede ser utilizado con el carácter '*').
state: Define si el cuadro de texto está habilitado ("normal") o deshabilitado ("disabled").
textvariable: Asocia una variable de control (StringVar) para almacenar el valor del texto ingresado.
'''

import tkinter as tk

def obtener_texto():
    texto_ingresado = cuadro_texto.get()
    etiqueta.config(text="Texto ingresado: " + texto_ingresado)

ventana = tk.Tk()

etiqueta = tk.Label(ventana, text="Texto ingresado: ")
etiqueta.pack()

cuadro_texto = tk.Entry(ventana, width=30)
cuadro_texto.pack()

boton = tk.Button(ventana, text="Obtener Texto", command=obtener_texto)
boton.pack()

ventana.mainloop()