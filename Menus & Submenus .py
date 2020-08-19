from tkinter import *

root=Tk()

fileMenu=Menu(root)

myMenu=Menu(fileMenu,tearoff=0)
myMenu.add_command(label="File")
myMenu.add_separator()
myMenu.add_command(label="Exit",command=quit)

fileMenu.add_cascade(label="file",menu=myMenu)

root.config(menu=fileMenu)



root.mainloop()