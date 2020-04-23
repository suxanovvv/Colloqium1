#43. Задано два натуральних числа a і b. Змінній w привласнити значення
#істина, якщо в одновимірному цілочисельному масиві є хоча б один елемент, кратний а
#і не кратний b.

#Підготував Суханов Андрій Олександрович, 122Б.

import numpy as np #Імпортуємо numpy, random.
import random

while True:
    while True:
        #Користувач вводить "задані числа".
        try:
            a,b=int(input('Введіть число а: ')), int(input('Введіть число b: '))
        except ValueError:
            print('Input numbers!! ')
            break
    
        #Генеруємо масив випадковими числами.
        A=np.array([random.randint(3,20) for i in range(15)])
        print('Масив: ', A)

        w=False #змінній w привласнимо значення False.
        for i in range(len(A)): #Отримуємо доступ до елементів матриці А.
            if A[i]%a==0 and A[i]%b!=0: 
                w=True #Якщо умова стверджується, то w=True
        print(f'w={w}')

        #Чи бажаєте повторити програму?
        result=input('Введіть "1", щоб продовжити, інше - для виходу: ')
        if result=='1':
            continue
        break
    break
    
