#33. Заданий масив А (1:20). Знайти добуток всіх його ненульових елементів.

#Підготував Суханов Андрій Олександрович, 122Б.

import numpy as np #Імпортуємо numpy, random.
import random

while True:
    #Генеруємо масив рандомними числами:
    A=np.array([random.randint(-3,3) for i in range(1,20)])

    print('Масив: ', A)

    multiply=1
    for i in range(len(A)): #Отримаємо доступ до елементів масиву.
        if A[i]!=0: #Якщо елемент ненулевий, то примножимо його у multiply.
            multiply*=A[i]
    print('Добуток усіх ненульових елементів: ', multiply)

    #Чи бажаєте повторити програму?
    result=input('Введіть "1", щоб продовжити, інше - для виходу: ')
    if result=='1':
        continue
    break
        
