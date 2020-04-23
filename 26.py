#26. Напишіть програму аналізу значень температури хворого за добу:
#визначте мінімальне і максимальне значення, середнє арифметичне. Заміри
#температури виробляються шість раз на добу і результати вводяться з клавіатури у
#масив T.

#Підготував Суханов Андрій Олександрович, 122Б.

import numpy as np #імпортуємо numpy.

while True:
    while True:
        #Ініціалізуємо масив нулями.
        T=np.zeros(6, dtype=float)

        for i in range(len(T)):
            try: #Вводимо елементи масиву та перевіряємо їх на наявність числа.
                T[i]=float(input(f'Введіть результат вимірювання \
температури хворого, {i+1}-ий вимір: '))
                continue
            except ValueError:
                print('Input numbers!! ')
                break

        print()
        print('Температура хворого: ', T)


        #Знаходимо усі необхідні значення.
        T_max=max(T)
        T_min=min(T)
        T_aver=np.mean(T)


        #Виводимо ці значення.
        print('Мінімальна температура хворого за добу: ', T_min)
        print('Максимальна температура хворого за добу: ', T_max)
        print('Середнє значення температури хворого за добу: ', T_aver)


        #Чи бажаєте повторити програму?
        result=input('Введіть "1", щоб продовжити, інше - для виходу: ')
        if result=='1':
            continue
        break
    break
    
