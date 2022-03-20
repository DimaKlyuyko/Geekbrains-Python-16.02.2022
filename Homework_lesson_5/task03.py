# 3. Создать текстовый файл (не программно),
# построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

# мой файл
# Ivanov 100
# Petrov 550
# Korshumov 300
# Pushkin 400
# Esenin 250
# Dostoevskiy 350
# Gogol 150
# Vetrov 450
# Turgenev 500
# Chechov 200

with open('for_task_03.txt') as stream:
    my_dict = {}
    for line in stream.readlines():
        temp_list = line.replace('\n', '').split()
        my_dict[temp_list[0]] = int(temp_list[1])

    average_salary = round(sum(my_dict.values()) / len(my_dict.values()))
    print("Средняя заработная плата =", average_salary, '\n')

    print("Фамилии сотрудников с ЗП ниже среднего (полученного шагом ранее):")
    for surname in my_dict.keys():
        if my_dict.get(surname) < average_salary:
            print(surname)
