from process.priemka import *
from process.transporting import *

# задержка - 5 минут
def cleaning():
    global fr_b_massive_priemka
    global fr_b_massive_cleaning # массив очищенных фруктов и ягод

    for i in range(0, len(fr_b_massive_priemka)):
        fr_b_massive_priemka[i] -= 100
        fr_b_massive_priemka[i] += 100