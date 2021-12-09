from threading import Thread
from process.priemka import *

# запуск потоков
priemka_d = Thread(target=priemka_dough, args=(1,), daemon=True)
priemka_f = Thread(target=priemka_fill_fr_b, args=(1,), daemon=True)
priemka_l = Thread(target=priemka_fill_long, args=(1,), daemon=True)
