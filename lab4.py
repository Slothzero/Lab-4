# Лабораторная работа №4, вариант 5

from tkinter import *
from tkinter import messagebox
from random import randint

# создаем окно
window = Tk()
window.title('Activator')
window.resizable(0, 0)
canvas = Canvas(window, width=1280, height=720, bd=0)
canvas.pack()

# вставляем картинку
bg = PhotoImage(file = 'game.png')
canvas.create_image(0, 0, image=bg, anchor=NW)

# добавляем поле ввода
txt = Entry(window, font=('Consolas', 30), width=18)
txt.place(x=150, y=550)
txt.focus()

# добавляем надписи
canvas.create_text(150, 510, text='Введите первый блок ключа активации', font=('Consolas', 15), fill='white', anchor=NW)
canvas.create_text(150, 530, text='Ключ может содержать только латинские буквы A-Z и цифры 0-9', font=('Consolas', 10), fill='white', anchor=NW)

# функция проверяет корректность ввода
def valid():
    text = txt.get()
    if ((text.isalnum() and text.isupper()) or (text.isdigit())) and (len(text) == 5):
        return True
    else:
        return False

# функция генерирует ключ и выводит соответствующее сообщение по нажатию на кнопку
# скорее всего я неправильно понял метод генерации ключа, поэтому сделал так , как сделал
def click():
    if valid():
        first = txt.get() # первый блок ключа
        second = txt.get() # второй
        second = second[3:5]
        third = '' # третий
        for i in range(3):
            n = randint(48, 83)
            if n > 57:
                n += 7
            second = second + chr(n)
        for i in range(5):
            n = randint(48, 83)
            if n > 57:
                n += 7
            third = third + chr(n)
        txt.delete(0, last=END)
        txt.insert(0, f'{first}-{second}-{third}')
        canvas.create_text(150, 300, text='Ключ сгенерирован!', font=('Consolas', 20),
                           fill='white', anchor=NW)
    else:
        messagebox.showwarning(title='Ошибка', message='Некорректный ввод, попробуйте еще раз')


# кнопка
btn = Button(window, text='Далее', font=('Consolas', 15), command=click)
btn.place(x=150, y=620)

window.mainloop()