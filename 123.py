# Создать класс Книжная полка, где есть два
# поля - список Книг и тип материала из которого
# сделана полка ( к примеру дерево). Для создания
# этого класса нужно создать еще два класса
# (Книга и Материал). В методах класса Полка нужно
# сделать метод, который выводит все книги на
# полке на экран

# class Shelf:
# def __init__(material):
# def __init__(material):
#     self.material = material
#     books = []


class books(object):
    book1 = "pushkin"
    book2 = "gogol"
    book3 = "dostoevsky"

class material(object):
    material1 = "iron"
    material2 = "tree"
    material3 = "black tree"

class polka:
    def __init__(self,material, books):
        self.material = material
        self.books = books









