class Pastry:
    def __init__(self):
        self.dough = ''
        self.fill = ''
        self.decor = ''

    def set_dough(self, dough):
        self.dough = dough

    def set_fill(self, fill):
        self.fill = fill

    def set_decor(self, decor):
        self.decor = decor

    def get_dough(self):
        return self.dough

    def get_fill(self):
        return self.fill

    def get_decor(self):
        return self.decor
