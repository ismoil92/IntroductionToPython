
# Задача номер 1. Сделать игру морской бой с размерам 4 на 4, с одним корабликом.
from random import randint
import File as f
N = 4

#Поля для пользователя
persons = list(range(N))
for i in range(N):
    persons[i] = list(range(N))

for i in range(N):
    for j in range(N):
        persons[i][j] = 0


#Поля для компьютера
computers = list(range(N))
for i in range(N):
    computers[i] = list(range(N))

for i in range(N):
    for j in range(N):
        computers[i][j] = 0

print("Пользователь введите координату для вставки корабля. от 0 до 3")
shipX = int(input("Введите координату по оси Х:"))
shipY = int(input("Введите координату по оси Y:"))

while not((shipX>=0 and shipX<=3) and (shipY>=0 and shipY<=3)):
    print("Вы ввели некорректный координату, повторите ещё раз")
    print("Введите координату для вставки корабля. от 0 до 3")
    shipX = int(input("Введите координату по оси Х:"))
    shipY = int(input("Введите координату по оси Y:"))

persons[shipX][shipY] = '#'
print()
#for i in range(N):
#    for j in range(N):
#        print(persons[i][j], end=' ')
#    print()
#print('==================================================')

compX = randint(0,3)
compY = randint(0,3)

computers[compX][compY] = '#'

j =0
while j<N*N:
   compX = randint(0,3)
   compY = randint(0,3)
   if persons[compX][compY] == '#':
        persons[compX][compY] ='*'
        print("Компьютер победил")
        break;
   elif persons[compX][compY] == 0:
        print("Компьютер: Мимо")
        persons[compX][compY] ='*'
   else:
       while  persons[compX][compY] =='*':
            print("Компьютер, вы сюда стреляли, Повторите ещё раз")
            compX = randint(0,3)
            compY = randint(0,3)
            if persons[compX][compY] == '#':
                persons[compX][compY] ='*'
                print("Компьютер победил")
                break;
            elif persons[compX][compY] == 0:
                print("Компьютер: Мимо")

   x,y = f.EnterToCoordinate()
   if computers[x][y] =='#':
        computers[x][y] ='*'
        print("Пользователь победил")
        break
   elif computers[x][y] == 0:
        print("Пользователь, Мимо")
        computers[x][y] ='*'
   else:
       while  computers[x][y] =='*':
           print("Пользователь, вы сюда стреляли, Повторите ещё раз")
           x,y = f.EnterToCoordinate()
           if computers[x][y] =='#':
                computers[x][y] ='*'
                print("Пользователь победил")
                break
           elif computers[x][y] == 0:
             print("Пользователь, Мимо")
             computers[x][y] ='*'

   j-=1



print("==================================================")

print("Computers")
for i in range(N):
    for j in range(N):
        print(computers[i][j], end=' ')
    print()


print()
print("Persons")
for i in range(N):
    for j in range(N):
        print(persons[i][j], end=' ')
    print()

#=====================================================================================

# Задача номер 2. Создать игру крестики-нолики
#import File as f
#from random import randint

#N = 3
#A = list(range(N))
#for i in range(N):
#    A[i] = list(range(N))

#for i in range(N):
#    for j in range(N):
#        A[i][j] = '#'

#for i in range(N):
#    for j in range(N):
#        print(A[i][j], end=' ')
#    print()

#print('---------------------------------------------')

#print("0 - O, 1 - X")
#type_X_O = randint(0,1)


#compStep, PersonStep = '',''

