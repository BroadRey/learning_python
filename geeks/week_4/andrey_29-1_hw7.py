# Сгенерировал список с элементами в диапазоне [1, 10), ибо в ТЗ двусмысленная формулировка
ten = list(range(1, 10))
evens = list(filter(lambda x: x % 2 == 0, ten))
print(list(map(lambda x: x ** 2, evens)))


def find_elem_by_index(index, ten=[1, 2, 3, 4, 5]):
    try:
        return ten[index]
    except IndexError:
        print(
            f"\nВы вышли за диапазон допустимых индексов элементов списка.\nМаксимальный индекс: {len(ten) - 1}. Минимальный индекс: {-len(ten)}\n")
        raise
    except TypeError:
        print("\nВы передали в функцию что-то отличное от списка.")
        raise


while True:
    try:
        index = input(
            "Введите индекс элемента в списке или символ 'q' для выхода: ")

        if index == 'q':
            print("\nДо свидания!\n")
            break

        index = int(index)
        # По ТЗ не требовалось передавать в функцию список, введенный пользователем, потому отталкиваюсь от default значения
        print(find_elem_by_index(index))
    except ValueError:
        print("\nИндекс должен быть целым числом.\nПопробуйте еще раз!\n")
    except IndexError:
        print("Попробуйте еще раз!\n")
    except TypeError:
        print("Данная бизнес-логика сюда не забросит, но вы все равно больше так не делайте!\n")
