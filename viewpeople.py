from tkinter import *
import sqlite3
from tkinter import messagebox

con = sqlite3.connect('database.db')
cur = con.cursor()


class viewpeople(Toplevel):
    def __init__(self, person_id):
        Toplevel.__init__(self)
        self.geometry("650x550+600+200")
        self.title('Display Contacts')
        self.resizable(False, False)
        self.person_id = person_id
        # creating top frames
        self.first = Frame(self, height=150, bg='white')
        self.first.pack(fill=X)

        self.icon = PhotoImage(file='icon.png')
        self.icon_label = Label(self.first, image=self.icon, bg='white')
        self.icon_label.place(x=170, y=40)

        self.heading = Label(self.first, text="Display Contacts", bg='white', fg='black', font='algerian 20 bold')
        self.heading.place(x=230, y=50)

        # creating bottom frames
        self.last = Frame(self, height=500, bg='#b897f0')
        self.last.pack(fill=X)

        # Taking data
        query = "select * from 'addressbook' where ID = '{}'".format(person_id)
        result = cur.execute(query).fetchone()
        fname = result[1]
        lname = result[2]
        phone = result[3]
        mail = result[4]
        address = result[5]

        #displaying
        self.first_name = Label(self.last, text='First Name', font='ariel 15 bold', fg='white', bg='black')
        self.first_name.place(x=40, y=40)
        self.entry_fname = Entry(self.last, width=30, bd=4)
        self.entry_fname.insert(0, fname)
        self.entry_fname.config(state='disabled')
        self.entry_fname.place(x=200, y=40)

        self.last_name = Label(self.last, text='Last Name', font='ariel 15 bold', fg='white', bg='black')
        self.last_name.place(x=40, y=80)
        self.entry_lname = Entry(self.last, width=30, bd=4)
        self.entry_lname.insert(0, lname)
        self.entry_lname.config(state='disabled')
        self.entry_lname.place(x=200, y=80)

        self.num = Label(self.last, text='Phone Number', font='ariel 15 bold', fg='white', bg='black')
        self.num.place(x=40, y=120)
        self.entry_num = Entry(self.last, width=30, bd=4)
        self.entry_num.insert(0, phone)
        self.entry_num.config(state='disabled')
        self.entry_num.place(x=200, y=120)

        self.last_email = Label(self.last, text='Email ID', font='ariel 15 bold', fg='white', bg='black')
        self.last_email.place(x=40, y=160)
        self.entry_email = Entry(self.last, width=30, bd=4)
        self.entry_email.insert(0, mail)
        self.entry_email.config(state='disabled')
        self.entry_email.place(x=200, y=160)

        self.addr = Label(self.last, text='Address', font='ariel 15 bold', fg='white', bg='black')
        self.addr.place(x=40, y=200)
        self.entry_addr = Text(self.last, width=23, height=7)
        self.entry_addr.insert(1.0, address)
        self.entry_addr.config(state='disabled')
        self.entry_addr.place(x=200, y=200)

        def viewpeople(self):
            id = self.person_id
            name = self.entry_fname.get()
            surname = self.entry_lname.get()
            phone = self.entry_num.get()
            email = self.entry_email.get()
            address = self.entry_addr.get(1.0, 'end-1c')

            query = "update 'addressbook' set name='{}', surname='{}', phone='{}', email='{}', address='{}' where ID='{}'".format(
                name, surname, phone, email, address, id)
            try:
                cur.execute(query)
                con.commit()
                messagebox.showinfo('Updated!')
                self.destroy()
            except EXCEPTION as e:
                messagebox.showerror("error!! " + str(e))