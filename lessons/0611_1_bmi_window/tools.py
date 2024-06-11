from tkinter.simpledialog import Dialog
from tkinter import ttk, Misc
import tkinter as tk

class CustomMessagebox(Dialog):
    def __init__(self, parent:Misc, title:str, name:str, bmi:float, status:str, advice:str, status_color:str):
        self.parent = parent
        self.name = name
        self.bmi = bmi
        self.status = status
        self.advice = advice
        style = ttk.Style()
        style.configure('status.TLabel', foreground=status_color)
        super().__init__(parent=parent, title=title)


        result_message = f"Hey {name}!\n   Your BMI is:{bmi:.1f}\n   {status}\n   {advice}"
        print(result_message)

    def body(self, master):
        content_frame = ttk.Frame(master, width=100, height=100, style='input.TFrame')
        
        # NAME
        label_name = ttk.Label(content_frame, text="Who's dis:")
        label_name.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
        self.value_name = ttk.Label(content_frame, text = self.name)
        self.value_name.grid(row=0, column=1, padx=5, pady=5)
        
        # BMI
        label_bmi = ttk.Label(content_frame, text="BMI:")
        label_bmi.grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
        self.value_bmi = ttk.Label(content_frame, text = f'{self.bmi:.1f}')
        self.value_bmi.grid(row=1, column=1, padx=5, pady=5)

        # STATUS
        label_status = ttk.Label(content_frame, text="Status:")
        label_status.grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)
        self.value_status = ttk.Label(content_frame, text = self.status, style='status.TLabel')
        self.value_status.grid(row=2, column=1, padx=5, pady=5)        

        # ADVICE
        label_advice = ttk.Label(content_frame, text="Advice:")
        label_advice.grid(row=3, column=0, padx=5, pady=5, sticky=tk.E)
        self.value_advice = ttk.Label(content_frame, text = self.advice)
        self.value_advice.grid(row=3, column=1, padx=5, pady=5)       

        content_frame.pack(pady=10,padx=30)

    def apply(self):
        print(self.parent.name_value.set(''))
        print(self.parent.height_value.set(''))
        print(self.parent.weight_value.set(''))

    def buttonbox(self):
        box = ttk.Frame(self)
        self.ok_buttton = tk.Button(box, text="FINE.", width=10, command=self.ok, default=tk.ACTIVE)
        self.ok_buttton.pack(side=tk.LEFT, padx=5, pady=5)
        box.pack()

    def ok(self):
        print("'FINE' button was clicked.")
        super().ok()

         