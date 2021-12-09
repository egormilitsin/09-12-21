# Создать класс Автомобиль, у которого есть поля: список колес, двигатель и коробка передач.
# В классе автомобиль реализовать метод для получения
# информации о кол-во лошадиных сил у двигателя, типе трансмиссии и кол-во колес
# Колесо, двигатель, коробка передач - это отдельные классы

class Engine:
    def __init__(self, performance):
        self.performance = performance

class Transmission:
    def __init__(self, gears):
        self.gears = gears

class Wheel:
    def __init__(self,radius):
        self.radius=radius

en1=Engine(240)
tr1=Transmission(7)
wheels=[Wheel(19),Wheel(19),Wheel(19),Wheel(19)]
class Car:
    def __init__(self, engine,trans,wheels):
        self.engine=engine
        self.trans=trans
        self.wheels=wheels


    def info(self):
        return f"мощность: {self.engine.performance} количество передач:{self.trans.gears} " \
               f" Количество колес: {len(self.wheels)} "


беха=Car(en1,tr1,wheels)

print(беха.info())
