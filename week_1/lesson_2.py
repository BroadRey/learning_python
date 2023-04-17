from itertools import product


dict_ = {}

while True:
    product = input('Введите название продукта: ')
    
    if product == 'stop':
        break
    
    price = int(input('Введите цену продукта: '))
    dict_[product] = price
    
new_products = []

while True: 
    product = input('Введите название нового продукта: ')
    
    if product == 'stop':
        break
    
    new_products.append(product)    

for products_name in dict_.items():
    va

# Напишите программу, которая постоянно просит пользователя ввести названия продуктов и цены. Хранить все
# из них в словаре, ключами которого являются названия продуктов, а значениями — цены.
# Когда пользователь закончит вводить продукты и цены, разрешите им повторно вводить продукт.
# назовите и напечатайте соответствующую цену или сообщение, если товара нет в словаре