from tkinter import *

root=Tk()

root.geometry("644x344")
root.title("Travel Form")
Label(root,text="\t \tWelcome to Travel Form",font="comicsansms 13 bold",pady=15).grid(row=0,column=3)

def getval():
    print("User Applied")


name=Label(root,text="Name:")
phone=Label(root,text="Phone:")
gender=Label(root,text="Gender:")
location=Label(root,text="Location:")

name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
location.grid(row=4,column=2)

nameVal=StringVar()
phoneVal=IntVar()
genderVal=StringVar()
locationVal=StringVar()
food_serviceVal=IntVar()

nameEntry=Entry(root,textvariable=nameVal)
phoneEntry=Entry(root,textvariable=phoneVal)
genderEntry=Entry(root,textvariable=genderVal)
locationEntry=Entry(root,textvariable=locationVal)
food_serviceEntry=Entry(root,textvariable=food_serviceVal)

nameEntry.grid(row=1,column=3)
phoneEntry.grid(row=2,column=3)
genderEntry.grid(row=3,column=3)
locationEntry.grid(row=4,column=3)

food_service=Checkbutton(text="Want to prebook your Meals?",variable=food_serviceVal)
food_service.grid(row=6,column=3)
Button(text="Apply",command=getval).grid(row=7,column=3)


root.mainloop()