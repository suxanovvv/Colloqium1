#37. Розсортуйте заданий лінійний масив по зростанню.

#Підготував Суханов Андрій Олександрович, 122Б.

import numpy as np #Імпортуємо numpy.

while True:
    while True:
        #Ініціалізуємо масив нулями.
        A=np.zeros(8, dtype=int)

        for i in range(len(A)): #Отримуємо доступ до елементів матриці А.
            try: #Перевірка на входження чисел.
                A[i] =int(input('Введіть елементи масиву: '))
                continue
            except ValueError:
                print('Input numbers!! ')
                break

        print('Ваш масив: ', A)
        print()

        #Використаємо бульбашкове сортування.
        n=len(A)
        count=0
        exchange=0
        for i in range(1,n):
            for j in range(n-1, i-1, -1):
                count+=1
                if (A[j-1]>A[j]):
                    exchange+=1
                    A[j], A[j-1]=A[j-1], A[j]
        print('Ваш масив відсортовано: ', A)

        print('Під час бульбашкового сортування відбулось кількість \
обмінів елементів: ', exchange)
        print('Під час бульбашкового сортування відбулось кількість \
порівнянь: ', count)

        #Чи бажаєте повторити програму?
        result=input('Введіть "1", щоб продовжити, інше - для виходу: ')
        if result=='1':
            continue
        break
    break
