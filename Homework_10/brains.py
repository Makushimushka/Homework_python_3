

import random


def bot_brain(n, m):
    """K - всего конфет
    m - максимальное количество штук за один раз"""
    if n % (m + 1) != 0:
        return n % (m + 1)
    elif m > n:
        return n
    else:
        return random.randint(1, m)


def move_draw_b():
    return random.randint(0, 1)

def draw():
    user_input = int(input(f"Ход игрока {players[player]} :"))
    if user_input <= m:
        n = n - user_input
        print(f"Остаток: {n}")
        if n == 0:
            print(f"Победа игрока {players[player]}")



def candies_game(players=['Уася', 'Семён']):
    n = 2021
    m = 28
    player = random.randint(0, 1)

    while n > 0:
        try:
            if "bot" in players[player]:
                user_input = players_brain(n, m)
                # print(f"Ход бота {user_input} :")
                print('{color}Ход {} {} : {endcolor}'.format(players[player], user_input, color='\x1b[1;32m',
                                                             endcolor='\x1b[0m'))
            else:
                user_input = int(input(f"Ход игрока {players[player]} :"))

            if user_input <= m:
                n = n - user_input
                print(f"Остаток: {n}")
                if n == 0:
                    print(f"Победа игрока {players[player]}")
                player = (lambda x: 1 if x == 0 else 0)(player)

            else:
                print('{color}Введите число меньше {}! {endcolor}'.format(m, color='\x1b[1;31m', endcolor='\x1b[0m'))

        except:
            print('{color}Введите число меньше {}! {endcolor}'.format(m, color='\x1b[1;31m', endcolor='\x1b[0m'))