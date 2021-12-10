import tkinter as tk


def add_window():
    op = tk.Tk()
    op.title('Потоки производства')
    op.geometry('1000x400')
    op.resizable(False, False)

    frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
    frm_form.pack(side=tk.TOP)

    global rtos_text  # текстовое поле для вывода текущих характеристик
    rtos_text = tk.Text(width=600, height=25)
    rtos_text.pack()

    op.mainloop()


# очистка текстового поля
def clear():
    global rtos_text
    rtos_text.delete('1.0', 'end')


# добавление информации в текстовое поле
def ins(tmp):
    global rtos_text
    rtos_text.insert('1.0', f'{tmp}')
