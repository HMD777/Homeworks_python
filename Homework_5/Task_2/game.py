from random import randint as rand
from players import next_player
from bot import bot


def game_start(start_player):
    total_move = 2021
    player = start_player
    count = 1
    game_var = int(input(
        'Пожалуйста, выберите вариант игры:\n Введите 1 - если хоите сыграть с реальным человеком. \n Введите 2 - если хоите сыграть с ботом.\n'))
    while game_var < 1 or game_var > 2:
        game_var = int(input(
            'Ошибка! Пожалуйста, выберите вариант игры:\n Введите 1 - если хоите сыграть с реальным человеком. \n Введите 2 - если хоите сыграть с ботом.\n'))

    if game_var == 1:
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

    if game_var == 2:
        if player == 1:
            game_player = 'Бот'
        else:
            game_player = 'Игрок'
        while total_move > 0:
            if player == 1:
                player_move = bot(total_move, 28)
                print(f'{count}. Бот ввел число: {player_move}.')
            else:
                player_move = int(
                    input(f'{count}. Ваш ход Игрок! Введите число от 1 до 28 :'))
                while player_move < 1 or player_move > 28 or total_move < player_move:
                    player_move = int(
                        input(f'{count}. Ошибка! {player} введите число от 1 до 28 :'))
            player = next_player(player)
            total_move -= player_move
            count += 1
            print(f'Остаток: {total_move}')
        return print(f'{game_player} wins this game!')
