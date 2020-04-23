#41. Змінній t привласнити значення істина, якщо максимальний елемент
#одновимірного масиву єдиний і не перевищує наперед заданого числа а.

#Підготував Суханов Андрій Олександрович, 122Б

import numpy as np #Імпортуємо numpy.

while True:
    while True:
        #Користувач вводить "задане число".
        try:
            a=int(input('Задайте будь-яке число: '))
        except ValueError:
            print('Input numbers!! ')
            break

        print()
        #Ініціалізуємо масив нулями.
        A=np.zeros(8, dtype=int)

        t=False #Змінній t поки привласнимо значення False.
        count=0
        for i in range(len(A)): #Отримуємо доступ до елементів матриці А.
            try: #Перевірка на входження чисел.
                A[i] =int(input('Введіть елементи масиву: '))
                continue
            except ValueError:
                print('Input numbers!! ')
                break

        A_max=max(A) #Знайдемо максимальне значення масиву.
            
        if A[i]==A_max:
            count+=1 #Перевірка чи єдиний цей максимальний елемент у масиві.
        if A_max<a and count==1:
            t=True #Якщо все так, то t=True.
        print(f't={t}')


        #Чи бажаєте повторити програму?
        result=input('Введіть "1", щоб продовжити, інше - для виходу: ')
        if result=='1':
            continue
        break
    break



