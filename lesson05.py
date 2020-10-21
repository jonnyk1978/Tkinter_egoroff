# Знакомство с виджетами. Виджет Entry

import tkinter as tk



def get_entry():
	value = name.get()
	if value:
		print(value)
	else:
		print('Empty entry')

def submit():
	print(name.get())
	print(password.get())
	name.delete(0, tk.END)
	password.delete(0, tk.END)

win = tk.Tk()

win.geometry(f"400x500+100+200")
win.title('Моё первое графическое приложение')

# Текст
tk.Label(win, text='Имя:').grid(row=0, column=0, stick='e')
tk.Label(win, text='Пароль:').grid(row=1, column=0, stick='e')

# Поля ввода
name = tk.Entry(win)
password = tk.Entry(win, show='*')
name.grid(row=0, column=1)
password.grid(row=1, column=1)

# Кнопки
tk.Button(win, text='get', command=get_entry).grid(row=2, column=0, stick='we')
#tk.Button(win, text='delete', command=lambda: name.delete(0, len(name.get()))).grid(row=0, column=3, stick='we')
#tk.Button(win, text='delete', command=lambda: name.delete(0, 'end')).grid(row=2, column=0, stick='we')
tk.Button(win, text='delete', command=lambda: name.delete(0, tk.END)).grid(row=2, column=1, stick='we')
tk.Button(win, text='insert', command=lambda: name.insert(0, 'hello')).grid(row=2, column=2, stick='we')
tk.Button(win, text='submit', command=submit).grid(row=2, column=3, stick='we')

# задание минимальных размеров grid'а
win.grid_columnconfigure(0, minsize=100)
win.grid_columnconfigure(1, minsize=100)


win.mainloop()
