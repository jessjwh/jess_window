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

        title_frame = ttk.Frame(self, style='Top.TFrame', borderwidth=2, relief='groove')
        ttk.Label(title_frame, text='AQI Display', style='Top.TLabel').pack(expand=True, fill='y')
        title_frame.pack(ipadx=100, ipady=30, padx=10, pady=10)

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