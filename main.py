from threading import Thread
from process.priemka import *
from printing import *
from process.expedition import *

def main():
    # запуск потоков
    priemka_d = Thread(target=priemka_dough)
    priemka_f = Thread(target=priemka_fr_b)
    priemka_l = Thread(target=priemka_fill_long)
    clean = Thread(target=cleaning_fr)
    cooking = Thread(target=choose_dough)
    package = Thread(target=packaging_products)
    exped = Thread(target=expedition_products)
    printing_now = Thread(target=printing)
    priemka_d.start()
    priemka_f.start()
    priemka_l.start()
    clean.start()
    cooking.start()
    package.start()
    exped.start()
    printing_now.start()

main()
