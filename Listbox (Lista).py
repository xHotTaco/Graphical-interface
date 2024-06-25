'''
El widget Listbox se crea utilizando la clase Listbox de Tkinter. Puedes personalizar su apariencia y comportamiento utilizando diversos parámetros y opciones. Algunos de los parámetros comunes son:

width: Especifica el ancho del cuadro de lista en caracteres.
height: Especifica la altura del cuadro de lista en líneas.
selectmode: Define el modo de selección, puede ser "single" (solo se puede seleccionar un elemento a la vez) o "multiple" (se pueden seleccionar múltiples elementos).
exportselection: Controla si la selección del cuadro de lista se puede exportar a otros widgets o aplicaciones.
activestyle: Define el estilo visual del elemento seleccionado.
listvariable: Permite asociar una variable de control (StringVar, IntVar, etc.) para almacenar y manipular la selección del cuadro de lista.
'''

import tkinter as tk

def obtener_seleccion():
    seleccionados = cuadro_lista.curselection()
    for index in seleccionados:
        elemento = cuadro_lista.get(index)
        print("Elemento seleccionado:", elemento)

ventana = tk.Tk()

cuadro_lista = tk.Listbox(ventana, width=30, selectmode="multiple")
cuadro_lista.pack()

elementos = ["Elemento 1", "Elemento 2", "Elemento 3", "Elemento 4"]

for elemento in elementos:
    cuadro_lista.insert(tk.END, elemento)

boton = tk.Button(ventana, text="Obtener", command=obtener_seleccion)
boton.pack()

ventana.mainloop()