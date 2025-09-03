# импортируем библиотеку с окнами (интерфейсом)
# tkinter, pyqt, pyside6
# from tkinter import *
# from tkinter import ttk

# # использование всей библиотеки
# import time
# # использование одного метода из всей библиотеки
# time.sleep(0.00001)

# импорт всех функций, классов и переменных из библиотеки! может вызвать коллизию имен!
# from tkinter import *

# # импорт всей библиотеки с присвоением псевдонима
# import tkinter as tk
#
# from tkinter import ttk
#
# from . import calc
#
# # calc.calc()


from tkinter import *
from tkinter import ttk
import time
from threading import Thread

hours = 0
minutes = 0
seconds = 0


def start_timer():
    global hours
    hours = 0
    global minutes
    minutes = 0
    global seconds
    seconds = 0

    while True:
        # seconds = seconds + 1
        seconds += 1
        if seconds > 59:
            minutes += 1
            seconds = 0

        if minutes > 59:
            hours += 1
            minutes = 0

        if hours > 23:
            minutes = 0
            seconds = 0
            hours = 0

        if minutes > 5:
            break

        time.sleep(0.0001)
        print(f"{hours}:{minutes}:{seconds}")


def start_new_thread():
    Thread(target=start_timer).start()


root = Tk()

frm = ttk.Frame(root, padding=100)
root.title("таймер с интерфейсом на Phyton")
root.geometry("640x480")
frm.grid()

# часы
ttk.Label(frm, text="00").grid(column=0, row=0)
# двоеточие
ttk.Label(frm, text=":").grid(column=1, row=0)
# минуты
ttk.Label(frm, text="00").grid(column=2, row=0)
# двоеточие
ttk.Label(frm, text=":").grid(column=3, row=0)
# секунды
ttk.Label(frm, text="00").grid(column=4, row=0)
# кнопка стоп
Button(text="stop",
       background="#555",
       foreground="#ccc",
       padx="20",
       pady="8",
       font="16"
       ).grid(column=1, row=1)

# кнопка старт
Button(text="start",
       background="#555",
       foreground="#ccc",
       padx="20",
       pady="8",
       font="16",
       command=start_timer
       ).grid(column=3, row=1)

# ttk.Label(frm, text="Any").grid(column=0, row=1)
# ttk.Label(frm, text="Alex").grid(column=1, row=1)
# ttk.Label(frm, text="Ivan").grid(column=2, row=1)


#  1    2    3
# Any Alex Ivan


# ttk.Label(frm, text="Hello world!").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)

# print_to_console()
root.mainloop()

#
# Thread(target= autoc).start()
#
# def autoc():
# global click
# while True:
#     print("auto-click + 1")
#     time.sleep(1)
#     click += 1
#     lbl.configure(text=int(click))
