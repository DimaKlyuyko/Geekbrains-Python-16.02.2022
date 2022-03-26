# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов метод должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    title: str = "Какое-то название."

    def draw(self):
        print("Запуск отрисовки Stationery.")


class Pen(Stationery):
    def draw(self):
        print("Запуск отрисовки Pen.")


class Pencil(Stationery):
    def draw(self):
        print("Запуск отрисовки Pencil.")


class Handle(Stationery):
    def draw(self):
        print("Запуск отрисовки Handle.")


first = Stationery()
second = Pen()
third = Pencil()
fourth = Handle()

first.draw()
second.draw()
third.draw()
fourth.draw()
