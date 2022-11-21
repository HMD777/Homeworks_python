from random import randint


def rand_players():
    player = randint(1, 2)
    if player == 1:
        return 1
    else:
        return 2


def next_player(current_player):
    if current_player == 1:
        return 2
    else:
        return 1
