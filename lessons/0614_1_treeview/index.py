import tkinter as tk
from tkinter import ttk, messagebox
from ttkthemes import ThemedTk
import data


class Window(ThemedTk):
    def __init__(self, theme:str='arc', **kwargs):
        super().__init__(theme=theme, **kwargs)
        self.title("YouBike2.0 In Taipei")
        try:
            self.__data = data.load_data()
        except Exception as error:
            messagebox.showwarning(title="Error", message=str(error))

        self._display_interface()

    def _display_interface(self):
        mainFrame = ttk.Frame(borderwidth=1, relief="groove")
        ttk.Label(mainFrame, text="YouBike2.0 Realtime Data", font=('Helvetica', 16)).pack(pady=(20,10))


        tableFrame = ttk.Frame(mainFrame)
        columns = ('sna', 'sarea', 'mday', 'ar', 'total', 'rent_bikes', 'retuen_bikes')
        tree = ttk.Treeview(tableFrame, columns=columns, show='headings')
        # define headings
        tree.heading('sna', text='Site')
        tree.heading('sarea', text='Area')
        tree.heading('mday', text='Date')
        tree.heading('ar', text='Address')
        tree.heading('total', text='Total')
        tree.heading('rent_bikes', text='Available')
        tree.heading('retuen_bikes', text='Spots')

        # define column width
        tree.column('sarea', width=70, anchor=tk.CENTER)
        tree.column('mday', width=120, anchor=tk.CENTER)
        tree.column('ar', minwidth=100)
        tree.column('total', width=50, anchor=tk.CENTER)
        tree.column('rent_bikes', width=50, anchor=tk.CENTER)
        tree.column('retuen_bikes', width=50, anchor=tk.CENTER)

        # add data to the treeview
        for site in self.data:
            tree.insert('', tk.END, 
                        values=(site['sna'], site['sarea'], site['mday'], site['ar'], site['total'], site['rent_bikes'], site['retuen_bikes']))
        
        tree.grid(row=0, column=0, sticky='nsew')

        scrollbar = ttk.Scrollbar(tableFrame, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')

        tableFrame.pack(expand=True, fill=tk.BOTH, ipadx=20, ipady=20)

        mainFrame.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)


    @property
    def data(self)->list[dict]:
        return self.__data
    

def main():
    window = Window(theme='breeze')
    window.mainloop()

if __name__ == '__main__':
    main()