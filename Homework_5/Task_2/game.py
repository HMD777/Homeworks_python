from random import randint as rand
from players import next_player


def game_start(start_player=1):
    total_move = 2021
    player = start_player
    count = 1
    while total_move > 0:
        player_move = int(
            input(f'{count}. Ваш ход Игрок №{player}! Введите число от 1 до 28 :'))
        while player_move < 1 or player_move > 28 or total_move < player_move:
            player_move = int(
                input(f'{count}. Ошибка! Игрок №{player} введите число от 1 до 28 :'))
        player = next_player(player)
        total_move -= player_move
        count += 1
        print(f'Остаток: {total_move}')
    return print(f'Игрок №{player} wins this game!')
