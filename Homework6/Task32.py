# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

import random
a=int(input('Введите минимальное значение диапазона: '))
b=int(input('Введите максимальное значение диапазона: '))
length_massive=int(input('Введите длину массива:'))
my_list=[random.randint(-20,20) for _ in range(length_massive)]
print(my_list)
my_list_1=[]
for i in range(len(my_list)):
    if a <= my_list[i] <= b:
        
      