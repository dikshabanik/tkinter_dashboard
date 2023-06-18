from tkinter import *
root = Tk()

#creating a Label Widget
#myLabel = Label(root, text="Hello World")
myLabel1 = Label(root, text="Hello World")
myLabel2 = Label(root, text="Hiii")

#packing a widget
#myLabel.pack()

#using the grid system
myLabel1.grid(row=0,column=0)
myLabel2.grid(row=0,column=1)

#creating an event loop
root.mainloop()

#positioning with tkinter's grid system

