from pastry.pastry import *


class Pie(Pastry):
    def __init__(self):
        self.dough = 'flaky-yeast'
        self.fill = ['chocolate', 'creme', 'caramel', 'poppy', 'cinnamon', 'vanilla', ''] + \
                    ['apple', 'raspberry', 'strawberry', 'lemon', 'cherry', '', 'peach', 'berries']
