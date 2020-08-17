from tkinter import *

root=Tk()

root.geometry("455x244")

photo=PhotoImage(file="1.png")

photo_label=Label(image=photo)

photo_label.pack()

root.mainloop()