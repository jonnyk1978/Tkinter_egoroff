# Знакомство с виджетами. Виджет Label

import tkinter as tk

win = tk.Tk()

win.title("Моё первое графическое приложение")
win.geometry("500x600+10+100")  # 500 - ширина, 600 - высота, 10 - отступ от левого края, 100 - отступ от верхнего края

# Создание виджета Label с текстом (text), подложкой (bg), цветом текста (fg), шрифтом (font),
# отступом от горизонтальных краёв (padx), отступом от вертикальных краёв (pady),
# ширина виджета в символах (width), высота виджета в символах (height),
# расположение текста в виджете по сторонам света (anchor),
# подъём виджета над фоном (relief), высота подъёма над фоном (bd),
# выравнивание текста (justify)
# и его привязка к окну win
label1 = tk.Label(win,
                  text='''Каля-баля!
                  pasiwfasojgl
                  89asd97gsoiusio
                  897asf89AS78FASIFUIO''',
                  bg='#A9A9A9',
                  fg='red',
                  font=('Arial', 20, 'bold'),
                  padx=20,
                  pady=50,
                  width=20,
                  height=10,
                  anchor='ne',
                  relief=tk.RAISED,
                  bd=10,
                  justify=tk.RIGHT)

label1.pack()								# отображение виджета в окне

win.mainloop()
