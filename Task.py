import random
length_mass=int(input('Введите длину массива: '))
search_number=int(input('Введите искомое число: '))
my_list=[random.randint(1,20) for _ in range(length_mass)]
print(f'Массив: {my_list}')
min_delta=max(my_list)
for index in range(length_mass):
    if abs(search_number-my_list[index])<min_delta:
               min_delta=abs(search_number-my_list[index])
               search_number=my_list[index]
print(f'Максимально близкое к искомому числу - число {min_delta} встречается {my_list.count(search_number)} раз.')           
