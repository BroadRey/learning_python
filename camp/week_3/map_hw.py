def multiply_even_nums(nums: list) -> list:
    even_nums = filter(lambda x: x % 2, nums)
    result = list(map(lambda x: x*2, even_nums))
    return result


def find_upper_strings(strings: list) -> list:
    def find_capital_letters(string):
        result = ''
        for char in string:
            if char.isupper():
                result += char

        return result

    result = [str_ for str_ in map(find_capital_letters, strings) if str_]
    return result


def calc_square_even_nums(strings: list) -> list:
    def find_even_nums(str_):
        num = int(str_)

        if num % 2 == 0:
            num **= 2
            return num

        return None

    result = [num for num in map(lambda x: find_even_nums(x), strings)
              if num != None]
    return result


def calculate_len_square(strings: list) -> list:
    result = list(map(lambda x: len(x)**2, strings))
    return result