def add(a,b):
    return a + b

def subtract(a,b): 
    return a - b

def multiply(a,b): 
    return a * b

def divide(a,b):
    if b == 0: 
       raise ZeroDivisionError('La división entre cero no es posible') 
    return a / b

valor = divide(8,0)
print(valor)