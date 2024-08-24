countries = {"MX", "COL", "ARG", "USA"}
northAm = {"USA", "CANADA"}
centralAm = {"MX", "GT", "BZ"}
southAm = {"COL", "BZ", "ARG"}

# Escribe tu solución 👇
def unique_elements (element_a, element_b, element_c, element_d):
    return element_a.union(element_b, element_c, element_d)


new_set = unique_elements(countries, northAm, centralAm, southAm)
print(new_set)
