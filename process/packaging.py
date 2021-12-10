import time
from process import expedition
from process.transporting import *

ready_product = 0
product_name = ''


# упаковка партии длится 5 минут
def packaging_products():
    while True:
        global ready_product
        global product_name
        if ready_product >= 100:
            time.sleep(0.083)
            ready_product -= 100
            transport()
            expedition.expedition_product += 100
            expedition.expedition_massive.append(product_name)