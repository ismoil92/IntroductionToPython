from random import randint

def CreateField(n):
    fields = list(range(n))
    for i in range(n):
        fields[i] = list(range(n))

    for i in range(n):
        for j in range(n):
            fields[i][j] =0
    return fields


def EnterToCoordinate():
    print("Введите координату для корабля. от 0 до 3")
    X = int(input("Введите координату по оси Х:"))
    Y = int(input("Введите координату по оси Y:"))
    while not ((X>=0 and X<=3)  and (Y >=0 and Y<=3)):
        print("Вы ввели некорректный координату, повторите ещё раз")
        X = int(input("Введите координату по оси Х:"))
        Y = int(input("Введите координату по оси Y:"))

    return (X, Y)

def RandomCoordinate():
    return randint(0,3), randint(0,3)

def PrintField(fields):
    for i in range(len(fields)):
        for j in range(len(fields)):
            print(fields[i][j], end=' ')
        print()

def PersonFireOnBattleField(computers):
    isTrue = False
    x,y = EnterToCoordinate()
    print()
    if computers[x][y] =='#':
          computers[x][y] ='*'
          print("Пользователь победил")
          isTrue = True
    elif computers[x][y] == 0:
        print("Пользователь, Мимо")
        print()
        computers[x][y] ='*'
    else:
       while  computers[x][y] =='*':
           print("Пользователь, вы сюда стреляли, Повторите ещё раз")
           x,y = EnterToCoordinate()
           print()
           if computers[x][y] =='#':
                computers[x][y] ='*'
                print("Пользователь победил")
                print()
                isTrue = True
                break
           elif computers[x][y] == 0:
             print("Пользователь, Мимо")
             print()
             computers[x][y] ='*'

    return isTrue

def ComputerFireOnBattleField(persons):
    isTrue = False
    x, y = RandomCoordinate()
    if persons[x][y] == '#':
        persons[x][y] ='*'
        print("Компьютер победил")
        isTrue = True
    elif persons[x][y] == 0:
        print("Компьютер: Мимо")
        print()
        persons[x][y] ='*'
    else:
       while  persons[x][y] =='*':
            print("Компьютер, вы сюда стреляли, Повторите ещё раз")
            x = randint(0,3)
            y = randint(0,3)
            if persons[x][y] == '#':
                persons[x][y] ='*'
                print("Компьютер победил")
                isTrue = True
                break;
            elif persons[x][y] == 0:
                print("Компьютер: Мимо")
                print()
    return isTrue


