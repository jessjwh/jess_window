import tkinter as tk
from tkinter import ttk, messagebox, Misc
from ttkthemes import ThemedTk
import data
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Window(ThemedTk):
    def __init__(self, theme:str='arc', **kwargs):
        super().__init__(theme=theme, **kwargs)
        self.title("YouBike2.0 In Taipei")
        try:
            self.__data = data.load_data()
        except Exception as error:
            messagebox.showwarning(title="Error", message=str(error))

        self._display_interface()

    @property
    def data(self)->list[dict]:
        return self.__data

    def _display_interface(self):
        mainFrame = ttk.Frame(borderwidth=1, relief="groove")
        ttk.Label(mainFrame, text="YouBike2.0 Realtime Data", font=('arial',16)).pack(pady=(20,10))


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
        tree.column('sarea',width=70,anchor=tk.CENTER)
        tree.column('mday',width=120,anchor=tk.CENTER)
        tree.column('ar',minwidth=100)
        tree.column('total',width=50,anchor=tk.CENTER)
        tree.column('rent_bikes',width=50,anchor=tk.CENTER)
        tree.column('retuen_bikes',width=50,anchor=tk.CENTER)

        # bind
        tree.bind('<<TreeviewSelect>>', self.item_selected)

        # add data to the treeview
        for site in self.data:
            tree.insert('', tk.END, 
                        values=(site['sna'], site['sarea'], site['mday'], site['ar'], site['total'], site['rent_bikes'], site['retuen_bikes']))
        
        tree.grid(row=0, column=0, sticky='nsew')

        scrollbar = ttk.Scrollbar(tableFrame, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')

        tableFrame.pack(ipadx=20, ipady=20)

        self.pieChartFrame = PieChartFrame(mainFrame)
        self.pieChartFrame.pack()
        mainFrame.pack(padx=10, pady=10)

    def item_selected(self,event):
        tree = event.widget
        records:list[list] = []       
        for selected_item in tree.selection()[:3]:
            item = tree.item(selected_item)            
            record:list = item['values']
            records.append(record)
        self.pieChartFrame.infos = records

class PieChartFrame(ttk.Frame):
    def __init__(self,master:Misc, **kwargs):
        super().__init__(master=master, **kwargs)
        self.configure({'borderwidth':2,'relief':'groove'})
        #self.config({'borderwidth':2,'relief':'groove'})        
        #self['borderwidth'] = 2
        #self['relief'] = 'groove'
        style = ttk.Style()
        style.configure('abc.TFrame', background = '#ffffff')
        self.configure(style = 'abc.TFrame')

    @property
    def infos(self)->None:
        return None

    @infos.setter
    def infos(self,datas:list[list]) -> None:
        for w in self.winfo_children():
            w.destroy()

        for data in datas:
            sitename:str = data[0]
            area:str = data[1]
            info_time:str = data[2]
            address:str = data[3]
            total:int = data[4]
            rents:int = data[5]
            returns:int = data[6]
            oneFrame = ttk.Frame(self, style='abc.TFrame')
            ttk.Label(oneFrame,text="Area: ").grid(row=0,column=0, sticky='e')
            ttk.Label(oneFrame,text=area).grid(row=0,column=1, sticky='w')

            ttk.Label(oneFrame,text="Site: ").grid(row=1,column=0, sticky='e')
            ttk.Label(oneFrame,text=sitename).grid(row=1,column=1, sticky='w')

            ttk.Label(oneFrame,text="Time: ").grid(row=2,column=0, sticky='e')
            ttk.Label(oneFrame,text=info_time).grid(row=2,column=1, sticky='w')

            ttk.Label(oneFrame,text="Address: ").grid(row=3,column=0, sticky='e')
            ttk.Label(oneFrame,text=address).grid(row=3,column=1, sticky='w')

            ttk.Label(oneFrame,text="Total: ").grid(row=4,column=0, sticky='e')
            ttk.Label(oneFrame,text=str(total)).grid(row=4,column=1, sticky='w')

            ttk.Label(oneFrame,text="Bikes: ").grid(row=5,column=0, sticky='e')
            ttk.Label(oneFrame,text=str(rents)).grid(row=5,column=1, sticky='w')

            ttk.Label(oneFrame,text="Spots: ").grid(row=6,column=0, sticky='e')
            ttk.Label(oneFrame,text=str(returns)).grid(row=6,column=1, sticky='w')


            def func(pct, allvals):
                absolute = int(np.round(pct/100.*np.sum(allvals)))
                return f"{absolute:d}pcs - {pct:.1f}%"

            values = [rents, returns]
            labels = ['Rentable Bikes','Empty Spots']
            colors = ['DarkSalmon','IndianRed']
            figure = plt.figure(figsize=(5,5),dpi=72)
            axes = figure.add_subplot()
            axes.pie(values,colors=colors,
                    labels=labels,
                    labeldistance=0.4,
                    shadow=True,
                    autopct=lambda pct: func(pct, values),
                    textprops=dict(color="white"))
            axes.legend(title="Rate:",
                        loc="center left",
                        bbox_to_anchor=(0,0,0,2))

            canvas = FigureCanvasTkAgg(figure,oneFrame)
            canvas.draw()
            canvas.get_tk_widget().grid(row=7,column=0,columnspan=2)

            for item in canvas.get_tk_widget().find_all():
                canvas.get_tk_widget().delete(item)

            oneFrame.pack(side='left',expand=True,fill='both')    

def main():
    def on_closing():
        window.destroy()
    
    window = Window(theme='breeze')
    window.protocol("WM_DELETE_WINDOW", on_closing)
    window.mainloop()

if __name__ == '__main__':
    main()