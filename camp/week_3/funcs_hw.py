# task_1 (a)
def add_excitement(strings: list) -> None:
    for ix in range(len(strings)):
        strings[ix] += '!'


# task_1 (b)
def add_excitement(strings: list) -> list:
    result = [elem+'!' for elem in strings]
    return result


# task_2
def match(str_1: str, str_2: str) -> int:
    if not str_1 or not str_2:
        return 0

    match_counter = 0

    for ix, char in enumerate(str_1):
        if char == str_2[ix]:
            match_counter += 1

    return match_counter


# task_3
def findall(str_: str, letter: str) -> list:
    if len(letter) > 1:
        return list()

    all_occurrences = [ix for ix, char in enumerate(str_) if char == letter]
    return all_occurrences