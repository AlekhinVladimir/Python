# Задача 26: Напишите программу, которая на вход принимает 
# два числа A и B, и возводит число А в целую степень B с 
# помощью рекурсии
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

a=int(input('Введите число А: '))
b=int(input('Введите число B: '))
def degr(a,b):
    if (b==1):
        return (a)
    else:
        return(a*degr(a,b-1))
# print(degr(a,b))   
print(f'Результат возведения числа {a} в степень {b} равен {degr(a,b)}.')