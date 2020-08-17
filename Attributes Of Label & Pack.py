from tkinter import *

root=Tk()

root.geometry("400x500")

root.title("TEST GUI")

title_label=Label(text='''Microsoft Corporation (/maɪkroʊ.sɒft/) is an American multinational technology company with headquarters in Redmond, Washington.
\n It develops, manufactures, licenses, supports, and sells computer software, consumer electronics, personal computers, and related services.
\n Its best known software products are the Microsoft Windows line of operating systems, the Microsoft Office suite, and the Internet Explorer and Edge web browsers.
\n Its flagship hardware products are the Xbox video game consoles and the Microsoft Surface lineup of touchscreen personal computers.'''
,bg="red",fg="white",padx=23,pady=94,font=("comicsansms",10,"bold"),borderwidth=3,relief=SUNKEN)

#important pack option

title_label.pack(side=BOTTOM,anchor="n",fill=X)

root.mainloop()