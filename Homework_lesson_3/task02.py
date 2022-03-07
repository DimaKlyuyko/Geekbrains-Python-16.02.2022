# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


# Surname специально не введен, чтобы проработать default значение аргумента

def user_info(name="empty",
              surname="empty",
              bd="empty",
              city="empty",
              email="empty",
              phone="empty"):
    print(f"Name = {name}. Surname = {surname}. Birthday = {bd}.\nCity = {city}. E-mail = {email}. Phone={phone}")


user_info(phone="1234567890", city="Paris", email="12345@mail.com", bd="10.10.2010", name="John")
