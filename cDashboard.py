import tkinter as tk
import tkinter as tk
from tkinter import ttk
import sqlite3
from sqlite3 import Error
import DatabaseClass as db
import time
from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
from io import BytesIO

class Container(tk.Tk):
    def __init__(self, *args, **kwargs):        
        tk.Tk.__init__(self, *args, **kwargs)

        self.grid_rowconfigure(0, weight=0)
        self.myFont = ("Arial bold", 16)
        self.myFont2 = ("Arial", 12)

        #creates frame for header
        self.TopFrame = tk.Frame(self, bg = "HotPink")
        self.TopFrame.grid(row = 0, column = 0, sticky = 'we')

        #widgets for time
        self.time_string = time.strftime('%I:%M:%S:%p')
        self.timeLabel = tk.Label(self.TopFrame, text = self.time_string, font = self.myFont, bg="HotPink")
        self.timeLabel.grid(row = 0, column = 2, sticky = "we")
        self.changeClock()

        label = tk.Label(self.TopFrame, text="Aoibhe's Boutique", font = self.myFont, bg="HotPink")
        label.grid(row = 0, column = 1, pady=10,padx=10, sticky = "nw")

        #creates frame to hold buttons
        self.ButtonFrame = tk.Frame(self, bg="white", pady=10)
        self.ButtonFrame.grid(row=1, column=0, sticky='we')

        #home button
        btnHome = ttk.Button(self.ButtonFrame, text="Home", command=lambda: self.show_frame(Home))
        btnHome.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

        #dresses button
        btnCust = ttk.Button(self.ButtonFrame, text="Dresses", command=lambda: self.show_frame(Dresses))
        btnCust.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")


        #contact form button
        btnOrders = ttk.Button(self.ButtonFrame, text="Contact Us", command=lambda: self.show_frame(Contact))
        btnOrders.grid(row=0, column=3, padx=5, pady=5, sticky="nsew")

        #account button
        btnSupplier = ttk.Button(self.ButtonFrame, text="Account", command=lambda: self.show_frame(Account))
        btnSupplier.grid(row=0, column=4, padx=5, pady=5, sticky="nsew")

        #quit button
        btnQuit = ttk.Button(self.ButtonFrame, text="Quit", command=self.destroy)
        btnQuit.grid(row=0, column=5, padx=5, pady=5, sticky="nsew")

        container = tk.Frame(self, bg="HotPink")
        container.grid(column=0, row=2,sticky = "nsew")
        container.grid_rowconfigure(1, weight = 1)

        #dictionary to hold windows
        self.frames = {}

        for F in (Home, Dresses, Contact, Account):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="wens")
        self.show_frame(Home)
        
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def get_page(self, page_class):
        return self.frames[page_class]

    def changeClock(self):
        self.time2 = time.strftime('%H:%M:%S:%p')
        self.timeLabel.configure(text=self.time2)
        self.TopFrame.after(200, self.changeClock)

class BasicWidget():
    def __init__(self, master, text, row, column):
        self.master = master
        self.text = text
        self.row = row
        self.column = column
        self.label = tk.Label(self.master, text=self.text)
        self.label.grid(row=self.row, column=self.column, padx=5, pady=5, sticky="we")
        self.entryVar = tk.StringVar()
        self.entry = tk.Entry(self.master, textvariable=self.entryVar)
        self.entry.grid(row=self.row, column=self.column + 1, padx=5, pady=5, sticky="we")

class Home(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background="HotPink")

        self.grid_rowconfigure(0, weight=0)
        self.myFont = ("Arial bold", 16)
        self.myFont2 = ("Arial bold", 14)

        label = tk.Label(self, text="Welcome!", font=self.myFont, bg="HotPink")
        label.grid(row=0, column=2, pady=10, padx=10, sticky="nesw")

        #Logo
        self.logo = PhotoImage(file=r"C:\Users\Aoibh\OneDrive\Photos\Saved Pictures\logo.png")
        self.logoButton = ttk.Button(self, text='Logo', image=self.logo, command=lambda: controller.show_frame(Home)).grid(row=2, column=2, padx=5, pady=5, sticky="nsew")

        #Welcome message
        message = tk.Label(self, text="About Us"
                                      "\n Aoibhe's Boutique is a formal dress rental store located in Belfast. "
                                      "\n We offer a wide range of dresses which can be rented for up to 3 days."
                                      "\n Browse our dresses online or call to book an appointment to view our in store showroom."
                                      "\n After renting, simply return the dress on the agreed date!", font=self.myFont2, bg="HotPink")
        message.grid(row=3, column=2, pady=10, padx=10, sticky="nesw")

        #Logo
        self.map = PhotoImage(file=r"C:\Users\Aoibh\OneDrive\Photos\Saved Pictures\map.png").subsample(2, 2)
        self.mapButton = ttk.Button(self, text='Logo', image=self.map, command=lambda: controller.show_frame(Home)).grid(row=4, column=2, padx=5, pady=5, sticky="nsew")


