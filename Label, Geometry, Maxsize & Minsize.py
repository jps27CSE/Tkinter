from tkinter import *


root=Tk()

#Width X Height 

root.geometry("644x434")

#Width, Height

root.minsize(300,100)

#Width, Height

root.maxsize(1200,988)

#Label

text=Label(text="Hello Jack")

#packing 
text.pack()


root.mainloop()