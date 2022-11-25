
# Задача номер 1.  Вводим с клавиатуры целое число X и У.
# Выводим на экран количество чисел между Х и У, которые делятся на 2 и 3.

#X = int(input("Введите число X:"))
#Y = int(input("Введите число Y:"))

#i = X
#while i <= Y:
#    if i % 2==0 and i % 3 == 0:
#        print(f"i={i}")
#    i+=1

#=================================================================================



# Задача номер 2.Вводим с клавиатуры целое число X Далее вводим Х целых чисел.
# Необходимо вывести на экран максимальное и второе максимальное число из введенных чисел.

#X = int(input("Введите число X:"))
#i=0
#firstMax=0
#secondMax=0
#temp=0
#while i <X:
#    numb = int(input("Введите число:"))
#    if i==0:
#        firstMax = numb
#    if numb > firstMax:
#        secondMax = firstMax
#        firstMax = numb
#    i+=1
#print(f"Первый максимальный элемент:{firstMax}")
#print(f"Второй максимальный элемент:{secondMax}")



#============================================================================================



# Задача номер 3.Вводим с клавиатуры целое число - это зарплата.Нужно вывести в консоль -
# Минимальное кол-во  купюр, которыми можно выдать ЗП.
# И сколько, и каких бухгалтер выдаст 25 рублевых купюр,  10 рублевых, 3 рублевых и 1 рублевых



#salary = int(input("Введите зарплату:"))
#twenty_five_bill = 0
#count_twenty_five = 0
#ten_bill = 0
#count_ten =0
#three_bill = 0
#count_three =0
#one_bill = 0
#count_one =0
#while salary >=25:
#    count_twenty_five = salary//25
#    twenty_five_bill=count_twenty_five*25
#    salary = salary-twenty_five_bill

#while salary >=10:
#    count_ten = salary//10
#    ten_bill = count_ten*10
#    salary=salary - ten_bill

#while salary >=3:
#    count_three = salary//3
#    three_bill = count_three*3
#    salary = salary - three_bill

#while salary >=1:
#    count_one = salary//1
#    one_bill = count_one*1
#    salary = salary - one_bill

#print(f"25 купюрные:{count_twenty_five}, 10 купюрные:{count_ten}, 3 купюрные:{count_three}, 1 купюрные:{count_one}")

# =================================================================================


# Задача номер 4.Вводим с клавиатуры многозначное число.Необходимо узнать и 
# сказать последовательность цифр этого числа при просмотре слева направо упорядочена по возрастанию
# или нет. Например 1579 - да ( 1 меньше 5, 5 меньше 7, а 7 меньше 9), 1427 - нет

number = int(input("Введите многозачное число:"))
isTrue = False

while number >0 :
    a = number % 10
    number //= 10
    b = number % 10
    if a > b:
        isTrue = True
    else:
        isTrue = False
        break

print(isTrue)