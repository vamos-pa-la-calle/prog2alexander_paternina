print("selecione una de las siguientes opciones")
print("1. persona") 
print("2. vehiculo")
print("3. universidad")
print("4. nota")
print("5. salir")  
          

while(True):
      
    opcion =int(input("digita una opcion"))
  
    if opcion == 1:
      print("has precionado la opcion persona")
    if opcion == 2:
      print("has prcionado la opcion vehiculo")
    if opcion == 3:
      print("has precionado la opcion universidad")
    if opcion == 4:
      print("has precionado la opcion notas")
    if opcion == 5:
     print("has precionado la opcion salir")
     break
    if opcion >=6:
     print("opcion invalida")    
    