'''
El widget Checkbutton se crea utilizando la clase Checkbutton de Tkinter. Puedes personalizar su apariencia y comportamiento utilizando diversos parámetros y opciones. Algunos de los parámetros comunes son:

text: Especifica el texto que se muestra junto a la casilla de verificación.
variable: Permite asociar una variable de control (IntVar, StringVar, etc.) para almacenar y manipular el estado de la casilla de verificación.
onvalue y offvalue: Establecen los valores que se asignan a la variable de control cuando la casilla de verificación está seleccionada (onvalue) o deseleccionada (offvalue).
command: Especifica la función que se ejecutará cuando el estado de la casilla de verificación cambie.
state: Define el estado inicial de la casilla de verificación, puede ser "normal" (habilitada) o "disabled" (deshabilitada).
'''

import tkinter as tk

def obtener_estado():
    if variable.get() == 1:
        print("La casilla de verificación está seleccionada")
    else:
        print("La casilla de verificación no está seleccionada")

ventana = tk.Tk()

variable = tk.IntVar()

casilla_verificacion = tk.Checkbutton(ventana, text="Opción 1", variable=variable, command=obtener_estado)
casilla_verificacion.pack()

ventana.mainloop()