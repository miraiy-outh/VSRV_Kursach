from threading import Thread
from process.cooking import *

# запуск потоков
priemka_d = Thread(target=priemka_dough, args=(1,), daemon=True)
priemka_f = Thread(target=priemka_fr_b, args=(1,), daemon=True)
priemka_l = Thread(target=priemka_fill_long, args=(1,), daemon=True)
cooking = Thread(target=choose_dough, args=(1,), daemon=True)
