def calculate_winnings(roulette_result, player_choice, balance, bet_count):
    if roulette_result == player_choice:
        return balance + bet_count*2

    return balance - bet_count
