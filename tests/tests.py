def calculate_total(products, discount=0):
    total =  0
    for product in products:
        total+= product["price"]*(1-discount)
    return total

def test_calculate_total_with_empty_list():
    print('Probando')
    assert calculate_total([], 0.10) == 0
    # Esta condición que estoy escribiendo aquí, debe dar verdadero

def test_calculate_total_with_single_product(): 
    products = [
        {"name": "Notebook",
         "price": 5
         }
    ]
    assert calculate_total(products, 0.10) == 4.5

def test_calculate_total_with_multiple_product(): 
    products = [
        {"name": "Notebook",
         "price": 10
         },
        {"name": "Book",
         "price": 12
         }
    ]
    assert calculate_total(products,0.10) == 19.8


if __name__=='__main__':
    test_calculate_total_with_empty_list()
    test_calculate_total_with_single_product()
    test_calculate_total_with_multiple_product()