from tkinter import *
# it's for the root window and it needs to be there before starting any tkinter file
root = Tk() 
#Now making anything in tkinter is a 2 step process
#1-to make it as text ,thing's it's gonna have etx
#2-to put it on the screen for user to see..

#here we created the thing i.e a Label
myLabel = Label( root , text="Hello World This is my first tkinter program")
#now we'll pack it or put it ont he screen using one of the way i.e pack()
#pack() just put stuff as it is with no modification ..just fills the empty space kinda thing
myLabel.pack()

#creating a loop to track the processing of running program
root.mainloop()