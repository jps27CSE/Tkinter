from tkinter import *

root=Tk()

root.geometry("800x600")
root.minsize(500,300)

f1=Frame(root,bg="grey",borderwidth=6,relief=SUNKEN)
f1.pack(side=LEFT,fill="y")

root.title("TESTING GUI")

l=Label(f1,text="Project FRAME")
l.pack(pady=250)

f2=Frame(root,bg="grey",borderwidth=8,relief=SUNKEN)
f2.pack(side=TOP,fill="x")

l=Label(f2,text="welcome to testing GUI", font="Helvetica 16 bold",fg="blue")
l.pack()
root.mainloop()