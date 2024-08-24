#Modificando conjuntos crud_set
set_countries = {'col', 'mex', 'bol'}

#Tamaño del conjunto
size = len(set_countries)
print(f'Tamaño del conjunto: {size}')

#Preguntamos si colombia esta en el conjunto
print('col' in set_countries)

#Preguntamos si peru esta en el conjunto
print('pe' in set_countries)

#Agregamos un elemento al conjunto
set_countries.add('pe')
print(set_countries)

#Si queremos agregar otra vez a Peru no se agregara porque solo se puede agregar un elemento a la vez
set_countries.add('pe')
print(set_countries)

#Update / actualizar
set_countries.update({'ar', 'ecua', 'pe'})
print(set_countries)  #peru no se agrega porque ya esta en el conjunto

#Remove / eliminar
set_countries.remove('col')
print(set_countries)

#Remover un elemento que no existe
#set_countries.remove('ars') = error

#Remover evitando errores
set_countries.discard('args')
print(set_countries)

#Contamos la cantidad de elementos que hay en el conjunto
print(len(set_countries))
