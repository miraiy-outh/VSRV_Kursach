from process.priemka import *
from process.transporting import *
import time

# задержка - 5 секунд
def cleaning():
    transporting() #транспортировка из другого помещения
    global fr_b_massive_priemka
    global fr_b_massive_cleaning # массив очищенных фруктов и ягод
    tmp = 0
    for i in range(0, len(fr_b_massive_priemka)):
        if fr_b_massive_priemka[i] <= 0:
            tmp = 1
    if tmp == 0:
        for i in range(0, len(fr_b_massive_priemka)):
            fr_b_massive_priemka[i] -= 100
            fr_b_massive_priemka[i] += 100
    time.sleep(5)