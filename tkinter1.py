from tkinter import *
root = Tk()

#creating a Label Widget
#myLabel = Label(root, text="Hello World")
#myLabel1 = Label(root, text="Hello World")
#myLabel2 = Label(root, text="Hiii")

#packing a widget
#myLabel.pack()

#using the grid system
#positioning with tkinter's grid system
#myLabel1.grid(row=0,column=0)
#myLabel2.grid(row=1,column=1)

#to get a text after clicking a button
def myClick():
    myLabel = Label(root, text="hey, "+ e.get()) #get() is used to display
    myLabel.pack()

#creating buttons
#whil naming function undr command, dont give ()
#to apply colour to text in the button use fg command
#to apply colour to the bg of button use bg command
#hex colour codes can also be used
myButton = Button(root, text="Click me!", padx=50, pady=20, command = myClick, fg="blue", bg="yellow")
myButton.pack()

#creating input fields
e = Entry(root, width=50, bg="black", fg="white")
e.pack()
#a text box is formed just below the button
e.insert(0, "Enter your name") #a text gets inserted inside the textbox

#creating an event loop
root.mainloop()