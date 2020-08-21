from tkinter import *

root=Tk()

root.geometry("455x233")
root.title("Scrollbar")

scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)

#listbox=Listbox(root,yscrollcommand=scrollbar.set)
#for i in range(344):
    

##listbox.pack(fill="both",padx=22)
text=Text(root,yscrollcommand=scrollbar.set)
text.pack(fill=BOTH)

scrollbar.config(command=text.yview)

scrollbar.config(command=text.yview)


root.mainloop()