#Крестики-Нолики
X = "X"
O = "O"
EMPTY = " " #Пустое поле
TIE = "Ничья"
NUM_SQUARES = 9 #Количество клеток на поле

#Функция (display_instruct) выводит правила игры
def display_instruct():
    """Выводит на экран инструкцию для игрока"""
    print(
        """Добро пожаловать,чтобы сделать ход введите число от 0 до 8
        Числа соответствуют клеткам поля ниже:
        
        0 | 1 | 2 
        ---------
        3 | 4 | 5 
        ---------
        6 | 7 | 8
        
        Поехали!!!\n"""
    )
display_instruct()

#Функция (ask_yes_no) задаёт вопрос,на который нужно ответить да или нет
def ask_yes_no(question):
    """Отвечать надо - да или нет"""
    response = None
    while response not in("y", "n"):
        response = input(question).lower()
    return response

#Фунция (ask_number) запрашивает число с диапазона
def ask_number(question,low,high):
    """Просит ввести число из диапазона"""
    response = None
    while response not in range(low,high):
        response = int(input(question))
    return response

#Функция (pieces) спрашивает чей ход первый
def pieces():
    """Определяет принадлежность первого хода"""
    go_first = ask_yes_no("Хочешь оставить за собой первый ход? :(y/n)")
    if go_first == "y":
        print("Человек ходит первым крестиками")
        human = X
        computer = O
    else:
        print("Компьютер ходит первым крестиками")
        computer = X
        human = O
    return computer, human

#Функция (new_board) создаёт новую игровую доску и возвращает её
def new_board():
    """Создаёт новую игровую доску"""
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

#Функция (display_board)выводит переданную ей доску
def display_board(board):
    """Отображает игровую доску на экране"""
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\t", board[6], "|", board[7], "|", board[8], "\n")

#Функция (legal_moves) принимает доску и возвращает список доступных ходов
def legal_moves(board):
    """Создаёт список доступных ходов"""
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves

#Функция определяет победителя
def winner(board):
    """Определяет победителя в игре"""
    WEYS_TO_WIN = ((1,2,3),(3,4,5),(6,7,8),
                   (0,3,6),(1,4,7),(2,5,8),
                   (0,4,8),(2,4,6))
    for row in WEYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] !=EMPTY:
            winner = board[row[0]]
            return winner
        if EMPTY not in board:
            return TIE
    return None

#функция принимает доску и тип фишек игрока-человека
def human_move(board,human):
    """Получает ход человека"""
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Твой ход-выбери одну из клеток", O, NUM_SQUARES)
        if move not in legal:
            print("Клетка занята...выбери другую!\n")
            return move

#Функция принимает доску и тип фишек компьютера



