from tkinter import *
from tkinter import messagebox as mb

def btn_click():
	login = loginInput.get()
	password = passField.get()
	info_str = f'Данные: {str(login)}, {str(password)}'
	# messagebox = mb.showinfo(title='Название', message='')
	mb.showinfo(title='Название', message=info_str)

	# окно с ошибкой
	#mb.showerror(title='', message='Error always!!!')


root = Tk()

root['bg'] = '#FAFAFA'
root.title('Название программы')
root.wm_attributes('-alpha', 0.7)
root.geometry('300x250')

root.resizable(width=False, height=False)

canvas = Canvas(root, width=300, height=250)
canvas.pack()

frame = Frame(root, bg='red')
frame.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)

title = Label(frame, text='Текст-подсказка', bg='grey', font=40)
title.pack()
btn = Button(frame, text='Кнопка', bg='yellow', command=btn_click)
btn.pack()

loginInput = Entry(frame, bg='white')
loginInput.pack()

passField = Entry(frame, bg='white', show='*')
passField.pack()


root.mainloop()
