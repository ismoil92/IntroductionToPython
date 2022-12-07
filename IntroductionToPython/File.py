def EnterToXorO():
    print("Введите координату для вставки. от 0 до 2")
    persX = int(input("Введите координату по оси Х:"))
    persY = int(input("Введите координату по оси Y:"))
    while not ((persX>=0 and persX<=2)  and (persY >=0 and persY<=2)):
        print("Вы ввели некорректный координату, повторите ещё раз")
        persX = int(input("Введите координату по оси Х:"))
        persY = int(input("Введите координату по оси Y:"))

    return (persX, persY)


def EnterToCoordinate():
    print("Введите координату для вставки корабля. от 0 до 3")
    persX = int(input("Введите координату по оси Х:"))
    persY = int(input("Введите координату по оси Y:"))
    while not ((persX>=0 and persX<=3)  and (persY >=0 and persY<=3)):
        print("Вы ввели некорректный координату, повторите ещё раз")
        persX = int(input("Введите координату по оси Х:"))
        persY = int(input("Введите координату по оси Y:"))

    return (persX, persY)


