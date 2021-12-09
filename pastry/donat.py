from pastry.pastry import *

class Donut(Pastry):
    def __init__(self):
        self.dough = 'yeast'
        self.fill = ['chocolate','creme','caramel','poppy','cinnamon', 'vanilla', ''] + \
                    ['apple', 'raspberry', 'strawberry', 'lemon', 'cherry', '', 'peach', 'berries']
        self.decor = ['chocolate', 'sugar']