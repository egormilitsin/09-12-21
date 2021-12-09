# Создать класс Экран, от которого наследуется класс Монитор и Телевизор,
# переопределить методы у экрана обязательно. Методы придумаете сами -
# цель реализовать полиморфизм

class Screen(object):
    def shows(self):
        print("показывает")
    def glows(self):
        print("светится")
class Monitor(Screen):
    def shows(self):
        print("показывает от компьютера")
class Tv(Screen):
    def shows(self):
        print("показывает TV")

