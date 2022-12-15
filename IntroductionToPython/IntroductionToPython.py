# Задача номер 1. Требуется по запросу выдавать N различных паролей длиной M символов,
# состоящих из строчных # и прописных латинских букв # и цифр, кроме тех,
# которые легко перепутать между собой: «l» (L маленькое),
# «I» (i большое), «1» (цифра), «o» и «O» # (большая и маленькая буквы) и «0» (цифра).
# Решение должно содержать две функции: вспомогательную generate_password(m),
# возвращающую случайный пароль длиной m символов, и основную main(n, m),
#  возвращающую список из n различных паролей, каждый длиной m символов.

#import PasswordGenerateClass as pgc

#n = int(input("Введите n:"))
#m = int(input("Введите m:"))

#passwords = pgc.Password_Lists(n, m)

#print(passwords)

#=========================================================================================

# Задача номер 2. Сделать Предыдущее ДЗ с использование функций

# Морской Бой

#import SeaBattle as sb


#N = 4
#persons = sb.CreateField(N)
#computers = sb.CreateField(N)

#print("Введите координат для добавление корабля")
#personX, personY = sb.EnterToCoordinate()
#print()
#persons[personX][personY] = '#'

#compX, compY = sb.RandomCoordinate()

#computers[compX][compY] ='#'



#print("Поля пользователя")
#sb.PrintField(persons)
#print()
#for i in range(N*N):
#    is_computers = sb.ComputerFireOnBattleField(persons)
#    if is_computers:
#        break
#    is_person = sb.PersonFireOnBattleField(computers)

#    if is_person:
#        break

#    print("Поля пользователя")
#    sb.PrintField(persons)
#    print()


#print("Поля компьютера")
#sb.PrintField(computers)
#print()
#print("Поля пользователя")
#sb.PrintField(persons)

#===================================================================================

# Крестики-нолики
#import TicTacToe as tic
#N = 3
#fields = tic.CreateField(N)

#tic.PrintField(fields)

#userStep, compStep = '',''

#types = tic.RandomType()

#if types == 0:
#    compStep ='O'
#    userStep ='X'
#    print(f"User:{userStep}, Computer:{compStep}")
#    print()
#else:
#    compStep ='X'
#    userStep ='O'
#    print(f"User:{userStep}, Computer:{compStep}")
#    print()

#for i in range(N*N):
#    if tic.ComputerStep(fields, compStep):
#        break
#    tic.PrintField(fields)
#    if tic.UserStep(fields, userStep):
#        break
#    tic.PrintField(fields)

#tic.PrintField(fields);

#======================================================================================
# Задача номер 3. Сделать поле чудес . Компьютер загадывает слово. А мы его угадываем.
# Делаем с помощью функций. Кто хочет посложней - добавляем очки и барабан. 

import FieldOfDreams as fd
from random import randint

dicts ={"Москва":"Столица России?",
       "Менделеев":"Кто придумал таблицу элементов по предметам Химии?",
       "Семь":"Сколько материков на Земле?",
       "Бангладеш":"Самая густонаселенная страна в мире",
       }


keys = fd.AddList(dicts)

index = randint(0, 3)
question = fd.GetQuestionByDictionary(dicts, keys, index)

fields = fd.AddListField(keys)

print(question)
answer = fields[index]
print(answer)
while True:
    answer_or_symbol = fd.PlayGame(keys, index)
    if len(answer_or_symbol)>1:
        answer = answer_or_symbol
        print(answer)
        break
    else:
        sym = keys[index]
        idx = []
        for i in range(len(sym)):
            if answer_or_symbol == sym[i]:
                idx.append(i)
        myanswer = list(answer)
        for j in range(len(idx)):
            myanswer[idx[j]] = str(answer_or_symbol)
        print(myanswer)

