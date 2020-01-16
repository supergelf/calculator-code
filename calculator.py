from tkinter import *
from math import sqrt
from math import pow
from math import pi
from math import factorial
from math import sin 
from math import cos 
from math import tan 


root = Tk()
root.title('Calculator')
root.configure(background='#d5f5ee')

e = Entry(root, width=20, borderwidth=5, font=('Calibri', 40))
e.grid(row=0, column=0, columnspan=6, padx=1, pady=10, ipady=15)


def button_click(number):
    e.insert(END, number)

def button_clear():
    e.delete(0,END)

def button_add():
    first_number = e.get()
    global f_num 
    global math
    math = 'addition'
    f_num = float(first_number)
    e.delete(0,END)

def button_equal():
    second_number = e.get()
    e.delete(0,END)

    if math == 'addition':
        e.insert(0, f_num + float(second_number))
    if math == 'subtraction':
        e.insert(0, f_num - float(second_number))
    elif math == 'multiplication':
        e.insert(0, f_num * float(second_number))
    if math == 'division':
        e.insert(0, f_num / float(second_number))
    if math == 'square root':
        e.insert(0, sqrt(f_num))
    if math == 'exponent':
        e.insert(0, f_num**float(second_number)) 
    if math == 'factorial':
        e.insert(0, factorial(f_num))
    if math == 'sinus':
        e.insert(0, sin(f_num))
    if math == 'cosinus':
        e.insert(0, cos(f_num))
    if math == 'tangent':
        e.insert(0, tan(f_num))

def button_subtract():
    first_number = e.get()
    global f_num 
    global math
    math = 'subtraction'
    f_num = float(first_number)
    e.delete(0,END)

def button_multiply():
    first_number = e.get()
    global f_num 
    global math
    math = 'multiplication'
    f_num = float(first_number)
    e.delete(0,END)

def button_divide():
    first_number = e.get()
    global f_num 
    global math
    math = 'division'
    f_num = float(first_number)
    e.delete(0,END)

def button_square_root():
    first_number = e.get()
    global f_num 
    global math
    math = 'square root'
    f_num = float(first_number)

def button_exponent():
    first_number = e.get()
    global f_num 
    global math
    math = 'exponent'
    f_num = float(first_number)
    e.delete(0,END)

def button_factorial():
    first_number = e.get()
    global f_num 
    global math
    math = 'factorial'
    f_num = float(first_number)
    e.delete(0,END)

def button_sinus():
    first_number = e.get()
    global f_num 
    global math
    math = 'sinus'
    f_num = float(first_number)
    e.delete(0,END)

def button_cosinus():
    first_number = e.get()
    global f_num 
    global math
    math = 'cosinus'
    f_num = float(first_number)
    e.delete(0,END)

def button_tangent():
    first_number = e.get()
    global f_num 
    global math
    math = 'tangent'
    f_num = float(first_number)
    e.delete(0,END)


def button_delete():
    e.delete(0)


# define buttons
button_1 = Button(root, text='1', font=('Calibri',30), padx=20, pady=1, command=lambda: button_click(1), bg='#d5f5ee')
button_2 = Button(root, text='2', font=('Calibri',30), padx=20, pady=1, command=lambda: button_click(2), bg='#d5f5ee')
button_3 = Button(root, text='3', font=('Calibri',30), padx=20, pady=1, command=lambda: button_click(3), bg='#d5f5ee')
button_4 = Button(root, text='4', font=('Calibri',30), padx=20, pady=1, command=lambda: button_click(4), bg='#d5f5ee')
button_5 = Button(root, text='5', font=('Calibri',30), padx=20, pady=1, command=lambda: button_click(5), bg='#d5f5ee')
button_6 = Button(root, text='6', font=('Calibri',30), padx=20, pady=1, command=lambda: button_click(6), bg='#d5f5ee')
button_7 = Button(root, text='7', font=('Calibri',30), padx=20, pady=1, command=lambda: button_click(7), bg='#d5f5ee')
button_8 = Button(root, text='8', font=('Calibri',30), padx=20, pady=1, command=lambda: button_click(8), bg='#d5f5ee')
button_9 = Button(root, text='9', font=('Calibri',30), padx=20, pady=1, command=lambda: button_click(9), bg='#d5f5ee')
button_0 = Button(root, text='0', font=('Calibri',30), padx=20, pady=1, command=lambda: button_click(0), bg='#d5f5ee')

button_punktum = Button(root, text='.', font=('Calibri',30), padx=32, pady=1, command=lambda: button_click('.'), bg='#d5f5ee')
#button_pi = Button(root, text='𝜋', font=('Calibri',30), padx=27, pady=1, command=lambda: button_click(pi), bg='#d5f5ee')


button_add = Button(root, text='+', font=('Calibri',30), padx=25, pady=1, command=button_add, bg='#d5f5ee')
button_equal= Button(root, text='=', font=('Calibri',30), padx=64, pady=1, command=button_equal, bg='#d5f5ee')
button_clear = Button(root, text='Clear', font=('Calibri',25), padx=41, pady=9, command=button_clear, bg='#d5f5ee')

button_subtract = Button(root, text='-', font=('Calibri',28), padx=30, pady=5, command=button_subtract, bg='#d5f5ee') 
button_minus = Button(root, text='f-', font=('Calibri',30), padx=24, pady=1, command=lambda: button_click('-'), bg='#d5f5ee') 

button_multiply = Button(root, text='x', font=('Calibri',28), padx=28, pady=5, command=button_multiply, bg='#d5f5ee')
button_divide = Button(root, text='/', font=('Calibri',30), padx=28, pady=2, command=button_divide, bg='#d5f5ee')

button_delete = Button(root, text='Del', font=('Calibri',25), padx=16, pady=10, command=button_delete, bg='#d5f5ee')
button_quit = Button(root, text= 'Quit', command=root.quit, font=('Calibri', 22), padx=8, pady=13, bg='#d5f5ee')
button_square_root = Button(root, text='√x', font=('Calibri',28), padx=21, pady=5, command=button_square_root, bg='#d5f5ee')

button_exponent = Button(root, text='x^n', font=('Calibri',25), padx=16, pady=9, command=button_exponent, bg='#d5f5ee')
button_factorial = Button(root, text='x!', font=('Calibri',30), padx=23, pady=1, command=button_factorial, bg='#d5f5ee')

button_sinus = Button(root, text='sin(x)', font=('Calibri',22), padx=7, pady=14, command=button_sinus, bg='#d5f5ee')
button_cosinus = Button(root, text='cos(x)', font=('Calibri',22), padx=5, pady=12, command=button_cosinus, bg='#d5f5ee')
button_tangent = Button(root, text='tan(x)', font=('Calibri',23), padx=4, pady=11, command=button_tangent, bg='#d5f5ee')

# Put buttons on screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_multiply.grid(row=3, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_subtract.grid(row=2, column=3)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_add.grid(row=1, column=3)

#sbutton_pi.grid(row=4, column=4)
button_0.grid(row=4, column=0)
button_equal.grid(row=4, column=1, columnspan=2)
button_divide.grid(row=4, column=3)

button_delete.grid(row=5, column=3)
button_punktum.grid(row=3, column=4)
button_clear.grid(row=5, column=1, columnspan=2)
button_square_root.grid(row=1, column=4)

button_exponent.grid(row=2, column=4)
button_quit.grid(row=5, column=0)
button_factorial.grid(row=5, column=4)

button_sinus.grid(row=1, column=5)
button_cosinus.grid(row=2, column=5)
button_tangent.grid(row=3, column=5)
button_minus.grid(row=4, column=5)


root.mainloop()