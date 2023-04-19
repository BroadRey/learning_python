monday = input("Введите расходы за понедельник: ")
tuesday = input("Введите расходы за вторник: ")
wednesday = input("Введите расходы за среду: ")
thursday = input("Введите расходы за четверг: ")
friday = input("Введите расходы за пятницу: ")
saturday = input("Введите расходы за субботу: ")
sunday = input("Введите расходы за воскресенье: ")

sum_of_expenses = int(monday) + int(tuesday) + int(wednesday) + \
    int(thursday) + int(friday) + int(saturday) + int(sunday)

print(f"\nОбщая сумма расходов за неделю: {sum_of_expenses}")
print(f"\nСредний расход в день: {round(sum_of_expenses / 7, 1)}")
