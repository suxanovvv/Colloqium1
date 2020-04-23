#53. В масиві X (1: n) кожен елемент рівний 0, 1 або 5. Переставити елементи
#масиву так, щоб спочатку розташовувалися всі нулі, потім все одиниці, а потім всі
#п'ятірки. Додаткового масиву не заводити.

import numpy as np #Імпортуємо numpy.

while True:
    while True:
        try: #вибираємо розмір нашого масиву та перевірка, чи там число.
            n=int(input('Виберіть розмірність масиву не більшу, ніж 30: '))
        except ValueError:
                print('Input numbers!! ')
                break
            
        if n>30: #Масив повинен бути розміром не більше, ніж 30.
            print('Виберіть розмір масиву від 1 до 30!')
            break
        else:
            if 1>=n>=30:
                continue

        #Ініціалізуємо наш масив нулями.
        A=np.zeros(n, dtype=int)

        for i in range(len(A)):
            try: #Перевірка на входження чисел.
                #Заповнюємо масив числами.
                A[i] =int(input('Заповність масив лише 0, 1 або 5: '))
                if A[i]==1 or A[i]==5 or A[i]==0:
                    continue
                else:
                    print('Введіть лише числа 0, 1, 5!')
                    break
                    continue
            
            except ValueError:
                print('Input numbers!! ')
                break
        print('Ваш масив з 0,1 та 5: ', A)

        #Будемо сортувати наш масив методом selection sort.
        n=len(A)
        for i in range(n-1):
            min=i
            for j in range(i+1,n):
                if A[j]<A[min]:
                    min=j
            A[i], A[min]=A[min], A[i]
        print('Ваш масив відсортовано медотом selection sort: ', A)


        #Чи бажаєте повторити програму?
        result=input('Введіть "1", щоб продовжити, інше - для виходу: ')
        if result=='1':
            continue
        break
    break
