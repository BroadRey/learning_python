while True:
    try:
        # Не совсем понятно формулировка заказчика 'Пользователь загадывает число до 100'. Решил, что ввиду имелся диапазон [0, 100)
        num = input('Введите целое число от 0 до 100 или "q" для выхода: ')

        if num == 'q':
            break

        num = int(num)
    except ValueError:
        print('\nВы ввели недопустимый набор символов. Попробуйте еще раз!\n')
        continue

    if num < 0 or num >= 100:
        print('''
Введенное вами число выходит за диапазон разрешенных значений.
Следуйте предложенной инструкции!
''')
        continue

    array = list(range(100))
    min_index = 0
    max_index = len(array)
    mid_elem_index = (min_index + max_index) // 2
    attempts_counter = 0
    attempts_log = []

    while array[mid_elem_index] != num and min_index <= max_index:
        print(f'''
Загаданное вами число больше числа {array[mid_elem_index]}?

Варианты ответов:
    1) да, больше
    2) меньше
''')
        answer = input("Введите ваш ответ: ")

        if answer == 'да, больше':
            min_index = mid_elem_index + 1
            attempts_counter += 1
            # Под списком попыток в ТЗ подразумевается список уточняющих вопросов пользователю. ТЗ составлено некорректно (двусмысленно). Требуется уточнение от заказчика
            attempts_log.append(answer)
        elif answer == 'меньше':
            max_index = mid_elem_index - 1
            attempts_counter += 1
            attempts_log.append(answer)
        else:
            print('''Вы ввели некорректный ответ на вопрос.
Попробуйте еще раз!''')
            # Неверные ответы пользователя также логируются
            attempts_log.append(answer)
            continue

        mid_elem_index = (min_index + max_index) // 2

    if num == array[mid_elem_index]:
        print(f'Вы загадали число {array[mid_elem_index]}')

        if attempts_counter == 0:
            attempts_counter += 1
            attempts_log.append("Банарный поиск сразу нашел число")

        with open('results.txt', 'w') as file:
            result = f'''Количество попыток: {attempts_counter}
Список попыток: {str(attempts_log)}
Загаданное число: {array[mid_elem_index]}'''
            file.write(result)
    else:
        # В данном случае не логируем, ибо флоу с ложью со стороны пользователя надо обговорить с заказчиком
        print('Вы где-то соврали при ответе на вопросы. Загадывайте число по-новой!')
        continue