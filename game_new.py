import tkinter as tk
from tkinter.ttk import *
from tkinter import messagebox
import random

window = tk.Tk()
window.title("Game")
chance_count = []


def level1():
    moves = 10
    if list1 != [1, 2, 3, 4, 5, 6, 7, 8, ' ']:
        list1.clear()
        for new in range(1, 9):
            list1.append(new)
        list1.append(' ')
        cpu_ai(moves)
    else:
        cpu_ai(moves)
    grid_change()
    chance_count.clear()


def level2():
    moves = 30
    if list1 != [1, 2, 3, 4, 5, 6, 7, 8, ' ']:
        list1.clear()
        for new in range(1, 9):
            list1.append(new)
        list1.append(' ')
        cpu_ai(moves)
    else:
        cpu_ai(moves)
    grid_change()
    chance_count.clear()


def level3():
    moves = 50
    if list1 != [1, 2, 3, 4, 5, 6, 7, 8, ' ']:
        list1.clear()
        for new in range(1, 9):
            list1.append(new)
        list1.append(' ')
        cpu_ai(moves)
    else:
        cpu_ai(moves)
    grid_change()
    chance_count.clear()


def level4():
    moves = 100
    if list1 != [1, 2, 3, 4, 5, 6, 7, 8, ' ']:
        list1.clear()
        for new in range(1, 9):
            list1.append(new)
        list1.append(' ')
        cpu_ai(moves)
    else:
        cpu_ai(moves)
    grid_change()
    chance_count.clear()


def help_m():
    instrct = 'You will see all numbers from 1 to 8 in the grid. Your aim is to arrange ' \
              'all these numbers in ascending order in the grid so that the blank space is at the ' \
              'bottom right corner of the grid.\n\nYou can move any number above, below, to the right or to ' \
              'the left of the blank space.\n\nNote that diagonal move is not allowed.'
    messagebox.showinfo('Instructions', instrct)


l1 = Button(window, text='Easy', command=level1)
l2 = Button(window, text='Medium', command=level2)
l3 = Button(window, text='Hard', command=level3)
l4 = Button(window, text='Insane', command=level4)
l5 = Button(window, text='Help', command=help_m)
l1.grid(column=0, row=0)
l2.grid(column=1, row=0)
l3.grid(column=2, row=0)
l4.grid(column=0, row=1)
l5.grid(column=2, row=1)


def check_win():

    if list1 == [1, 2, 3, 4, 5, 6, 7, 8, ' ']:
        final = 'You took ' + str(len(chance_count)) + ' moves to win.'
        messagebox.showinfo('Game Over', final)


def chance1():
    for i in range(0, 2):
        if list1[1 + (2 * i)] == ' ':
            list1[1 + (2 * i)] = list1[0]
            list1[0] = ' '
            grid_change()
            chance_count.append(1)
            check_win()
            break


def chance2():
    for i in range(0, 3):
        if list1[(2 * i)] == ' ':
            list1[(2 * i)] = list1[1]
            list1[1] = ' '
            grid_change()
            chance_count.append(1)
            check_win()
            break


def chance3():
    for i in range(0, 2):
        if list1[(5 ** i)] == ' ':
            list1[(5 ** i)] = list1[2]
            list1[2] = ' '
            grid_change()
            chance_count.append(1)
            check_win()
            break


def chance4():
    for i in range(0, 3):
        if list1[(5 * i) - i ** 2] == ' ':
            list1[(5 * i) - i ** 2] = list1[3]
            list1[3] = ' '
            grid_change()
            chance_count.append(1)
            check_win()
            break


def chance5():
    for i in range(0, 4):
        if list1[((2 * i) + 1)] == ' ':
            list1[((2 * i) + 1)] = list1[4]
            list1[4] = ' '
            grid_change()
            chance_count.append(1)
            check_win()
            break


def chance6():
    for i in range(0, 3):
        if list1[2 ** (i + 1)] == ' ':
            list1[2 ** (i + 1)] = list1[5]
            list1[5] = ' '
            grid_change()
            chance_count.append(1)
            check_win()
            break


def chance7():
    for i in range(0, 2):
        if list1[(4 * i) + 3] == ' ':
            list1[(4 * i) + 3] = list1[6]
            list1[6] = ' '
            grid_change()
            chance_count.append(1)
            check_win()
            break


