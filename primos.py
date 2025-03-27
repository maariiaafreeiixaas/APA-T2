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
    esPrimo retornarà True si el número introducido"
    solo es divisible por él mismo y uno,
    o False en caso contrario.

    >>> esPrimo(1023)
    False

    >>> esPrimo(1021)
    True
    """
    for prova in range(2, numero): #range va del primero al postúltimo
        if numero % prova == 0:
            return False
    
    return True

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    