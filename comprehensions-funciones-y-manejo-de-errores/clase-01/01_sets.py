#conjuntos o sets
set_countries = {'col', 'mex', 'bol'}
print(set_countries)
print(type(set_countries))

#conjunto con numeros
set_numbers = {1, 2, 2, 443, 23}
print(set_numbers)

#conjunto con varios tipos de datos
set_types = {1, 'hola', False, 12.12}
print(set_types)

#conjuntos a partir de un string
set_from_string = set('hoola')
print(set_from_string)

#conjuntos a partir de una tupla
set_from_tuples = set(('abc', 'cbv', 'as', 'abc'))
print(set_from_tuples)

#conjuntos a partir de una lista
numbers = [1, 2, 3, 1, 2, 3, 4]
set_numbers = set(numbers) 
print(set_numbers)

#lo cambiamos a formato lista otra vez
unique_numbers = list(set_numbers)
print(unique_numbers)

