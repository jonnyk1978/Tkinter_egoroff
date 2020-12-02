# Знакомство с виджетами. Виджет Radiobutton

import tkinter as tk


def select_level():
	level = level_var.get()

	if level == 1:
		print('Easy')
	elif level == 2:
		print('Medium')
	elif level == 3:
		print('Hard')


win = tk.Tk()
win.geometry(f"300x400+100+200")
win.title('Мое первое графическое приложение')

level_var = tk.IntVar()
text_var = tk.StringVar()

tk.Label(win, text='Выберите уровень сложности').pack()
tk.Radiobutton(win, text='Easy', variable=level_var, value=1, command=select_level).pack()
tk.Radiobutton(win, text='Middle', variable=level_var, value=2, command=select_level).pack()
tk.Radiobutton(win, text='Hard', variable=level_var, value=3, command=select_level).pack()

win.mainloop()
