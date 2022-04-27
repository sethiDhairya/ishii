from tkinter import *
root=Tk()
root.geometry('400x300')
root.title("Check Box")

def ag():
    print(var1.get(),var2.get(),var3.get())

Label(root,text="Your Age..").pack()

var1=IntVar()
var2=IntVar()
var3=IntVar()

r1=Checkbutton(root,text="19",variable=var1).pack(anchor="w")
r1=Checkbutton(root,text="20",variable=var2).pack(anchor="w")
r1=Checkbutton(root,text="21",variable=var3).pack(anchor="w")

b=Button(root,text="OK",command=ag).pack()
 
root.mainloop()
