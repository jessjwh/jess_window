import tkinter as tk
from tkinter import ttk

def get_names() -> list[str]:
    with open('names.txt', encoding='utf-8') as file:
        content:str = file.read()
    names:list[str] = content.split()
    return names
    # for name in names:
    #     print(name)

# names:list[str] = get_names()
# print(__name__)

class Window(tk.Tk):
    def __init__(self, title:str = "Hello!", **kwargs):
        super().__init__(**kwargs)
        self.title(title)
        label:ttk.Label = ttk.Label(self, 
                                    text='Hey Jess!',
                                    font=('Arial', 30, 'bold'),
                                    foreground='#f98')
        label.pack(padx=100,pady=40)
        ttk.Button(self, text='Wave Back!').pack()

if __name__ == '__main__':
    names:list[str] = get_names()
    # print(names)
    window:Window = Window(title='My First GUI')
    window.mainloop()