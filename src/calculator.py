
#====================================================================
# Script: calculator.py
# Descripción: Funciones básicas de una calculadora
# Autor: Laura Ramos Granados
# Fecha: 28/01/26
#====================================================================

def add(a,b):
    """
    >>> add(5,7)
    12
    """
    return a + b

def subtract(a,b): 
    return a - b

def multiply(a,b): 
    return a * b

def divide(a,b):
    """
    >>> divide(10,0)
    Traceback (most recent call last):
    ...
    ZeroDivisionError: La división entre cero no es posible
    """
    if b == 0: 
       raise ZeroDivisionError('La división entre cero no es posible') 
    return a / b

