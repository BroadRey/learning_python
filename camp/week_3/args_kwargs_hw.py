# task_1
def max_value(*nums) -> int:
    if not nums:
        return -1

    max_num = max(nums)
    return max_num


# task_2
def merge_lists(*lists) -> list:
    if not lists:
        return list()

    final_list = [elem for arr in lists for elem in arr]
    return final_list


# task_3
def print_user_data(**user_data):
    for key, value in user_data.items():
        print(f'{key.capitalize()}: {value}')