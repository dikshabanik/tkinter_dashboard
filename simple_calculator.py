
from tkinter import *

root =Tk()
root.title("Simple Calculator")

e=Entry(root, width=50, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0,str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    first_number=e.get()
    global f_num 
    f_num = int(first_number)

#creating the buttons
b1=Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
b2=Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
b3=Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
b4=Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
b5=Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
b6=Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
b7=Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
b8=Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
b9=Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
b0=Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
b_add=Button(root, text="+", padx=39, pady=20, command=lambda: button_add())
b_equal=Button(root, text="=", padx=91, pady=20, command=lambda: button_add())
b_clear=Button(root, text="clr", padx=79, pady=20, command=lambda: button_clear())

#stacking the number buttons
#1,2,3 bottom
b1.grid(row=3, column=0)
b2.grid(row=3, column=1)
b3.grid(row=3, column=2)
#4,5,6 middle
b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)
#7,8,9 topmost
b7.grid(row=1, column=0)
b8.grid(row=1, column=1)
b9.grid(row=1, column=2)
# 0 bottom-most, at the centre
b0.grid(row=4, column=0)

#stacking the operator buttons
b_add.grid(row=5, column=0)
b_equal.grid(row=5, column=1)
b_clear.grid(row=4, column=1)


root.mainloop() #always make sure to add this command to get output
