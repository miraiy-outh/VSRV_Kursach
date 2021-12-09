import random

from pastry.bun import *
from pastry.croissant import *
from pastry.donat import *
from pastry.konvertick import *
from pastry.pie import *
from pastry.sochnick import *
from pastry.vatrushka import *
from pastry.yazichok import *

from process.priemka import *
from process.transporting import *
from process.cleaning import *
from process.packaging import *

# всего на приготовление слоеного теста уходит 45 секунд
def cooking_flaky():
    global dough_massive_priemka
    tmp = 0

    for i in range(0, len(dough_massive_priemka)):
        if i != 5 and dough_massive_priemka[i] < 1000:
            tmp = 1
    if tmp == 0:
        for i in range(0, len(dough_massive_priemka)):
            if i != 5:
                dough_massive_priemka[i] -= 1000;
                time.sleep(15)  # замес
                time.sleep(30)  # слоение


# всего на приготовление дрожжевого теста уходит 95 секунд
def cooking_yeast():
    global dough_massive_priemka
    tmp = 0

    for i in range(0, len(dough_massive_priemka)):
        if dough_massive_priemka[i] < 1000:
            tmp = 1
    if tmp == 0:
        for i in range(0, len(dough_massive_priemka)):
            dough_massive_priemka[i] -= 1000;
            time.sleep(5)  # замес опары
            time.sleep(60)  # брожение опары
            time.sleep(30)  # замес теста


# всего на приготовление слоено-дрожжевого теста уходит 80 секунд
def cooking_flaky_yeast():
    global dough_massive_priemka
    tmp = 0

    for i in range(0, len(dough_massive_priemka)):
        if dough_massive_priemka[i] < 1000:
            tmp = 1
    if tmp == 0:
        for i in range(0, len(dough_massive_priemka)):
            dough_massive_priemka[i] -= 1000;
            time.sleep(5)  # замес опары
            time.sleep(30)  # брожение опары
            time.sleep(15)  # замес теста
            time.sleep(30)  # слоение


def choose_dough():
    transporting()
    global ready_product
    global product_name
    global pastry_count  # количество приготовленного товара каждого вида
    global fr_b_massive_ready
    global fr_b_name
    global long_name
    pastry_massive = ['bun', 'croissant', 'donut', 'konvertick', 'pie', 'sochnick', 'vatrushka', 'yazichok']

    # выбор изделия
    choice = random.randint(0, len(pastry_massive) - 1)
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
    elif choice == 'vatrushka':
        product = Vatrushka()
    elif choice == 'yazichok':
        product = Yazichok()
    else:
        pass

    # определение начинки и ее приготовление
    choice_fill = random.randint(0, len(product.get_fill()) - 1)
    if fr_b_name.find(product.get_fill()[choice_fill]) != -1:
        if fr_b_massive_ready[fr_b_name.find(product.get_fill()[choice_fill])] >= 100:
            fr_b_massive_ready[fr_b_name.find(product.get_fill()[choice_fill])] -= 100
            time.sleep(15)
    if long_name.find(product.get_fill()[choice_fill]) != -1:
        if long_name[long_name.find(product.get_fill()[choice_fill])] >= 100:
            long_name[long_name.find(product.get_fill()[choice_fill])] -= 100
            time.sleep(10)

    # определение вида теста
    if product.get_dough() == 'flaky':
        cooking_flaky()
    elif product.get_dough() == 'yeast':
        cooking_yeast()
    elif product.get_dough() == 'flaky-yeast':
        cooking_flaky_yeast()
    ready_product += 100
    product_name = [product.get_dough() + '' + product.get_fill()[choice_fill]]