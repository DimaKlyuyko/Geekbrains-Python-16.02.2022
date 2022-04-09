"""
4.
Начните работу над проектом «Склад оргтехники».
Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

5.
Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру, например словарь.

6.
Продолжить работу над вторым заданием.
Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.
"""


# Исключение не дающее разместить на складе больше техники, чем доступно
class StoreException(Exception):
    def __init__(self, free_space, needle):
        self.free_space = free_space
        self.needle = needle

    def __str__(self):
        return f"Current free space = {self.free_space}. Needle free space = {self.needle}."


class Warehouse:
    capacity: int
    location: str
    storage: list

    def __init__(self, loc, cap=10):
        self.location = loc
        self.capacity = cap
        self.storage = []

    # Метод, отвечающий за приём оргтехники на склад. Указываем, какую технику и в каком количестве принять
    def store(self, office_equipment_type, arg_for_type, count):
        if isinstance(count, int):  # валидация, чтобы count было целым числом
            if self.capacity - len(self.storage) >= count:
                for i in range(count):
                    self.storage.append(office_equipment_type(arg_for_type))
            else:
                raise StoreException((self.capacity - len(self.storage)), count)
        else:
            print("Количество техники указано как строка, а не как число.")

    def shipment(self, obj, departament, count):
        z = 0
        for i in self.storage:
            if z < count:
                if type(i) == obj:
                    departament.office_storage.append(i)
                    z += 1
                else:
                    continue
            else:
                break

        for item in dep1.office_storage:
            self.storage.remove(item)


class OfficeEquipment:
    brand: str = "Epson"
    guarantee_period: int = 3


class Printer(OfficeEquipment):
    ptype: int

    def __init__(self, ptype: int):
        self.ptype = ptype


class Scanner(OfficeEquipment):
    color: str

    def __init__(self, color: str):
        self.color = color


class Xerox(OfficeEquipment):
    xerox_speed: int

    def __init__(self, speed: int):
        self.xerox_speed = speed


class Departament:
    def __init__(self, city):
        self.city = city
        self.office_storage = []


# создание склада
wh1 = Warehouse("Los Angeles")

# приём разной техники на склад
wh1.store(Scanner, "white", 4)
wh1.store(Xerox, 16, 3)
wh1.store(Printer, 1, 2)
wh1.store(Printer, 1, "Special for validation.")

# wh1.store(Printer, 1, 2) - Выдаст исключение "__main__.StoreException: Current free space = 1. Needle free space = 2."

# проверка текущего количества техники на складе
print(len(wh1.storage))

# какая техника находится на складе
print(wh1.storage)

# создание подразделения
dep1 = Departament("Miami")

# передача техники на офис (подразделение)
# указываем тип техники, какой офис и сколько
wh1.shipment(Scanner, dep1, 2)

# смотрим какая техника сейчас находится на офисе
print(dep1.office_storage)

# смотрим теперь остаток на складе, после переноса техники на офис
print(len(wh1.storage))
print(wh1.storage)
