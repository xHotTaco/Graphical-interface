'''
El widget Radiobutton se crea utilizando la clase Radiobutton de Tkinter. Puedes personalizar su apariencia y comportamiento utilizando diversos parámetros y opciones. Algunos de los parámetros comunes son:

text: Especifica el texto que se muestra junto al botón de opción.
variable: Permite asociar una variable de control (IntVar, StringVar, etc.) para almacenar y manipular el estado del botón de opción seleccionado.
value: Establece el valor que se asigna a la variable de control cuando el botón de opción está seleccionado.
command: Especifica la función que se ejecutará cuando se seleccione el botón de opción.
state: Define el estado inicial del botón de opción, puede ser "normal" (habilitado) o "disabled" (deshabilitado).
'''

import tkinter as tk

def obtener_seleccion():
    seleccion = variable.get()
    if seleccion == 1:
        print("Opción 1 seleccionada")
    elif seleccion == 2:
        print("Opción 2 seleccionada")
    elif seleccion == 3:
        print("Opción 3 seleccionada")

ventana = tk.Tk()

variable = tk.IntVar()

opcion1 = tk.Radiobutton(ventana, text="Opción 1", variable=variable, value=1, command=obtener_seleccion)
opcion1.pack()

opcion2 = tk.Radiobutton(ventana, text="Opción 2", variable=variable, value=2, command=obtener_seleccion)
opcion2.pack()

opcion3 = tk.Radiobutton(ventana, text="Opción 3", variable=variable, value=3, command=obtener_seleccion)
opcion3.pack()

ventana.mainloop()