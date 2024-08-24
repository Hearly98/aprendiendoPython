<h1>Función print()</h1>

La funcion print es una herramientas que usaremos de multiples maneras a lo largo de nuestro codigo

## Iniciando con un "Hola mundo"
```Python
print('Hola mundo')
```
El uso mas sencillo de print consiste en pasar un texto en comillas que se imprimirá en la terminal
```Python
print("Nunca pares de aprender")
```
## El uso de la coma en print
La coma en la funcion print se usa para separar variables, al hacer esto Python automaticamente añade un espacio entre ellas
```Python
print("Nunca", "pares", "de", "aprender")

#Resultado: "Nunca pares de aprender"
```

## Concatenación
Al concatenar cadenas con el operador +, Python no añade un espacio entre ellas
```Python
print("Nunca" + "pares" + "de" + "aprender")

#Resultado: "Nuncaparesdeaprender"
```
## Uso de sep

El parametro sep permite especificar cómo separar los elementos al imprimir

```Python
#Nota: Puedes cambiar sep por cualquier cadena de caracteres como separador

print("Nunca", "pares", "de", "aprender", sep=",")

```
## Uso de end

El parámetro end cambia lo que se imprime al final de la llamada a print

End es un salto de linea, lo que hace que cada llamada a print comience en una nueva linea.
```Python
print("Nunca", end=" ")
print("pares de aprender")

```
## Impresión de variables
Puedes usar print para mostrar el valor de las variables

Esto es útil para depurar y ver los varloes de las variables en diferentes puntos del programa
```Python
frase = "Nunca pares de aprender"
author = "Platzi"
print("Frase:", frase, "Autor:", author)

#Resultado: 
#Frase: Nunca pares de aprender Autor: Platzi
```

## Uso de formato con f-strings

Las f-strings permiten insertar expresiones dentro de cadenas de texto. Esto hace que sea más legible y facil de escribir

Se antepone la <strong>f</strong> a la cadena de texto, al hacer esto puedes incluir las variables directamente dentro de las llaves {}
```Python
frase = "Nunca pares de aprender"
author = "Platzi"
print(f"Frase: {frase}, Autor: {author}")

#Resultado:
#Frase: Nunca pares de aprender, Autor: Platzi
```

## Uso de formato con format

El metodo format es otra manera de insertar valores en cadenas de texto

```Python
frase = "Nunca pares de aprender"
author = "Platzi"
print("Frase: {}, Autor: {}".format(frase, author))

#Resultado
#Frase: Nunca pares de aprender, Autor: Platz
```

## Impresión con formato específico

Permite controlar el formato de los números al imprimir.

```Python
valor = 3.14159
print("Valor: {:.2f}".format(valor))
#Resultado: Valor: 3.14
```

## Saltos de línea y caracteres especiales

Los saltos de linea en Python se indican con la secuencia de espace /n.

```Python

print("Hola\nmundo")
#Resultado:
#Hola
#mundo
```

Para evitar confusiones de sintaxis al usar comillas simples o dobles usamos secuencias de escape
```Python
print('Hola soy \'Carli\'')
#Resultado
# Hola soy 'Carli'
```

Las secuencias de escape son utiles si necesitamos imprimir una ruta de archivo en windows

```Python
print("La ruta de archivo es: C:\\Users\\Usuario\\Desktop\\archivo.txt")
#Resultado:
#La ruta de archivo es: C:\Users\Usuario\Desktop\archivo.txt
```