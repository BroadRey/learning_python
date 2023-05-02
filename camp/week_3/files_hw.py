# task_1
file_name = input('Enter the file name: ')
file_content = input('Enter the file content: ')

with open(f'{file_name}.txt', 'w') as file:
    file.write(file_content)


# task_2
file_name = input('Enter the file name: ')
with open(f'{file_name}.txt', 'r') as file:
    print(len(file.read().split()))


# task_3
file_name = input('Enter the file name: ')
with open(f'{file_name}.txt', 'r') as file:
    file_strings = file.read().split()
    file_strings = file_strings[::-1]
    [print(str_) for str_ in file_strings]


# task_4
file_name = input('Enter the file name: ')
with (open(f'{file_name}.txt', 'r') as file,
      open(f'copy_{file_name}.txt', 'w') as copy_file):
    copy_file.write(file.read())