from tkinter import *

root=Tk()

root.geometry("455x233")
root.title("Radio Button")

var=IntVar()

Label(root,text="what would you like to have?",font="lucida 19 bold",
justify=LEFT,padx=14).pack()

radio=Radiobutton(root,text="Pizza",padx=14,variable=var,value=1).pack(anchor="w")
radio=Radiobutton(root,text="Burger",padx=14,variable=var,value=2).pack(anchor="w")
radio=Radiobutton(root,text="Sandwich",padx=14,variable=var,value=3).pack(anchor="w")
radio=Radiobutton(root,text="Icecream",padx=14,variable=var,value=4).pack(anchor="w")

root.mainloop()