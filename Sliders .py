from tkinter import *

root=Tk()

root.geometry("455x233")

myslider=Scale(root,from_=0,to=100,tickinterval=50)
myslider.pack()

myslider2=Scale(root,from_=0,to=100,orient=HORIZONTAL,tickinterval=50)
myslider2.pack()

root.mainloop()