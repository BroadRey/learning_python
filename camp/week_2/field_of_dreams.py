str_ = input('Введите слово: ')
mask = ['_'] * len(str_)

while True:
    letter = input('Введите букву: ').lower()
    pre_presult = ''.join(mask)

    if letter in mask:
        print('\nВы уже отгадали эту букву! Попробуйте снова!')
        print('Сейчас слово выглядит так:', pre_presult, end='\n\n')
        continue

    if str_.count(letter) <= 0:
        print('\nВведенной буквы нет в загаданном слове!')
        print('Сейчас слово выглядит так:', pre_presult, end='\n\n')
        continue

    for i, elem in enumerate(str_):
        if elem == letter:
            mask[i] = letter
            pre_presult = ''.join(mask)

    if str_ == pre_presult:
        print(
            f'Ура! Вы отгадали! Загаданное слово: "{pre_presult.capitalize()}"')
        break

    print('\nСейчас слово выглядит так:', pre_presult, end='\n\n')