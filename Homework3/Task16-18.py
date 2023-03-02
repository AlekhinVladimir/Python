# Первая задача:
# Задаем длину списка наполненного рандомными числами от 1 до 100.
# Вводим искомое число X
# Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
# которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению



import random
length_mass=int(input('Введите длину массива: '))
search_number=int(input('Введите искомое число: '))
my_list=[random.randint(1,100) for _ in range(length_mass)]
print(f'Массив: {my_list}')
if my_list.count(search_number)!=0:
    print(f'Искомое число {search_number} встречается {my_list.count(search_number)} раз.')
else:
     min_delta=my_list[0]
     for index in my_list:
          if abs(index-search_number)<abs(min_delta-search_number):
               min_delta=index
            #    search_number=my_list[index]
     print(f'Максимально близкое к искомому числу - число {min_delta} встречается {my_list.count(min_delta)} раз.')           

