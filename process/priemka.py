# продукты для теста - для 1 партии используется 1000 ед. сырья; задержка - 60 сек.
def priemka_dough():
    global flour
    global sugar
    global milk
    global water
    global egg
    global yeast

    flour += 2000
    sugar += 2000
    milk += 2000
    water += 2000
    egg += 2000
    yeast += 2000

    # сколько на данный момент поставлено сырья для теста
    global dough_massive_priemka
    dough_massive_priemka = [flour, sugar, milk, water, egg, yeast]


# фруктово-ягодная начинка - для 1 партии используется 50 ед. сырья
# скоропортящаяся, поэтому поставляется маленькими партиями и чаще (10 сек), чем другое сырье
def priemka_fill_fr_b():
    global apple
    global raspberry
    global strawberry
    global lemon
    global cherry
    global peach
    global berries

    apple += 100
    raspberry += 100
    strawberry += 100
    lemon += 100
    cherry += 100
    peach += 100
    berries += 100

    # сколько на данный момент поставлено фруктов и ягод
    global fr_b_massive_priemka
    fr_b_massive_priemka = [apple, raspberry, strawberry, lemon, cherry, peach, berries]


# долгохранящаяся начинка - для 1 партии используется 50 ед. сырья; поставляется часто (30 сек)
def priemka_fill_long():
    global chocolate
    global creme
    global caramel
    global poppy
    global cinnamon
    global vanilla
    chocolate += 200
    creme += 200
    caramel += 200
    poppy += 200
    cinnamon += 200
    vanilla += 200

    # сколько на данный момент поставлено долгохр. начинок
    global long_massive_priemka
    long_massive_priemka = [chocolate, creme, caramel, poppy, cinnamon, vanilla]