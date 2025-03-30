from tkinter import *

root = Tk()

def myClick():
    myLabel1= Label(root, text="Hey i've been clicked!!").pack()

myButton= Button(root, text="Click Me!" , command=myClick , fg="pink" ,bg="black").pack()
#command is to listen the event and then call function
#fg= stands for for-ground color  bg=background color
#no use of () when calling function here after command
root.mainloop()