# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

# мой список
# Ship
# House
# Sky and stars
# Mineral water

with open('for_task_02.txt') as stream:
    print("Количество строк = ", len(stream.readlines()))
    stream.seek(0)

    for count, line in enumerate(stream.readlines(), start=1):
        x = int(line.count(' ')) + 1
        print(f"Строка {count}. Количество слов = ", x)
