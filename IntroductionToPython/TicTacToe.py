
from random import randint


def CreateField(n):
    fields = list(range(n))
    for i in range(n):
        fields[i] = list(range(n))
    for i in range(n):
        for j in range(n):
            fields[i][j] = '#'

    return fields


def PrintField(fields):
    for i in range(len(fields)):
        for j in range(len(fields)):
            print(fields[i][j], end=' ')
        print()
    print()


def EnterCoordinate():
    print("Введите координату для вставки. от 0 до 2")
    X = int(input("Введите координату по оси Х:"))
    Y = int(input("Введите координату по оси Y:"))
    while not ((X>=0 and X<=2)  and (Y >=0 and Y<=2)):
        print("Вы ввели некорректный координату, повторите ещё раз")
        X = int(input("Введите координату по оси Х:"))
        Y = int(input("Введите координату по оси Y:"))

    return (X, Y)

def RandomCoordinate():
    return randint(0,2), randint(0,2)

def RandomType():
    return randint(0,1)

def ComputerStep(fields, compStep):
    isTrue = False
    while True:
            x,y = RandomCoordinate()
            if fields[x][y] =='#':
                fields[x][y] = compStep
                break
            else:
                print("Компьютер повторите попытку")
    if compStep == 'X':
            if fields[0][0] == 'X' and fields[0][1] == 'X' and fields[0][2] =='X':
                print("Компьютер выиграл")
                isTrue = True
            elif fields[1][0] == 'X' and fields[1][1] == 'X' and  fields[1][2] == 'X':
                print("Компьютер выиграл")
                isTrue = True
            elif fields[2][0] == 'X' and fields[2][1] == 'X' and fields[2][2] == 'X':
                print("Компьютер выиграл")
                isTrue = True
            elif fields[0][0] == 'X' and fields[1][0] == 'X' and fields[2][0] == 'X':
                print("Компьютер выиграл")
                isTrue = True
            elif fields[0][1] == 'X' and fields[1][1] == 'X' and fields[2][1] == 'X':
                print("Компьютер выиграл")
                isTrue = True
            elif fields[0][2] == 'X' and fields[1][2] == 'X' and fields[2][2] == 'X':
                print("Компьютер выиграл")
                isTrue = True
            elif fields[0][0] == 'X' and fields[1][1] == 'X' and fields[2][2] == 'X':
                print("Компьютер выиграл")
                isTrue = True
            elif fields[2][0] == 'X' and fields[1][1] == 'X' and fields[0][2] == 'X':
                print("Компьютер выиграл")
                isTrue = True
    elif compStep =='O':
            if fields[0][0] == 'O' and fields[0][1] == 'O' and fields[0][2] =='O':
                print("Компьютер выиграл")
                isTrue = True
            elif fields[1][0] == 'O' and fields[1][1] == 'O' and  fields[1][2] == 'O':
                print("Компьютер выиграл")
                isTrue = True
            elif fields[2][0] == 'O' and fields[2][1] == 'O' and fields[2][2] == 'O':
                print("Компьютер выиграл")
                isTrue = True
            elif fields[0][0] == 'O' and fields[1][0] == 'O' and fields[2][0] == 'O':
                print("Компьютер выиграл")
                isTrue = True
            elif fields[0][1] == 'O' and fields[1][1] == 'O' and fields[2][1] == 'O':
                print("Компьютер выиграл")
                isTrue = True
            elif fields[0][2] == 'O' and fields[1][2] == 'O' and fields[2][2] == 'O':
                print("Компьютер выиграл")
                isTrue = True
            elif fields[0][0] == 'O' and fields[1][1] == 'O' and fields[2][2] == 'O':
                print("Компьютер выиграл")
                isTrue = True
            elif fields[2][0] == 'O' and fields[1][1] == 'O' and fields[0][2] == 'O':
                print("Компьютер выиграл")
                isTrue = True
    return isTrue

def UserStep(fields, userStep):
     isTrue = False
     while True:
        (x,y) = EnterCoordinate()
        if fields[x][y] == '#':
            fields[x][y] = userStep
            break
        else:
             print("Пользователь повторите попытку")
     if userStep == 'X':
        if fields[0][0] == 'X' and fields[0][1] == 'X' and fields[0][2] =='X':
             print("Пользователь выиграл")
             isTrue = True
             
        elif fields[1][0] == 'X' and fields[1][1] == 'X' and  fields[1][2] == 'X':
            print("Пользователь выиграл")
            isTrue = True
        elif fields[2][0] == 'X' and fields[2][1] == 'X' and fields[2][2] == 'X':
            print("Пользователь выиграл")
            isTrue = True
        elif fields[0][0] == 'X' and fields[1][0] == 'X' and fields[2][0] == 'X':
            print("Пользователь выиграл")
            isTrue = True
        elif fields[0][1] == 'X' and fields[1][1] == 'X' and fields[2][1] == 'X':
            print("Пользователь выиграл")
            isTrue = True
        elif fields[0][2] == 'X' and fields[1][2] == 'X' and fields[2][2] == 'X':
            print("Пользователь выиграл")
            isTrue = True
        elif fields[0][0] == 'X' and fields[1][1] == 'X' and fields[2][2] == 'X':
            print("Пользователь выиграл")
            isTrue = True
        elif fields[2][0] == 'X' and fields[1][1] == 'X' and fields[0][2] == 'X':
            print("Пользователь выиграл")
            isTrue = True
     elif userStep =='O':
        if fields[0][0] == 'O' and fields[0][1] == 'O' and fields[0][2] =='O':
            print("Пользователь выиграл")
            isTrue = True
        elif fields[1][0] == 'O' and fields[1][1] == 'O' and  fields[1][2] == 'O':
            print("Пользователь выиграл")
            isTrue = True
        elif fields[2][0] == 'O' and fields[2][1] == 'O' and fields[2][2] == 'O':
            print("Пользователь выиграл")
            isTrue = True
        elif fields[0][0] == 'O' and fields[1][0] == 'O' and fields[2][0] == 'O':
            print("Пользователь выиграл")
            isTrue = True
        elif fields[0][1] == 'O' and fields[1][1] == 'O' and fields[2][1] == 'O':
            print("Пользователь выиграл")
            isTrue = True
        elif fields[0][2] == 'O' and fields[1][2] == 'O' and fields[2][2] == 'O':
            print("Пользователь выиграл")
            isTrue = True
        elif fields[0][0] == 'O' and fields[1][1] == 'O' and fields[2][2] == 'O':
            print("Пользователь выиграл")
            isTrue = True
        elif fields[2][0] == 'O' and fields[1][1] == 'O' and fields[0][2] == 'O':
            print("Пользователь выиграл")
            isTrue = True
     return isTrue
