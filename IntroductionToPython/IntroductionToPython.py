
import ConsoleBot as bot

week_list = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]

weeks ={1:"monday.txt", 2:"tuesday.txt", 3:"wednesday.txt", 4:"thursday.txt", 5:"friday.txt", 
        6:"saturday.txt", 7:"sunday.txt"}

bot.CreateTextFileForWeekSchedule(weeks, week_list)

bot.RunningBot(weeks)