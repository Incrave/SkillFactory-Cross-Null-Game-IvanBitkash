# Создаем пустое поле 3x3
board = [[' ' for _ in range(3)] for _ in range(3)]

# Функция для вывода игрового поля
def print_board():
    for row in board:
        print('|'.join(row))
        print('-' * 5)

# Функция для проверки, есть ли выигрышная комбинация
def check_win(player):
    # Проверка строк
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Проверка столбцов
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Проверка диагоналей
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

# Функция для осуществления хода
def make_move(row, col, player):
    if row < 1 or row > 3 or col < 1 or col > 3:
        print("Некорректные координаты!")
        return False

    if board[row-1][col-1] != ' ':
        print("Эта ячейка уже занята!")
        return False

    board[row-1][col-1] = player
    return True

# Основной игровой цикл
current_player = 'X'

while True:
    print_board()

    # Запрос ввода координат от игрока
    row = int(input("Введите номер строки (1-3): "))
    col = int(input("Введите номер столбца (1-3): "))

    # Ход игрока
    if make_move(row, col, current_player):
        # Проверка на победу
        if check_win(current_player):
            print_board()
            print(f"Игрок {current_player} победил!")
            break

        # Проверка на ничью
        if all(cell != ' ' for row in board for cell in row):
            print_board()
            print("Ничья!")
            break

        # Смена текущего игрока
        current_player = 'O' if current_player == 'X' else 'X'
