import tkinter as tk
from tkinter import ttk, messagebox
from ttkthemes import ThemedTk
from tools import CustomMessagebox

class Window(ThemedTk):
    def __init__(self, theme:str | None, **kwargs):
        super().__init__(**kwargs)
        self.title("BMI Calculator")
        # self.configure(bg="#f97")
        # self.geometry("350x350+100+50")
        self.resizable(False, False)
        style = ttk.Style()
        style.configure('input.TFrame', background="#f99")
        style.configure('press.TButton', font=("Helvetica", 14))

#====================================================================================
        titleFrame = ttk.Frame(self)
        title_label = ttk.Label(self, text="Am I Fat?", font=("Helvetica", 24))
        title_label.pack(pady=30)
        titleFrame.pack(padx=100,pady=(0,10))
#------------------------------------------------------------------------------------
        input_frame = ttk.Frame(self, width=100, height=100, style='input.TFrame')
        input_frame.pack(pady=5)

        # NAME
        label_name = ttk.Label(input_frame, text="Who's dis:")
        label_name.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
        self.name_value = tk.StringVar()
        self.name_value.set('')
        entry_name = ttk.Entry(input_frame, textvariable=self.name_value)
        entry_name.grid(row=0, column=1, padx=5, pady=5)

        # HEIGHT
        label_height = ttk.Label(input_frame, text="Height (cm):")
        label_height.grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
        self.height_value = tk.StringVar()
        self.height_value.set('')
        entry_height = ttk.Entry(input_frame, textvariable=self.height_value)
        entry_height.grid(row=1, column=1, padx=5, pady=5)
        
        # WEIGHT
        label_weight = ttk.Label(input_frame, text="Weight (kg):")
        label_weight.grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)
        self.weight_value = tk.StringVar()
        self.weight_value.set('')
        entry_weight = ttk.Entry(input_frame, textvariable=self.weight_value)
        entry_weight.grid(row=2, column=1, padx=5, pady=5)        

        input_frame.pack(pady=10,padx=30)
#------------------------------------------------------------------------------------
        button_cal = ttk.Button(self, text="LET'S SEEE!", command=self.show_bmi_result, style='press.TButton')
        button_cal.pack(side=tk.RIGHT, padx=(0,35), pady=(20), ipadx=10)
#====================================================================================
    def show_bmi_result(self):
        try:
            name:str = self.name_value.get()
            height:int = int(self.height_value.get())
            weight:int = int(self.weight_value.get())

        except Exception:
            messagebox.showwarning(Warning, "You entered the wrong thing, dummy!")
        else:
            self.show_result(name=name, weight=weight, height=height)

    def show_result(self, name:str, height:int, weight:int):
        bmi = weight / (height/100) **2
        if bmi < 18.5:
            status = "You're too skinny!"
            ideal_weight = 18.5 * (height/100)**2
            weight_change = ideal_weight-weight
            advice = f'Put on another {abs(weight_change):.1f}kg to be healthier.'
        elif 18.5 <= bmi <=24.9:
            status = "You're fit!"
            ideal_weight = 18.5 * (height/100)**2
            weight_change = ideal_weight-weight
            advice = 'Keep it up!'
        else:
            status = "You're a bit fat!"
            ideal_weight = 24.9 * (height/100)**2
            weight_change = ideal_weight-weight
            advice = f'Try lose another {abs(weight_change):.1f}kg to be healthier.'
        
        CustomMessagebox(self, title="BMI", name=name, bmi=bmi, status=status, advice=advice)

def __repr__(self):
    return "I'm the entity of 'Window'"

def main():
    window = Window(theme='arc')
    window.mainloop()

if __name__ == '__main__':
    main()