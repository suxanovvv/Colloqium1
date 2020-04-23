#21. Знайти добуток всіх елементів масиву дійсних чисел, менших заданого
#числа. Розмірність масиву - 10. Заповнення масиву здійснити випадковими числами
#від 50 до 100.

#Підготував Суханов Андрій Олександрович, 122Б.

import numpy as np #імпортуємо numpy.
import random

while True:
    while True:
        #Генеруємо масив дійсними числами.
        A=np.array([random.uniform(50,100) for i in range(10)])
        print('Масив: ', A) #Виведемо масив на екран.
        print()

        try: #Введемо "задане число" та перевіримо, чи користувач ввів дійсно число.
            n=int(input('Задайте будь-яке ціле число більше 50: '))
        except ValueError:
            print('Input numbers!! ')
            break

        count=1 #лічильник буде - 1, щоб отримувати добуток чисел.
        for i in range(len(A)):
            if A[i]<n: #Якщо елемент менше, ніж "задане число", то:
                count*=A[i] #Множмо у count ей елемент.

        print(f'Знайдемо добуток чисел, менших від {n}.')
        #Якщо count==1, то чисел, що менші, ніж "задане число" не зустрілось.
        if count==1:
            print(f'Немає чисел у масиві, менших, ніж {n}.')
        else:
            print(f'Добуток чисел, які менші, ніж {n} буде {count}.')


        #Чи бажаєте повторити програму?
        result=input('Введіть "1", щоб продовжити, інше - для виходу: ')
        if result=='1':
            continue
        break
    break

