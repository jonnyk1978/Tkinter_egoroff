# Введение в tkinter. Главное окно.

import tkinter as tk

win = tk.Tk()

logo = tk.PhotoImage(file='logo.png')

win.title("Моё первое графическое приложение")
win.geometry("500x600+10+100")  # 500 - ширина, 600 - высота, 10 - отступ от левого края, 100 - отступ от верхнего края
win.resizable(True, True)       # возможность изменения размеров окна по ширине и высоте
win.minsize(300, 400)			# минимальные размеры окна (ширина, высота)
win.maxsize(1024, 768)			# максимальные размеры окна (ширина, высота)
win.iconphoto(False, logo)		# установка логотипа окна
win.config(background='red')
#win.config(bg='red')			# вариант написания background
#win.config(bg='#2DFF00')		# вариант указания цвета

win.mainloop()
