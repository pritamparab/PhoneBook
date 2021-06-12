from tkinter import *
import datetime
date = datetime.datetime.now().date()
date = str(date)

from contacts import contacts
from addpeople import addpeople

class app(object):
    def __init__(self, rut):
        self.rut = rut
        #creating top frames
        self.first = Frame(rut, height=150, bg='black')
        self.first.pack(fill=X)

        self.icon = PhotoImage(file='icon.png')
        self.icon_label = Label(self.first, image=self.icon, bg='black')
        self.icon_label.place(x=170,y=40)

        self.heading = Label(self.first, text="PhoneBook App", bg='black', fg='white', font='algerian 20')
        self.heading.place(x=230,y=50)

        self.date_label = Label(self.first, text="Date : "+date, bg='black', fg='white', font='ariel 10 bold')
        self.date_label.place(x=530,y=10)

        #creating bottom frames
        self.last = Frame(rut, height=500, bg='#351173')
        self.last.pack(fill=X)

        self.viewButton = Button(self.last, text='View Contacts', bg='white', font='redaction 12 bold', command=self.contacts)
        self.viewButton.place(x=250,y=70)

        self.addButton = Button(self.last, text=' Add Contacts ', bg='white', font='redaction 12 bold', command=self.addpeople)
        self.addButton.place(x=250, y=140)

        self.label = Label(self.last, text="By : Pritam Parab", fg='white', bg='#351173', font='algerian 15')
        self.label.place(x= 220,y=300)

    def contacts(self):
        people = contacts()

    def addpeople(self):
        people = addpeople()

def main():
    root = Tk()
    a = app(root)
    root.title("Phone Book")
    root.geometry("650x550+600+200")
    root.resizable(False, False)
    root.mainloop()

if __name__ == '__main__':
    main()