from pprint import pprint
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import tools
from tkinter import messagebox
from tkinter.simpledialog import Dialog

class Window(ThemedTk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title("AQI Display")
        style = ttk.Style()
        style.configure('Top.TFrame')
        style.configure('Top.TLabel',font=('Helvetica',16))

        title_frame = ttk.Frame(self, style='Top.TFrame', borderwidth=1, relief='groove')
        ttk.Label(title_frame, text='AQI Display', style='Top.TLabel').pack(expand=True, fill='y')
        title_frame.pack(ipadx=50, ipady=30, padx=10, pady=20)

        func_frame = ttk.Frame(self, style='Top.TFrame', borderwidth=1, relief='groove')
        ttk.Button(func_frame, text="AQI Best 5",command=self.click1).pack(side='left', expand=True)
        ttk.Button(func_frame, text="AQI Worst 5",command=self.click2).pack(side='left', expand=True)
        ttk.Button(func_frame, text="pm2.5 Best 5",command=self.click3).pack(side='left', expand=True)
        ttk.Button(func_frame, text="pm2.5 Worst 5",command=self.click4).pack(side='left', expand=True)
        func_frame.pack(ipadx=60, ipady=30, padx=10, pady=15)
    

    def download_parse_data(self) ->list[dict] | None:
        try:
            all_data:dict[any] = tools.download_json()
        except Exception as error:
            messagebox.showwarning("There's a mistake. Please try again later.")
            return
        else:
            data:list[dict] = tools.get_data(all_data)
            return data

    def click1(self):
        data:list[dict] = self.download_parse_data()
        print(data)

    def click2(self):
        messagebox.showerror("Error","Error message")

    def click3(self):
        messagebox.showwarning("Warning","Warning message")

    def click4(self):
        ShowInfo(parent=self,title="This is a dialog.")

class ShowInfo(Dialog):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    def body(self, master):
            text = tk.Text(self,height=8,font=('Helvetica',16),width=30)
            text.pack(padx=5,pady=5)
            text.insert(tk.INSERT,"Hello Jess")
            text.config(state='disabled')
            return None


def main():
    window = Window(theme="arc")
    window.mainloop()
    

if __name__ == '__main__':
    main()

