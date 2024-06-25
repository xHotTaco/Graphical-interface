
'''
Parámetros comunes del widget Button:

text: Especifica el texto que se mostrará en el botón.
command: Especifica la función que se ejecutará cuando el botón sea presionado.
width: Define el ancho del botón en caracteres.
height: Define la altura del botón en líneas.
bg o background: Establece el color de fondo del botón.
fg o foreground: Define el color del texto o los elementos del botón.
font: Define la fuente y el tamaño del texto en el botón.
state: Define el estado del botón, puede ser "normal" (habilitado) o "disabled" (deshabilitado).
relief: Define el estilo de relieve del botón.
padx y pady: Agregan espacio interno horizontal (padx) y vertical (pady) alrededor del texto del botón.
'''

import tkinter as tk


def cambiar_texto():
    etiqueta.config(text="¡Texto cambiado!")

ventana = tk.Tk()
ancho_pantalla = ventana.winfo_screenwidth() #método para obtener Ancho
alto_pantalla = ventana.winfo_screenheight() #método para obtener Alto

ancho_ventana = 300
alto_ventana = 100
posicion_x = (ancho_pantalla - ancho_ventana) // 2
posicion_y = (alto_pantalla - alto_ventana) // 2

# Establecer el tamaño y la posición de la ventana
ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{posicion_x}+{posicion_y}")



etiqueta = tk.Label(ventana, text="Texto original")
etiqueta.pack()
# Crear un botón con texto y función de comando
boton1 = tk.Button(ventana, text="Cambiar", command=cambiar_texto)
boton1.pack()

# Crear un botón con colores de fondo y texto personalizados
boton2 = tk.Button(ventana, text="Botón 2", bg="blue", fg="white", font=("Arial", 12))
boton2.pack()

# Crear un botón deshabilitado
boton3 = tk.Button(ventana, text="Deshabilitado", state="disabled")
boton3.pack()

ventana.mainloop()