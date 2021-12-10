import time
from process.cooking import *
from process.expedition import *
from window import *


# вывод количества продуктов на разных этапах приготовления
def printing():
    while True:
        time.sleep(0.16)
        printed_info = f'''
        Приемка: сырье для теста:
        {priemka.dough_name}
        {priemka.dough_massive_priemka}

        Приемка: фруктово-ягодная начинка:
        {priemka.fr_b_name}
        {priemka.fr_b_massive_priemka}

        Приемка: долгохранящаяся начинка:
        {priemka.long_name}
        {priemka.long_massive_priemka}

        Очистка:
        {priemka.fr_b_name}
        {cleaning.fr_b_massive_ready}

        Готовых к отправке изделий: {packaging.ready_product}

        К экспедиции готовы: 
        {expedition.expedition_massive}
        '''
        clear()
        ins(printed_info)
