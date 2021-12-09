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

# всего на приготовление слоеного теста уходит 45 секунд
def cooking_flaky():
    print('----------------cooking_flaky-------------------')
    tmp = 0

    for i in range(0, len(priemka.dough_massive_priemka)):
        if i != 5 and priemka.dough_massive_priemka[i] < 1000:
            tmp = 1
    if tmp == 0:
        for i in range(0, len(priemka.dough_massive_priemka)):
            if i != 5:
                priemka.dough_massive_priemka[i] -= 1000;
                time.sleep(1)  # замес
                time.sleep(1)  # слоение


# всего на приготовление дрожжевого теста уходит 95 секунд
def cooking_yeast():
    print('---------------cooking_yeast----------------')
    tmp = 0

    for i in range(0, len(priemka.dough_massive_priemka)):
        if priemka.dough_massive_priemka[i] < 1000:
            tmp = 1
    if tmp == 0:
        for i in range(0, len(priemka.dough_massive_priemka)):
            priemka.dough_massive_priemka[i] -= 1000;
            time.sleep(1)  # замес опары
            time.sleep(1)  # брожение опары
            time.sleep(1)  # замес теста


# всего на приготовление слоено-дрожжевого теста уходит 80 секунд
def cooking_flaky_yeast():
    print('---------------cooking_flaky_yeast----------------')
    tmp = 0

    for i in range(0, len(priemka.dough_massive_priemka)):
        if priemka.dough_massive_priemka[i] < 1000:
            tmp = 1
    if tmp == 0:
        for i in range(0, len(priemka.dough_massive_priemka)):
            priemka.dough_massive_priemka[i] -= 1000;
            time.sleep(1)  # замес опары
            time.sleep(1)  # брожение опары
            time.sleep(1)  # замес теста
            time.sleep(1)  # слоение



def choose_dough():
    transport()
    print('------------------choose_dough---------------------')
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
    print('-----------------------choose_fill----------------------')
    choice_fill = random.randint(0, len(product.get_fill()) - 1)
    if priemka.fr_b_name.count(product.get_fill()[choice_fill]) == 1:
        if cleaning.fr_b_massive_ready[priemka.fr_b_name.index(product.get_fill()[choice_fill])] >= 100:
            cleaning.fr_b_massive_ready[priemka.fr_b_name.index(product.get_fill()[choice_fill])] -= 100
            time.sleep(15)
    elif priemka.long_massive_priemka.count(product.get_fill()[choice_fill]) == 1:
        if priemka.long_name[priemka.long_massive_priemka.index(product.get_fill()[choice_fill])] >= 100:
            priemka.long_name[priemka.long_massive_priemka.index(product.get_fill()[choice_fill])] -= 100
            time.sleep(10)

    # определение вида теста
    if product.get_dough() == 'flaky':
        cooking_flaky()
    elif product.get_dough() == 'yeast':
        cooking_yeast()
    elif product.get_dough() == 'flaky-yeast':
        cooking_flaky_yeast()

    packaging.ready_product += 100
    tmp = choice + product.get_fill()[choice_fill]
    print(f'-------------------{tmp}--------------------')
    packaging.product_name = [tmp]