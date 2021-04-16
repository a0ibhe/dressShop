import tkinter as tk
from tkinter import ttk
import sqlite3
from sqlite3 import Error
import DatabaseClass as db
import time
from tkinter import * 
from tkinter.ttk import *
import smtplib
          


class Container(tk.Tk):
    def __init__(self, *args, **kwargs):        
        tk.Tk.__init__(self, *args, **kwargs)


        self.grid_rowconfigure(0, weight=0)
        self.myFont = ("Arial bold", 16)
        self.myFont2 = ("Arial", 12)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
       
      
        self.frames = {}

        for F in (Dash, customers):
         frame = F(container, self)
         self.frames[F] = frame
         frame.grid(row=0, column=0, sticky="nsew")
         self.show_frame(Dash)
         
         
    def show_frame(self, cont):
       frame = self.frames[cont]
       frame.tkraise()

class Dash(tk.Frame):
   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.configure(background = "HotPink")

       self.grid_rowconfigure(0, weight=0)
       self.myFont = ("Arial bold", 16)
       self.myFont2 = ("Arial", 12)

       #create a frame to hold header (logo, clock, info)
       self.TopFrame = tk.Frame(self, bg = "HotPink")
       self.TopFrame.grid(row = 0, column = 0, sticky = 'nesw')


       #widgets for date & time
       self.time_string = time.strftime('%I:%M:%S:%p')
       self.timeLabel = tk.Label(self.TopFrame, text = self.time_string, font = self.myFont2, bg = "HotPink")
       self.timeLabel.grid(row = 1, column = 5, sticky = "s")
       self.changeClock()

       label = tk.Label(self.TopFrame, text="Staff Dashboard", font = self.myFont, bg = "HotPink")
       label.grid(row = 0, column = 5, pady=10,padx=10, sticky = "nesw")

       # create a frame to hold buttons
       self.ButtonFrame = tk.Frame(self, bg="azure", pady=10)
       self.ButtonFrame.grid(row=1, column=0, sticky='nesw')
          
        # Customer
       self.customersLabel = tk.Label(self, text = 'Customers', font = self.myFont2).grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
       self.photo1 = PhotoImage(file = r"C:\Users\Aoibh\OneDrive\Photos\Saved Pictures\people.png").subsample(6, 6) 
       self.customersButton = ttk.Button(self, text = 'Customers', image = self.photo1, command=lambda: controller.show_frame(customers)).grid(row=3, column=0, padx=5, pady=5, sticky="nsew") 


        # Rentals Btn
       self.rentalsLabel = tk.Label(self, text = 'Rentals', font = self.myFont2).grid(row=2, column=1, padx=5, pady=5, sticky="nsew")
       self.photo2 = PhotoImage(file = r"C:\Users\Aoibh\OneDrive\Photos\Saved Pictures\dress.png").subsample(6, 6) 
       self.rentalsButton = ttk.Button(self, text = 'Rentals', image = self.photo2,  command=lambda: controller.show_frame(Rentals)).grid(row=3, column=1, padx=5, pady=5, sticky="nsew")

        ##Stock
       self.stockLabel = tk.Label(self, text = 'Stock', font = self.myFont2).grid(row=2, column=2, padx=5, pady=5, sticky="nsew")
       self.photo3 = PhotoImage(file = r"C:\Users\Aoibh\OneDrive\Photos\Saved Pictures\stocks.png").subsample(6, 6) 
       self.stockButton = ttk.Button(self, text = 'Stock', image = self.photo3,  command=lambda: controller.show_frame(Stock)).grid(row=3, column=2, padx=5, pady=5, sticky="nsew")

      #deliveries
       self.delLabel = tk.Label(self, text = 'Deliveries', font = self.myFont2).grid(row=4, column=0, padx=5, pady=5, sticky="nsew")
       self.photo4 = PhotoImage(file = r"C:\Users\Aoibh\OneDrive\Photos\Saved Pictures\del.png").subsample(6, 6) 
       self.delButton = ttk.Button(self, text = 'Deliveries', image = self.photo4, command=lambda: controller.show_frame(Deliveries)).grid(row=5, column=0, padx=5, pady=5, sticky="nsew")


        # Email
       self.mailLabel = tk.Label(self, text = 'Email', font = self.myFont2).grid(row=4, column=1, padx=5, pady=5, sticky="nsew")
       self.photo5 = PhotoImage(file = r"C:\Users\Aoibh\OneDrive\Photos\Saved Pictures\email.png").subsample(6, 6) 
       self.mailButton = ttk.Button(self, text = 'Email', image = self.photo5, command=lambda: controller.show_frame(Email)).grid(row=5, column=1, padx=5, pady=5, sticky="nsew")

        ##   Account
       self.accLabel = tk.Label(self, text = 'Account', font = self.myFont2).grid(row=4, column=2, padx=5, pady=5, sticky="nsew")
       self.photo6 = PhotoImage(file = r"C:\Users\Aoibh\OneDrive\Photos\Saved Pictures\acc.png").subsample(6, 6) 
       self.accButton = ttk.Button(self, text = 'Account', image = self.photo6, command=lambda: controller.show_frame(Account)).grid(row=5, column=2, padx=5, pady=5, sticky="nsew")



   def changeClock(self):
        # method to update the clock time
       self.time2 = time.strftime('%H:%M:%S:%p')
       self.timeLabel.configure(text=self.time2)
       self.TopFrame.after(200, self.changeClock)

