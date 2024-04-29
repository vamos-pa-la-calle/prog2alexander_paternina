import tkinter as tk

ventana=tk.Tk()
def registrar():
    LframeNombre = tk.Label(frame,text=cnombre.get())
    LframeNombre.pack()
    Lframeapellido = tk.Label(frame,text=capellido.get())
    Lframeapellido.pack()
    Lframeedad = tk.Label(frame,text=cedad.get())
    Lframeedad.pack()
    
ventana.title("alexander")
ventana.geometry("800x600") 
ventana.resizable(True,True)

ventana.config(bg="black")

lnombre=tk.Label(ventana,text="nombre:")
lnombre.place(x=5,y=10)
cnombre=tk.Entry(ventana, width=30)
cnombre.place(x=80,y=10)

lapellido=tk.Label(ventana,text="apellido:")
lapellido.place(x=5,y=40)
capellido=tk.Entry(ventana, width=30)
capellido.place(x=80,y=40)

ledad=tk.Label(ventana,text="edad:")
ledad.place(x=5,y=70)
cedad=tk.Entry(ventana, width=30)
cedad.place(x=80,y=70)

#boton para mostrar informacion
registrar=tk.Button(ventana,text="registrar",command=registrar)
registrar.place(x=130,y=100)
frame = tk.Frame(ventana,width=300,height=150,relief="raised",bd=1)
frame.place(x=20,y=130)

ventana.mainloop()

