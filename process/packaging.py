import time
from process.expedition import *
from process.transporting import *

# упаковка партии длится 5 секунд
def packaging():
    transporting()
    global ready_product
    global product_name
    global expedition_product
    global expedition_massive
    if ready_product >= 100:
        ready_product -= 100
        time.sleep(5)
        expedition_product += 100
        expedition_massive.append(product_name)