import tkinter as tk 
from PIL import Image, ImageTk # Requiere instalar Pillow 

ventana = tk.Tk()
#Agregando icono a la ventana
#path = Image.open("c:\Users\Biblioteca\Pictures\Screenshots\Captura de pantalla (1).png")
#icono = ImageTk.PhotoImage(path)
#ventana.iconphoto(True, icono)
# Establecemos el nombre del titulo de la ventana.
ventana.title("interfaz") 
# Establecemos el tamaño de la ventana. ventana.geometry("<ancho>x<alto>+<posición_x>+<posición_y>")

# Obtener las dimensiones de la pantalla
ancho_pantalla = ventana.winfo_screenwidth() #método para obtener Ancho
alto_pantalla = ventana.winfo_screenheight() #método para obtener Alto

# Establecer el tamaño completo de la ventana
ventana.geometry(f"{900}x{900}")
# Definimos si la ventana puede ser modificada en su tamaño.
ventana.resizable(True, True) 
# Podemos añadir configuraciones adicionales a la ventana con la funcion config
ventana.config(bg="gray")



etiqueta = tk.Label(ventana, text="¡Hola, mundo!",bg="yellow", fg="blue", font=("Arial", 16), width=20, height=2, anchor="center")
etiqueta.pack()


# Inicializamos la aplicacion
ventana.mainloop()