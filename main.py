from tkinter import *
from tkinter import filedialog

w = Tk()
w.geometry("400x600")
w.title('Text Editor')
w.config(background="#FAFBF9")


def open():
    f = filedialog.askopenfile(mode='r', filetypes=[('text files', '*.txt')])
    if f is not None:
        content = f.read()  # used for reading and storing contents of file "f"
        e.delete(1.0, END)  # clearing the entry field and making way for the text to be loaded
    e.insert(INSERT, content)  # used for entering the contents of file "f" in entry box "e"\


def clear():
    e.delete(1.0, END)  # USED FOR deleting the contents of entry "e" from 1.0 to end of file


def new():
    window = Tk()
    window.geometry("130x100")

    def new_save():
        open = filedialog.asksaveasfile(mode='w', defaultextension='*.txt')
        if open is None:
            return
        text = str(e.get(1.0, END))
        open.write(text)
        open.close()
        window.destroy()

    def new_clear():
        e.delete(1.0, END)
        window.destroy()  # used to destroy the dialog box

    button = Button(window, text='Save', borderwidth=1, activebackground='sky blue', command=new_save).place(x=10, y=30)
    button1 = Button(window, text='Dont Save', borderwidth=1, activebackground='sky blue', command=new_clear).place(
        x=60, y=30)


def save():
    open = filedialog.asksaveasfile(mode='w', defaultextension='*.txt')
    if open is None:
        return
    text = str(e.get(1.0, END))
    open.write(text)
    open.close()


def ex():
    w.quit()


b1 = Button(w, text='Open', borderwidth=0, background='#FAFBF9', activebackground='sky blue', command=open)
b1.place(x=10, y=10)
b2 = Button(w, text='Save', borderwidth=0, background='#FAFBF9', activebackground='sky blue', command=save)
b2.place(x=50, y=10)
b3 = Button(w, text='Clear', borderwidth=0, background='#FAFBF9', activebackground='sky blue', command=clear)
b3.place(x=85, y=10)
b4 = Button(w, text='New', borderwidth=0, background='#FAFBF9', activebackground='sky blue', command=new)
b4.place(x=120, y=10)
b5 = Button(w, text='Exit', borderwidth=0, background='#FAFBF9', activebackground='sky blue', command=ex)
b5.place(x=160, y=10)

e = Text(w, height=33, width=46, wrap=WORD)
e.place(x=10, y=40)

w.mainloop()
