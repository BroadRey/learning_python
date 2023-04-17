# Task 1
while True:
    product_to_price = dict()
    product = str()
    price = -1

    print('Now we are going to fill in the list of products\n'
          'You must to enter the name of products and their prices one by one\n'
          'If you want to stop, enter the word "stop"', end='\n\n')

    continue_question = input(
        'Do you want to continue? (press "y" or "n" button): ').lower()

    if continue_question == 'y':
        pass
    elif continue_question == 'n':
        break
    else:
        print('You entered the wrong answer to the question. Let`s try again!', end='\n\n')
        continue

    while True:
        product = input('Enter the name of product: ')

        if product == 'stop':
            print('\nYou finished to fill in the list of products')
            break

        price = int(input('Enter the price of the product: '))

        if price == 'stop':
            print('\nYou finished to fill in the list of products')
            break

        product_to_price[product] = price

    print('Now we will try to find the product we are looking for', end='\n\n')
    desired_product = input(
        'Enter the name of the product you are looking for: ')

    if desired_product not in product_to_price:
        print(
            'The product you are looking for is not on the product list. Let`s try again!', end='\n\n')
        continue

    print(
        f'The price of {product} is {product_to_price[desired_product]}', end='\n\n')


# Task 2
while True:
    product_to_price = {'potato': 15,
                        'carrot': 45,
                        'watermelon': 100
                        }

    print('Let`s try to find products that cost less than the desired price \n')
    product_cost = int(input(
        'Enter the maximum price of the products you are looking for: '))

    required_products = [product for product,
                         price in product_to_price.items() if price <= product_cost]

    print('Suitable products on request:',
          f'\t{", ".join(required_products)}', sep='\n', end='\n\n')

    continue_question = input(
        'Do you want to continue? (press "y" to continue or something else to finish): ').lower()

    if continue_question == 'y':
        continue

    break


# Task 3
months_to_days = {'january': 31,
                  'february': 28,
                  'march': 31,
                  'april': 30,
                  'may': 31,
                  'june': 30,
                  'july': 31,
                  'august': 31,
                  'september': 30,
                  'october': 31,
                  'november': 30,
                  'december': 31
                  }

month_input = input('Please, enter the name of any month: ').lower()

if month_input not in months_to_days:
    print('You entered the month that doesn`t exist!')
else:
    print(f'In a given month has {months_to_days[month_input]} days')
    print('Name of months in sorted order:', ', '.join(
        sorted(months_to_days)), sep='\n\t')
    print('Months with 31 days:',
          ','.join([month for month, day
                    in months_to_days.items()
                    if day == 31]),
          sep='\n\t')

    sorted_months_by_days = sorted(
        months_to_days.items(), key=lambda item: item[1])
    print('Months in sorted order by number of days:',
          '\n\t'.join([f'{month}: {day}' for month,
                      day in sorted_months_by_days]),
          sep='\n\t')


# Task 4
logins_to_passwords = {'vaskya': 'baer$2',
                       'test': 'test',
                       'burka': 'af@!arKKASF',
                       'kolyan': '1233123fsdf',
                       'igor': 'igor12380',
                       'elephant': 'big_SL0NE_boss',
                       'google_master': "boss_of@G@@Gle24",
                       'gorniiy': 'gor@tebeNetov@rish123',
                       'oktyabrkii': 'v2mK@Kmne777',
                       'zelenka': '300huncnid$@$'
                       }


user_login = input('Enter you login: ').lower()
user_password = input('Enter you password: ')

if user_login not in logins_to_passwords:
    print('The entered login does not exist!')
elif user_password != logins_to_passwords[user_login]:
    print('Incorrect password')
else:
    print('Logged in successfully')
