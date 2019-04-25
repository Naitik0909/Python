import tkinter as tk
from tkinter.ttk import *
from tkinter import messagebox
import random

window = tk.Tk()
window.title("Game")
chance_count = []

img1 = tk.PhotoImage(file='Dog01.png')
img2 = tk.PhotoImage(file='Dog02.png')
img3 = tk.PhotoImage(file='Dog03.png')
img4 = tk.PhotoImage(file='Dog04.png')
img5 = tk.PhotoImage(file='Dog05.png')
img6 = tk.PhotoImage(file='Dog06.png')
img7 = tk.PhotoImage(file='Dog07.png')
img8 = tk.PhotoImage(file='Dog08.png')
img9 = tk.PhotoImage(file='white.png')


def level1():            #for easy
    moves = 10           #number of moves taken by cpu to shuffle
    if list1 != [img1, img2, img3, img4, img5, img6, img7, img8, img9]:
        for i in [img1, img2, img3, img4, img5, img6, img7, img8, img9]:
            list1.append(i)
        cpu_ai(moves)
    else:
        cpu_ai(moves)
    grid_change()
    chance_count.clear()


def level2():          #for medium
    moves = 30
    if list1 != [img1, img2, img3, img4, img5, img6, img7, img8, img9]:
        for i in [img1, img2, img3, img4, img5, img6, img7, img8, img9]:
            list1.append(i)
        cpu_ai(moves)
    else:
        cpu_ai(moves)
    grid_change()
    chance_count.clear()


def level3():          #for hard
    moves = 50
    if list1 != [img1, img2, img3, img4, img5, img6, img7, img8, img9]:
        for i in [img1, img2, img3, img4, img5, img6, img7, img8, img9]:
            list1.append(i)
        cpu_ai(moves)
    else:
        cpu_ai(moves)
    grid_change()
    chance_count.clear()


def level4():         #for insane
    moves = 150
    if list1 != [img1, img2, img3, img4, img5, img6, img7, img8, img9]:
        for i in [img1, img2, img3, img4, img5, img6, img7, img8, img9]:
            list1.append(i)
        cpu_ai(moves)
    else:
        cpu_ai(moves)
    grid_change()
    chance_count.clear()


def help_m():
    instrct = 'First, choose a difficulty. Then try to arrange the shuffled picture as it was before.'
    messagebox.showinfo('Instructions', instrct)


l1 = Button(window, text='Easy', command=level1, width=15)
l2 = Button(window, text='Medium', command=level2, width=15)
l3 = Button(window, text='Hard', command=level3, width=15)
l4 = Button(window, text='Insane', command=level4, width=15)
l5 = Button(window, text='Help', command=help_m, width=15)
l1.grid(column=0, row=0)
l2.grid(column=1, row=0)
l3.grid(column=2, row=0)
l4.grid(column=0, row=1)
l5.grid(column=2, row=1)


def check_win():
    counter = 'Moves: ' + str(len(chance_count))
    label1 = tk.Label(window, text=counter, width=10, height=1)

    label1.grid(column=1, row=1)

    if list1 == [img1, img2, img3, img4, img5, img6, img7, img8, img9]:
        final = 'You took ' + str(len(chance_count)) + ' moves to win.'
        messagebox.showinfo('Game Over', final)


def chance1():
    for i in range(0, 2):
        if list1[1 + (2 * i)] == img9:
            list1[1 + (2 * i)] = list1[0]
            list1[0] = img9
            grid_change()
            chance_count.append(1)
            check_win()
            break


def chance2():
    for i in range(0, 3):
        if list1[(2 * i)] == img9:
            list1[(2 * i)] = list1[1]
            list1[1] = img9
            grid_change()
            chance_count.append(1)
            check_win()
            break


def chance3():
    for i in range(0, 2):
        if list1[(5 ** i)] == img9:
            list1[(5 ** i)] = list1[2]
            list1[2] = img9
            grid_change()
            chance_count.append(1)
            check_win()
            break


def chance4():
    for i in range(0, 3):
        if list1[(5 * i) - i ** 2] == img9:
            list1[(5 * i) - i ** 2] = list1[3]
            list1[3] = img9
            grid_change()
            chance_count.append(1)
            check_win()
            break


def chance5():
    for i in range(0, 4):
        if list1[((2 * i) + 1)] == img9:
            list1[((2 * i) + 1)] = list1[4]
            list1[4] = img9
            grid_change()
            chance_count.append(1)
            check_win()
            break


