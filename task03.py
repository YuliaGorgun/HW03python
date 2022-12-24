# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random
my_list = []
for _ in range(5):
    amount = random. randint(0,2)
    my_list.append(round(random.uniform(1,10), amount))
print(my_list)
new_list = []
new_list = [round(i % 1,2) for i in my_list if i % 1 != 0]
print(f"Разница между максимальным и минимальным значением дробной части элементов: {max(new_list) - min(new_list)}")

