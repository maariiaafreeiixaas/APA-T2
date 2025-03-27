# Segunda tarea de APA 2023: Manejo de números primos

## Nom i cognoms: Maria Freixas Solé

## Fichero `primos.py`

- El alumno debe escribir el fichero `primos.py` que incorporará distintas funciones relacionadas con el manejo
  de los números primos.

- El fichero debe incluir una cadena de documentación que incluirá el nombre del alumno y los tests unitarios
  de las funciones incluidas.

- Cada función deberá incluir su propia cadena de documentación que indicará el cometido de la función, los
  argumentos de la misma y la salida proporcionada.

- Se valorará lo pythónico de la solución; en concreto, su claridad y sencillez, y el uso de los estándares marcados
  por PEP-8. También se valorará su eficiencia computacional.

### Determinación de la *primalidad* y descomposición de un número en factores primos

Incluya en el fichero `primos.py` las tres funciones siguientes:

- `esPrimo(numero)`   Devuelve `True` si su argumento es primo, y `False` si no lo es.
- `primos(numero)`    Devuelve una **tupla** con todos los números primos menores que su argumento.
- `descompon(numero)` Devuelve una **tupla** con la descomposición en factores primos de su argumento.

### Obtención del mínimo común múltiplo y el máximo común divisor

Usando las tres funciones del apartado anterior (y cualquier otra que considere conveniente añadir), escriba otras
dos que calculen el máximo común divisor y el mínimo común múltiplo de sus argumentos:

- `mcm(numero1, numero2)`:  Devuelve el mínimo común múltiplo de sus argumentos.
- `mcd(numero1, numero2)`:  Devuelve el máximo común divisor de sus argumentos.

Estas dos funciones deben cumplir las condiciones siguientes:

- Aunque se trate de una solución sub-óptima, en ambos casos deberá partirse de la descomposición en factores
  primos de los argumentos usando las funciones del apartado anterior.

- Aunque también sea sub-óptimo desde el punto de vista de la programación, ninguna de las dos funciones puede
  depender de la otra; cada una debe programarse por separado.

### Obtención del mínimo común múltiplo y el máximo común divisor para un número arbitrario de argumentos

Escriba las funciones `mcmN()` y `mcdN()`, que calculan el mínimo común múltiplo y el máximo común divisor para un
número arbitrario de argumentos:

- `mcm(*numeros)`:  Devuelve el mínimo común múltiplo de sus argumentos.
- `mcd(*numeros)`:  Devuelve el máximo común divisor de sus argumentos.

### Tests unitarios

La cadena de documentación del fichero debe incluir los tests unitarios de las cinco funciones. En concreto, deberán
comprobarse las siguientes condiciones:

- `esPrimo(numero)`:  Al ejecutar `[ numero for numero in range(2, 50) if esPrimo(numero) ]`, la salida debe ser
                      `[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]`.
- `primos(numeor)`: Al ejecutar `primos(50)`, la salida debe ser `(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)`.
- `descompon(numero)`: Al ejecutar `descompon(36 * 175 * 143)`, la salida debe ser `(2, 2, 3, 3, 5, 5, 7, 11, 13)`.
- `mcm(num1, num2)`: Al ejecutar `mcm(90, 14)`, la salida debe ser `630`.
- `mcd(num1, num2)`: Al ejecutar `mcd(924, 780)`, la salida debe ser `12`.
- `mcmN(numeros)`: Al ejecutar `mcm(42, 60, 70, 63)`, la salida debe ser `1260`.
- `mcdN(numeros)`: Al ejecutar `mcd(840, 630, 1050, 1470)`, la salida debe ser `210`.

### Entrega

#### Ejecución de los tests unitarios

Inserte a continuación una captura de pantalla que muestre el resultado de ejecutar el fichero `primos.py` con la opción
*verbosa*, de manera que se muestre el resultado de la ejecución de los tests unitarios.



#### Código desarrollado

Inserte a continuación el contenido del fichero `primos.py` usando los comandos necesarios para que se realice el
realce sintáctico en Python del mismo.

