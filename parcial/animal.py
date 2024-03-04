class animal:
    def __init__(self,nombre, fecha_de_vacunas,numero_de_patas, propietario ): 
      
     self.nombre = nombre  
     self.fecha_de_vacunas = fecha_de_vacunas 
     self.numero_de_patas = numero_de_patas
     self.propietario = propietario 
  
    def obtener_animal(self):
        print("su nombre es:",self.nombre)
      
    def obtener_fecha_de_vacunas(self):
        print("la fecha es:",self.fecha_de_vacunas) 
      
    def obtener_numero_de_patas(self):
        print("numero de patas es:",self.numero_de_patas)
        
    def obtener_propietario(self):
        print("nombre del propietario es:",self.propietario)
      
x = animal("luna","12/12/23",4,"alexander")
x.obtener_animal()
x.obtener_fecha_de_vacunas()
x.numero_de_patas()
x.obtener_propietario()
  
         
     
     
     
  
