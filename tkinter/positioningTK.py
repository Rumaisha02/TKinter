#GRID SYSYTEM FOR POSITIONING

from tkinter import *
root = Tk() 

myLabel1 = Label( root , text="Hello World ")
myLabel2 = Label( root , text="This is my first tkinter program")
myLabel3 = Label( root , text=" My name is rumaisha qadeer")

#now we'll use grid() to position these ont he same screen as intro.py 
myLabel1.grid(row=0,column=0)
myLabel2.grid(row=1,column=0)
myLabel3.grid(row=2,column=2)

#creating a loop to track the processing of running program
root.mainloop()