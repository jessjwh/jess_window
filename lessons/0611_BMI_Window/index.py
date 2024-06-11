import tkinter as tk
from tkinter import ttk, messagebox
from ttkthemes import ThemedTk

class Window(ThemedTk):
    def __init__(self, theme:str | None, **kwargs):
        super().__init__(**kwargs)
        self.title("BMI Calculator")
        # self.configure(bg="#f97")
        # self.geometry("350x350+100+50")
        self.resizable(False, False)
        style = ttk.Style()
        style.configure('input.TFrame', background="#f99")
        style.configure('press.TButton', font=("Helvetica", 18))

#====================================================================================
        titleFrame = ttk.Frame(self)
        title_label = ttk.Label(self, text="Am I Fat?", font=("Helvetica", 24))
        title_label.pack(pady=30)
        titleFrame.pack(padx=100,pady=(0,10))
#------------------------------------------------------------------------------------
        input_frame = ttk.Frame(self, width=100, height=100, style='input.TFrame')
        input_frame.pack(pady=5)

        label_name = ttk.Label(input_frame, text="Who's dis:")
        label_name.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
        self.entry_name = ttk.Entry(input_frame)
        self.entry_name.grid(row=0, column=1, padx=5, pady=5)

        label_height = ttk.Label(input_frame, text="Height (cm):")
        label_height.grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
        self.entry_height = ttk.Entry(input_frame)
        self.entry_height.grid(row=1, column=1, padx=5, pady=5)

        label_weight = ttk.Label(input_frame, text="Weight (kg):")
        label_weight.grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)
        self.entry_weight = ttk.Entry(input_frame)
        self.entry_weight.grid(row=2, column=1, padx=5, pady=5)        

        input_frame.pack(pady=10,padx=30)
#------------------------------------------------------------------------------------
        button_cal = ttk.Button(self, text="LET'S SEEE!", command=self.show_bmi_result, style='press.TButton')
        button_cal.pack(side=tk.RIGHT, padx=(0,35), pady=(20), ipadx=10)
#====================================================================================

    def show_bmi_result(self):
        try:
            name:str = self.entry_name.get()
            height:int = int(self.entry_height.get())
            weight:int = int(self.entry_weight.get())

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

        result_message = f"Hey {name}!:\n   Your BMI is:{bmi:.1f}\n   {status}\n   {advice}"
        print(result_message)



def main():
    window = Window(theme='arc')
    window.mainloop()

if __name__ == '__main__':
    main()