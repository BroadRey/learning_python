# Интернет магазин
#  1. Создать класс Товар, имеющий переменные имя, цена, рейтинг. 
#  2. Создать класс Категория, имеющий переменные имя и массив товаров. Создать несколько объектов класса Категория. 
#  3. Создать класс Basket, содержащий массив купленных товаров. 
#  4. Создать класс User, содержащий логин, пароль и объект класса Basket. Создать несколько объектов класса User.
#  5. Вывести на консоль каталог продуктов.
#  6. Вывести на консоль покупки посетителей магазина.


class Product:
    def __init__(self,
                 name: str,
                 price: float,
                 rating: float) -> None:
        self.__name: str = name
        self.__price: float = price
        self.__rating: float = rating

    def __str__(self) -> str:
        return (
            f'name: {self.__name} | '
            f'price: {self.__price} | '
            f'rating: {self.__rating}'
        )


class Category:
    def __init__(self,
                 name: str,
                 products: list[Product]) -> None:
        self.__name: str = name
        self.__products: list[Product] = products

    def __str__(self) -> str:
        result = ''
        for product in self.__products:
            result += str(product) + '\n'

        return result


class Busket:
    def __init__(self,
                 products: list[Product]) -> None:
        self.__products: list[Product] = products

    def __str__(self) -> str:
        result = ''
        for product in self.__products:
            result += str(product) + '\n'

        return result


class User:
    def __init__(self,
                 login: str,
                 password: str,
                 busket: Busket) -> None:
        self.__login: str = login
        self.__password: str = password
        self.__busket: Busket = busket

    def __str__(self) -> str:
        return (
            f'{self.__login} busket:\n'
            f'{self.__busket}'
        )


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
    print(category)

print('-----------------------------------------')

print('User buskets:', end='\n\n')
for user in (andrey, vasya):
    print(user)