'''python
"""
Maria Freixas Solé
Módulo que define funciones con números primos

>>> esPrimo(4)
False

>>> esPrimo(-2)
True

>>> esPrimo(-4)
False
"""

def esPrimo(numero):
    """"
    esPrimo retornará True si el número introducido
    solo es divisible por él mismo y uno, o False en caso contrario.
    Para ello, recorre desde 2 hasta numero-1, si es divisible por prova significa que tiene
    un divisor distinto de 1 y él mismo (NO PRIMO).

    >>> esPrimo(1023)
    False

    >>> esPrimo(1021)
    True
    """
    for prova in range(2, numero): #range va del primero al postúltimo
        if numero % prova == 0:
            return False
    
    return True


def primos(numero):
    """
    primos retornará una tupla con todos los numeros primos menores que el número introducido.
    Para ello, se crea una lista vacía que recorre de 2 hasta numero-1. 
    Verificamos con esPrimo() y se añaden los primos a la lista.

    >>> primos(50)
    (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)
    """
    return tuple(n for n in range(2, numero) if esPrimo(n))


def descompon(numero):
    """
    descompon devuelve una tupla con la descomposición en factores primos del número introducido.
    Para ello, se prueba con todos los números primos menores o iguales al número, si uno es divisor del número dado, 
    se almacena y se divide el número repetidamente.

    >>> descompon(36 * 175 * 143)
    (2, 2, 3, 3, 5, 5, 7, 11, 13)
    """
    factores = []
    divisor = 2
    while numero > 1:
        while numero % divisor == 0:
            factores.append(divisor)
            numero //= divisor
        divisor += 1
    return tuple(factores)

def mcm(numero1, numero2):
    """
    mcm devuelve el mínimo común múltiplo de dos números.
    Para ello utilizaremos la función descompon hecha previamente para agilizar el trabajo,
    se toma la mayor potencia de cada factor primo y multiplica los factores seleccionados para obtener el MCM.

    >>> mcm(90, 14) 
    630
    """
    factores1 = descompon(numero1)
    factores2 = descompon(numero2)
    factores_comunes = list(set(factores1) | set(factores2))
    resultado = 1
    for factor in factores_comunes:
        resultado *= factor ** max(factores1.count(factor), factores2.count(factor))
    return resultado

def mcd(numero1, numero2):
    """
    mcd devuelve el máximo común divisor de dos números.
    Para ello utilizaremos la función descompon definida previamente para agilizar el trabajo,
    se toma los factores comunes con menor exponente y multiplica los factores seleccionados para obtener el MCD.

    >>> mcd(924, 780)
    12
    """
    factores1 = descompon(numero1)
    factores2 = descompon(numero2)
    factores_comunes = list(set(factores1) & set(factores2))
    resultado = 1
    for factor in factores_comunes:
        resultado *= factor ** min(factores1.count(factor), factores2.count(factor))
    return resultado

def mcmN(*numeros):
    """
    mcmN devuelve el mínimo común múltiplo de una lista de números.
    Se usa mcm() de dos números en forma iterativa para todos los valores en la lista.

    >>> mcmN(42, 60, 70, 63)
    1260
    """
    return reduce(mcm, numeros)

def mcdN(*numeros):
    """
    mcdN devuelve el máximo común divisor de una lista de números.
    Se usa mcd() de dos números en forma iterativa para todos los valores en la lista.

    >>> mcdN(840, 630, 1050, 1470)
    210
    """
    return reduce(mcd, numeros)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
'''

#### Subida del resultado al repositorio GitHub ¿y *pull-request*?

El fichero `primos.py`, la imagen con la ejecución de los tests unitarios y este mismo fichero, `README.md`, deberán
subirse al repositorio GitHub mediante la orden `git push`. Si los profesores de la asignatura consiguen montar el
sistema a tiempo, la entrega se formalizará realizando un *pull-request* al propietario del repositorio original.

El fichero `README.md` deberá respetar las reglas de los ficheros Markdown y visualizarse correctamente en el repositorio,
incluyendo la imagen con la ejecución de los tests unitarios y el realce sintáctico del código fuente insertado.
