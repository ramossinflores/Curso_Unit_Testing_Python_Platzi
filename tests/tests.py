def calculate_total(products):
    total =  0
    for product in products:
        total+= product["price"]
    return total

def test_calculate_total_with_empty_list():
    print('Probando')
    assert calculate_total([]) == 0
    # Esta condición que estoy escribiendo aquí, debe dar verdadero

def test_calculate_total_with_single_product(): 
    products = [
        {"name": "Notebook",
         "price": 5
         }
    ]
    assert calculate_total(products) == 5

def test_calculate_total_with_multiple_product(): 
    products = [
        {"name": "Notebook",
         "price": 10
         },
        {"name": "Book",
         "price": 12
         }
    ]
    assert calculate_total(products) == 22


if __name__=='__main__':
    test_calculate_total_with_empty_list()
    test_calculate_total_with_single_product()
    test_calculate_total_with_multiple_product()