from os import name, system
from random import choice
from time import sleep


class MemoryGame:
    def __init__(self, row_length: int, column_lenght: int, attempts) -> None:
        if row_length <= 0 or column_lenght <= 0:
            raise ValueError('Ошибка в установке размера поля')

        self.__row_lenght = row_length
        self.__column_lenght = column_lenght
        self.__game_field = self.__generate_game_field(
            row_length, column_lenght)
        self.__is_game_finished = False
        self.__config_attempts = attempts
        self.__user_attempts = 0
        self.__guessed_coordinates = list()
        self.__game_greeting()

    def __game_greeting(self):
        print('Игра начинается!',
              f'Количество возможных ошибок при отгадывании: {self.__config_attempts}',
              'Начальное поле выглядит следующим образом:', sep='\n')

        print(self)

    def __generate_game_field(self, row_lenght: int, column_length: int) -> list:
        if row_lenght * column_length % 2:
            raise ValueError('Недопустимая размерность поля')

        game_field = [[None for _ in range(column_length)]
                      for _ in range(row_lenght)]

        puzzled_numbers = list(range((column_length * row_lenght) // 2)) * 2
        exist_coordinates = list()

        for row in range(row_lenght):
            for column in range(column_length):
                exist_coordinates.append((row, column))

        while len(exist_coordinates) > 0:
            try:
                random_row_coord, random_column_coord = choice(
                    exist_coordinates)
                random_pazzled_number = choice(puzzled_numbers)
            except IndexError:
                break

            exist_coordinates.remove((random_row_coord, random_column_coord))
            puzzled_numbers.remove(random_pazzled_number)

            game_field[random_row_coord][random_column_coord] = random_pazzled_number

        return game_field

    def restart_game(self):
        self.__is_game_finished = False
        self.__guessed_coordinates = list()
        self.__user_attempts = 0
        self.__game_field = self.__generate_game_field(
            self.__row_lenght, self.__column_lenght)

        self.__game_greeting()

    def __str__(self) -> str:
        result = ''

        for column in range(self.__column_lenght):
            for row in range(self.__row_lenght):
                if (row, column) not in self.__guessed_coordinates:
                    result += '*'
                    continue
                result += str(self.__game_field[row][column])
            result += '\n'

        return result

    def __request_coordinates(self, text_for_user):
        coordinates = input(text_for_user).split()

        if len(coordinates) != 2:
            raise ValueError('Формат ввода был нарушен!')

        row_coord, column_coord = [int(i) - 1 for i in coordinates]

        if (row_coord, column_coord) in self.__guessed_coordinates:
            raise ValueError(
                'Вы ввели координату, которую уже вводили! Попробуйте еще раз!')

        if (row_coord >= self.__row_lenght
                or row_coord < 0
                or column_coord >= self.__column_lenght
                or column_coord < 0):
            raise ValueError('Координата ячейки превышает размер поля!')
        return (row_coord, column_coord)

    def __clear_console(self, timeout=0):
        sleep(timeout)
        return system('cls' if name == 'nt' else 'clear')

    def choose_cards(self) -> bool:
        if self.__is_game_finished:
            print('Игра завершена! Начните игру заново!')
            return True

        first_coordonates = tuple()

        while True:
            try:
                first_coordonates = self.__request_coordinates(
                    'Введите две координаты первой ячейки через пробел, начиная с 1: ')
                break
            except ValueError as e:
                print(e)
                continue

        row_coord_1, column_coord_1 = first_coordonates
        self.__guessed_coordinates.append((row_coord_1, column_coord_1))

        print(self)

        second_coordinates = tuple()

        while True:
            try:
                second_coordinates = self.__request_coordinates(
                    'Введите две координаты второй ячейки через пробел, начиная с 1: ')
                break
            except ValueError as e:
                print(e)
                continue

        row_coord_2, column_coord_2 = second_coordinates
        self.__user_attempts += 1
        self.__guessed_coordinates.append((row_coord_2, column_coord_2))

        print(self)

        if (self.__game_field[row_coord_1][column_coord_1]
                != self.__game_field[row_coord_2][column_coord_2]):
            if self.__user_attempts == self.__config_attempts:
                self.__is_game_finished = True
                print('У вас закончились попытки')
                return True

            self.__guessed_coordinates.remove(
                (row_coord_1, column_coord_1))
            self.__guessed_coordinates.remove(
                (row_coord_2, column_coord_2))

        game_field_lenght = self.__row_lenght * self.__column_lenght
        if len(self.__guessed_coordinates) == game_field_lenght:
            print('Вы выиграли!')
            self.__is_game_finished = True
            return True

        self.__clear_console(2)

        print('На данный момент поле выглядит следующим образом:\n', self, sep='')
        return False


game = MemoryGame(row_length=1, column_lenght=4, attempts=2)

is_game_finished = game.choose_cards()
while not is_game_finished:
    is_game_finished = game.choose_cards()
