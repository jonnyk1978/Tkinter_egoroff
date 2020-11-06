# Знакомство с виджетами. Checkbutton

import tkinter as tk


def select_all():
	for check in [over_18, commercial, follow]:
		check.select()  # метод select "отмечает" Checkbutton


def deselect_all():
	for check in [over_18, commercial, follow]:
		check.deselect()  # метод select снимает "отметку" Checkbutton


def switch_all():
	for check in [over_18, commercial, follow]:
		check.toggle()  # метод toggle инвертирует "отметку" Checkbutton


win = tk.Tk()
win.geometry(f"300x400+100+200")
win.title('Моё первое графическое приложение')

over_18 = tk.Checkbutton(win, text='Вам исполнилось 18?')
commercial = tk.Checkbutton(win, text='Хотите получать рекламу?')
follow = tk.Checkbutton(win, text='Хотите подписаться на канал?', indicatoron=0)  # indicatoron=0 - checkbox в виде кнопки

over_18.pack()
commercial.pack()
follow.pack()

tk.Button(win, text='select_all', command=select_all).pack()
tk.Button(win, text='DEselect_all', command=deselect_all).pack()
tk.Button(win, text='switch_all', command=switch_all).pack()

win.mainloop()
