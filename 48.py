#48. Наведено список прізвищ брокерів товарної біржі з N чоловік. Поміняйте
#місцями прізвища брокерів: першого і останнього, другого і передостаннього, третього
#з початку і третього від кінця і т.д.

#Підготував Суханов Андрій, 122Б.

import numpy as np

while True:
    #Користувач вводить прізвище брокера:
    A=np.array([input('Введіть прізвище брокера: ') for i in range(6)])
    print('Прізвища брокерів: ', A)

    #За умовою задачі міняємо прізвище брокера перше на останнє, \
    #передостаннє на друге, у програмному вигляді - це функція reverse, \
    #а для масиву ми використовуємо зріз, який "перевертає" наш масив.
    H=A[::-1]
    print('Після зміни їх прізвищ список виглядає так: ', H)

    #Чи бажаєте повторити програму?
    result=input('Введіть "1", щоб продовжити, інше - для виходу: ')
    if result=='1':
        continue
    break

    

