board = [[' ' for x in range(3)] for y in range(3)]


def print_board():
    row1 = "1 | {} | {} | {} |".format(board[0][0], board[0][1], board[0][2])
    row2 = "2 | {} | {} | {} |".format(board[1][0], board[1][1], board[1][2])
    row3 = "3 | {} | {} | {} |".format(board[2][0], board[2][1], board[2][2])
    row4 = "  _______________"
    row5 = "    1   2   3"
    print()
    print(row1)
    print(row2)
    print(row3)
    # print(row4)
    print(row5)
    print()


def player_move(icon):
    print("Ваш ход, Player {}".format(icon))
    while True:
        choice = input("Введите координаты хода: ").split()
        if len(choice) != 2:
            print('Введите две координаты')
            continue
        if not (choice[0].isdigit() and choice[1].isdigit()):
            print('Введите числа')
            continue
        row, col = map(int, choice)
        if not (row >= 1 and row < 4 and col >= 1 and col < 4):
            print('Вышли из диапазона')
            continue
        if board[row-1][col-1] == ' ':
            board[row-1][col-1] = icon
        else:
            print()
            print("Это место уже занято!")
            continue
        break


def is_victory(icon):
    if (board[0][0] == icon and board[0][1] == icon and board[0][2] == icon) or \
       (board[1][0] == icon and board[1][1] == icon and board[1][2] == icon) or \
       (board[2][0] == icon and board[2][1] == icon and board[2][2] == icon) or \
       (board[0][0] == icon and board[1][0] == icon and board[2][0] == icon) or \
       (board[0][1] == icon and board[1][1] == icon and board[2][1] == icon) or \
       (board[0][2] == icon and board[1][2] == icon and board[2][2] == icon) or \
       (board[0][0] == icon and board[1][1] == icon and board[2][2] == icon) or \
       (board[2][0] == icon and board[1][1] == icon and board[0][2] == icon):
        return True
    else:
        return False


def is_draw():
    for row in board:
        if ' ' in row:
            return False
    return True


def main():
    while True:
        print_board()
        player_move('X')
        if is_victory('X'):
            print_board()
            print("X победил! Поздравляем!")
            break
        elif is_draw():
            print_board()
            print("Это ничья!")
            break
        print_board()
        player_move('O')
        if is_victory('O'):
            print_board()
            print("O победил! Поздравляем!")
            break
        elif is_draw():
            print_board()
            print("Это ничья!")
            break


if __name__ == "__main__":
    main()
