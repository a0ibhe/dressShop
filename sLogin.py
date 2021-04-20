import tkinter as tk
from tkinter import ttk
import sDashboard as sd
import Main as lp

class Container(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (sd.Dash,lp.Container):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            # self.show_frame(Container)


# Login page for staff / the owner
class staffLogin(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        tk.Frame.__init__(self, parent)

        self.configure(background="Thistle")
        self.myFont = ("Arial bold", 16)
        self.myFont2 = ("Arial", 12)
        title = tk.Label(self, text="Staff Login", font=self.myFont, bg="Thistle").grid(row=0, column=1, padx=5, pady=5)

        self.username = tk.Label(self, text="Username: ", font=self.myFont2, bg="Thistle").grid(row=1, column=0, padx=5,pady=5)
        self.usernameVar = tk.StringVar()
        self.entryUsername = tk.Entry(self, textvariable=self.usernameVar).grid(row=1, column=1, padx=5, pady=5)

        self.staffPassword = tk.Label(self, text="Password: ", font=self.myFont2, bg="Thistle").grid(row=2, column=0, padx=5, pady=5)
        self.staffPasswordVar = tk.StringVar()
        self.entryStaffPassword = tk.Entry(self, textvariable=self.staffPassword).grid(row=2, column=1, padx=5, pady=5)

        loginButton = tk.Button(self, text="Login", command=lambda: controller.show_frame(sd.Dash)).grid(row=3, column=1, padx=5, pady=5)
        backButton = tk.Button(self, text="Back", command=lambda: controller.show_frame(lp.Container)).grid(row=4, column=1, sticky="s")

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



