from process import priemka
from process.transporting import *
import time

fr_b_massive_ready = [0] * 7


# 30 минут
def cleaning_fr():
    while True:
        global fr_b_massive_ready
        transport() #транспортировка из другого помещения
        for i in range(0, len(priemka.fr_b_massive_priemka) - 1):
            if fr_b_massive_ready[i] <= 150 and priemka.fr_b_massive_priemka[i] < 200:
                fr_b_massive_ready[i] += 50
                priemka.fr_b_massive_priemka[i] -= 50
        time.sleep(4)
