#35. Дан лінійний масив цілих чисел. Перевірте, чи є він упорядкованим по
#спаданню.

#Підготував Суханов Андрій Олександрович, 122Б.

import numpy as np

while True:
    while True:
        #Ініціалізуємо масив нулями.
        A=np.zeros(10, dtype=int)


        flag=False
        for i in range(len(A)):
            try: #Перевірка на входження чисел.
                A[i]=int(input('Введіть елемент масиву: '))
                continue
            except ValueError:
                print('Input numbers!! ')
                break

        B=sorted(A)[::-1] #Відсортуємо масив А за спаданням i будемо \
        #порівнювати його елeменти з відортованим масивом B.
        for j in range(len(B)):
            if A[i]==B[j]:
                flag=True
            else:
                if A[i]!=B[j]:
                    flag=False

        if not flag:
            print('Ваш масив не відсортований за спаданням. Відсортуймо його!')
            A=B #Якщо масив не відсортований, то відсортуймо його!
            print('Результат сортування: ', A)
        else:
            print('Ваш масив і так відсортований.')

        #Чи бажаєте повторити програму?
        result=input('Введіть "1", щоб продовжити, інше - для виходу: ')
        if result=='1':
            continue
        break
    break
