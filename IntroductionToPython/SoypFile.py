# Класс для создание супа
class Soup:
    # функция (или конструктор) с двумя параметрами, soup_name имя супа и product - основной ингридиент
    def __init__(self, soup_name, product):
        self.soup_name = soup_name
        if product != "":
            self.product = product
            self.isTrue = True
        else:
            self.isTrue = False

    # Функция для вывода на консоль
    def show_my_soup(self):
        if self.isTrue:
            print("Хотите добавки (y/n):", end="")
            if input() == "y":
                return f"{self.soup_name} - {self.product} + добавка"
            else:
                return f"{self.soup_name} - {self.product} без добавки"
        else:
            return "Обычный кипяток!!"




