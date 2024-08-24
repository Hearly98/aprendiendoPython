<h1>Prueba Platzi Clase 03</h1>
<p>Para resolver este desafío, debes escribir un algoritmo que elimine los elementos repetidos para obtener un conjunto único llamado <strong>new_set</strong>.

Este algoritmo recibirá como entrada cuatro conjuntos de países, estos países serán de todo el continente americano divididos de la siguiente manera:</p>

<ul>
  <li>countries - Países del continente en general.</li>
  <li>northAmerica - Países del norte de América.</li>
  <li>centralAmerica - Países del centro de América.</li>
  <li>southAmerica - Países del sur de América.</li>
</ul>

<p>
En resumen, el algoritmo deberá eliminar los elementos repetidos de los cuatro conjuntos de países y obtener un conjunto único llamado new_set.</p>

<strong>Ejemplo 1:</strong>
```python
Input: 
{"MX", "COL", "ARG", "USA"},
{"USA", "CA"},
{"MX", "GT", "BZ"},
{"COL", "BZ", "ARG"}

Output:
{'ARG', 'USA', 'CANADA', 'GT', 'COL', 'MX', 'BZ'}
```
<strong>Ejemplo 2:</strong>
```python
Input:
{"BOL"},
{"CA"},
{"MX"},
{"COL"}

Output:

{'COL', 'CA', 'BOL', 'MX'}
```