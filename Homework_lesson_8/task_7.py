"""
7. Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.

Проверьте работу проекта, создав экземпляры класса (комплексные числа) и
выполнив сложение и умножение созданных экземпляров.

Проверьте корректность полученного результата.
"""


class ComplexNumber:
    a: int
    b: int
    z: str

    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b
        if b > 0:
            self.z = f"{a}+{b}i"
        else:
            self.z = f"{a}{b}i"

    def __str__(self):
        return self.z

    def __add__(self, other):
        return ComplexNumber(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return ComplexNumber(self.a * other.a, self.b * other.b)


number1 = ComplexNumber(3, -4)
number2 = ComplexNumber(-5, 12)
print(number1)
print(number2)

print(number1 + number2)
print(number1 * number2)
