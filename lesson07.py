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


def show():
	print('Флаг 18 is', over_18_value.get())
	print('Реклама is', commercial_value.get())

win = tk.Tk()

over_18_value = tk.StringVar()
over_18_value.set('No')  # двустороння связь
commercial_value = tk.IntVar()

win.geometry(f"300x400+100+200")
win.title('Моё первое графическое приложение')

# text - текст подписи Checkbutton'а
# textvariable - имя переменной, привязанной к состоянию Checkbutton'а
# offvalue - содержимое переменной, имя которой указано в textvariable, в снятом состоянии
# onvalue - содержимое переменной, имя которой указано в textvariable, в отмеченном состоянии
over_18 = tk.Checkbutton(win, text='Вам исполнилось 18?', variable=over_18_value, offvalue='No', onvalue='Yes')
commercial = tk.Checkbutton(win, text='Хотите получать рекламу?', variable=commercial_value, offvalue=0, onvalue=1)
follow = tk.Checkbutton(win, text='Хотите подписаться на канал?', indicatoron=0)  # indicatoron=0 - checkbox в виде кнопки

over_18.pack()
commercial.pack()
follow.pack()

tk.Button(win, text='select_all', command=select_all).pack()
tk.Button(win, text='DEselect_all', command=deselect_all).pack()
tk.Button(win, text='switch_all', command=switch_all).pack()
tk.Button(win, text='Show', command=show).pack()

win.mainloop()
