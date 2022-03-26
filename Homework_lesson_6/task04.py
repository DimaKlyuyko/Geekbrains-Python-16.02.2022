# 4. Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы:
# go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов, и также покажите результат.

class Car:
    speed: int
    color: str
    name: str
    is_police: bool = False

    def go(self):
        if self.is_police is False:
            x = "Гражданская машина"
        else:
            x = "Полицейская машина"

        return f"{x} {self.color} {self.name} поехала."

    def stop(self):
        if self.is_police is False:
            x = "Гражданская машина"
        else:
            x = "Полицейская машина"

        return f"{x} {self.color} {self.name} остановилась."

    def turn(self, direction: str):
        if self.is_police is False:
            x = "Гражданская машина"
        else:
            x = "Полицейская машина"

        return f"{x} {self.color} {self.name} повернула {direction}."

    def show_speed(self):
        return f"Текущая скорость {self.color} {self.name} = {self.speed} км/ч."


class TownCar(Car):
    def show_speed(self):  # переопределяю метод show_speed
        return f"Скорость {self.color} {self.name} = {self.speed} км/ч."

    def __init__(self, name, color, speed):
        self.name = name
        self.color = color
        self.speed = speed
        if self.speed <= 60:
            print(f"Машина класса TownCar создана.")
        else:
            x = self.speed - 60
            print(f"Машина класса TownCar создана, однако, вы превысили скорость на {x} км/ч")


class SportCar(Car):
    def __init__(self, name, color, speed):
        self.name = name
        self.color = color
        self.speed = speed
        print(f"Машина класса SportCar создана.")


class WorkCar(Car):
    def show_speed(self):  # переопределяю метод show_speed
        return f"Скорость {self.color} {self.name} = {self.speed} км/ч."

    def __init__(self, name, color, speed):
        self.name = name
        self.color = color
        self.speed = speed
        if self.speed <= 40:
            print(f"Машина класса WorkCar создана.")
        else:
            x = self.speed - 40
            print(f"Машина класса WorkCar создана, однако, вы превысили скорость на {x} км/ч.")


class PoliceCar(Car):
    def __init__(self, name, color, speed):  # переопределяю конструктор, для присвоения статуса "Полицейская"
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = True
        print(f"Машина класса PoliceCar создана.")


print("Создание экземпляров разных классов и передача атрибутов:")
car_1 = TownCar("Kia", "White", 40)
car_2 = SportCar("lamborghini", "Red", 200)
car_3 = WorkCar("BMW", "Black", 70)
car_4 = PoliceCar("Opel", "Green", 90)

print("\nАтрибуты экземпляров:")
print(car_1.name, car_1.color, car_1.speed, car_1.is_police, type(car_1))
print(car_2.name, car_2.color, car_2.speed, car_2.is_police, type(car_2))
print(car_3.name, car_3.color, car_3.speed, car_3.is_police, type(car_3))
print(car_4.name, car_4.color, car_4.speed, car_4.is_police, type(car_4))

print("\nВызов методов:")
print(car_1.go())
print(car_2.show_speed())
print(car_3.stop())
print(car_4.turn("направо"))
