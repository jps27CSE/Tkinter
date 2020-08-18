from tkinter import *

root=Tk()

root.geometry("600x400")

def getval():
    print("User Name:",userval.get())
    print("User Password:",userpasval.get())


username=Label(root,text="UserName:")
userpass=Label(root,text="User Password:")

username.grid()
userpass.grid(row=1)

userval=StringVar()
userpasval=StringVar()

userEntry=Entry(root,textvariable=userval)
userPassEntry=Entry(root,textvariable=userpasval)

userEntry.grid(row=0,column=1)
userPassEntry.grid(row=1,column=1)

button1=Button(text="Submit",command=getval)
button1.grid()

root.mainloop()