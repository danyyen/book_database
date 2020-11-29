
from tkinter import *
from backend_OOP import Database

db= Database()                                  #instantiates the database class in the backend_oop module

class Library_Widget:
    '''class initializes all functions needed to setup the window widget'''

    def __init__(self):
        
        #labels --- this creates all labels for the entry
        t1 = Label(window, text= "Title")
        t1.grid(row=0, column=0)
        a1 = Label(window, text= "Author")
        a1.grid(row=0, column=3)
        y1 = Label(window, text= "Year")
        y1.grid(row=1, column=0)
        s1 = Label(window, text= "ISBN")
        s1.grid(row=1, column=3)
        textbl= Label(window, text= "Book List")
        textbl.grid(row=2, column=0)

        #entries---- this creates the entry box and also stores data values of the entry box
        self.t1_val = StringVar()                                        
        self.title = Entry(window, textvariable = self.t1_val)                    
        self.title.grid(row=0, column= 1)

        self.a1_val = StringVar()                                        
        self.auth = Entry(window, textvariable = self.a1_val)                    
        self.auth.grid(row=0, column= 4)

        self.y1_val = IntVar()                                        
        self.yr = Entry(window, textvariable = self.y1_val)                    
        self.yr.grid(row=1, column= 1)

        self.s1_val = IntVar()                                        
        self.isbn = Entry(window, textvariable = self.s1_val)                    
        self.isbn.grid(row=1, column= 4)

        #listbox --- this is where the list of entries are displayed
        self.list_box = Listbox(window, height= 10, width= 40)
        self.list_box.grid(row=3, column=0, rowspan=10, columnspan=3)

        #buttons ---- this activates each button to perform a function assigned to it
        v1= Button(window, text= 'View All', width=10, command=self.view_command)
        v1.grid(row=3, column=4)

        s2= Button(window, text= 'Search Entry', width=10, command=self.search_command)  
        s2.grid(row=4, column=4)

        a2= Button(window, text= 'Add Entry', width=10, command=self.add_command)
        a2.grid(row=5, column=4)

        u1= Button(window, text= 'Update Entry', width=10, command=self.update2)
        u1.grid(row=6, column=4)

        d1= Button(window, text= 'Delete', width=10, command=self.del_comm)
        d1.grid(row=7, column=4)

        c2= Button(window, text="Close", width=10, command=window.destroy)
        c2.grid(row=9, column=4)

        #Scroll Bar--- this activates the scrolling function of the listbox
        sb1 = Scrollbar(window)
        sb1.grid(row=5, column=3, rowspan=2)

        self.list_box.configure(yscrollcommand= sb1.set)
        sb1.configure(command= self.list_box.yview)

        sb2 = Scrollbar(window)
        sb2.grid(row=5, column=3, rowspan=2)

        self.list_box.configure(xscrollcommand= sb2.set)
        sb2.configure(command= self.list_box.xview)

        #bind is used to bind a function to a widget event(listbox)
        self.list_box.bind('<<ListboxSelect>>', self.get_selected)
    
    def view_command(self):
        '''the function displays all books available in the listbox.
           clears all previous entry in the list box
           iterates through what the view function returns and inserts it into listbox'''
        self.list_box.delete(0,'end')
        for row in db.view():
            self.list_box.insert('end', row)

    def search_command(self):
        '''the function searches for a specified book in the list of books.
           clears all previous entry in the list box
           iterates through what the search function returns and inserts it into listbox if found'''
        self.list_box.delete(0,'end')
        for row in db.search(self.t1_val.get(),self.a1_val.get(),int(self.y1_val.get()),int(self.s1_val.get())):
            self.list_box.delete(0,'end')
            self.list_box.insert('end', row)
            
    def add_command(self):
        '''the function adds a book into the list of books.
           clears all previous entry in the list box
           iterates through what the search function returns and inserts it into listbox if found'''
        db.insert(self.t1_val.get(),self.a1_val.get(),int(self.y1_val.get()),int(self.s1_val.get()))   #gets all values from the entry space
        self.list_box.delete(0,'end')
        self.list_box.insert('end', (self.t1_val.get(),self.a1_val.get(),int(self.y1_val.get()),int(self.s1_val.get())) )

    def get_selected(self,event):
        ''' this is used to view the selected row of listbox in the entry path, the delete method clears previous entry selected from listbox'''
        try:
            global index_val
            Index= self.list_box.curselection()[0]    #returns a tuple showing the index of a select row in the listbox- [0] selects the first index in the tuple
            self.index_val= self.list_box.get(Index)       # returns the content of the selected index and makes it a global variable
            
            self.title.delete(0,'end')
            self.title.insert('end', self.index_val[1])
            self.auth.delete(0,'end')
            self.auth.insert('end', self.index_val[2])
            self.yr.delete(0,'end')
            self.yr.insert('end', self.index_val[3])
            self.isbn.delete(0,'end')
            self.isbn.insert('end', self.index_val[4])
        except IndexError:
            pass
        

    def del_comm(self):
        '''this function makes the delete button delete a row in the listbox, 
           index val is a tuple, index 1 value is used as argument for delete_entry function'''
        try:
            db.delete_entry(self.index_val[0])   #index val is a tuple, index_val[0] represents ID used as argument for delete_entry function
        except NameError:
            print('click view-all button to see all books, \nthen click on one of the items in list box you want to delete before clicking delete button')

    def update2(self):
        '''this function makes the update button alter 
           a book info and updates it in list of books'''
        try:
            db.update(self.index_val[0],self.t1_val.get(),self.a1_val.get(),int(self.y1_val.get()),int(self.s1_val.get()))
        except NameError:
            print('click view-all button to see all books, \nthen click on one of the items in list box you want to update before clicking update button')


window = Tk()                         #creates an empty window widget

buttons=Library_Widget()            #instantiates the Library_Widget class 

window.wm_title('Book_Library')       #gives the window widget a title

window.mainloop()