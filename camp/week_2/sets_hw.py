# task_1
first_str_list = input('Введите первый список чисел через запятую: ')
second_str_list = input('Введите второй список чисел через запятую: ')
first_int_list = [int(i) for i in first_str_list.split(',')]
second_int_list = [int(i) for i in second_str_list.split(',')]

result = set(first_int_list) & set(second_int_list)
print((f'Общие элементы: {result}')
      if len(result) > 0
      else 'Общие элементы отсутствуют')

# task_2
first_str_list = input('Введите первый список чисел через запятую: ')
second_str_list = input('Введите второй список чисел через запятую: ')
first_int_list = [int(i) for i in first_str_list.split(',')]
second_int_list = [int(i) for i in second_str_list.split(',')]

result = set(first_int_list) - set(second_int_list)
print((f'Результат: {result}')
      if len(result) > 0
      else 'Списки равны')

# task_3
first_str_list = input('Введите первый список чисел через запятую: ')
first_int_list = [int(i) for i in first_str_list.split(',')]
print(f'Результат: {set(first_int_list)}')

# task_4
first_str_list = input('Введите первый список чисел через запятую: ')
first_int_list = [int(i) for i in first_str_list.split(',')]
print(f'Результат: {len(set(first_int_list))}')
