from random import randint


def bot(current_value, max_move=28):
    bot_move = current_value % (max_move+1)
    if bot_move < 1 or bot_move > 28:
        bot_move = randint(1, 28)
    return bot_move
