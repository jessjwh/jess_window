import tkinter as tk

def get_names() -> list[str]:
    with open('names.txt', encoding='utf-8') as file:
        content:str = file.read()
    names:list[str] = content.split()
    return names
    # for name in names:
    #     print(name)

# names:list[str] = get_names()
# print(__name__)

if __name__ == '__main__':
    names:list[str] = get_names()
    # print(names)
    window:tk.Tk = tk.Tk()
    window.mainloop()