class BasicWidget:
   def __init__(self, master, text, row, column):
      self.master = master
      self.text = text
      self.row = row
      self.column = column
      self.label =tk.Label(self.master, text = self.text)
      self.label.grid(row =self.row, column = self.column, padx = 5, pady = 5, sticky = "we")
      self.entryVar = tk.StringVar()
      self.entry = tk.Entry(self.master, textvariable = self.entryVar)
      self.entry.grid(row =self.row, column = self.column+1, padx = 5, pady = 5, sticky = "we")
       

#Class for CRUD for the customer details
class customers(tk.Frame):
   def __init__(self, parent, controller):
      self.controller = controller
      self.row = 0
      self.column = 0
      self.myFont = ("Arial bold", 16)
      self.myFont2 = ("Arial", 12)
      
      tk.Frame.__init__(self, parent)
      self.configure(background = "HotPink")
      self.myFont = ("Arial bold", 12)
      title = tk.Label(self,  text = "Customers", font = self.myFont, bg = "HotPink").grid(row = self.row, column = self.column, padx = 5, pady =5)
      self.column+=1

      self.myDB = db.Database("CUSTOMERS.db")
      self.CUSTOMERSFields = self.myDB.getFields("CUSTOMERS")
      CUSTOMERSFields = self.CUSTOMERSFields

      for f in CUSTOMERSFields:
         wid = BasicWidget(self, f, self.row, self.column +1)
         self.row+=1

      #creates treeview for customers
      self.tree = ttk.Treeview(self, columns = (CUSTOMERSFields))
      #sets vertical scrollbar
      vsb = ttk.Scrollbar(self, orient ="vertical", command =self.tree.yview)
      vsb.grid(row = self.row, column = 11, sticky = 'nsew')
      self.tree.configure(yscrollcommand=vsb.set)
      self.tree.grid(row=self.row, column=1, columnspan=10, sticky ='nsew')

      #creates headings
      for field in range(0, len(CUSTOMERSFields)):
         self.tree.heading(f'#{field}', text=CUSTOMERSFields[field])
         self.tree.column(f'#{field}', stretch=tk.FALSE, minwidth=75, width=100)
      self.populateTree(self.myDB.getAll("CUSTOMERS"))
      self.row+=1
      self.tree.bind('<ButtonRelease-1>', self.populateWidgets)

       #creates buttons
      self.buttons = ["Search", "Add", "Update", "Delete", "Back"]

      self.searchBox = ttk.Entry(self)
      self.searchBox.insert(0, "Enter Name: ")
      self.searchBox.grid(row = self.row, column = self.column, padx = 5, pady =5, sticky = "we")
      self.searchBox.bind('<Button-1>',  self.clear)
      self.column+=1

      for i in range(0, len(self.buttons)):
         self.navButton = ttk.Button(self, text = self.buttons[i], command = lambda x=self.buttons[i]:self.crud(x))
         self.navButton.grid(row = self.row, column = self.column, padx = 5, pady =5, sticky = "we")
         self.column+=1

   def crud(self, txt):
      if txt == "Search":
         self.search()
      if txt == "Add":
         self.addWindow()
      if txt == "Update":
         self.update()
      if txt == "Delete":
         self.delete()
      if txt == "Back":
         self.controller.show_frame(Dash)

  #Allows you to search for a customer
   def search(self):
      self.myDB = db.Database("CUSTOMERS.db")
      searchCriteria = self.searchBox.get()
      results = self.myDB.retrieveData("CUSTOMERS", "customerForename", searchCriteria)
      self.populateTree(results)
      self.myDB.close()

   def addWindow(self):    
      self.addwindow = tk.Toplevel()
      for i in range(1, len(self.CUSTOMERSFields)):
         BasicWidget(self.addwindow, self.CUSTOMERSFields[i], i, 0)
      self.addButton = ttk.Button(self.addwindow, text = "Add", command = self.addRecord)
      self.addButton.grid(row = len(self.CUSTOMERSFields)+1, column = 0, padx = 5, pady =5, sticky = "we")
      self.closeButton = ttk.Button(self.addwindow, text = "close", command = self.addwindow.destroy)
      self.closeButton.grid(row = len(self.CUSTOMERSFields)+1, column = 1, padx = 5, pady =5, sticky = "we")

   def addRecord(self):
      self.wids = self.addwindow.winfo_children()
      data =  [wid.get() for wid in self.wids if type(wid) == tk.Entry]
      self.myDB = db.Database("CUSTOMERS.db")
      self.myDB.createData("CUSTOMERS", data)
      self.populateTree(self.myDB.getAll("CUSTOMERS"))
      self.myDB.close()
      entryWids = [wid for wid in self.wids if type(wid) == tk.Entry]
      for wid in entryWids:
         wid.delete(0, "end")
      self.addwindow.destroy()

   def update(self):
      self.myDB = db.Database("CUSTOMERS.db")
      fields = self.myDB.getFields("CUSTOMERS")
      self.wids = self.winfo_children()
      data = [wid.get() for wid in self.wids if type(wid) == tk.Entry]
      for i in range (1, len(fields)):
         self.myDB.updateData("CUSTOMERS", fields[i], data[i], fields[0], data[0])
      self.populateTree(self.myDB.getAll("CUSTOMERS"))
      self.myDB.close()
      
   def delete(self):
      curItem = self.tree.focus()
      id = self.tree.item(curItem)['text']
      self.myDB = db.Database("CUSTOMERS.db")
      self.myDB.deleteRecord("customerID", "CUSTOMERS", id)
      self.populateTree(self.myDB.getAll("CUSTOMERS"))
      self.myDB.close()
      

   #adds entities to tree
   def populateTree(self, data):
      self.tree.delete(*self.tree.get_children())
      for record in data:
         self.tree.insert("", "end", text = str(record[0]), values = (record[1],  record[2],  record[3], record[4],  record[5],  record[6], record[7],  record[8],  record[9], record[10]))
      self.myDB.close()

   #allows you to edit entities by clicking on tree
   def populateWidgets(self, evt): 
      self.wids = self.winfo_children()
      EntryWidgets = [wid for wid in self.wids if type(wid)==tk.Entry]
      for widget in EntryWidgets:
         widget.delete(0,"end")
      curItem = self.tree.focus()
      id = self.tree.item(curItem)['text']
      record = self.tree.item(curItem)['values']
      EntryWidgets[0].insert(0, id)
      for i in range(0, len(EntryWidgets)-1):
         EntryWidgets[i+1].insert(0, record[i])

   def clear(self, evf):
      self.searchBox.delete(0, "end")