#if type_X_O == 0:
#    compStep ='O'
#    PersonStep ='X'
#    print(f"Computer:{compStep}")
#else:
#    compStep ='X'
#    PersonStep ='O'
#    print(f"Computer:{compStep}")
#i=0
#while i<N*N:
#    while True:
#        compX = randint(0,2)
#        compY = randint(0,2)
#        if A[compX][compY] =='#':
#            A[compX][compY] = compStep
#            break
#        else:
#            print("Компьютер повторите попытку")  
#    for i in range(N):
#        for j in range(N):
#             print(A[i][j], end=' ')
#        print()
#    print("=================================================")
#    if compStep == 'X':
#        if A[0][0] == 'X' and A[0][1] == 'X' and A[0][2] =='X':
#            print("Компьютер выиграл")
#            break
#        elif A[1][0] == 'X' and A[1][1] == 'X' and  A[1][2] == 'X':
#            print("Компьютер выиграл")
#            break
#        elif A[2][0] == 'X' and A[2][1] == 'X' and A[2][2] == 'X':
#            print("Компьютер выиграл")
#            break
#        elif A[0][0] == 'X' and A[1][0] == 'X' and A[2][0] == 'X':
#            print("Компьютер выиграл")
#            break
#        elif A[0][1] == 'X' and A[1][1] == 'X' and A[2][1] == 'X':
#            print("Компьютер выиграл")
#            break
#        elif A[0][2] == 'X' and A[1][2] == 'X' and A[2][2] == 'X':
#            print("Компьютер выиграл")
#            break
#        elif A[0][0] == 'X' and A[1][1] == 'X' and A[2][2] == 'X':
#            print("Компьютер выиграл")
#            break
#        elif A[2][0] == 'X' and A[1][1] == 'X' and A[0][2] == 'X':
#            print("Компьютер выиграл")
#            break
#    elif compStep =='O':
#        if A[0][0] == 'O' and A[0][1] == 'O' and A[0][2] =='O':
#            print("Компьютер выиграл")
#            break
#        elif A[1][0] == 'O' and A[1][1] == 'O' and  A[1][2] == 'O':
#            print("Компьютер выиграл")
#            break
#        elif A[2][0] == 'O' and A[2][1] == 'O' and A[2][2] == 'O':
#            print("Компьютер выиграл")
#            break
#        elif A[0][0] == 'O' and A[1][0] == 'O' and A[2][0] == 'O':
#            print("Компьютер выиграл")
#            break
#        elif A[0][1] == 'O' and A[1][1] == 'O' and A[2][1] == 'O':
#            print("Компьютер выиграл")
#            break
#        elif A[0][2] == 'O' and A[1][2] == 'O' and A[2][2] == 'O':
#            print("Компьютер выиграл")
#            break
#        elif A[0][0] == 'O' and A[1][1] == 'O' and A[2][2] == 'O':
#            print("Компьютер выиграл")
#            break
#        elif A[2][0] == 'O' and A[1][1] == 'O' and A[0][2] == 'O':
#            print("Компьютер выиграл")
#            break
#    while True:
#        (x,y) = f.EnterToXorO()
#        if A[x][y] == '#':
#            A[x][y] = PersonStep
#            break
#        else:
#             print("Пользователь повторите попытку")
#    for i in range(N):
#        for j in range(N):
#             print(A[i][j], end=' ')
#        print()
#    print("=================================================")
#    if PersonStep == 'X':
#        if A[0][0] == 'X' and A[0][1] == 'X' and A[0][2] =='X':
#            print("Пользователь выиграл")
#            break
#        elif A[1][0] == 'X' and A[1][1] == 'X' and  A[1][2] == 'X':
#            print("Пользователь выиграл")
#            break
#        elif A[2][0] == 'X' and A[2][1] == 'X' and A[2][2] == 'X':
#            print("Пользователь выиграл")
#            break
#        elif A[0][0] == 'X' and A[1][0] == 'X' and A[2][0] == 'X':
#            print("Пользователь выиграл")
#            break
#        elif A[0][1] == 'X' and A[1][1] == 'X' and A[2][1] == 'X':
#            print("Пользователь выиграл")
#            break
#        elif A[0][2] == 'X' and A[1][2] == 'X' and A[2][2] == 'X':
#            print("Пользователь выиграл")
#            break
#        elif A[0][0] == 'X' and A[1][1] == 'X' and A[2][2] == 'X':
#            print("Пользователь выиграл")
#            break
#        elif A[2][0] == 'X' and A[1][1] == 'X' and A[0][2] == 'X':
#            print("Пользователь выиграл")
#            break
#    elif PersonStep =='O':
#        if A[0][0] == 'O' and A[0][1] == 'O' and A[0][2] =='O':
#            print("Пользователь выиграл")
#            break
#        elif A[1][0] == 'O' and A[1][1] == 'O' and  A[1][2] == 'O':
#            print("Пользователь выиграл")
#            break
#        elif A[2][0] == 'O' and A[2][1] == 'O' and A[2][2] == 'O':
#            print("Пользователь выиграл")
#            break
#        elif A[0][0] == 'O' and A[1][0] == 'O' and A[2][0] == 'O':
#            print("Пользователь выиграл")
#            break
#        elif A[0][1] == 'O' and A[1][1] == 'O' and A[2][1] == 'O':
#            print("Пользователь выиграл")
#            break
#        elif A[0][2] == 'O' and A[1][2] == 'O' and A[2][2] == 'O':
#            print("Пользователь выиграл")
#            break
#        elif A[0][0] == 'O' and A[1][1] == 'O' and A[2][2] == 'O':
#            print("Пользователь выиграл")
#            break
#        elif A[2][0] == 'O' and A[1][1] == 'O' and A[0][2] == 'O':
#            print("Пользователь выиграл")
#            break
#    i-=1


