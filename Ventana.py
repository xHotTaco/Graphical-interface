'''
Importamos tkinter para poder hacer uso de la interfas y sacar una ventana
'''
import tkinter as tk

'''
iniciamos la ventana de  esta manera para hacer uso 
"ventana = tk.Tk()" con esto llamamos a la ventana
Y con esto "ventana.mainloop()" hacemos que se quede abierta
'''
ventana = tk.Tk()


'''
Podemos darle caracteristicas en especifico a la ventana

'''


#Para ponerla en la mitad de la pantalla

# Obtener las dimensiones de la pantalla
ancho_pantalla = ventana.winfo_screenwidth() #método para obtener Ancho
alto_pantalla = ventana.winfo_screenheight() #método para obtener Alto

# Calcular las coordenadas para centrar la ventana
ancho_ventana = 800
alto_ventana = 600
posicion_x = (ancho_pantalla - ancho_ventana) // 2
posicion_y = (alto_pantalla - alto_ventana) // 2

# Establecer el tamaño y la posición de la ventana
ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{posicion_x}+{posicion_y}")

ventana.mainloop()