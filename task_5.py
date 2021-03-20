"""
5. Реализовать класс Stationery (канцелярская принадлежность).
определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print(f"Запуск отрисовки ручкой '{self.title}'")


class Pencil(Stationery):
    def draw(self):
        print(f"Запуск отрисовки карандашом '{self.title}'")


class Handle(Stationery):
    def draw(self):
        print(f"Запуск отрисовки маркером '{self.title}'")


pe = Pen("black")
pe.draw()

pl = Pencil("metal")
pl.draw()

ha = Handle("permanent")
ha.draw()
