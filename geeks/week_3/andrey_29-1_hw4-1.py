def is_valid_mentor_name(name):
    if not name.isalpha():
        print("Имя ментора должно состоять только из букв. Попробуйте еще раз!\n")
        return False

    if len(name) > 15:
        print("Имя ментора не может содержать более 15 букв. Попробуйте еще раз!\n")
        return False

    return True


def is_valid_index(index, lenght_of_array):
    if index >= lenght_of_array:
        print(
            "Вы ввели число, превышающее индекс последнего ментора в списке. Попробуйте еще раз!\n")
        return False

    if index < -lenght_of_array:
        print(
            "Отрицательный индекс превышает длину строки. Попробуйте еще раз!\n")
        return False

    return True


def is_str_contains_negative_number(string):
    if len(string) == 0:
        return False

    if string[0] == "-":
        return string[1:].isnumeric()

    return False


mentors = ["Аблай", "Вова", "Марлен",  "Асылбек"]

while True:
    print('Команды для взаимодействия с программой:')
    print('\t1. "Добавление" - позволяет добавить ментора в список')
    print('\t2. "Изменение" - позволяет изменить имя существующего ментора на новое')
    print('\t3. "Удаление" - позволяет удалить ментора из списка по имени или индексу')
    print('\t4. "Выход" - завершение исполнения программы\n')
    print("На данный момент список выглядит так: ")
    print(f"\t{mentors}\n")

    command = input("Введите название команды: ")

    if command.lower() == "добавление":
        if len(mentors) >= 5:
            print("В списке не может быть больше 5 менторов. Попробуйте удалить или изменить ментора! Перезапуск программы...\n")
            continue

        old_name = input("Введите имя добавляемого ментора: ").capitalize()

        if not is_valid_mentor_name(old_name):
            continue

        if old_name in mentors:
            print("Введенное имя присутствует в списке. Попробуйте ввести другое имя!\n")
            continue

        mentors.append(old_name)
        print("Ментор добавлен! Перезапуск программы...\n")
    elif command.lower() == "изменение":
        if len(mentors) == 0:
            print(
                "Список пуст, поэтому изменять нечего! Попробуйте ввести другую команду!\n")
            continue

        old_name = input("Введите имя изменяемого ментора: ").capitalize()

        if not is_valid_mentor_name(old_name):
            continue

        if old_name not in mentors:
            print("Введенное имени нет в списке. Попробуйте еще раз!\n")
            continue

        new_name = input("Введите новое имя ментора: ").capitalize()

        if not is_valid_mentor_name(new_name):
            continue

        if new_name in mentors:
            print("Введенное имя присутствует в списке. Попробуйте ввести другое имя!\n")
            continue

        mentors[mentors.index(old_name)] = new_name
        print("Ментор изменен! Перезапуск программы...\n")
    elif command.lower() == "удаление":
        if len(mentors) == 0:
            print(
                "Список пуст, поэтому удалять нечего! Попробуйте ввести другую команду!\n")
            continue

        remover = input(
            "Введите имя или индекс строки с именем ментора: ")

        if len(remover) == 0:
            print("Вы ввели пустую строку. Попробуйте еще раз!")

        if remover.isalpha():
            name = remover.capitalize()

            if name not in mentors:
                print("Введенное имени нет в списке. Попробуйте еще раз!\n")
                continue

            mentors.remove(name)
            print("Ментор удален! Перезапуск программы...\n")
            continue

        if remover.isnumeric() or is_str_contains_negative_number(remover):
            index = int(remover)

            if not is_valid_index(index, len(mentors)):
                continue

            mentors.pop(index)
            print("Ментор удален! Перезапуск программы...\n")
    elif command.lower() == "выход":
        print("\nИтоговый кортеж:", f"{tuple(mentors)}\n")
        break
    else:
        print("Вы ввели несуществующую команду. Попробуйте еще раз!\n")
