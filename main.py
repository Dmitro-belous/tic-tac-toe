def greets():
    print('-----------------')
    print('Приветствуем вас ')
    print('     в игре      ')
    print('"Крестики-нолики"')
    print('-----------------')
    print('Формат ввода: x y')
    print('x - номер строки')
    print('y - номер столбца')


def show(fn):
    print()
    print("  | 0 | 1 | 2 |")
    print("---------------")
    for i, row in enumerate(fn):
        row_str = f"{str(i)} | {' | '.join(row)} |"
        print(row_str)
        print("---------------")


def ask():
    while True:
        cord = input("Ваш ход: ").split()
        if len(cord) != 2:
            print("Введите 2 координаты!")
            continue
        x, y = cord
        if not(x.isdigit()) or not(y.isdigit()):
            print("Введите числа!")
            continue
        x, y = int(x), int(y)
        if 0 > x or x > 2 or 0 > y or y > 2:
            print("Координаты вне диапазона!")
            continue
        if field[x][y] != " ":
            print("Клетка уже занята!")
            continue
        return x, y


def check_win(f):
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)),
                ((0, 0), (1, 1), (2, 2)), ((0, 2), (1, 1), (2, 0)))
    for cord in win_cord:
        symbols = []
        for el in cord:
            symbols.append(f[el[0]][el[1]])
        if symbols == ["X", "X", "X"]:
            print("Крестики выиграли!")
            return True

        if symbols == ["0", "0", "0"]:
            print("Нолики выиграли!")
            return True
    return False


greets()
field = [[" " for _ in range(3)] for i in range(3)]
num = 0
while True:
    num += 1
    show(field)
    if num % 2 == 1:
        print("Ходит крестик")
    else:
        print("Ходит нолик")
    x, y = ask()
    if num % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"
    if check_win(field):
        break
    if num == 9:
        print("Ничья")
        break
