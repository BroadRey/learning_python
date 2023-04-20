from random import choice
from decouple import config
from winner import calculate_winnings


class Game:
    def __init__(self):
        self.__balance = int(config('MY_MONEY'))

    def play_roulette(self):
        old_balance = self.__balance

        if old_balance == None:
            raise ValueError('Starting balance didn\'t set')

        roulette_range = range(1, 31)

        while True:
            print(f'Your balance is {self.__balance}$')

            player_choice = int(
                input('Select the number from 1 to 30 that you want to bet on: '))

            if not self.__is_valid_player_choice(player_choice, roulette_range):
                print(
                    'Your choise is out of the range of numbers on which you can bet! Let\'s try again!\n')
                continue

            bet_count = int(input('Enter the bet amount: '))

            if not self.__is_valid_bet(bet_count, self.__balance):
                print('The bet size is incorrect! Let\'s try again!\n')
                continue

            roulette_result = choice(roulette_range)
            print(f'The number {roulette_result} came out on the roulette wheel!\n')

            self.__balance = calculate_winnings(
                roulette_result, player_choice, self.__balance, bet_count)

            if old_balance < self.__balance:
                print('Congratulations! You won!')
            else:
                print('Oh, I\'m so sorry... You lose...')

            old_balance = self.__balance

            print(f'Your balance is {self.__balance}$\n')

            if self.__balance == 0:
                print('You are bankrupt! Sorry...')
                break

            playing_again = input('Do you want to play again(yes/no)?\n'
                                  'Answer: ')

            if playing_again.lower() == 'no':
                print(f'Great! You winnings are {self.__balance}')
                break

    def __is_valid_bet(self, bet, balance):
        return True if 0 < bet <= balance else False

    def __is_valid_player_choice(self, player_choice, roulette_range):
        return True if 0 < player_choice <= roulette_range[-1] else False