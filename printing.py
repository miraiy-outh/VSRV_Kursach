import time
from process.cooking import *

#вывод количества продуктов на разных этапах приготовления
def printing():
    global dough_name
    global dough_massive_priemka
    global fr_b_massive_priemka
    global long_massive_priemka

    print('Приемка: сырье для теста:\n')
    print(dough_name, '\n')
    print(dough_massive_priemka, '\n')
    print('Приемка: фруктово-ягодная начинка:\n')
    print(fr_b_name, '\n')
    print(fr_b_massive_priemka, '\n')
    print('Приемка: долгохранящаяся начинка:\n')
    print(long_name, '\n')
    print(long_massive_priemka, '\n')

    global fr_b_massive_ready

    print('Очистка:')
    print(fr_b_name, '\n')
    print(fr_b_massive_ready, '\n')

    global ready_product
    print('Готовых к отправке изделий:', ready_product, '\n')

    time.sleep(10)

