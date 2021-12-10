import time
from tkinter import messagebox

expedition_product = 0
expedition_massive = []


# проверка на экспедицию каждый час
def expedition_products():
    while True:
        global expedition_product
        global expedition_massive
        global exp_signal
        if expedition_product >= 500:
            messagebox.showinfo("Экспедиция отправлена!", f'{expedition_massive}')  # сообщение об отправке
            expedition_massive = []
            expedition_product -= 1000
        time.sleep(1)
