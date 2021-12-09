from process import priemka
from process.transporting import *
import time

fr_b_massive_ready = [0] * 7


# задержка - 5 секунд
def cleaning_fr():
    transport() #транспортировка из другого помещения
    print('-------------------cleaning----------------------')
    tmp = 0
    for i in range(0, len(priemka.fr_b_massive_priemka)):
        if priemka.fr_b_massive_priemka[i] < 100:
            tmp = 1
    if tmp == 0:
        for i in range(0, len(priemka.fr_b_massive_priemka)):
            priemka.fr_b_massive_priemka[i] -= 100
            priemka.fr_b_massive_priemka[i] += 100
    time.sleep(5)
