#Дані про направлення вітру (північний, південний, західний, східний) і сили
#вітру за декаду листопада зберігаються в масиві. Визначити, скільки днів дув
#південний вітер з силою, що перевищує 8 м/c.

#Підготував Суханов Андрій Олександрович студент 1-го курсу групи 122Б.

import numpy as np #імпортуємо numpy, random.
import random

while True:
    #Генеруємо вітер для чотирьох напрямків світу.
    A=np.array([random.randint(5,10) for i in range(10)])
    B=np.array([random.randint(5,12) for i in range(10)])           
    C=np.array([random.randint(3,9) for i in range(10)])
    D=np.array([random.randint(7,15) for i in range(10)])

    print('Північний вітер: ', A)
    print('Південний вітер: ', B)
    print('Західний вітер: ', C)
    print('Східний вітер: ', D)
    print()

    count=0
    for i in range(len(A)): #Отримуємо доступ до кожного елементу масиву.
        if A[i]>8: #Якщо сила вітру більше 8м/c, то ми враховуємо\
            count+=1 #у count та виводимо його.
    print(f'Північний вітер дув з силою більше, ніж 8 м/c {count} днів.')

    count1=0
    #Аналогічно і з іншими блоками коду.
    for i in range(len(B)):
        if B[i]>8:
            count1+=1
    print(f'Південний вітер дув з силою більше, ніж 8 м/c {count1} днів.')

    count2=0
    for i in range(len(C)):
        if C[i]>8:
            count2+=1
    print(f'Західний вітер дув з силою більше, ніж 8 м/c {count2} днів.')

    count3=0
    for i in range(len(D)):
        if D[i]>8:
            count3+=1
    print(f'Східний вітер дув з силою більше, ніж 8 м/c {count3} днів.')

    #Чи бажаєте повторити програму?
    result=input('Введіть "1", щоб продовжити, інше - для виходу: ')
    if result=='1':
        continue
    break