class Rentals(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        self.row = 0
        self.column = 0
        self.myFont = ("Arial bold", 16)
        self.myFont2 = ("Arial", 12)
          
        tk.Frame.__init__(self, parent)
        self.configure(background = "HotPink")
        self.myFont = ("Arial bold", 12)
        title2 = tk.Label(self,  text = "Rentals", font = self.myFont, bg = "HotPink").grid(row = self.row, column = self.column, padx = 5, pady =5)
        self.column+=1

        self.myDB = db.Database("RENTALS.db")
        self.RENTALSFields = self.myDB.getFields("RENTALS")
        RENTALSFields = self.RENTALSFields

        for f in RENTALSFields:
            wid = BasicWidget(self, f, self.row, self.column +1)
            self.row+=1

          #creates treeview for rentals
        self.tree = ttk.Treeview(self, columns = (RENTALSFields))
          #sets vertical scrollbar
        vsb = ttk.Scrollbar(self, orient ="vertical", command =self.tree.yview)
        vsb.grid(row = self.row, column = 11, sticky = 'nsew')
        self.tree.configure(yscrollcommand=vsb.set)
        self.tree.grid(row=self.row, column=1, columnspan=10, sticky ='nsew')

          #creates headings
        for field in range(0, len(RENTALSFields)):
            self.tree.heading(f'#{field}', text=RENTALSFields[field])
            self.tree.column(f'#{field}', stretch=tk.FALSE, minwidth=75, width=100)
        self.populateTree(self.myDB.getAll("RENTALS"))
        self.row+=1
        self.tree.bind('<ButtonRelease-1>', self.populateWidgets)

          #creates buttons
        self.buttons = ["Search", "Add", "Update", "Delete", "Back"]
        self.searchBox = ttk.Entry(self)
        self.searchBox.insert(0, "Enter Name: ")
        self.searchBox.grid(row = self.row, column = self.column, padx = 5, pady =5, sticky = "we")
        self.searchBox.bind('<Button-1>',  self.clear)
        self.column+=1

        for i in range(0, len(self.buttons)):
            self.navButton = ttk.Button(self, text = self.buttons[i], command = lambda x=self.buttons[i]:self.crud(x))
            self.navButton.grid(row = self.row, column = self.column, padx = 5, pady =5, sticky = "we")
            self.column+=1

    def crud(self, txt):
     if txt == "Search":
        self.search()
     if txt == "Add":
        self.addWindow()
     if txt == "Update":
        self.update()
     if txt == "Delete":
        self.delete()
     if txt == "Back":
        self.controller.show_frame(Dash)

 #Allows you to search for a rental
    def search(self):
        self.myDB = db.Database("RENTALS.db")
        searchCriteria = self.searchBox.get()
        results = self.myDB.retrieveData("RENTALS", "customerID", searchCriteria)
        self.populateTree(results)
        self.myDB.close()

    def addWindow(self):
     self.addwindow = tk.Toplevel()
     for i in range(1, len(self.RENTALSFields)):
        BasicWidget(self.addwindow, self.RENTALSFields[i], i, 0)
     self.addButton = ttk.Button(self.addwindow, text = "Add", command = self.addRecord)
     self.addButton.grid(row = len(self.RENTALSFields)+1, column = 0, padx = 5, pady =5, sticky = "we")
     self.closeButton = ttk.Button(self.addwindow, text = "close", command = self.addwindow.destroy)
     self.closeButton.grid(row = len(self.RENTALSFields)+1, column = 1, padx = 5, pady =5, sticky = "we")

    def addRecord(self):
        self.wids = self.addwindow.winfo_children()
        data =  [wid.get() for wid in self.wids if type(wid) == tk.Entry]
        self.myDB = db.Database("RENTALS.db")
        self.myDB.createData("RENTALS", data)
        self.populateTree(self.myDB.getAll("RENTALS"))
        self.myDB.close()
        entryWids = [wid for wid in self.wids if type(wid) == tk.Entry]
        for wid in entryWids:
            wid.delete(0, "end")
        self.addwindow.destroy()

    def update(self):
     self.myDB = db.Database("RENTALS.db")
     fields = self.myDB.getFields("RENTALS")
     self.wids = self.winfo_children()
     data = [wid.get() for wid in self.wids if type(wid) == tk.Entry]
     for i in range (1, len(fields)):
        self.myDB.updateData("RENTALS", fields[i], data[i], fields[0], data[0])
     self.populateTree(self.myDB.getAll("RENTALS"))
     self.myDB.close()

    def delete(self):
     curItem = self.tree.focus()
     id = self.tree.item(curItem)['text']
     self.myDB = db.Database("RENTALS.db")
     self.myDB.deleteRecord("RentalID", "RENTALS", id)
     self.populateTree(self.myDB.getAll("RENTALS"))
     self.myDB.close()


  #adds entities to tree
    def populateTree(self, data):
     self.tree.delete(*self.tree.get_children())
     for record in data:
        self.tree.insert("", "end", text = str(record[0]), values = (record[1],  record[2],  record[3], record[4],  record[5],  record[6], record[7],  record[8],  record[9], record[10]))
     self.myDB.close()

  #allows you to edit entities by clicking on tree
    def populateWidgets(self, evt):
     self.wids = self.winfo_children()
     EntryWidgets = [wid for wid in self.wids if type(wid)==tk.Entry]
     for widget in EntryWidgets:
        widget.delete(0,"end")
     curItem = self.tree.focus()
     id = self.tree.item(curItem)['text']
     record = self.tree.item(curItem)['values']
     EntryWidgets[0].insert(0, id)
     for i in range(0, len(EntryWidgets)-1):
        EntryWidgets[i+1].insert(0, record[i])

    def clear(self, evf):
     self.searchBox.delete(0, "end")


class Stock(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        self.row = 0
        self.column = 0
        self.myFont = ("Arial bold", 16)
        self.myFont2 = ("Arial", 12)

        tk.Frame.__init__(self, parent)
        self.configure(background="HotPink")
        self.myFont = ("Arial bold", 12)
        title2 = tk.Label(self, text="Stock", font=self.myFont, bg="HotPink").grid(row=self.row, column=self.column,padx=5, pady=5)
        self.column += 1

        self.myDB = db.Database("STOCK.db")
        self.STOCKFields = self.myDB.getFields("STOCK")
        STOCKFields = self.STOCKFields

        for f in STOCKFields:
            wid = BasicWidget(self, f, self.row, self.column + 1)
            self.row += 1

        self.tree = ttk.Treeview(self, columns=(STOCKFields))
        vsb = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        vsb.grid(row=self.row, column=11, sticky='nsew')
        self.tree.configure(yscrollcommand=vsb.set)
        self.tree.grid(row=self.row, column=1, columnspan=10, sticky='nsew')

        # creates headings
        for field in range(0, len(STOCKFields)):
            self.tree.heading(f'#{field}', text=STOCKFields[field])
            self.tree.column(f'#{field}', stretch=tk.FALSE, minwidth=75, width=100)
        self.populateTree(self.myDB.getAll("STOCK"))
        self.row += 1
        self.tree.bind('<ButtonRelease-1>', self.populateWidgets)

        # creates buttons
        self.buttons = ["Search", "Add", "Update", "Delete", "Back"]
        self.searchBox = ttk.Entry(self)
        self.searchBox.insert(0, "Enter Name: ")
        self.searchBox.grid(row=self.row, column=self.column, padx=5, pady=5, sticky="we")
        self.searchBox.bind('<Button-1>', self.clear)
        self.column += 1

        for i in range(0, len(self.buttons)):
            self.navButton = ttk.Button(self, text=self.buttons[i], command=lambda x=self.buttons[i]: self.crud(x))
            self.navButton.grid(row=self.row, column=self.column, padx=5, pady=5, sticky="we")
            self.column += 1

    def crud(self, txt):
        if txt == "Search":
            self.search()
        if txt == "Add":
            self.addWindow()
        if txt == "Update":
            self.update()
        if txt == "Delete":
            self.delete()
        if txt == "Back":
            self.controller.show_frame(Dash)

    # Allows you to search for a rental
    def search(self):
        self.myDB = db.Database("STOCK.db")
        searchCriteria = self.searchBox.get()
        results = self.myDB.retrieveData("STOCK", "ItemID", searchCriteria)
        self.populateTree(results)
        self.myDB.close()

    def addWindow(self):
        self.addwindow = tk.Toplevel()
        for i in range(1, len(self.STOCKFields)):
            BasicWidget(self.addwindow, self.RENTALSFields[i], i, 0)
        self.addButton = ttk.Button(self.addwindow, text="Add", command=self.addRecord)
        self.addButton.grid(row=len(self.STOCKFields) + 1, column=0, padx=5, pady=5, sticky="we")
        self.closeButton = ttk.Button(self.addwindow, text="close", command=self.addwindow.destroy)
        self.closeButton.grid(row=len(self.STOCKFields) + 1, column=1, padx=5, pady=5, sticky="we")

    def addRecord(self):
        self.wids = self.addwindow.winfo_children()
        data = [wid.get() for wid in self.wids if type(wid) == tk.Entry]
        self.myDB = db.Database("STOCK.db")
        self.myDB.createData("STOCK", data)
        self.populateTree(self.myDB.getAll("STOCK"))
        self.myDB.close()
        entryWids = [wid for wid in self.wids if type(wid) == tk.Entry]
        for wid in entryWids:
            wid.delete(0, "end")
        self.addwindow.destroy()

    def update(self):
        self.myDB = db.Database("STOCK.db")
        fields = self.myDB.getFields("STOCK")
        self.wids = self.winfo_children()
        data = [wid.get() for wid in self.wids if type(wid) == tk.Entry]
        for i in range(1, len(fields)):
            self.myDB.updateData("STOCK", fields[i], data[i], fields[0], data[0])
        self.populateTree(self.myDB.getAll("STOCK"))
        self.myDB.close()

    def delete(self):
        curItem = self.tree.focus()
        id = self.tree.item(curItem)['text']
        self.myDB = db.Database("STOCK.db")
        self.myDB.deleteRecord("ItemID", "STOCK", id)
        self.populateTree(self.myDB.getAll("STOCK"))
        self.myDB.close()

    # adds entities to tree
    def populateTree(self, data):
        self.tree.delete(*self.tree.get_children())
        for record in data:
            self.tree.insert("", "end", text=str(record[0]), values=(
            record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9],
            record[10]))
        self.myDB.close()

    # allows you to edit entities by clicking on tree
    def populateWidgets(self, evt):
        self.wids = self.winfo_children()
        EntryWidgets = [wid for wid in self.wids if type(wid) == tk.Entry]
        for widget in EntryWidgets:
            widget.delete(0, "end")
        curItem = self.tree.focus()
        id = self.tree.item(curItem)['text']
        record = self.tree.item(curItem)['values']
        EntryWidgets[0].insert(0, id)
        for i in range(0, len(EntryWidgets) - 1):
            EntryWidgets[i + 1].insert(0, record[i])

    def clear(self, evf):
        self.searchBox.delete(0, "end")



class Deliveries(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        self.row = 0
        self.column = 0
        self.myFont = ("Arial bold", 16)
        self.myFont2 = ("Arial", 12)

        tk.Frame.__init__(self, parent)
        self.configure(background="HotPink")
        self.myFont = ("Arial bold", 12)
        title2 = tk.Label(self, text="Deliveries", font=self.myFont, bg="HotPink").grid(row=self.row, column=self.column,padx=5, pady=5)
        self.column += 1

        self.myDB = db.Database("DELIVERIES.db")
        self.DELIVERIESFields = self.myDB.getFields("DELIVERIES")
        DELIVERIESFields = self.DELIVERIESFields

        for f in DELIVERIESFields:
            wid = BasicWidget(self, f, self.row, self.column + 1)
            self.row += 1

        self.tree = ttk.Treeview(self, columns=(DELIVERIESFields))
        vsb = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        vsb.grid(row=self.row, column=11, sticky='nsew')
        self.tree.configure(yscrollcommand=vsb.set)
        self.tree.grid(row=self.row, column=1, columnspan=10, sticky='nsew')

        for field in range(0, len(DELIVERIESFields)):
            self.tree.heading(f'#{field}', text=DELIVERIESFields[field])
            self.tree.column(f'#{field}', stretch=tk.FALSE, minwidth=75, width=100)
        self.populateTree(self.myDB.getAll("DELIVERIES"))
        self.row += 1
        self.tree.bind('<ButtonRelease-1>', self.populateWidgets)

        self.buttons = ["Search", "Add", "Update", "Delete", "Back"]
        self.searchBox = ttk.Entry(self)
        self.searchBox.insert(0, "Enter Name: ")
        self.searchBox.grid(row=self.row, column=self.column, padx=5, pady=5, sticky="we")
        self.searchBox.bind('<Button-1>', self.clear)
        self.column += 1

        for i in range(0, len(self.buttons)):
            self.navButton = ttk.Button(self, text=self.buttons[i], command=lambda x=self.buttons[i]: self.crud(x))
            self.navButton.grid(row=self.row, column=self.column, padx=5, pady=5, sticky="we")
            self.column += 1

    def crud(self, txt):
        if txt == "Search":
            self.search()
        if txt == "Add":
            self.addWindow()
        if txt == "Update":
            self.update()
        if txt == "Delete":
            self.delete()
        if txt == "Back":
            self.controller.show_frame(Dash)

    def search(self):
        self.myDB = db.Database("DELIVERIES.db")
        searchCriteria = self.searchBox.get()
        results = self.myDB.retrieveData("DELIVERIES", "DeliveryID", searchCriteria)
        self.populateTree(results)
        self.myDB.close()

    def addWindow(self):
        self.addwindow = tk.Toplevel()
        for i in range(1, len(self.STOCKFields)):
            BasicWidget(self.addwindow, self.RENTALSFields[i], i, 0)
        self.addButton = ttk.Button(self.addwindow, text="Add", command=self.addRecord)
        self.addButton.grid(row=len(self.DELIVERIESFields) + 1, column=0, padx=5, pady=5, sticky="we")
        self.closeButton = ttk.Button(self.addwindow, text="close", command=self.addwindow.destroy)
        self.closeButton.grid(row=len(self.DELIVERIESFields) + 1, column=1, padx=5, pady=5, sticky="we")

    def addRecord(self):
        self.wids = self.addwindow.winfo_children()
        data = [wid.get() for wid in self.wids if type(wid) == tk.Entry]
        self.myDB = db.Database("STOCK.db")
        self.myDB.createData("STOCK", data)
        self.populateTree(self.myDB.getAll("STOCK"))
        self.myDB.close()
        entryWids = [wid for wid in self.wids if type(wid) == tk.Entry]
        for wid in entryWids:
            wid.delete(0, "end")
        self.addwindow.destroy()

    def update(self):
        self.myDB = db.Database("DELIVERIES.db")
        fields = self.myDB.getFields("DELIVERIES")
        self.wids = self.winfo_children()
        data = [wid.get() for wid in self.wids if type(wid) == tk.Entry]
        for i in range(1, len(fields)):
            self.myDB.updateData("DELIVERIES", fields[i], data[i], fields[0], data[0])
        self.populateTree(self.myDB.getAll("DELIVERIES"))
        self.myDB.close()

    def delete(self):
        curItem = self.tree.focus()
        id = self.tree.item(curItem)['text']
        self.myDB = db.Database("DELIVERIES.db")
        self.myDB.deleteRecord("DeliveryID", "DELIVERIES", id)
        self.populateTree(self.myDB.getAll("DELIVERIES"))
        self.myDB.close()

    # adds entities to tree
    def populateTree(self, data):
        self.tree.delete(*self.tree.get_children())
        for record in data:
            self.tree.insert("", "end", text=str(record[0]), values=(
            record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9],
            record[10]))
        self.myDB.close()

    # allows you to edit entities by clicking on tree
    def populateWidgets(self, evt):
        self.wids = self.winfo_children()
        EntryWidgets = [wid for wid in self.wids if type(wid) == tk.Entry]
        for widget in EntryWidgets:
            widget.delete(0, "end")
        curItem = self.tree.focus()
        id = self.tree.item(curItem)['text']
        record = self.tree.item(curItem)['values']
        EntryWidgets[0].insert(0, id)
        for i in range(0, len(EntryWidgets) - 1):
            EntryWidgets[i + 1].insert(0, record[i])

    def clear(self, evf):
        self.searchBox.delete(0, "end")

class Email(tk.Frame):
    def __init__(self, parent, controller):
      
        tk.Frame.__init__(self, parent)
        self.configure(background = "Thistle")
        self.myFont = ("Arial bold", 16)
        self.myFont2 = ("Arial", 12)
        title = tk.Label(self,  text = "Email", font = self.myFont, bg = "HotPink").grid(row = 0, column = 1, padx = 5, pady =5)

    def sendEmail(self):
        self.addressInfo = address.get()
        self.emailTextInfo = emailText.get()
        print(self.addressInfo, self.emailBodyInfo)
        self.email = "aoibhesdressshop@gmail.com"
        self.password = "DressShop15"
        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        self.server.starttls()
        self.server.login(self.email, self.password)
        self.server.sendmail(self.email, self.addressInfo, self.emailTextInfo)
        print("Message sent")
        self.addressEntry.delete(0, END)
        self.emailText.delete(0, END)

    def widgets(self):
        self.recipientEmail = Label(text="Recipient's Email' :")
        self.emailText= Label(text="Message :")
        self.recipientEmail.place(x=15, y=70)
        self.emailTextEntry.place(x=15, y=140)
        self.address = StringVar()
        self.emailText = StringVar()
        self.emailEntry = Entry(textvariable=address, width="30").place(x=15, y=100)
        self.emailTextEntry = Entry(textvariable=email_body, width="30").place(x=15, y=180)
        button = tk.Button(self, text="Send Message", command=sendEmail()).pack()

        

if __name__ =="__main__":
    staffDashboard = Container()
    staffDashboard.state('zoomed')
    staffDashboard.configure(background='HotPink')
    s = ttk.Style()
    s.configure('TNotebook.Tab', font=('Arial', '14'))
    s.theme_use('clam')
    s.configure('TButton', background = 'light grey', foreground = 'black', width = 20, borderwidth=1, focusthickness=3, focuscolor='none')
    s.map('TButton', background=[('active','HotPink')])
    s.configure("TMenubutton", background="HotPink")
    staffDashboard.mainloop()