def chance6():
    for i in range(0, 3):
        if list1[2 ** (i + 1)] == img9:
            list1[2 ** (i + 1)] = list1[5]
            list1[5] = img9
            grid_change()
            chance_count.append(1)
            check_win()
            break


def chance7():
    for i in range(0, 2):
        if list1[(4 * i) + 3] == img9:
            list1[(4 * i) + 3] = list1[6]
            list1[6] = img9
            grid_change()
            chance_count.append(1)
            check_win()
            break


def chance8():
    for i in range(0, 3):
        if list1[((2 * i) + 4)] == img9:
            list1[((2 * i) + 4)] = list1[7]
            list1[7] = img9
            grid_change()
            chance_count.append(1)
            check_win()
            break


def chance9():
    for i in range(0, 2):
        if list1[((2 * i) + 5)] == img9:
            list1[((2 * i) + 5)] = list1[8]
            list1[8] = img9
            grid_change()
            chance_count.append(1)
            check_win()
            break


list1 = [img1, img2, img3, img4, img5, img6, img7, img8, img9]


def cpu_ai(moves):      #function to set the game and shuffle randomly according to difficulty
    cpu_moves = []
    while len(cpu_moves) < moves:
        r = random.randint(0, 8)
        if r == 0:
            for i in range(0, 2):
                if list1[1 + (2 * i)] == img9:
                    list1[1 + (2 * i)] = list1[0]
                    list1[0] = img9
                    cpu_moves.append(1)
                    break

        if r == 1:
            for i in range(0, 3):
                if list1[(2 * i)] == img9:
                    list1[(2 * i)] = list1[1]
                    list1[1] = img9
                    cpu_moves.append(1)
                    break

        if r == 2:
            for i in range(0, 2):
                if list1[(5 ** i)] == img9:
                    list1[(5 ** i)] = list1[2]
                    list1[2] = img9
                    cpu_moves.append(1)
                    break

        if r == 3:
            for i in range(0, 3):
                if list1[(5 * i) - i ** 2] == img9:
                    list1[(5 * i) - i ** 2] = list1[3]
                    list1[3] = img9
                    cpu_moves.append(1)
                    break

        if r == 4:
            for i in range(0, 4):
                if list1[((2 * i) + 1)] == img9:
                    list1[((2 * i) + 1)] = list1[4]
                    list1[4] = img9
                    cpu_moves.append(1)
                    break

        if r == 5:
            for i in range(0, 3):
                if list1[2 ** (i + 1)] == img9:
                    list1[2 ** (i + 1)] = list1[5]
                    list1[5] = img9
                    cpu_moves.append(1)
                    break

        if r == 6:
            for i in range(0, 2):
                if list1[(4 * i) + 3] == img9:
                    list1[(4 * i) + 3] = list1[6]
                    list1[6] = img9
                    cpu_moves.append(1)
                    break

        if r == 7:
            for i in range(0, 3):
                if list1[2 ** (i + 1)] == img9:
                    list1[2 ** (i + 1)] = list1[5]
                    list1[5] = img9
                    cpu_moves.append(1)
                    break

        if r == 8:
            for i in range(0, 2):
                if list1[((2 * i) + 5)] == img9:
                    list1[((2 * i) + 5)] = list1[8]
                    list1[8] = img9
                    cpu_moves.append(1)
                    break


def grid_change():
    btn1 = tk.Button(window, width=100, height=100, command=chance1, bg="grey", image=list1[0])
    btn2 = tk.Button(window, width=100, height=100, command=chance2, bg="grey", image=list1[1])
    btn3 = tk.Button(window, width=100, height=100, command=chance3, bg="grey", image=list1[2])
    btn4 = tk.Button(window, width=100, height=100, command=chance4, bg="grey", image=list1[3])
    btn5 = tk.Button(window, width=100, height=100, command=chance5, bg="grey", image=list1[4])
    btn6 = tk.Button(window, width=100, height=100, command=chance6, bg="grey", image=list1[5])
    btn7 = tk.Button(window, width=100, height=100, command=chance7, bg="grey", image=list1[6])
    btn8 = tk.Button(window, width=100, height=100, command=chance8, bg="grey", image=list1[7])
    btn9 = tk.Button(window, width=100, height=100, command=chance9, bg="grey", image=list1[8])
    btn1['border'] = '0'
    btn2['border'] = '0'
    btn3['border'] = '0'
    btn4['border'] = '0'
    btn5['border'] = '0'
    btn6['border'] = '0'
    btn7['border'] = '0'
    btn8['border'] = '0'
    btn9['border'] = '0'
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
