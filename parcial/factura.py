class factura:
    def __init__(self,id,vendedor,factura_de_compra):
        self.id = id 
        self.vendedor = vendedor
        self.factura_de_compra = factura_de_compra
    
        
    def  obtener_vendedor(self):
        print("el vendedor es:",self.vendedor)
        
    def obtener_factura_de_compra(self):
         print("la fecha de compra es:",self.factura_de_compra)
               
class detalle_de_la_factura(factura):
    def __init__(self,id,vendedor,factura_de_compra,producto,precio,cantidad):
        super().__init__(id,vendedor,factura_de_compra)
        self. producto = producto
        self. precio = precio
        self. cantidad = cantidad
    
        
    def obtener_datos_de_la_compra(self):
        print("el id es:",self.id,"el producto es:",self.producto) 
        
    def calcular_total(self):
        self.total = self.cantidad*self.precio
        print("el totales:",self.total)
        
x = detalle_de_la_factura(25145,"alexander","20/20/21","carro",50.000,5)   
x.obtener_vendedor()
x.obtener_factura_de_compra()
x.obtener_datos_de_la_compra()
x.calcular_total()
    
    
              
        