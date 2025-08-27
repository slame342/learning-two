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

root = Tk()

frm = ttk.Frame(root, padding=100)
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

# ttk.Label(frm, text="Any").grid(column=0, row=1)
# ttk.Label(frm, text="Alex").grid(column=1, row=1)
# ttk.Label(frm, text="Ivan").grid(column=2, row=1)


#  1    2    3
# Any Alex Ivan


# ttk.Label(frm, text="Hello world!").grid(column=0, row=0)
#
#
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()
