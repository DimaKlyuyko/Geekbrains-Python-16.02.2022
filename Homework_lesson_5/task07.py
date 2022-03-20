# 7. Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.

# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:

# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

# мой файл
# firm_1 001 10000 5000
# firm_2 002 14000 4000
# firm_3 002 12000 13000
# firm_4 002 25000 15000
# firm_5 003 5000 2000

import json

my_list = []
my_dict = {}
avg_dict = {}

with open('for_task_07.txt') as stream1:
    for line in stream1.readlines():
        temp_list = line.replace('\n', '').split()
        profit = int(temp_list[2]) - int(temp_list[3])
        my_dict[temp_list[0]] = profit

    my_list.append(my_dict)

    list_of_positive_profits = [x for x in my_dict.values() if x > 0]

    average_profit = round(
        sum(list_of_positive_profits) / len(list_of_positive_profits)
    )

    avg_dict["average_profit"] = average_profit

    my_list.append(avg_dict)

with open('json_task_07.json', 'w') as stream2:
    json.dump(my_list, stream2)
