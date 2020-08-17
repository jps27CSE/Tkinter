from tkinter import *

root=Tk()

root.geometry("400x600")

frame=Frame(root,bg="grey")
frame.pack(fill="x")

l=Label(frame,text="Welcome")
l.pack()

b1=Button(text="Hello everyone",fg="red",bg="black")
b1.pack()

root.mainloop()