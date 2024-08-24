import random
dict = {}
for i in range(1, 5):
  dict[i] = i * 2

print(dict)

#{key: value for var in iterable}}
dict_v2 = { i: i * 2 for i in range(1, 5)}
print(dict_v2)


#Lista de paises
countries = ['col', 'mex', 'bol', 'pe']
population = {}
for country in countries:
  population[country] = random.randint(1, 100)

print(population)

population_v2 = {country: random.randint(1, 100) for country in countries}
print(population_v2)

names = ['nico', 'zule', 'santi']
ages = [12, 56, 98]

#zip hace la union de 2 listas
print(list(zip(names, ages)))

dict_v3 = {name: age for (age, name) in zip(ages, names)}
print(dict_v3)