
perro={
'nombre': 'diana',
  'color': 'negro',
    'raza': 'pincher',
      'patas': '4',
        'edad': 'un años'

}

print(perro)

estudiante={
'nombre' : 'alexander',
 'apellido': 'paternina',
  'sexo' : 'hombre',
   'edad': '32',
    'estado civil': 'soltero',
     'habilidades': ['comer', 'dormir', 'jugar'],
      'pais': 'colombia',
       'ciudad': 'cartagena',

}
print(estudiante)

print(f"(key): (value)")
         
for key, value in estudiante.items():
    print(f"{key} : {value}")
         
longitud_estudiante = len(estudiante)
print("longitud_estudiante", longitud_estudiante)

print("\nValue of habilidades")
for habilidades in estudiante ['habilidades']:
   print(habilidades)

print("\nhabilidades actualizado")
estudiante['habilidades'].extend(['volar'])
print(estudiante['habilidades'])

print("\nsolo keys")
for key in estudiante:
    print(key)

print("\nsolo valores")
print(estudiante.values())

print("\ncambiar el dicionario por una lista de elementos")
print(estudiante.items)

print("\nborrar elemento")
estudiante.pop('nombre')  
print(estudiante)

print("\nelementos borrados")
estudiante.clear         