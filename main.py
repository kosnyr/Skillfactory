from random import randint


def display_board(board):
    print(f'  0  1   2')
    for i in range(3):
        print(f'{i} {board[i][0]} | {board[i][1]} | {board[i][2]}')


def player_input():
    marker = ' '
    while marker != 'X' and marker != 'O':
        marker = input('Выберите, чем вы будете играть x или o?').upper()
    if marker == 'X':
        return ('X', 'O')  # (Игрок1, игрок2)
    else:
        return ('O', 'X')


def place_marker(board, marker, row, column):
    board[row][column] = marker


def win_check(board, mark):
    if (
            (board[0][0] == board[0][1] == board[0][2] == mark) or
            (board[1][0] == board[1][1] == board[1][2] == mark) or
            (board[2][0] == board[2][1] == board[2][2] == mark)
    ):
        return True
    elif (
            (board[0][0] == board[1][0] == board[2][0] == mark) or
            (board[0][1] == board[1][1] == board[2][1] == mark) or
            (board[0][2] == board[1][2] == board[2][2] == mark)
    ):
        return True
    elif (
            (board[2][0] == board[1][1] == board[0][2] == mark) or
            (board[0][0] == board[1][1] == board[2][2] == mark)
    ):
        return True
    else:
        return False


def choose_first():
    if randint(0, 100) > 50:
        return 'Игрок1'
    else:
        return 'Игрок2'


def space_check(board, row, column):
    return board[row][column] == ' '


def full_check(board):
    for i in range(3):
        for j in range(3):
            if space_check(board, i, j):
                return False
            else:
                return True


def player_choice(board):
    row = -1
    column = -1
    while (
             row not in [0, 1, 2] or
             column not in [0, 1, 2] or
            not space_check(board, row, column)
    ):
        row, column = int(input('Выбелите строку')), int(input('Выбелите столбец'))

    return row, column


def replay():
    choice = input('Хотите сыграть еще раз? Введите yes или no').lower()
    return choice == 'yes'


# Игра Крестики-Нолики

print('Добро пожаловать в игру Крестики-Нолики!')
while True:
    the_board = [[' '] * 3 for i in range(3)]
    player1_marker, player2_marker = player_input()
    first = choose_first()
    print(f'{first} ходит первым')
    game_on = True
    while game_on:
        if first == 'Игрок1':
            display_board(the_board)
            position_row, position_column = player_choice(the_board)
            place_marker(the_board, player1_marker, position_row, position_column)
            if win_check(the_board, player1_marker):
                print('Игрок1 выиграл!')
                game_on = False
            else:
                if full_check(the_board):
                    print('Ничья')
                    game_on = False
                else:
                    first = 'Игрок2'

        if first == 'Игрок2':
            display_board(the_board)
            position_row, position_column = player_choice(the_board)
            place_marker(the_board, player2_marker, position_row, position_column)
            if win_check(the_board, player2_marker):
                print('Игрок2 выиграл!')
                game_on = False
            else:
                if full_check(the_board):
                    print('Ничья')
                    game_on = False
                else:
                    first = 'Игрок1'

    if not replay():
        print('Всего доброго')
        break