class Dresses(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background="HotPink")

        self.grid_rowconfigure(0, weight=0)
        self.myFont = ("Arial bold", 16)
        self.priceFont = ("Arial", 8)

        titleLabel = tk.Label(self, text="Place rental", font=self.myFont, bg="HotPink")
        titleLabel.grid(row=0, column=6, pady=10, padx=10, sticky="nesw")

        myDB = db.Database("database.db")
        self.basket = []
        basket = self.basket

        #Dress One
        self.imgLabel = tk.Label(self)
        primaryKey = myDB.getPrimaryKey("ItemID", "Stock")
        self.render = Image.open(BytesIO(myDB.getItemPictures(primaryKey[0] [0])))
        self.render = self.render.resize((100, 100), Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(self.render)

        label = tk.Label(self, text="£45 per day", font=self.priceFont, bg="white")
        self.dressPrice = tk.StringVar()
        self.dressPrice.set(45)
        label.grid(row=2, column=6, pady=0, padx=10, sticky="nesw")

        sizeVar = tk.StringVar(self)
        sizeVar.set("-")
        entrySize = tk.OptionMenu(self, sizeVar, "S", "M", "L").grid(row=3, column=6, pady=10, padx=10, sticky="nw")

        self.days = tk.StringVar
        entryDays = tk.Spinbox(self, from_=0, to=3, textvariable=self.days).grid(row=4, column=6, pady=10, padx=10, sticky="nw")
        self.days.get(self)

        self.dressButton = ttk.Button(self, text='Pink Dress', image= self.image, command= lambda:  self.rentDress(self.dressPrice, 5))
        self.dressButton.grid(row=1, column=6, padx=10, pady=10, sticky="nsew")


        #Dress Two
        self.imgLabel2 = tk.Label(self)
        primaryKey2 = myDB.getPrimaryKey("ItemID", "Stock")
        self.render2 = Image.open(BytesIO(myDB.getItemPictures(primaryKey2[1] [0])))
        self.render2 = self.render2.resize((100, 100), Image.ANTIALIAS)
        self.image2 = ImageTk.PhotoImage(self.render2)
        self.dressButton2 = ttk.Button(self, text='Account', image=self.image2)
        self.dressButton2.grid(row=1, column=7, pady=10, padx=10, sticky="nesw")

        label2 = tk.Label(self, text="£40 per day", font=self.priceFont, bg="white")
        label2.grid(row=2, column=7, pady=0, padx=10, sticky="nesw")

        sizeVar2 = tk.StringVar(self)
        sizeVar2.set("-")
        entrySize2 = tk.OptionMenu(self, sizeVar2, "S", "M", "L").grid(row=3, column=7, pady=10, padx=10, sticky="nw")

        qtyVar2 = tk.StringVar()
        entryQty2 = tk.Spinbox(self, from_=0, to=3, textvariable=qtyVar2).grid(row=4, column=7, pady=10, padx=10, sticky="nw")

        #Dress Three
        self.imgLabel3 = tk.Label(self)
        primaryKey3 = myDB.getPrimaryKey("ItemID", "Stock")
        self.render3 = Image.open(BytesIO(myDB.getItemPictures(primaryKey3[2][0])))
        self.render3 = self.render3.resize((100, 100), Image.ANTIALIAS)
        self.image3 = ImageTk.PhotoImage(self.render3)

        self.dressButton3 = ttk.Button(self, text='Account', image=self.image3,command=lambda: controller.show_frame(Dresses))
        self.dressButton3.grid(row=1, column=8, pady=10, padx=10, sticky="nesw")

        label3 = tk.Label(self, text="£55 per day", font=self.priceFont, bg="white")
        label3.grid(row=2, column=8, pady=0, padx=10, sticky="nesw")

        sizeVar3 = tk.StringVar(self)
        sizeVar3.set("-")
        entrySize3 = tk.OptionMenu(self, sizeVar3, "S", "M", "L").grid(row=3, column=8, pady=10, padx=10, sticky="nw")

        qtyVar3 = tk.StringVar()
        entryQty3 = tk.Spinbox(self, from_=0, to=3, textvariable=qtyVar3).grid(row=4, column=8, pady=10, padx=10, sticky="nw")

        #Dress Four
        self.imgLabel4 = tk.Label(self)
        self.imgLabel4.grid(row=1, column=9, pady=10, padx=10, sticky="nesw")
        primaryKey4 = myDB.getPrimaryKey("ItemID", "Stock")
        self.render4 = Image.open(BytesIO(myDB.getItemPictures(primaryKey4[3][0])))
        self.render4 = self.render4.resize((100, 100), Image.ANTIALIAS)
        self.image4 = ImageTk.PhotoImage(self.render4)
        self.imgLabel4.configure(image=self.image4)

        self.dressButton4 = ttk.Button(self, text='Account', image=self.image4,command=lambda: controller.show_frame(Dresses))
        self.dressButton4.grid(row=1, column=9, pady=10, padx=10, sticky="nesw")

        label4 = tk.Label(self, text="£40 per day", font=self.priceFont, bg="white")
        label4.grid(row=2, column=9, pady=0, padx=10, sticky="nesw")

        sizeVar4 = tk.StringVar(self)
        sizeVar4.set("-")
        entrySize4 = tk.OptionMenu(self, sizeVar4, "S", "M", "L").grid(row=3, column=9, pady=10, padx=10, sticky="nw")

        qtyVar4 = tk.StringVar()
        entryQty4 = tk.Spinbox(self, from_=0, to=3, textvariable=qtyVar4).grid(row=4, column=9, pady=10, padx=10, sticky="nw")

        #Dress Five
        self.imgLabel5 = tk.Label(self)
        self.imgLabel5.grid(row=1, column=10, pady=10, padx=10, sticky="nesw")
        primaryKey5 = myDB.getPrimaryKey("ItemID", "Stock")
        self.render5 = Image.open(BytesIO(myDB.getItemPictures(primaryKey5[4][0])))
        self.render5 = self.render5.resize((100, 100), Image.ANTIALIAS)
        self.image5 = ImageTk.PhotoImage(self.render5)
        self.imgLabel5.configure(image=self.image5)

        self.dressButton5 = ttk.Button(self, text='Account', image=self.image5,command=lambda: controller.show_frame(Dresses))
        self.dressButton5.grid(row=1, column=10, pady=10, padx=10, sticky="nesw")

        label5 = tk.Label(self, text="£55 per day", font=self.priceFont, bg="white")
        label5.grid(row=2, column=10, pady=0, padx=10, sticky="nesw")

        sizeVar5 = tk.StringVar(self)
        sizeVar5.set("-")
        entrySize5 = tk.OptionMenu(self, sizeVar5, "S", "M", "L").grid(row=3, column=10, pady=10, padx=10, sticky="nw")

        qtyVar5 = tk.StringVar()
        entryQty5 = tk.Spinbox(self, from_=0, to=3, textvariable=qtyVar5).grid(row=4, column=10, pady=10, padx=10, sticky="nw")

        #Dress Six
        self.imgLabel6 = tk.Label(self)
        primaryKey6 = myDB.getPrimaryKey("ItemID", "Stock")
        self.render6 = Image.open(BytesIO(myDB.getItemPictures(primaryKey6[5][0])))
        self.render6 = self.render6.resize((100, 100), Image.ANTIALIAS)
        self.image6 = ImageTk.PhotoImage(self.render6)

        self.dressButton6 = ttk.Button(self, text='Account', image=self.image6,command=lambda: controller.show_frame(Dresses))
        self.dressButton6.grid(row=5, column=6, pady=10, padx=10, sticky="nesw")

        label6 = tk.Label(self, text="£45 per day", font=self.priceFont, bg="white")
        label6.grid(row=6, column=6, pady=0, padx=10, sticky="nesw")

        sizeVar6 = tk.StringVar(self)
        sizeVar6.set("-")
        entrySize6 = tk.OptionMenu(self, sizeVar6, "S", "M", "L").grid(row=7, column=6, pady=10, padx=10, sticky="nw")

        qtyVar6 = tk.StringVar()
        entryQty6 = tk.Spinbox(self, from_=0, to=3, textvariable=qtyVar6).grid(row=8, column=6, pady=10, padx=10, sticky="nw")

        #Dress Seven
        self.imgLabel7 = tk.Label(self)
        self.imgLabel7.grid(row=5, column=7, pady=10, padx=10, sticky="nesw")
        primaryKey7 = myDB.getPrimaryKey("ItemID", "Stock")
        self.render7 = Image.open(BytesIO(myDB.getItemPictures(primaryKey7[6][0])))
        self.render7 = self.render7.resize((100, 100), Image.ANTIALIAS)
        self.image7 = ImageTk.PhotoImage(self.render7)
        self.imgLabel7.configure(image=self.image7)

        self.dressButton7 = ttk.Button(self, text='Account', image=self.image7,command=lambda: controller.show_frame(Dresses))
        self.dressButton7.grid(row=5, column=7, pady=10, padx=10, sticky="nesw")

        label7 = tk.Label(self, text="£55 per day", font=self.priceFont, bg="white")
        label7.grid(row=6, column=7, pady=0, padx=10, sticky="nesw")

        sizeVar7 = tk.StringVar(self)
        sizeVar7.set("-")
        entrySize7 = tk.OptionMenu(self, sizeVar7, "S", "M", "L").grid(row=7, column=7, pady=10, padx=10, sticky="nw")

        qtyVar7 = tk.StringVar()
        entryQty7 = tk.Spinbox(self, from_=0, to=3, textvariable=qtyVar7).grid(row=8, column=7, pady=10, padx=10, sticky="nw")


        #Dress Eight
        self.imgLabel8 = tk.Label(self)
        self.imgLabel8.grid(row=5, column=8, pady=10, padx=10, sticky="nesw")
        primaryKey8 = myDB.getPrimaryKey("ItemID", "Stock")
        self.render8 = Image.open(BytesIO(myDB.getItemPictures(primaryKey8[7][0])))
        self.render8 = self.render8.resize((100, 100), Image.ANTIALIAS)
        self.image8 = ImageTk.PhotoImage(self.render8)
        self.imgLabel8.configure(image=self.image8)

        self.dressButton8 = ttk.Button(self, text='Account', image=self.image8,command=lambda: controller.show_frame(Dresses))
        self.dressButton8.grid(row=5, column=8, pady=10, padx=10, sticky="nesw")

        label8 = tk.Label(self, text="£40 per day", font=self.priceFont, bg="white")
        label8.grid(row=6, column=8, pady=0, padx=10, sticky="nesw")

        sizeVar8 = tk.StringVar(self)
        sizeVar8.set("-")
        entrySize8 = tk.OptionMenu(self, sizeVar8, "S", "M", "L").grid(row=7, column=8, pady=10, padx=10, sticky="nw")

        qtyVar8 = tk.StringVar()
        entryQty8 = tk.Spinbox(self, from_=0, to=3, textvariable=qtyVar6).grid(row=8, column=8, pady=10, padx=10, sticky="nw")

        #Dress Nine
        self.imgLabel9 = tk.Label(self)
        primaryKey9 = myDB.getPrimaryKey("ItemID", "Stock")
        self.render9 = Image.open(BytesIO(myDB.getItemPictures(primaryKey9[8][0])))
        self.render9 = self.render9.resize((100, 100), Image.ANTIALIAS)
        self.image9 = ImageTk.PhotoImage(self.render9)

        self.dressButton9 = ttk.Button(self, text='Account', image=self.image9,command=lambda: controller.show_frame(Dresses))
        self.dressButton9.grid(row=5, column=9, pady=10, padx=10, sticky="nesw")

        label9 = tk.Label(self, text="£55 per day", font=self.priceFont, bg="white")
        label9.grid(row=6, column=9, pady=0, padx=10, sticky="nesw")

        sizeVar9 = tk.StringVar(self)
        sizeVar9.set("-")
        entrySize9 = tk.OptionMenu(self, sizeVar9, "S", "M", "L").grid(row=7, column=9, pady=10, padx=10, sticky="nw")

        qtyVar9 = tk.StringVar()
        entryQty9 = tk.Spinbox(self, from_=0, to=3, textvariable=qtyVar9).grid(row=8, column=9, pady=10, padx=10, sticky="nw")

        #Dress Ten
        self.imgLabel10 = tk.Label(self)
        self.imgLabel10.grid(row=5, column=10, pady=10, padx=10, sticky="nesw")
        primaryKey10 = myDB.getPrimaryKey("ItemID", "Stock")
        self.render10 = Image.open(BytesIO(myDB.getItemPictures(primaryKey10[9][0])))
        self.render10 = self.render10.resize((100, 100), Image.ANTIALIAS)
        self.image10 = ImageTk.PhotoImage(self.render10)
        self.imgLabel10.configure(image=self.image10)

        self.dressButton10 = ttk.Button(self, text='Account', image=self.image10,command=lambda: controller.show_frame(Dresses))
        self.dressButton10.grid(row=5, column=10, pady=10, padx=10, sticky="nesw")

        label10 = tk.Label(self, text="£55 per day", font=self.priceFont, bg="white")
        label10.grid(row=6, column=10, pady=0, padx=10, sticky="nesw")

        sizeVar10 = tk.StringVar(self)
        sizeVar10.set("-")
        entrySize10 = tk.OptionMenu(self, sizeVar10, "S", "M", "L").grid(row=7, column=10, pady=10, padx=10, sticky="nw")

        qtyVar10 = tk.StringVar()
        entryQty10 = tk.Spinbox(self, from_=0, to=3, textvariable=qtyVar6).grid(row=8, column=10, pady=10, padx=10, sticky="nw")


        #Total Cost
        totalCost = tk.Label(self, text="Total cost: £", font=self.myFont, bg="white")
        totalCost.grid(row=9, column=6, pady=10, padx=10, sticky="nesw")


    def rentDress(self, cost, duration):
        self.finalCost = (int(cost.get())* duration)
        finalCostLabel = tk.Label(self, text=self.finalCost , font = self.myFont, bg="white")
        finalCostLabel.grid(row = 9, column = 7, pady=10,padx=10, sticky = "w")



class Contact(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background="HotPink")

        self.grid_rowconfigure(0, weight=0)
        self.myFont = ("Arial bold", 16)
        self.myFont2 = ("Arial", 14)

        self.label = tk.Label(self, text="Contact Form", font=self.myFont, bg="HotPink")
        self.label.grid(row=0, column=1, pady=10, padx=10, sticky="nesw")

        #Get name using entry box
        self.name = tk.Label(self, text="Full Name: ", font=self.myFont2, bg="HotPink").grid(row=1, column=0, pady=10, padx=10, sticky="nesw")
        self.nameVar = tk.StringVar()
        self.entryName = tk.Entry(self, textvariable=self.nameVar).grid(row=1, column=1, pady=10, padx=10, sticky="nesw")
        sName = self.nameVar.get()
        sName2 = self.nameVar.get()

        #Get email using entry box
        self.email = tk.Label(self, text="Email: ", font=self.myFont2, bg="HotPink").grid(row=2, column=0, pady=10, padx=10, sticky="nesw")
        self.emailVar = tk.StringVar()
        self.entryEmail = tk.Entry(self, textvariable=self.emailVar).grid(row=2, column=1, pady=10, padx=10, sticky="nesw")
        sEmail = self.emailVar.get()

        #Get message using entry box
        self.message = tk.Label(self, text="Message: ", font=self.myFont2, bg="HotPink").grid(row=3, column=0, pady=50, padx=100, sticky="nesw")
        self.messageVar = tk.StringVar()
        self.entryMessage = tk.Entry(self, textvariable=self.messageVar).grid(row=3, column=1, pady=10, padx=10, sticky="nesw")
        sMessage = self.messageVar.get()

        #Save button
        self.saveButton = tk.Button(self, text="Save", command=lambda: self.save(sName, sEmail, sMessage)).grid(row=4, column=1, pady=10, padx=10, sticky="nesw")

        #Other contact details
        self.details = tk.Label(self, text="Phone number: 44785655732 "
                                           "\n Email: aoibhesboutique@gmail.com"
                                           "\n Facebook: Aoibhe's Boutique ", font=self.myFont2, bg="white")
        self.details.grid(row=1, column=3, sticky="e")



    def save(self, sName, sEmail, sMessage):
        self.customerMessage = open((sName+"Reciept.txt"), "w+")
        self.customerMessage.write("Customer Query: \n" + sName + "\n" + sEmail + "\n" + sMessage)
        self.txt = tk.Label(self, text="Message sent", font=("Arial", 8), bg="HotPink").grid(row=5, column=1)


class Account(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background="HotPink")

        self.grid_rowconfigure(0, weight=0)
        self.myFont = ("Arial bold", 16)
        self.myFont2 = ("Arial", 12)

        label = tk.Label(self, text="Account", font=self.myFont, bg="HotPink")
        label.grid(row=0, column=5, pady=10, padx=10, sticky="nesw")
        
        


if __name__ =="__main__":
    customerDashboard = Container()
    customerDashboard.state('zoomed')
    customerDashboard.configure(background='HotPink')
    s = ttk.Style()
    s.configure('TNotebook.Tab', font=('Arial', '14'))
    s.theme_use('clam')
    s.configure('TButton', background = 'DeepPink1', foreground = 'white', width = 20, borderwidth=1, focusthickness=3, focuscolor='none')
    s.map('TButton', background=[('active','HotPink')])
    s.configure("TMenubutton", background="HotPink")
    customerDashboard.mainloop()