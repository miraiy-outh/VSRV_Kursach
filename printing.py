import time
from process.cooking import *

#вывод количества продуктов на разных этапах приготовления
def printing():
    time.sleep(10)

    print('Приемка: сырье для теста:')
    print(priemka.dough_name)
    print(priemka.dough_massive_priemka)
    print('Приемка: фруктово-ягодная начинка:')
    print(priemka.fr_b_name)
    print(priemka.fr_b_massive_priemka)
    print('Приемка: долгохранящаяся начинка:')
    print(priemka.long_name)
    print(priemka.long_massive_priemka)

    print('Очистка:')
    print(priemka.fr_b_name)
    print(cleaning.fr_b_massive_ready)

    print('Готовых к отправке изделий:', packaging.ready_product)
    print('-------------------------------------------------------')

