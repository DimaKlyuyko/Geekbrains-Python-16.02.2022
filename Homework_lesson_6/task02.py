# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна. Проверить работу метода.
#
# Например: 20м*5000м*25кг*5см = 12500 т

class Road:
    _length: int
    _width: int

    def __init__(self, length: int, width: int):
        self._length = length
        self._width = width

    def asphalt_mass_count(self):
        result = (self._length * self._width * 25 * 5) / 1000
        return f"{result} тонн"


road1 = Road(20, 5000)
road2 = Road(5, 100)
road3 = Road(30, 7500)

print(road1.asphalt_mass_count())
print(road2.asphalt_mass_count())
print(road3.asphalt_mass_count())
