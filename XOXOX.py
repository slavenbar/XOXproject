#Крестики-Нолики
X="X"
O="O"
EMPTY=" " #Пустое поле
TIE="Ничья"
NUM_SQUARES=9 #Количество клеток на поле

#Функция выводит правила игры
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

#Функция задаёт вопрос,на который нужно ответить да или нет
def ask_yes_no(question):
    """Отвечать надо - да или нет"""
    response = None
    while response not in("y", "n"):
        response = input(question).lower()
    return response
#Фунция запрашивает число с диапазона
def ask_number(question,low,high):
    """Просит ввести число из диапазона"""
    response = None
    while response not in range(low,high):
        response = int(input(question))
    return response
#Функция спрашивает чей ход первый
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
    return computer,human