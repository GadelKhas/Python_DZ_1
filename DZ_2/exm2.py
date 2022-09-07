'''
Напишите программу, которая принимает на вход число N и выдает набор 
произведений чисел от 1 до N.

Пример:

- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
'''

import random
def nabor(x):
    if x == 1:
        return 1
    else:
        return x * nabor(x - 1)
N = random.randint(1,10) #Чисто для рандома
print(f'Рандомное значение {N} :')
list = []
for q in range(1, N + 1):
    list.append(nabor(q)) #Метод append() в Python добавляет элемент в конец списка
print(f'Набор произведений чисел от 1 до {N}:  {list}')



