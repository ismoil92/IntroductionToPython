
# Задача номер 1. Написать программу, где создадим класс Soup (для определения типа супа),
# принимающий 1 аргумент - который отвечает за основной продукт к выбираемому супу.
# В этом классе создать метод show_my_soup(), выводящий на печать «Суп - {Основной продукт}»
#  в случае наличия добавки Это как доп к этой задаче 
#  - иначе отобразится следующая фраза: «Обычный кипяток».

#import SoypFile as sf

#soup = sf.Soup("Borsh","Капуста")

#print(soup.show_my_soup())

#=============================================================================================

# Задача номер 2. Нужно написать программу В ней используем классы - имя студента name,
# номер группы group и список полученных оценок progress.В самой программе вводим список всех
# студентов. В программе нужно вывести список студентов, отсортированный по имени,
# А так же студентов, у которых низкие оценки.

import StudentFile as sf

while True:
    select_input = int(input("\nВыберите одну из двух задач. 1-Добавить. 2 - Выводить:"))
    if select_input == 1:
        name = input("Введите имя:")
        group = int(input("Введите номер группы:"))
        progress =int(input("Введите оценку:"))
        student = sf.Student(name, group, progress)
    else:
        break


print("Введите одни из трёх задач. 1-Вывод студентов по оценкам, по убыванию.")
print("2-Вывод студентов по оценкам, по возрастанию. 3- Вывод студентов по имени")
select_number = int(input("Введите 1-3:"))

if select_number == 1:
    sf.Student.items.sort(key=lambda x:x.progress, reverse= True)
    success = sf.Student.items
    for i in range(len(success)):
        print(success[i])
elif select_number == 2:
    sf.Student.items.sort(key=lambda x:x.progress)
    failed = sf.Student.items
    for i in range(len(failed)):
        print(failed[i])
elif select_number == 3:
    sf.Student.items.sort(key=lambda x:x.name)
    names = sf.Student.items
    for i in range(len(names)):
        print(names[i])






