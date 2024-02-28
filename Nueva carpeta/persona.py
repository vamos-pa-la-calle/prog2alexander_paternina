class persona:
    def __init__(self,nombre,apellido,correo,telefono,cedula):
        self.nombre = nombre
        self.apellido = apellido 
        self.correo = correo
        self.telefono = telefono
        self.cedula = cedula 
    def obtenernombre(self):
         return f"mi nimbre es {self.nombre} {self.apellido} {self.correo} {self.telefono} {self.cedula}"


