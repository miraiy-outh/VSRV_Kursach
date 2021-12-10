import random

from pastry.bun import *
from pastry.croissant import *
from pastry.donut import *
from pastry.konvertick import *
from pastry.pie import *
from pastry.sochnick import *
from pastry.vatrushka import *
from pastry.yazichok import *

from process import cleaning
from process.cleaning import *
from process.packaging import *
from process import packaging


def choose_dough():
    while True:
        transport()
        global pastry_count  # количество приготовленного товара каждого вида
        global product
        pastry_massive = ['bun', 'croissant', 'donut', 'konvertick', 'pie', 'sochnick', 'vatrushka', 'yazichok']

        # выбор изделия
        choice = pastry_massive[random.randint(0, len(pastry_massive) - 1)]
        if choice == 'bun':
            product = Bun()
        elif choice == 'croissant':
            product = Croissant()
        elif choice == 'donut':
            product = Donut()
        elif choice == 'konvertick':
            product = Konvertick()
        elif choice == 'pie':
            product = Pie()
        elif choice == 'sochnick':
            product = Sochnick()
            choice_fill = product.get_fill()[0]
        elif choice == 'vatrushka':
            product = Vatrushka()
            choice_fill = product.get_fill()[0]
        else:
            product = Yazichok()
            choice_fill = ''

        # определение начинки и ее приготовление
        choice_fill = random.randint(0, len(product.get_fill()) - 1)  # выбор рандомной начинки
        rand_fill = product.get_fill()[choice_fill]  # выбранная начинка
        if rand_fill != 'tvorog':
            if priemka.fr_b_name.count(rand_fill) == 1:  # если начинка фруктово-ягодная
                if cleaning.fr_b_massive_ready[priemka.fr_b_name.index(rand_fill)] >= 100:  # если начинки достаточно
                    cleaning.fr_b_massive_ready[priemka.fr_b_name.index(rand_fill)] -= 100
                    time.sleep(0.25)
            elif priemka.long_massive_priemka.count(rand_fill) == 1:  # если это долгохранящаяся начинка
                if priemka.long_name[priemka.long_massive_priemka.index(rand_fill)] >= 100:  # если начинки достаточно
                    priemka.long_name[priemka.long_massive_priemka.index(rand_fill)] -= 100
                    time.sleep(0.16)

        # определение вида теста
        if product.get_dough() == 'flaky':  # слоеное (45 минут)
            tmp = 0
            for i in range(0, len(priemka.dough_massive_priemka)):
                if i != 5 and priemka.dough_massive_priemka[i] < 1000:
                    tmp = 1
            if tmp == 0:
                for i in range(0, len(priemka.dough_massive_priemka)):
                    if i != 5:
                        priemka.dough_massive_priemka[i] -= 1000
                        time.sleep(0.25)  # замес (15 минут)
                        time.sleep(0.5)  # слоение (30 минут)
        elif product.get_dough() == 'yeast':  # дрожжевое (95 минут)
            tmp = 0
            for i in range(0, len(priemka.dough_massive_priemka)):
                if priemka.dough_massive_priemka[i] < 1000:
                    tmp = 1
            if tmp == 0:
                for i in range(0, len(priemka.dough_massive_priemka)):
                    priemka.dough_massive_priemka[i] -= 1000
                    time.sleep(0.083)  # замес опары (5 минут)
                    time.sleep(1)  # брожение опары (1 час)
                    time.sleep(0.5)  # замес теста (30 минут)
        elif product.get_dough() == 'flaky-yeast':  # слоено-дрожжевое (80 минут)
            tmp = 0
            for i in range(0, len(priemka.dough_massive_priemka)):
                if priemka.dough_massive_priemka[i] < 1000:
                    tmp = 1
            if tmp == 0:
                for i in range(0, len(priemka.dough_massive_priemka)):
                    priemka.dough_massive_priemka[i] -= 1000
                    time.sleep(0.083)  # замес опары (5 минут)
                    time.sleep(0.5)  # брожение опары (30 минут)
                    time.sleep(0.25)  # замес теста (15 минут)
                    time.sleep(0.5)  # слоение (30 минут)

        packaging.ready_product += 100
        tmp = choice + ' ' + product.get_fill()[choice_fill]
        packaging.product_name = [tmp]
