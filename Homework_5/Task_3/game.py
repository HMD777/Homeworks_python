from player import rand_players
from player import next_player
from view import view_tic_tac
from view import tic_tac_rule
from view import tic_tac_view_2


def tic_tac_check(tic_tac_list):
    if tic_tac_list[0] == tic_tac_list[1] and tic_tac_list[1] == tic_tac_list[2] and (tic_tac_list[0] == ' X ' or tic_tac_list[0] == ' O '):
        return True
    elif tic_tac_list[3] == tic_tac_list[4] and tic_tac_list[4] == tic_tac_list[5] and (tic_tac_list[3] == ' X ' or tic_tac_list[3] == ' O '):
        return True
    elif tic_tac_list[6] == tic_tac_list[7] and tic_tac_list[7] == tic_tac_list[8] and (tic_tac_list[6] == ' X ' or tic_tac_list[6] == ' O '):
        return True
    elif tic_tac_list[0] == tic_tac_list[3] and tic_tac_list[3] == tic_tac_list[6] and (tic_tac_list[0] == ' X ' or tic_tac_list[0] == ' O '):
        return True
    elif tic_tac_list[1] == tic_tac_list[4] and tic_tac_list[4] == tic_tac_list[7] and (tic_tac_list[1] == ' X ' or tic_tac_list[1] == ' O '):
        return True
    elif tic_tac_list[2] == tic_tac_list[5] and tic_tac_list[5] == tic_tac_list[8] and (tic_tac_list[2] == ' X ' or tic_tac_list[2] == ' O '):
        return True
    elif tic_tac_list[0] == tic_tac_list[4] and tic_tac_list[4] == tic_tac_list[8] and (tic_tac_list[0] == ' X ' or tic_tac_list[0] == ' O '):
        return True
    elif tic_tac_list[2] == tic_tac_list[4] and tic_tac_list[4] == tic_tac_list[6] and (tic_tac_list[2] == ' X ' or tic_tac_list[2] == ' O '):
        return True
    else:
        return False


def next_tic_tac(tic_tac):
    if tic_tac == " X ":
        return " O "
    else:
        return " X "


def tic_tac_start():
    tic_tac_list = ['   ']*9
    tmp_list = []
    count = 9
    player = rand_players()
    tic_tac = ' X '
    tic_tac_rule()
    print(
        f'Игру начинает Игрок №{player}!\nЗа Вами закреплено "{tic_tac}"!\nЗа Игроком №{next_player(player)} закреплен "{next_tic_tac(tic_tac)}"')
    while count > 0:
        player_move = int(
            input(f'Игрок №{player} введите номер ячейки, в которую вы хотите ввести "{tic_tac}!: "'))
        if player_move >= 1 and player_move <= 9 and (player_move not in tmp_list):
            tic_tac_list[player_move-1] = tic_tac
            tmp_list.append(player_move)
            tic_tac_view_2()
            view_tic_tac(tic_tac_list)
            if tic_tac_check(tic_tac_list) == True:
                print(f'Игрок №{player} побеждает в этом раунде!')
                break
            player = next_player(player)
            tic_tac = next_tic_tac(tic_tac)
            count -= 1
        else:
            print('Ошибка! Введите корректные данные!')
