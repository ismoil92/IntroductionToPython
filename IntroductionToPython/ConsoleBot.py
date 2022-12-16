
# Функция для создание текстового файла для расписание недели
def CreateTextFileForWeekSchedule(weeks, week_list):
    for i in range(len(week_list)):
        with open(weeks[i+1], "w") as file:
            file.write(week_list[i])






# Функция для выбора текстового файла день недели, для записи расписание
# Входные параметры. словарь weeks день недели, number_day номер дня и input_text строку для записи
def SelectTextFileAndWrite(weeks, number_day, input_text):
    if number_day>=1 and number_day<=7:
        with open(weeks[number_day], "a") as file:
            file.write("\n"+input_text)
    else:
        print("Нет такого дни недели")




# Функция для выбора текстового файла день недели, для перезаписывать  расписание
# Входные параметры, словарь weeks день недели number_day номер дня и input_text строку для записи

def SelectTextFileAndOverWrite(weeks, number_day, input_text):
    if number_day>=1 and number_day<=7:
        with open(weeks[number_day], "w") as file:
            file.write(input_text)
    else:
        print("Нет такого дни недели")




# Функция для выбора текстового файла день недели, для вывода на консоль  расписанию
# Входные параметры. number_day номер дня и словарь weeks день недели
def SelectTextFileAndReadLineAndPrint(weeks, number_day):
    if number_day>=1 and number_day<=7:
        with open(weeks[number_day], "r") as file:
            for line in file:
                print(line, end='')
    else:
        print("Нет такого дни недели")

# Функция для работы консольного бота. Входные параметры словарь weeks день недели
def RunningBot(weeks):
    while True:
        print("\nВыберите команду для консольного бота. 1- записать. 2- перезаписать. 3- читать. 4-Выход:", end='')
        bot_input = int(input())
        if bot_input == 1:
            number_day = int(input("Введите номер день недели:"))
            input_text = input("Введите текст:")
            SelectTextFileAndWrite(weeks, number_day, input_text)
        elif bot_input == 2:
            number_day = int(input("Введите номер день недели:"))
            input_text = input("Введите текст:")
            SelectTextFileAndOverWrite(weeks, number_day, input_text)
        elif bot_input == 3:
            number_day = int(input("Введите номер день недели:"))
            SelectTextFileAndReadLineAndPrint(weeks, number_day)
        elif bot_input == 4:
            break
