import requests
from bs4 import BeautifulSoup as bs

#Функция для парсера веб сайта https://pogoda.uz и записывать в logger.txt файл
def ParserHtmlWebSite():
    response = requests.get("https://pogoda.uz/karshi/").text
    #print(response)
    soup = bs(response, "html.parser")
    weather = soup.find("div", class_="current-forecast")
    split_text = weather.text.split("\n")
    print("Погода в Каршах, днём:"+split_text[4])
    print("Погода в Каршах, ночью:"+split_text[5])
    with open ("logger.txt", "a") as file:
        file.write(f"Погода в Каршах, днём:{split_text[4]}\nПогода в Каршах, ночью:{split_text[5]}\n\n")