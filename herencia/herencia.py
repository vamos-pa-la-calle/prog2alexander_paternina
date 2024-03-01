class lote:
    def __int__(self, largo, ancho, constructora):
    
        self.largo = largo
        self.ancho = ancho
        self.constructora = constructora 
        
    def printconstructora(self) :
        print(self.constructora)
        
    def calcular_area(largo,ancho):
             
        x=largo*ancho
   
        
class casa(lote):
        
    def __init__(self,largo,ancho,constructora,propietario,telefono):
        super().__init__ (largo, ancho, constructora)
        self.propietario = propietario
        self.telefono = telefono
    
    def printpropietario(self):
        print(self.propietario)
        
    def printtelefono(self):
        print(self.telefono)        
            
            
                 
v = casa ("25","10","alexander","fredystar",3009403041) 

v.constructora()
v.telefono()
     
     
    