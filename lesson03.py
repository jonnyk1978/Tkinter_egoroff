# Знакомство с виджетами. Виджет Button

def say_hello():
	print('hello')

def add_label():
	label = tk.Label(win, text='New Label')
	label.pack()

def counter():
	global count
	count += 1
	btn4['text'] = f'Counter: {count}'

count = 0

import tkinter as tk

win = tk.Tk()

win.geometry(f"400x500+100+200")
win.title('Моё первое графическое приложение')

btn1 = tk.Button(win, text='Hello!', command=say_hello)	# создание кнопки
btn1.pack()												# отрисовка кнопки

btn2 = tk.Button(win, text='Add new label', command=add_label)	# создание кнопки
btn2.pack()

btn3 = tk.Button(win, text='Add new label lambda', command=lambda: tk.Label(win, text='new lambda').pack())	# создание кнопки
btn3.pack()

# state=tk.DISABLED - отключить кнопку
btn4 = tk.Button(win, text=f'Counter: {count}', command=counter, bg='red', activebackground='blue')
btn4.pack()

win.mainloop()
