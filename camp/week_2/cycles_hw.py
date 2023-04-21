from random import choice

# task_1
user_input = input('Type something: ')
i = 0
while i < len(user_input):
    print(user_input[i])
    i += 1
    
# task_2
password = 'secret_password'
i = 0
while i < 5:
    user_password = input('Enter your secret password: ')
    
    if user_password == password:
        print('You are successfully logged in!')
        break
    
    i += 1
else:
    print('You are removed from the system!')

# task_3
countries = ['Mexico', 'USA', 'China']
random_country = choice(countries).lower()
mask = ['-'] * len(random_country)

print('Загадана страна! Попробуйте угадать ее название на английском!\n'
      'Если вы 5 раз попробуете отгадать несуществующую в слове букву,' 
      'то игра закончится')
attempts = 0
while attempts < 5:
    letter = input('Введите букву: ').lower()
    pre_presult = ''.join(mask)

    if letter in mask:
        print('\nВы уже отгадали эту букву! Попробуйте снова!')
        print('Сейчас слово выглядит так:', pre_presult, end='\n\n')
        continue

    if random_country.count(letter) <= 0:
        print('\nВведенной буквы нет в загаданном слове!')
        print('Сейчас слово выглядит так:', pre_presult, end='\n\n')
        attempts += 1
        continue

    for i, elem in enumerate(random_country):
        if elem == letter:
            mask[i] = letter
            pre_presult = ''.join(mask)

    if random_country == pre_presult:
        country_index = list(map(str.lower, countries)).index(pre_presult)
        print(
            f'Ура! Вы отгадали! Загаданная страна: "{countries[country_index]}"')
        break

    print('\nСейчас слово выглядит так:', pre_presult, end='\n\n')
else:
    print('Вы израсходовали все попытки отгадать букву! Игра проиграна!')

# task_4
food_price = int(input('Enter the price of the food: '))
tip_percentage = int(input('Enter the percentage of the tip: '))

total_tips_amount = food_price * tip_percentage / 100
total_bill = food_price + total_tips_amount

print(f'Total amount of tips: {total_tips_amount}$')
print(f'Total bill: {total_bill}$')


integers = [0, 0, 0, 1, 0, 0, 1]

for i, elem in enumerate(integers):
    if elem != 0:
        integers[i] = 1
        break
else:
    print('There are no non-zero entries in the list!')