import time
from process import expedition
from process.transporting import *

ready_product = 0
product_name = ''


# упаковка партии длится 5 секунд
def packaging_products():
    print('------------------------packaging-----------------------')
    transport()
    global ready_product
    global product_name
    if ready_product >= 100:
        ready_product -= 100
        time.sleep(5)
        expedition.expedition_product += 100
        expedition.expedition_massive.append(product_name)