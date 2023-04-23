# task_1
def bubble_sort(list_):
    list_len = len(list_)

    if not list_len or list_len == 1:
        return list_

    is_sorted = True

    for outher in range(list_len - 1):
        for inner in range(list_len - outher - 1):
            if list_[inner] > list_[inner + 1]:
                is_sorted = False
                list_[inner], list_[inner + 1] = list_[inner + 1], list_[inner]

        if is_sorted:
            return list_

    return list_


print(bubble_sort([12, 2, 30, -1000, 0]))

# task_2
def binary_search(val, list_):
    is_result_ok = False
    first = 0
    last = len(list_) - 1
    middle = None
    pos = None

    while first < last:
        middle = (first + last) // 2

        if val == list_[middle]:
            last = first = middle
            is_result_ok = True
            pos = middle
            continue

        if val > list_[middle]:
            first = middle + 1
        else:
            last = middle - 1

    if is_result_ok:
        print(f'Элемент найден под индексом: {pos}')
        return

    print('Элемент не найден')


binary_search(3, [-100, 1, 2, 3, 4])