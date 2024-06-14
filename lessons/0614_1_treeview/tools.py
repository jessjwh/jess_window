from tkinter.simpledialog import Dialog
from tkinter import ttk, Misc
import tkinter as tk
from data import Info
import tkintermapview as tkmap

class CustomMessagebox(Dialog):
    def __init__(self, parent:Misc, title:str, site:Info):
        print(site)
        super().__init__(parent=parent, title=title)

    def body(self, master):
        content_frame = ttk.Frame(master, width=100, height=100, style='input.TFrame')   
        content_frame.pack(pady=10,padx=30)

    def apply(self):
        pass

    def buttonbox(self):
        box = ttk.Frame(self)
        self.ok_buttton = tk.Button(box, text="Fantastic!", width=10, command=self.ok, default=tk.ACTIVE)
        self.ok_buttton.pack(side=tk.LEFT, padx=5, pady=5)
        box.pack()

    def ok(self):
        super().ok()

         