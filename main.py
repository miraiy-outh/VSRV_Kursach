from threading import Thread
from process.cooking import *
from printing import *
# запуск потоков
priemka_d = Thread(target=priemka_dough, args=(1,), daemon=True)
priemka_f = Thread(target=priemka_fr_b, args=(1,), daemon=True)
priemka_l = Thread(target=priemka_fill_long, args=(1,), daemon=True)
cooking = Thread(target=choose_dough, args=(1,), daemon=True)
printing_now = Thread(target=printing, args=(1,), daemon=True)

