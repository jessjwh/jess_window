from tkinter import *
import tkinter as tk
from tkinter.simpledialog import Dialog
from tkinter import messagebox
from tkinter import ttk, Misc, Frame




class GetBMI(Dialog):

    def body(self, master):
        self.title("Tell Us About You")

        Label(master, text='Name:').grid(row=0, sticky=W)
        Label(master, text='Height (cm):').grid(row=1, sticky=W)
        Label(master, text='Weight (kg):').grid(row=2, sticky=W)

        self.name = Entry(master, width=12)
        self.height = Entry(master, width=12)
        self.weight = Entry(master, width=12)

        self.name.grid(row=0, column=1, sticky=W)
        self.height.grid(row=1, column=1, sticky=W)
        self.weight.grid(row=2, column=1, sticky=W)
        return self.name

    def apply(self):
        name = self.name.get()
        height = self.height.get()
        weight = self.weight.get()

        if not name != str or height != float or weight != float:
            messagebox.showerror('Error','Invalid Answer')
        else:
            pass
    
    def buttonbox(self) -> None:
        '''
        Customized button
        '''
        box=tk.Frame(self)
        self.ok_button = tk.Button(box, text='Get My BMI!', width=15, command=self.ok)
        self.ok_button.pack(pady=(10,10),ipady=10)
        box.pack()
    
    def ok(self) -> None:
        print("BMI button was clicked!")
        super().ok()


root = Tk()
dialog = GetBMI(root)