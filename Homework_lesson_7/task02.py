"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.

Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
Проверить работу этих методов на реальных данных.

Реализовать общий подсчет расхода ткани.

Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.
"""

from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def calculate(self):
        pass


class Coat(Clothes):
    _size: float

    def __init__(self, size: float):
        self._size = size

    @property
    def calculate(self):
        return self._size / 6.5 + 0.5


class Costume(Clothes):
    _height: float

    def __init__(self, height: float):
        self._height = height

    @property
    def calculate(self):
        return self._height * 2 + 0.3


my_coat = Coat(13)
my_costume = Costume(20)

print(f"Coat. Size = {my_coat._size}. Sum = {my_coat.calculate}.")
print(f"Costume. Height = {my_costume._height}. Sum = {my_costume.calculate}.")


class CompositeClothes(Clothes):
    def __init__(self, children: list):
        self.children = children

    def calculate(self):
        res = 0
        for item in self.children:
            res += item.calculate
        return f"Full sum = {res}."


calc = CompositeClothes([my_coat, my_costume])

print(calc.calculate())
