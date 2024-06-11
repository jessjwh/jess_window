from tkinter.simpledialog import Dialog
from tkinter import ttk, Misc
import tkinter as tk

class CustomMessagebox(Dialog):
    def __init__(self, parent:Misc, title:str, name:str, bmi:float, status:str, advice:str):
        self.name = name
        self.bmi = bmi
        self.status = status
        self.advice = advice
        super().__init__(parent=parent, title=title)


        result_message = f"Hey {name}!\n   Your BMI is:{bmi:.1f}\n   {status}\n   {advice}"
        print(result_message)

    def body(self, master):
        input_frame = ttk.Frame(self, width=100, height=100, style='input.TFrame')
        input_frame.pack(pady=5)

        label_name = ttk.Label(input_frame, text="Who's dis:")
        label_name.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
        self.value_name = ttk.Label(input_frame, text = self.name)
        self.value_name.grid(row=0, column=1, padx=5, pady=5)

        label_bmi = ttk.Label(input_frame, text="BMI:")
        label_bmi.grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
        self.value_bmi = ttk.Label(input_frame, text = f'{self.bmi:.1f}')
        self.value_bmi.grid(row=1, column=1, padx=5, pady=5)

        label_status = ttk.Label(input_frame, text="Status:")
        label_status.grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)
        self.value_status = ttk.Label(input_frame, text = self.status)
        self.value_status.grid(row=2, column=1, padx=5, pady=5)        

        label_advice = ttk.Label(input_frame, text="Advice:")
        label_advice.grid(row=3, column=0, padx=5, pady=5, sticky=tk.E)
        self.value_advice = ttk.Label(input_frame, text = self.advice)
        self.value_advice.grid(row=3, column=1, padx=5, pady=5)       

        input_frame.pack(pady=10,padx=30)
         