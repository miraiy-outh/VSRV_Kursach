import time

fr_b_name = ['apple', 'raspberry', 'strawberry', 'lemon', 'cherry', 'peach', 'berries']
long_name = ['chocolate', 'creme', 'caramel', 'poppy', 'cinnamon', 'vanilla']
dough_name = ['flour', 'sugar', 'milk', 'water', 'egg', 'yeast']

flour = 0
sugar = 0
milk = 0
water = 0
egg = 0
yeast = 0

apple = 0
raspberry = 0
strawberry = 0
lemon = 0
cherry = 0
peach = 0
berries = 0
tvorog = 0

chocolate = 0
creme = 0
caramel = 0
poppy = 0
cinnamon = 0
vanilla = 0

dough_massive_priemka = [0] * 6
fr_b_massive_priemka = [0] * 7
long_massive_priemka = [0] * 6


# продукты для теста - для 1 партии используется 1000 ед. сырья; поставляется раз в 24 часа
def priemka_dough():
    while True:
        global flour
        global sugar
        global milk
        global water
        global egg
        global yeast

        flour += 5000
        sugar += 5000
        milk += 5000
        water += 5000
        egg += 5000
        yeast += 5000

        # сколько на данный момент поставлено сырья для теста
        global dough_massive_priemka
        dough_massive_priemka = [flour, sugar, milk, water, egg, yeast]
        time.sleep(24)


# фруктово-ягодная (+ творог) начинка - для 1 партии используется 100 ед. сырья
# скоропортящаяся, поэтому поставляется маленькими партиями раз в 2 часа
def priemka_fr_b():
    while True:
        global apple
        global raspberry
        global strawberry
        global lemon
        global cherry
        global peach
        global berries
        global tvorog

        if apple <= 150: apple += 50
        if raspberry <= 150: raspberry += 50
        if strawberry <= 150: strawberry += 50
        if lemon <= 150: lemon += 50
        if cherry <= 150: cherry += 50
        if peach <= 150: peach += 50
        if berries <= 150: berries += 50
        if tvorog <= 150: tvorog += 50

        # сколько на данный момент поставлено фруктов и ягод
        global fr_b_massive_priemka
        fr_b_massive_priemka = [apple, raspberry, strawberry, lemon, cherry, peach, berries, tvorog]
        time.sleep(2)


# долгохранящаяся начинка - для 1 партии используется 100 ед. сырья; поставляется раз в 12 часов
def priemka_fill_long():
    while True:
        global chocolate
        global creme
        global caramel
        global poppy
        global cinnamon
        global vanilla
        if chocolate <= 50: chocolate += 250
        if creme <= 50: creme += 250
        if caramel <= 50: caramel += 250
        if poppy <= 50: poppy += 250
        if cinnamon <= 50: cinnamon += 250
        if vanilla <= 50: vanilla += 250

        # сколько на данный момент поставлено долгохр. начинок
        global long_massive_priemka
        long_massive_priemka = [chocolate, creme, caramel, poppy, cinnamon, vanilla]
        time.sleep(12)
