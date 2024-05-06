import tkinter as tk

class VentanaInicioSesion:
    def __init__(self, master):
        self.master = master
        self.master.title("Inicio de Sesión")
        self.master.geometry("800x500")
      
        self.frame_izquierdo = tk.Frame(self.master, bg="white", width=200, height=500)
        self.frame_izquierdo.pack(side=tk.LEFT, fill=tk.Y)
             
        self.logo = tk.Label(self.frame_izquierdo, text="logo",font=("Arial", 70))
        self.logo.pack(pady=200)
     
        self.frame_derecho = tk.Frame(self.master, bg="lightgray", width=600, height=500)
        self.frame_derecho.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.label_titulo = tk.Label(self.frame_derecho, text="Inicio de Sesión", font=("Arial", 18))
        self.label_titulo.pack(pady=20)

        self.label_usuario = tk.Label(self.frame_derecho, text="Usuario:", font=("Arial", 12))
        self.label_usuario.pack()

        self.entry_usuario = tk.Entry(self.frame_derecho, font=("Arial", 12), width=30)
        self.entry_usuario.pack(pady=50)

        self.label_clave = tk.Label(self.frame_derecho, text="Contraseña:", font=("Arial", 12))
        self.label_clave.pack()

        self.entry_clave = tk.Entry(self.frame_derecho, font=("Arial", 12), width=30, show="*")
        self.entry_clave.pack(pady=5)

        self.boton_ingresar = tk.Button(self.frame_derecho, text="Ingresar", font=("Arial", 20), command=self.ingresar)
        self.boton_ingresar.pack(pady=80)

    def ingresar(self):
        usuario = self.entry_usuario.get()
        clave = self.entry_clave.get()
        print("Usuario:", usuario)
        print("Clave:", clave)
        # Aquí puedes agregar la lógica para verificar el usuario y contraseña

def main():
    root = tk.Tk()
    app = VentanaInicioSesion(root)
    root.mainloop()

if __name__ == "__main__":
    main()


