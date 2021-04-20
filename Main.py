import tkinter as tk
from tkinter import ttk
import sqlite3
from sqlite3 import Error
import DatabaseClass as db
import cLogin as cl
import sLogin as sl


   
class Container(tk.Tk):
   def __init__(self, *args, **kwargs):
      tk.Tk.__init__(self, *args, **kwargs)

      self.configure(background="HotPink")
      self.myFont = ("Arial bold", 12)

      
      container = tk.Frame(self)
      container.pack(side="top", fill="both", expand = True)
      container.grid_rowconfigure(0, weight=1)
      container.grid_columnconfigure(0, weight=1)

      self.frames = {}

      for F in (cl.customerLogin, sl.staffLogin):
         frame = F(container, self)
         self.frames[F] = frame
         frame.grid(row=0, column=0, sticky="nsew")
         self.show_frame(Container)

      title = tk.Label(self, text="Login Portal", font=self.myFont, bg="HotPink").pack()
      customerLoginButton = tk.Button(self, text="Customer Login", command=lambda: controller.show_frame(cl.customerLogin)).pack()
      staffLoginButton = tk.Button(self, text="Staff Login", command=lambda: controller.show_frame(sl.staffLogin)).pack()


   def show_frame(self, cont):
      frame = self.frames[cont]
      frame.tkraise()

#Basic widgets to be used for all classes
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


 

#Main Program
if __name__ =="__main__":
   window = Container()
   window.mainloop()

