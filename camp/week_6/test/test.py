class Product:
    def __init__(self,
                 name: str,
                 price: float,
                 rating: float) -> None:
        self.__name: str = name
        self.__price: float = price
        self.__rating: float = rating

    @property
    def name(self):
        return self.__name


class Category:
    def __init__(self,
                 name: str,
                 products: list[Product]) -> None:
        self.__name: str = name
        self.__products: list[Product] = products

    @property
    def products(self):
        return self.__products


class Busket:
    def __init__(self,
                 products: list[Product]) -> None:
        self.__products: list[Product] = products

    @property
    def products(self):
        return self.__products


class User:
    def __init__(self,
                 login: str,
                 password: str,
                 busket: Busket) -> None:
        self.__login: str = login
        self.__password: str = password
        self.__busket: Busket = busket

    @property
    def busket(self):
        return self.__busket

    @property
    def login(self):
        return self.__login


apple = Product('apple', 10.4, 4)
juice = Product('juice', 40.5, 9)
fruits = Category('fruits', [apple, juice])

beaf = Product('beaf', 150.4, 10)
chicken = Product('chicken', 200.5, 9)
meat = Category('meat', [beaf, chicken])

andrey_busket = Busket([apple, chicken])
andrey = User('andrey_nagibator', 'nagibator_777', andrey_busket)

vasya_busket = Busket([juice, beaf])
vasya = User('vasya_super_boss', 'vasya_mega_super_boss12345', vasya_busket)

print('All products:', end='\n\n')
for category in (fruits, meat):
    for product in category.products:
        print(product.name)

print('\n-----------------------------------------\n')

print('User buskets:', end='\n\n')
for user in (andrey, vasya):
    print(f'{user.login}: ', end='')

    user_busket_products = user.busket.products
    for ix, product in enumerate(user_busket_products):
        if ix == len(user.busket.products) - 1:
            print(f'{product.name}')
            break

        print(f'{product.name}', end=', ')
