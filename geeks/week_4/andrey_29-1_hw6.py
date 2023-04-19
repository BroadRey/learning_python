def multiply(*numbers):
    if len(numbers) == 0:
        return 0

    result = 1
    for num in numbers:
        result *= num

    return result


def reverse_string(string='hello'):
    result = string[::-1]

    if result == string:
        return True

    return False


def calculator(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    elif operator == '%':
        return num1 % num2
    elif operator == '**':
        return num1 ** num2
    elif operator == '//':
        return num1 // num2
    else:
        print("Вы ввели недопустимый оператор!")