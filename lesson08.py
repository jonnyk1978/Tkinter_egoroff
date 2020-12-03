# Знакомство с виджетами. Виджет Radiobutton

import tkinter as tk

levels = {1: 'Easy', 2: 'Middle', 3: 'Hard'}


def select_level():
	level = level_var.get()
	level_text.set(f"Вы выбрали {level} уровень")
	print(levels[level])


win = tk.Tk()
win.geometry(f"300x400+100+200")
win.title('Мое первое графическое приложение')

level_var = tk.IntVar()
level_text = tk.StringVar()
race_var = tk.IntVar()

tk.Label(win, text='Выберите уровень сложности').pack()
tk.Radiobutton(win, text='Easy', variable=level_var, value=1, command=select_level).pack()
tk.Radiobutton(win, text='Middle', variable=level_var, value=2, command=select_level).pack()
tk.Radiobutton(win, text='Hard', variable=level_var, value=3, command=select_level).pack()
tk.Label(win, textvariable=level_text).pack()

tk.Label(win, text='Выберите расу').pack()
tk.Radiobutton(win, text='Эльфы', variable=race_var, value=1, command=select_level).pack()
tk.Radiobutton(win, text='Люди', variable=race_var, value=2, command=select_level).pack()
tk.Radiobutton(win, text='Орки', variable=race_var, value=3, command=select_level).pack()

win.mainloop()
