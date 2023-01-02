from telegram import Update, Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from Token_File import bot_token
import requests
from bs4 import BeautifulSoup as bs


#week_list =["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]

#weeks ={1:"monday.txt", 2:"tuesday.txt", 3:"wednesday.txt", 4:"thursday", 5:"friday.txt", 6:"saturday.txt", 7:"sunday.txt"}

#select_day_number = 0
#input_text = ""

def Telegram_Bot():
    bot = Bot(bot_token)
    updater = Updater(bot_token, use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler("start", start)
    getweather_handler = CommandHandler("weather", get_weather)
    message_handler = MessageHandler(Filters.text, message)
    butweather_handler = CallbackQueryHandler(button_weather)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(getweather_handler)
    dispatcher.add_handler(butweather_handler)
    dispatcher.add_handler(message_handler)


    #getday_handler = CommandHandler("getday", get_day)
    #getcommands_handler = CommandHandler("commands", get_commands)
    #button_handler = CallbackQueryHandler(button)
    #buttonfile_handler = CallbackQueryHandler(button_file)

    #dispatcher.add_handler(getday_handler)
    #dispatcher.add_handler(getcommands_handler)
    #dispatcher.add_handler(button_handler)
    #dispatcher.add_handler(buttonfile_handler)

    updater.start_polling()
    updater.idle()

def start(update, context):
    context.bot.send_message(update.effective_chat.id, "Привет")

def message(update, context):
    context.bot.send_message(update.effective_chat.id, update.message.text)

def get_weather(update, context):
    keyboard  =[
        [InlineKeyboardButton("Карши", callback_data ='1'), InlineKeyboardButton("Ташкент", callback_data ='2'), InlineKeyboardButton("Самарканд", callback_data ='3')]
        ]

    update.message.reply_text("Выберите город, чтобы узнать погоду", reply_markup = InlineKeyboardMarkup(keyboard))



def button_weather(update, context):
    query = update.callback_query
    query.answer()

    if query.data == '1':
        response = requests.get("https://pogoda.uz/karshi/").text
        soup = bs(response, "html.parser")
        weather = soup.find("div", class_="current-forecast")
        split_text = weather.text.split("\n")
        context.bot.send_message(update.effective_chat.id,"Погода в Каршах, днём:"+split_text[4])
        context.bot.send_message(update.effective_chat.id,"Погода в Каршах, ночью:"+split_text[5])
    elif query.data == '2':
        response = requests.get("https://pogoda.uz/tashkent/").text
        soup = bs(response, "html.parser")
        weather = soup.find("div", class_="current-forecast")
        split_text = weather.text.split("\n")
        context.bot.send_message(update.effective_chat.id,"Погода в Ташкенте, днём:"+split_text[4])
        context.bot.send_message(update.effective_chat.id,"Погода в Ташкенте, ночью:"+split_text[5])
    elif query.data == '3':
        response = requests.get("https://pogoda.uz/samarkand/").text
        soup = bs(response, "html.parser")
        weather = soup.find("div", class_="current-forecast")
        split_text = weather.text.split("\n")
        context.bot.send_message(update.effective_chat.id,"Погода в Самарканде, днём:"+split_text[4])
        context.bot.send_message(update.effective_chat.id,"Погода в Самарканде, ночью:"+split_text[5])





#==================================================================================================
    #if update.message.text =="Bob":
    #    context.bot.send_message(update.effective_chat.id, "Hello Bob")
    #else:
    #    context.bot.send_message(update.effective_chat.id, "It's not Bob")

#def get_day(update, context):
#    keyboard = [
#        [InlineKeyboardButton("Понедельник", callback_data ='1'), InlineKeyboardButton("Вторник", callback_data ='2')],
#        [InlineKeyboardButton("Среда", callback_data ='3'), InlineKeyboardButton("Четверг", callback_data ='4')],
#        [InlineKeyboardButton("Пятница", callback_data ='5'), InlineKeyboardButton("Суббота", callback_data ='6')],
#        [InlineKeyboardButton("Воскресенье", callback_data ='7')]
#    ]

#    update.message.reply_text("Enter day of:", reply_markup = InlineKeyboardMarkup(keyboard))

#def get_commands(update, context:CallbackContext):
#    keyboard = [
#        [InlineKeyboardButton("Записать", callback_data ='8'), InlineKeyboardButton("Перезаписать", callback_data ='9'), InlineKeyboardButton("Читать", callback_data ='0')]
#        ]

#    update.message.reply_text("Enter command:", reply_markup = InlineKeyboardMarkup(keyboard))



#def button(update, context):
#    query = update.callback_query
#    query.answer()

    
#    if query.data == '1':
#        select_day_number = int(query.data)
#        context.bot.send_message(update.effective_chat.id,"Monday")
#    elif query.data == '2':
#        select_day_number = int(query.data)
#        context.bot.send_message(update.effective_chat.id, "Tuesday")
#    elif query.data == '3':
#        select_day_number = int(query.data)
#        context.bot.send_message(update.effective_chat.id, "Wednesday")
#    elif query.data == '4':
#        select_day_number = int(query.data)
#        context.bot.send_message(update.effective_chat.id, "Thursday")
#    elif query.data == '5':
#        select_day_number = int(query.data)
#        context.bot.send_message(update.effective_chat.id, "Friday")
#    elif query.data == '6':
#        select_day_number = int(query.data)
#        context.bot.send_message(update.effective_chat.id, "Saturday")
#    elif query.data == '7':
#        select_day_number = int(query.data)
#        context.bot.send_message(update.effective_chat.id, "Sunday")



#def button_file(update, context):
#    query = update.callback_query
#    query.answer()


#    if query.data == '8':
#        with open(weeks[select_day_number], "a") as file:
#            file.write("\n"+input_text)
#    elif query.data == '9':
#        with open(weeks[select_day_number], "w") as file:
#            file.write(input_text)
#    elif query.data == '0':
#        with open(weeks[select_day_number], "r") as file:
#            for line in file:
#                context.bot.send_message(update.effective_chat.id, line)
