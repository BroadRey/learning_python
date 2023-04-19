data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')

letters = []
numbers = []

for elem in data_tuple:
    if type(elem) == str:
        letters.append(elem)
    else:
        numbers.append(elem)

numbers.remove(6.13)
letters.append(True)
numbers.remove(True)
numbers.insert(numbers.index(1), 2)

numbers.sort()
letters.reverse()
letters[1] = 'G'
letters[7] = 'c'

for i in range(len(numbers)):
    if type(numbers[i]) == int or type(numbers[i]) == float:
        numbers[i] = numbers[i] ** 2

letters = tuple(letters)
numbers = tuple(numbers)

print(letters, numbers)