# Размещение виджетов при помощи метода grid()

import tkinter as tk

win = tk.Tk()

win.geometry(f"400x500+100+200")
win.title('Моё первое графическое приложение')

btn1 = tk.Button(win, text='Hello 1')
btn2 = tk.Button(win, text='Hello 2')
btn3 = tk.Button(win, text='Hello 3')
btn4 = tk.Button(win, text='Hello world')
btn5 = tk.Button(win, text='Hello 5')
btn6 = tk.Button(win, text='Hello 6')
btn7 = tk.Button(win, text='Hello 7')
btn8 = tk.Button(win, text='Hello 8')

#btn1.pack()
#btn2.pack()

# альтернатива методу pack()
# метод grid() позволяет рапсологать виджеты в виде таблицы
btn1.grid(row=0, column=0)
btn2.grid(row=0, column=1, stick='w')
btn3.grid(row=1, column=0, stick='we')
btn4.grid(row=1, column=1)
btn5.grid(row=2, column=0)
btn6.grid(row=2, column=1, stick='e')
# columnspan=2 - объединение двух столбцов
# rowspan=2 - объединение двух строк
# stick='we' - растяжение виджета по сторонам света
btn7.grid(row=3, column=0, columnspan=2, stick='we')
btn8.grid(row=0, column=2, rowspan=4, stick='ns')

# задание минимальных размеров grid'а
win.grid_columnconfigure(0, minsize=200)
win.grid_columnconfigure(1, minsize=100)

# Наполнение виджетами в цикле
for i in range(4, 9):
	for j in range(2):
		tk.Button(win, text=f'Huyllo {i+10} {j+10}').grid(row=i, column=j)

win.mainloop()