def chance8():
    for i in range(0, 3):
        if list1[((2 * i) + 4)] == ' ':
            list1[((2 * i) + 4)] = list1[7]
            list1[7] = ' '
            grid_change()
            chance_count.append(1)
            check_win()
            break


def chance9():
    for i in range(0, 2):
        if list1[((2 * i) + 5)] == ' ':
            list1[((2 * i) + 5)] = list1[8]
            list1[8] = ' '
            grid_change()
            chance_count.append(1)
            check_win()
            break


list1 = [1, 2, 3, 4, 5, 6, 7, 8, ' ']


def cpu_ai(moves):
    cpu_moves = []
    while len(cpu_moves) < moves:
        r = random.randint(0, 8)
        if r == 0:
            for i in range(0, 2):
                if list1[1 + (2 * i)] == ' ':
                    list1[1 + (2 * i)] = list1[0]
                    list1[0] = ' '
                    cpu_moves.append(1)
                    break

        if r == 1:
            for i in range(0, 3):
                if list1[(2 * i)] == ' ':
                    list1[(2 * i)] = list1[1]
                    list1[1] = ' '
                    cpu_moves.append(1)
                    break

        if r == 2:
            for i in range(0, 2):
                if list1[(5 ** i)] == ' ':
                    list1[(5 ** i)] = list1[2]
                    list1[2] = ' '
                    cpu_moves.append(1)
                    break

        if r == 3:
            for i in range(0, 3):
                if list1[(5 * i) - i ** 2] == ' ':
                    list1[(5 * i) - i ** 2] = list1[3]
                    list1[3] = ' '
                    cpu_moves.append(1)
                    break

        if r == 4:
            for i in range(0, 4):
                if list1[((2 * i) + 1)] == ' ':
                    list1[((2 * i) + 1)] = list1[4]
                    list1[4] = ' '
                    cpu_moves.append(1)
                    break

        if r == 5:
            for i in range(0, 3):
                if list1[2 ** (i + 1)] == ' ':
                    list1[2 ** (i + 1)] = list1[5]
                    list1[5] = ' '
                    cpu_moves.append(1)
                    break

        if r == 6:
            for i in range(0, 2):
                if list1[(4 * i) + 3] == ' ':
                    list1[(4 * i) + 3] = list1[6]
                    list1[6] = ' '
                    cpu_moves.append(1)
                    break

        if r == 7:
            for i in range(0, 3):
                if list1[2 ** (i + 1)] == ' ':
                    list1[2 ** (i + 1)] = list1[5]
                    list1[5] = ' '
                    cpu_moves.append(1)
                    break

        if r == 8:
            for i in range(0, 2):
                if list1[((2 * i) + 5)] == ' ':
                    list1[((2 * i) + 5)] = list1[8]
                    list1[8] = ' '
                    cpu_moves.append(1)
                    break


def grid_change():
    btn1 = tk.Button(window, text=list1[0], width=10, height=5, command=chance1, bg="grey")
    btn2 = tk.Button(window, text=list1[1], width=10, height=5, command=chance2, bg="grey")
    btn3 = tk.Button(window, text=list1[2], width=10, height=5, command=chance3, bg="grey")
    btn4 = tk.Button(window, text=list1[3], width=10, height=5, command=chance4, bg="grey")
    btn5 = tk.Button(window, text=list1[4], width=10, height=5, command=chance5, bg="grey")
    btn6 = tk.Button(window, text=list1[5], width=10, height=5, command=chance6, bg="grey")
    btn7 = tk.Button(window, text=list1[6], width=10, height=5, command=chance7, bg="grey")
    btn8 = tk.Button(window, text=list1[7], width=10, height=5, command=chance8, bg="grey")
    btn9 = tk.Button(window, text=list1[8], width=10, height=5, command=chance9, bg="grey")

    btn1.grid(column=0, row=2)
    btn2.grid(column=1, row=2)
    btn3.grid(column=2, row=2)
    btn4.grid(column=0, row=3)
    btn5.grid(column=1, row=3)
    btn6.grid(column=2, row=3)
    btn7.grid(column=0, row=4)
    btn8.grid(column=1, row=4)
    btn9.grid(column=2, row=4)


grid_change()
window.mainloop()
