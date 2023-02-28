# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

import random
n_coins = int(input('Введите количество монет: '))
count_zero = 0
count_one = 0
for i in range(n_coins):
    side_coins = random.randint(0, 1)
    print(f'Сторона {i+1} монеты = {side_coins}')
    if side_coins == 0:
        count_zero += 1
    else:
        count_one += 1
if count_one > count_zero:
    print(f'Мин переворотов монеты: {count_zero}')
else:
    print(f'Мин переворотов монеты: {count_one}')
