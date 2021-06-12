from tkinter import *
import sqlite3
from tkinter import Listbox, messagebox

con = sqlite3.connect('database.db')
cur = con.cursor()

from addpeople import addpeople
from updatepeople import updatepeople
from viewpeople import viewpeople

class contacts(Toplevel):

    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x550+600+200")
        self.title('My Contacts')
        self.resizable(False, False)

        # creating top frames
        self.first = Frame(self, height=150, bg='white')
        self.first.pack(fill=X)

        self.icon = PhotoImage(file='icon.png')
        self.icon_label = Label(self.first, image=self.icon, bg='white')
        self.icon_label.place(x=170, y=40)

        self.heading = Label(self.first, text="My Contacts", bg='white', fg='black', font='algerian 20 bold')
        self.heading.place(x=230, y=50)

        # creating bottom frames
        self.last = Frame(self, height=500, bg='#b897f0')
        self.last.pack(fill=X)

        #showing contacts
        self.scroll = Scrollbar(self.last, orient=VERTICAL)

        self.listbox = Listbox(self.last, width=40, height=30)
        self.listbox.grid(row=0, column=0, padx=(40, 0))

        self.scroll.config(command=self.listbox.yview)
        self.scroll.grid(row=0, column=1, sticky=N+S)

        persons = cur.execute("select * from 'addressbook'").fetchall()
        count = 0
        for person in persons:
            self.listbox.insert(count, str(person[0]) +"    " + person[1] +" " + person[2])
            count += 1

        #adding buttons
        btn_add = Button(self.last, text='ADD', width=12, font='Sans 12 bold', command=self.addpeople)
        btn_add.grid(row=0, column=2, padx=20, pady=10, sticky=N)

        btn_display = Button(self.last, text='DISPLAY', width=12, font='Sans 12 bold', command=self.viewpeople)
        btn_display.grid(row=0, column=2, padx=20, pady=50, sticky=N)

        btn_update = Button(self.last, text='Update', width=12, font='Sans 12 bold', command=self.updatepeople)
        btn_update.grid(row=0, column=2, padx=20, pady=90, sticky=N)

        btn_delete = Button(self.last, text='DELETE', width=12, font='Sans 12 bold', command=self.delpeople)
        btn_delete.grid(row=0, column=2, padx=20, pady=130, sticky=N)

    def addpeople(self):
        people = addpeople()

    def updatepeople(self):
        selected_item = self.listbox.curselection()
        person = self.listbox.get(selected_item)
        person_id = person.split()
        person_id = person_id[0]
        people = updatepeople(person_id)

    def viewpeople(self):
        selected_item = self.listbox.curselection()
        person = self.listbox.get(selected_item)
        person_id = person.split()
        person_id = person_id[0]
        people = viewpeople(person_id)

    def delpeople(self):
        selected_item = self.listbox.curselection()
        person = self.listbox.get(selected_item)
        person_id = person.split()
        person_name = person_id[1]
        person_id = person_id[0]

        query = "delete from 'addressbook' where ID='{}'".format(person_id)
        answer = messagebox.askquestion("Delete "+person_name,"?")
        if answer == 'yes':
            try:
                cur.execute(query)
                con.commit()
                messagebox.showinfo("Deleted!")
                self.destroy()
            except Exception as e:
                messagebox.showinfo("Info "+str(e))