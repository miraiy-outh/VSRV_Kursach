import time

expedition_product = 0
expedition_massive = []


def expedition_products():
    print('--------------------expedition-----------------------')
    global expedition_product
    global expedition_massive
    if expedition_product >= 1000:
        print('Следующие продукты отправлены:\n')
        for i in range(0, len(expedition_massive)):
            print(expedition_massive[i], '\n')
        expedition_massive = []
        expedition_product -= 1000
        print('------------------------------------------------')
        time.sleep(60)