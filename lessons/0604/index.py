from pprint import pprint
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import tools

class Window(ThemedTk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title("AQI Display")
        style = ttk.Style()
        style.configure('Top.TFrame')
        style.configure('Top.TLabel',font=('Helvetica',25))

        title_frame = ttk.Frame(self, style='Top.TFrame', borderwidth=1, relief='groove')
        ttk.Label(title_frame, text='AQI Display', style='Top.TLabel').pack(expand=True, fill='y')
        title_frame.pack(ipadx=60, ipady=20, padx=10, pady=10)

        func_frame = ttk.Frame(self, style='Top.TFrame', borderwidth=1, relief='groove')
        ttk.Button(func_frame, text="AQI Best 5",command=self.click1).pack(side='left', expand=True)
        ttk.Button(func_frame, text="AQI Worst 5",command=self.click2).pack(side='left', expand=True)
        ttk.Button(func_frame, text="pm2.5 Best 5",command=self.click3).pack(side='left', expand=True)
        ttk.Button(func_frame, text="pm2.5 Worst 5",command=self.click4).pack(side='left', expand=True)
        func_frame.pack(ipadx=80, ipady=30, padx=10, pady=10)
    
    def click1(self):
        print("click1")

    def click2(self):
        print("click2")

    def click3(self):
        print("click3")

    def click4(self):
        print("click4")


def main():
    '''
    try:
        all_data:dict[any] = tools.download_json()
    except Exception as error:
        print(error)
    else:
        data:list[dict] = tools.get_data(all_data)
        pprint(data)
    '''
    window = Window(theme="yaru")
    window.mainloop()

if __name__ == '__main__':
    main()