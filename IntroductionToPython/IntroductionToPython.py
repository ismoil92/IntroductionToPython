
# Задача номер 1. Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

#from random import randint

#numb = int(input("Введите размер списка:"))

#lists = []

#for i in range(numb):
#    h = randint(0,20)
#    lists.append(h)
#    i+=1

#i=1
#summ=0
#while i<numb:
#    summ+=lists[i]
#    i+=2
#print(lists)
#print(f"Сумма элементов списка, стоящих на нечётной позиции:{summ}")

#================================================================================


# Задача номер 2. Написать программу, которая генерирует двумерный массив на A x B элементов
# ( A и B вводим с клавиатуры)И считаем средне-арифметическое каждой строки
# (не пользуемся встроенными методами подсчета суммы)

#from random import randint

#a = int(input("введите a:"))
#b = int(input("введите b:"))

#lists =list(range(a))
#for i in range(a):
#    lists[i] = list(range(b))

#for i in range(a):
#    for j in range(b):
#        lists[i][j] = randint(1, 20)
#        j+=1
#    j=0
#    i+=1
#print(lists)
#summ =0
#list_sum =[]
#for i in range(a):
#    for j in range(b):
#        summ+=lists[i][j]
#        j+=1
#    j=0
#    i+=1
#    list_sum.append(summ/b)
#    summ=0
#print(list_sum)

#===========================================================================

# Задача номер 3.  Сгенерируйте список на 30 элементов.
# Отсортируйте список по возрастанию, методом сортировки выбором.

from random import randint

n = 30
lists =[]

for i in range(n):
    lists.append(randint(1,20))
    i+1
print(lists)
print()
i, minIndex, temp = 0 ,0, 0

while i< n-1:
    minIndex = i
    j = i+1
    while j < n:
        if lists[j] < lists[minIndex]:
            minIndex = j
        j+=1
    temp = lists[i]
    lists[i] = lists[minIndex]
    lists[minIndex] = temp
    i+=1

print(lists)

