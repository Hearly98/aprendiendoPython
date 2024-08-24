<h1>Manejo de Excepciones en Python y uso de pass</h1>


## Errores y Excepciones

Errores: Son problemas en el código que pueden ser sintácticos. Los errores detienen la ejecución del programa.

Excepciones: Son eventos que ocurren durante la ejecución de un programa y que alteran el flujo normal del código. A diferencia de los errores, las excepciones pueden ser manejadas para que la ejecución del código no se detenga 

## Errores básicos en Python

SyntaxError: ocurre cuando hay un error en la sintaxis del código
```Python
#Código con SyntaxError
print("Hola mundo"

#Resultado
#SyntaxError: unexpected EOF while parsing
```
TypeError: se produce cuando se realiza una operación en un tipo de dato inapropiado.
```Python
#Codigo con TypeError
resultado = "10" + 5
#Resultado:
#TypeError: can only concatenate str (not "int") to str
```

## Try - except

Esta estructura permite intentar ejecutar un bloque de código y capturar las excepciones que puedan ocurrir. Esto evita que el programa se detenga abruptamente. sino que ofrece la oportunidad de informar al usuario sobre lo que salió mal y cómo puede solucionarlo.

Try se utiliza para definir un bloque de codigo donde se anticipa que puede ocurrir un error. Python ejecuta este bloque y, si ocurre una excepción transifere el control al bloque <strong>except</strong>

Except define un bloque de código que se ejecuta si ocurre una excepción en el bloque try. Aquí manejamos el error, permitiendo limpiar el desorden, o proporcionar mensajes informativos al usuario

## Estructura Basica

La estructura try-except es la siguiente:
```Python
try:
    # Código que puede generar una excepción
    pass
except NombreDeLaExcepcion:
    # Código que maneja la excepción
    pass
```

## Uso de pass

Pass es una declaración nula, no hace nada cuando se ejecuta pero util como marcador de posición para que la estructura del código sea valida.

```Python
def mi_funcion():
    pass  # Marcador de posición para el cuerpo de la función

print("Continuando con el código...")
#Resultado:
#Continuando con el código...
```

Esto evita errores de indentación y permite continuar con el desarrollo del código