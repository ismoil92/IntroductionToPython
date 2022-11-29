
# Задача номер 1. Вводим с клавиатуры десятичное число.
# Необходимо перевести его в шестнадцатиричную систему счисления.

#number = int(input("Введите число:"))
#sixteensDigit=""
#numb=0
#while number >= 16:
#    numb = number%16
#    if numb >=10 and numb<=15:
#        if numb == 10:
#            sixteensDigit+='A'
#        elif numb == 11:
#            sixteensDigit+='B'
#        elif numb == 12:
#            sixteensDigit+='C'
#        elif numb == 13:
#            sixteensDigit+='D'
#        elif numb == 14:
#            sixteensDigit+='E'
#        elif numb == 15:
#            sixteensDigit+='F'
#    else:
#        sixteensDigit+=str(numb)
#    number//=16


#if number == 10:
#    sixteensDigit+='A'
#elif number == 11:
#    sixteensDigit+='B'
#elif number == 12:
#    sixteensDigit+='C'
#elif number == 13:
#    sixteensDigit+='D'
#elif number == 14:
#    sixteensDigit+='E'
#elif number == 15:
#    sixteensDigit+='F'
#else:
#    n = number%16
#    number//=16
#    sixteensDigit+=str(n)

#result=""
#i = len(sixteensDigit)-1
#while i >=0:
#    result+=sixteensDigit[i]
#    i-=1
#print(f"Двоичный число переведана в шестнадцаричнию систему счислению:{result}")

#=========================================================================================


# Задача номер 2. Вводим с клавиатуры строку. Необходимо сказать,
# является ли эта строка дробным числом.




#text = input("Введите строку:")
#i = 0
#istrue = False

#if text[i]>='0' and text[i]<='9':
#    i+=1

#    while text[i]>='0' and text[i]<='9':
#        i+=1
#    if text[i] == '.':
#        i+=1
#        while text[i]>='0' and text[i]<='9':
#            i+=1
#            if i == len(text):
#                break
#            if text[i].isalpha():
#                istrue = False
#                break
#            istrue = True

#else:
#    print("Не является дробной числом")

#if istrue:
#    print("Является дробной числом")
#else:
#    print("Не является дробной числом 2")


#=====================================================================================


# Задача номер 3.Вводим с клавиатуры строку.
# Необходимо развернуть подстроку между первой и последней буквой "о".
# Если она только одна или её нет - то сообщить, что буква "о" -одна или не встречается

text = input("Введите строку:")
result = text.lower()
newtext =""
firstIndex =-1
lastIndex = -1
for i in range(len(result)):
    if result[i] == 'o' or result[i] == 'о':
        if firstIndex == -1:
            firstIndex = i
        else:
            if lastIndex == -1:
                lastIndex = i
            else:
                lastIndex = i
    i+=1


if firstIndex != -1 and lastIndex !=-1:
    i = lastIndex-1
    while i> firstIndex:
        newtext+=result[i]
        i-=1
    print(newtext)
else:
    if firstIndex != -1:
        print("В строке есть только одна буква о")
    else:
        print("В строке не одного буква о")
