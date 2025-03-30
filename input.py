from tkinter import *

root=Tk()
#inputing is tkinter is more like entry ..it's called Enter 
e= Entry(root, width=50)
e.pack()
e.insert(0, "Enter your name")
 
def myClick():
    varia= "Your text above: " + e.get()
    myLabel1= Label(root, text= varia)
    myLabel1.pack()

myButton= Button(root, text="Click Me!" , command=myClick , fg="pink" ,bg="black").pack()
root.mainloop()