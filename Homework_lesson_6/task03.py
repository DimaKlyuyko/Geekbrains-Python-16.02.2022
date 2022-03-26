# 3. Реализовать базовый класс Worker (работник),
# в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например,
# {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы:
# получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    name: str
    surname: str
    position: str

    income_dict = {"wage": 800, "bonus": 400}
    _income = income_dict


class Position(Worker):
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return self._income.get("wage") + self._income.get("bonus")


worker1 = Position("John", "Doe", "director")
worker2 = Position("Artur", "Pringles", "accountant")

print("Проверка значений атрибутов:")
print(worker1.name, worker1.surname, worker1.position, worker1.income_dict)

print("\nВызов методов экземпляра:")
print(worker2.get_full_name())
print(worker2.get_total_income())
