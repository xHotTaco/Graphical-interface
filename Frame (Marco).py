'''
El widget Frame se crea utilizando la clase Frame de Tkinter. Puedes personalizar su apariencia y comportamiento utilizando diversos parámetros y opciones. Algunos de los parámetros comunes son:

width: Especifica el ancho del marco en píxeles.
height: Especifica la altura del marco en píxeles.
bg o background: Establece el color de fondo del marco.
relief: Define el estilo de relieve o borde del marco.
borderwidth o bd: Define el ancho del borde del marco.
highlightbackground y highlightcolor: Establecen el color del resaltado del marco cuando se enfoca.
'''

import tkinter as tk

ventana = tk.Tk()

# Crear un marco con borde sólido
marco1 = tk.Frame(ventana, width=200, height=100, bd=2, relief="solid")
marco1.pack()

# Agregar una etiqueta al marco1
etiqueta1 = tk.Label(marco1, text="Marco 1")
etiqueta1.pack()
etiqueta3 = tk.Label(marco1, text="Marco 1")
etiqueta3.pack()
# Crear un marco con borde en relieve
marco2 = tk.Frame(ventana, width=200, height=100, bd=2, relief="raised")
marco2.pack()

# Agregar una etiqueta al marco2
etiqueta2 = tk.Label(marco2, text="Marco 2")
etiqueta2.pack()

ventana.mainloop()