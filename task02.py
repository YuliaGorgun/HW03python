# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]


my_list = [2, 3, 4, 5, 6]
new_list = []
print(my_list)
el = len(my_list)//2 + 1 if len(my_list) % 2 != 0 else len(my_list)//2
new_list = [my_list[i]*my_list[len(my_list)-i-1] for i in range(el)]
print(new_list)

