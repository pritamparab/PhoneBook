from tkinter import *
import sqlite3
from tkinter import messagebox

con = sqlite3.connect('database.db')
cur = con.cursor()

class addpeople(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x550+600+200")
        self.title('Add to contacts')
        self.resizable(False, False)

        # creating top frames
        self.first = Frame(self, height=150, bg='white')
        self.first.pack(fill=X)

        self.icon = PhotoImage(file='icon.png')
        self.icon_label = Label(self.first, image=self.icon, bg='white')
        self.icon_label.place(x=170, y=40)

        self.heading = Label(self.first, text="Create Contact", bg='white', fg='black', font='algerian 20 bold')
        self.heading.place(x=230, y=50)

        # creating bottom frames
        self.last = Frame(self, height=500, bg='#b897f0')
        self.last.pack(fill=X)

        #taking data from users
        self.first_name = Label(self.last, text='First Name', font='ariel 15 bold', fg='white', bg='black')
        self.first_name.place(x=40,y=40)
        self.entry_fname = Entry(self.last, width=30, bd=4)
        self.entry_fname.place(x=200, y=40)

        self.last_name = Label(self.last, text='Last Name', font='ariel 15 bold', fg='white', bg='black')
        self.last_name.place(x=40, y=80)
        self.entry_lname = Entry(self.last, width=30, bd=4)
        self.entry_lname.place(x=200, y=80)

        self.num = Label(self.last, text='Phone Number', font='ariel 15 bold', fg='white', bg='black')
        self.num.place(x=40, y=120)
        self.entry_num = Entry(self.last, width=30, bd=4)
        self.entry_num.place(x=200, y=120)

        self.last_email = Label(self.last, text='Email ID', font='ariel 15 bold', fg='white', bg='black')
        self.last_email.place(x=40, y=160)
        self.entry_email = Entry(self.last, width=30, bd=4)
        self.entry_email.place(x=200, y=160)

        self.addr = Label(self.last, text='Address', font='ariel 15 bold', fg='white', bg='black')
        self.addr.place(x=40, y=200)
        self.entry_addr = Text(self.last, width=23, height=7)
        self.entry_addr.place(x=200, y=200)

        #submit button
        button = Button(self.last, text='Add to Contact', bg='white', command=self.add_people)
        button.place(x=240, y=350)

    def add_people(self):                   #Adding to contacts
        name = self.entry_fname.get()
        surname = self.entry_lname.get()
        phone = self.entry_num.get()
        email = self.entry_email.get()
        address = self.entry_addr.get(1.0, 'end-1c')

        if name and phone !=" ":
            try:
                query = "insert into 'addressbook' (name, surname, phone, email, address) values(?,?,?,?,?) "
                cur.execute(query,(name, surname, phone, email, address))
                con.commit()
                messagebox.showinfo("Contact Added Successfully ")
                self.destroy()
            except EXCEPTION as e:
                messagebox.showerror("error!! "+str(e))
        else:
            messagebox.showerror("Error!! Name & PhoneNumber Required")

