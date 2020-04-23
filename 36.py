#36. Знайти суму додатніх елементів лінійного масиву цілих чисел.
#Розмірність масиву - 10. Заповнення масиву здійснити з клавіатури.

#Підготував Суханов Андрій Олександрович, 122Б.

import numpy as np #Імпортуємо numpy.

while True:
    while True:
        A=np.zeros(10, dtype=int)

        count=0
        for i in range(len(A)): #Отримуємо доступ до елементів матриці А.
            try: #Перевірка на входження чисел.
                A[i] =int(input('Введіть елементи масиву: '))
                continue
            except ValueError:
                print('Input numbers!! ')
                break
        
        for i in range(len(A)):
            if A[i]>0:
                count+=A[i]
                
        if count==0:
            print('У масиві немає додатніх елементів або вони нулеві.')

        else:
            print('Сума додатніх елементів масиву: ', count)

        #Чи бажаєте повторити програму?
        result=input('Введіть "1", щоб продовжити, інше - для виходу: ')
        if result=='1':
            continue
        break
    break

        
