#49. Задано дві таблиці. Одна містить найменування послуг, а інша - розцінки
#за ці послуги. Видаліть з обох таблиць все, що передує послузі, ціна якої G гривень.

#Підготував Суханов Андрій Олександрович, 122Б.

import numpy as np
import random

while True:
    while True:
        try: #Перевірка на входження числа.
            G=int(input('Введіть якусь ціну: '))
        except ValueError:
                    print('Input numbers!! ')
                    break

        #Задаємо масиви товарів і генеруємо для них ціни.
        goods=np.array(['Морозиво', 'Хліб', 'Шоколад', 'Whiskey', 'Ковбаса'])
        price=np.array([random.randint(20,300) for i in range(5)])

        print('Товари: ', goods)
        print('Ціни: ', price)

        for i in range(len(goods)):
            for j in range(len(price)):
                if price[j]<G:
                    i=j #пов'язуємо їх індекси, щоб видалити товар і ціну, що \
                    #е задовільняє умові, тобто ціна більша, ніж G.
                    goods[i]='' #тут ми видаляємо.
                    price[j]=0
        print(goods)
        print(price)

        #Чи бажаєте повторити програму?
        result=input('Введіть "1", щоб продовжити, інше - для виходу: ')
        if result=='1':
            continue
        break
    break
