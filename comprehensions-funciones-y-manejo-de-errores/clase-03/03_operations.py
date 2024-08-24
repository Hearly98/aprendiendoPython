#Union de los elementos de 2 conjuntos
set_a = {'col', 'mex', 'bol'}
set_b = {'pe', 'bol'}

set_c = set_a.union(set_b)
print(f'm1: Unión de elementos: {set_c}')

#Otra forma de hacer la unión de conjuntos
print(f'm2: Unión de elementos: {set_a | set_b}')

#Intersección de los elementos de 2 conjuntos
#Metodo 1
set_c = set_a.intersection(set_b)
print(f'm1: Intersección de los elementos:{set_c}')
#Metodo 2
print(f'm2: Intersección de los elementos: {set_a & set_b}')

#Diferencia de los elementos de 2 conjuntos
#En este metodo se realizará como una resta en la que dejará los elementos del primer conjunto y eliminara los elementos del segundo conjunto
#Metodo 1
set_c = set_a.difference(set_b)
print(f'm1: Diferencias en los elementos: {set_c}')
#Metodo 2
print(f'm2: Diferencias en los elementos: {set_a - set_b}')

#Diferencia simetrica de los elementos de 2 conjuntos
#En este metodo se realizará como una resta simetrica en la que dejará en los elementos los que no tengan en común
set_c = set_a.symmetric_difference(set_b)
#Metodo 1
print(f'm1: Diferencia simetrica en los elementos: {set_c}')
#Metodo 2
print(f' m2: Diferencia simetrica en los elementos: {set_a ^ set_b}')