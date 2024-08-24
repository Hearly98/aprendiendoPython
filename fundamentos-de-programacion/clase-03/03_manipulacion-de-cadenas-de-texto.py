name = 'Carli'
caracter = 'c'
print(type(caracter))

print(type(name))

#Comillas triples son sensibles a los saltos de linea
name2 = '''Carli


Marcela'''
print(name2)

name3 = 'CARLA Marcela'
print(name3[0])
print(name3[2])
#Si salimos de la cadena nos enviará un error de indexación
print(name3[-1])

last_name = 'Florida Roman'
print(name3 + " " + last_name)
print(5 * name3)
#Devuelve la longitud de la cadena o cuantos caracteres tiene la cadena
print(len(name))
print(last_name)
#Convertir a minuscula
print(name3.lower())
print(name3.upper())
