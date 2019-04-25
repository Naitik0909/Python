import tkinter as tk
from tkinter.ttk import *
from tkinter import messagebox
import random

window = tk.Tk()
window.title("Calculator")
list1 = []

def clk_one():
    list1.append(1)
    show_info()

def clk_two():
    list1.append(2)
    show_info()

def clk_three():
    list1.append(3)
    show_info()

def clk_four():
    list1.append(4)
    show_info()

def clk_five():
    list1.append(5)
    show_info()

def clk_six():
    list1.append(6)
    show_info()

def clk_seven():
    list1.append(7)
    show_info()

def clk_eight():
    list1.append(8)
    show_info()

def clk_nine():
    list1.append(9)
    show_info()

def clk_zero():
    list1.append(0)
    show_info()

def clk_pt():
    list1.append('.')
    show_info()

def clk_add():
    list1.append('+')
    show_info()

def clk_sub():
    list1.append('-')
    show_info()

def clk_mul():
    list1.append('*')
    show_info()

def clk_div():
    list1.append('/')
    show_info()

def show_info():
    ans = ''
    for i in list1:
        ans += str(i)
    label = tk.Label(window, text=ans)
    label.grid(column=0, row=0)

def clk_calc():
    ans = ''
    for i in list1:
        ans += str(i)
    ans = eval(ans)
    label = tk.Label(window, text=ans)
    label.grid(column=5, row=0)
    list1.clear()
    clear()

def clear():
    label = Label(window, text='                 ')
    label.grid(column=0, row=0)

def btn_ce():
    list1.pop()
    show_info()

def clk_ac():
    list1.clear()
    clear()
    label = tk.Label(window, text='     ')
    label.grid(column=5, row=0)

btn1 = tk.Button(window, text='1', width=8, height=4, command=clk_one, bg='grey')
btn2 = tk.Button(window, text='2', width=8, height=4, command=clk_two, bg='grey')
btn3 = tk.Button(window, text='3', width=8, height=4, command=clk_three, bg='grey')
btn4 = tk.Button(window, text='4', width=8, height=4, command=clk_four, bg='grey')
btn5 = tk.Button(window, text='5', width=8, height=4, command=clk_five, bg='grey')
btn6 = tk.Button(window, text='6', width=8, height=4, command=clk_six, bg='grey')
btn7 = tk.Button(window, text='7', width=8, height=4, command=clk_seven, bg='grey')
btn8 = tk.Button(window, text='8', width=8, height=4, command=clk_eight, bg='grey')
btn9 = tk.Button(window, text='9', width=8, height=4, command=clk_nine, bg='grey')
btn_add = tk.Button(window, text='+', width=5, height=4, command=clk_add, bg='cyan')
btn_sub = tk.Button(window, text='-', width=5, height=4, command=clk_sub, bg='cyan')
btn_divide = tk.Button(window, text='/', width=5, height=4, command=clk_div, bg='cyan')
btn_mul = tk.Button(window, text='x', width=5, height=4, command=clk_mul, bg='cyan')
btn_calc = tk.Button(window, text='=', width=5, height=4, command=clk_calc, bg='cyan')
btn_ce = tk.Button(window, text='CLR', width=5, height=4, command=btn_ce, bg='cyan')
btn_pt = tk.Button(window, text='.', width=5, height=4, command=clk_pt, bg='cyan')
btn_ac = tk.Button(window, text='AC', width=5, height=4, command=clk_ac, bg='yellow', fg='red')
btn_zero = tk.Button(window, text='0', width=5, height=4, command=clk_zero, bg='cyan')
label = tk.Label(window, text='    ')

label.grid()

btn1.grid(column=0, row=1)
btn2.grid(column=1, row=1)
btn3.grid(column=2, row=1)
btn4.grid(column=0, row=2)
btn5.grid(column=1, row=2)
btn6.grid(column=2, row=2)
btn7.grid(column=0, row=3)
btn8.grid(column=1, row=3)
btn9.grid(column=2, row=3)
btn_zero.grid(column=3, row=3)
btn_add.grid(column=3, row=1)
btn_sub.grid(column=3, row=2)
btn_mul.grid(column=4, row=2)
btn_divide.grid(column=5, row=2)
btn_calc.grid(column=5, row=3)
btn_ce.grid(column=4, row=1)
btn_ac.grid(column=5, row=1)
btn_pt.grid(column=4, row=3)
window.mainloop()