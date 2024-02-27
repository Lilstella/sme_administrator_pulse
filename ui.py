import configs
import database
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import askokcancel, WARNING

class CenterWidget:
    def center(self):
        self.update()
        w = self.winfo_width()
        h = self.winfo_height()
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()
        x = int((ws/2) - (w/2))
        y = int((hs/2) - (h/2))
        self.geometry('{}x{}+{}+{}'.format(w, h, x, y))

class CreateManyClientsWindow(Toplevel, CenterWidget):
    pass

class CreateClientWindow(Toplevel, CenterWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Add Client')
        self.build()
        self.center()
        self.resizable(False, False)
        self.transient(parent)
        self.grab_set()

    def build(self):
        top_frame = Frame(self)
        top_frame.pack(padx = 20, pady = 10)

        Label(top_frame, text = 'ID').grid(row = 0, column = 0)
        Label(top_frame, text = 'Name').grid(row = 0, column = 1)
        Label(top_frame, text = 'Surname').grid(row = 0, column = 2)
        Label(top_frame, text = 'Gender').grid(row = 0, column = 3)
        Label(top_frame, text = 'Age').grid(row = 0, column = 4)

        id = Entry(top_frame)
        id.grid(row = 1, column = 0)
        id.bind("<KeyRelease>", lambda event: self.validate(event, 0))

        name = Entry(top_frame)
        name.grid(row = 1, column = 1)
        name.bind("<KeyRelease>", lambda event: self.validate(event, 1))

        last_name = Entry(top_frame)
        last_name.grid(row = 1, column = 2)
        last_name.bind("<KeyRelease>", lambda event: self.validate(event, 2))

        gender = Entry(top_frame)
        gender.grid(row = 1, column = 3)
        gender.bind("<KeyRelease>", lambda event: self.validate(event, 3))

        age = Entry(top_frame)
        age.grid(row = 1, column = 4)
        age.bind("<KeyRelease>", lambda event: self.validate(event, 4))

        bottom_frame = Frame(self)
        bottom_frame.pack(pady = 10)

        create_bottom = Button(bottom_frame, text='Add', command = self.create_client)
        create_bottom.configure(state = DISABLED)
        create_bottom.grid(row = 0, column = 0)
        Button(bottom_frame, text='Cancel', command = self.close).grid(row = 0, column = 1)

        self.validates = [0, 0, 0, 0, 0]
        self.create_bottom = create_bottom
        self.id = id
        self.name = name
        self.last_name = last_name
        self.gender = gender
        self.age = age

    def create_client(self):
        self.master.treeview.insert(
            parent= '', index = 'end', iid = self.id.get(),
            values=(self.id.get(), self.name.get(), self.last_name.get(), self.gender.get(), self.age.get()))
        database.Clients.add(self.id.get(), self.name.get(), self.last_name.get(), self.gender.get(), self.age.get())
        self.close()
        
    def close(self):
        self.destroy()
        self.update()

    def validate(self, event, index):
        value = event.widget.get()
        genders = ['Male', 'Female', 'Other']
        if index == 0:
            valid = configs.valid_id(value, database.Clients.list_clients)
            if valid:
                event.widget.configure({'bg': 'palegreen1'})
            else:
                event.widget.configure({'bg': 'indianred1'})
        if index == 1:
            valid = value.isalpha() and len(value) >= 3 and len(value) <= 30
            if valid:
                event.widget.configure({'bg': 'palegreen1'})
            else:
                event.widget.configure({'bg': 'indianred1'})
        if index == 2:
            valid = value.isalpha() and len(value) >= 3 and len(value) <= 30
            if valid:
                event.widget.configure({'bg': 'palegreen1'})
            else:
                event.widget.configure({'bg': 'indianred1'})
        if index == 3:
            valid = value in genders
            if valid:
                event.widget.configure({'bg': 'palegreen1'})
            else:
                event.widget.configure({'bg': 'indianred1'})
        if index == 4:
            valid = value.isdigit() and len(value) <= 3
            if valid:
                event.widget.configure({'bg': 'palegreen1'})
            else:
                event.widget.configure({'bg': 'indianred1'})

        self.validates[index] = valid
        self.create_bottom.config(state=NORMAL if self.validates == [1, 1, 1, 1, 1] else DISABLED)

class EditClientWindow(Toplevel, CenterWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Modificate Client')
        self.center()
        self.build() 
        self.transient(parent)
        self.grab_set()

    def build(self):
        top_frame = Frame(self)
        top_frame.pack(padx = 20, pady = 10)

        Label(top_frame, text = 'ID').grid(row = 0, column = 0)
        Label(top_frame, text = 'Name').grid(row = 0, column = 1)
        Label(top_frame, text = 'Surname').grid(row = 0, column = 2)
        Label(top_frame, text = 'Gender').grid(row = 0, column = 3)
        Label(top_frame, text = 'Age').grid(row = 0, column = 4)

        id = Entry(top_frame)
        id.grid(row = 1, column = 0)

        name = Entry(top_frame)
        name.grid(row = 1, column = 1)
        name.bind("<KeyRelease>", lambda event: self.validate(event, 0))

        last_name = Entry(top_frame)
        last_name.grid(row = 1, column = 2)
        last_name.bind("<KeyRelease>", lambda event: self.validate(event, 1))

        gender = Entry(top_frame)
        gender.grid(row = 1, column = 3)
        gender.bind("<KeyRelease>", lambda event: self.validate(event, 2))

        age = Entry(top_frame)
        age.grid(row = 1, column = 4)
        age.bind("<KeyRelease>", lambda event: self.validate(event, 3))

        client = self.master.treeview.focus()
        atts = self.master.treeview.item(client, 'values')
        id.insert(0, atts[0])
        id.config(state = DISABLED)
        name.insert(0, atts[1])
        last_name.insert(0, atts[2])
        gender.insert(0, atts[3])
        age.insert(0, atts[4])

        bottom_frame = Frame(self)
        bottom_frame.pack(pady = 10)

        renew = Button(bottom_frame, text= 'Confirm', command = self.edit_client)
        renew.grid(row = 0, column = 0)
        Button(bottom_frame, text = 'Cancel', command = self.close).grid(row = 0, column = 1)

        self.validates = [1, 1]
        self.renew = renew
        self.id = id
        self.name = name
        self.last_name = last_name
        self.gender = gender
        self.age = age

    def edit_client(self):
        client = self.master.treeview.focus()
        self.master.treeview.item(client, values=(
            self.id.get(), self.name.get(), self.last_name.get(), self.gender.get(), self.age.get()))
        database.Clients.modificate(self.id.get(), self.name.get(), self.last_name.get(), self.gender.get(), self.age.get())
        self.close()
    
    def close(self):
        self.destroy()
        self.update()

    def validate(self, event, index):
        value = event.widget.get()
        valid = (value.isalpha() and len(value) >= 3 and len(value) <= 12)
        event.widget.configure({'bg': 'palegreen1' if valid else 'indianred1'})

        self.validates[index] = valid
        self.renew.config(state = NORMAL if self.validates == [1, 1] else DISABLED)

class MainWindow(Tk, CenterWidget):
    def __init__(self):
        super().__init__()
        self.title('Client Manager')
        self.resizable(False, False)
        self.build()
        self.center()

    def build(self):
        #Top frame
        top_frame = Frame(self)
        top_frame.pack()

        #Treeview
        treeview = ttk.Treeview(top_frame)
        treeview['columns'] = ('id', 'name', 'last_name', 'gender', 'age')

        treeview.column('#0', width = 0, stretch = NO)
        treeview.column('id', anchor = CENTER)
        treeview.column('name', anchor = CENTER)
        treeview.column('last_name', anchor = CENTER)
        treeview.column('gender', anchor = CENTER)
        treeview.column('age', anchor = CENTER)

        treeview.heading('#0', anchor = CENTER)
        treeview.heading('id', text = 'ID', anchor = CENTER)
        treeview.heading('name', text = 'Name', anchor = CENTER)
        treeview.heading('last_name', text = 'Surname', anchor = CENTER)
        treeview.heading('gender', text = 'Gender', anchor = CENTER)
        treeview.heading('age', text = 'Age', anchor = CENTER)
        
        #Introduce database in treeview
        for client in database.Clients.list_clients:
            treeview.insert(parent='', index='end', iid=client.id, values=(client.id, client.name, client.last_name, client.gender, client.age))

        treeview.pack()

        #Bottom frame
        bottom_frame = Frame(self)
        bottom_frame.pack(pady = 20, padx = 20)

        Button(bottom_frame, text = 'Add', command = self.create).grid(column = 0, row = 0)
        Button(bottom_frame, text = 'Add Many', command = self.create_many).grid(column = 1, row = 0)
        Button(bottom_frame, text = 'Modificate', command = self.modificate).grid(column = 2, row = 0)
        Button(bottom_frame, text = 'Remove',command = self.delete).grid(column = 3, row = 0)
        Button(bottom_frame, text = 'Remove All',command = self.delete_all).grid(column = 4, row = 0)
        
        self.treeview = treeview

    def delete(self):
        client = self.treeview.focus()
        if client:
            atts = self.treeview.item(client, 'values')
            confirm = askokcancel(message='Do you want remove the client: {} {}?'.format(atts[1], atts[2]),
                                    title='Confirm remove',
                                    icon= WARNING)
            if confirm:
                self.treeview.delete(client)
                database.Clients.remove(atts[0])

    def delete_all(self):
        confirm = askokcancel(message = 'Do you want remove al clients?',
                              title = 'Confirm remove',
                              icon = WARNING)
        if confirm:
            for client in self.treeview.get_children():
                self.treeview.delete(client)
            database.Clients.remove_all()
    
    def create_many(self):
        CreateManyClientsWindow(self)

    def create(self):
        CreateClientWindow(self)

    def modificate(self):
        EditClientWindow(self)