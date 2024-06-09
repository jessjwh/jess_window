from pprint import pprint
import tkinter as tk
from tkinter import ttk, Misc, Frame
from ttkthemes import ThemedTk
import tools
from tkinter import messagebox
from tkinter.simpledialog import Dialog
from datetime import datetime

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


    def update_data(self):
        if (tools.AQI.aqi_records is None) or (tools.AQI.update_time is None):
            tools.AQI.aqi_records = self.download_parse_data()
            tools.AQI.update_time = datetime.now()
        elif((datetime.now()-tools.AQI.update_time).seconds >= 60 * 60):
            tools.AQI.aqi_records = self.download_parse_data()
            tools.AQI.update_time = datetime.now()

    def click1(self):
        self.update_data()
        data:list[dict] = tools.AQI.aqi_records
        sorted_data:list[dict] = sorted(data,key=lambda value:value['aqi'])
        best5_aqi:list[dict] = sorted_data[:5]
        def abc(value:dict)->str:
            return f"{value['county']} - {value['site_name']} - 空氣品質:{value['aqi']} - 狀態:{value['status']} - {value['date']}"
        message_data:list[str] = list(map(abc,best5_aqi))
        message = "\n".join(message_data)
        print(message)
        ShowInfo(parent=self,title="AQI Best 5 Districts",message=message)

    def click2(self):
        self.update_data()
        data:list[dict] = tools.AQI.aqi_records
        sorted_data:list[dict] = sorted(data,key=lambda value:value['aqi'], reverse=True)
        best5_aqi:list[dict] = sorted_data[:5]
        def abc(value:dict)->str:
            return f"{value['county']} - {value['site_name']} - 空氣品質:{value['aqi']} - 狀態:{value['status']} - {value['date']}"
        message_data:list[str] = list(map(abc,best5_aqi))
        message = "\n".join(message_data)
        print(message)
        ShowInfo(parent=self,title="AQI Worst 5 Districts",message=message)
    
    def click3(self):
        self.update_data()
        data:list[dict] = tools.AQI.aqi_records
        sorted_data:list[dict] = sorted(data,key=lambda value:value['pm25'])
        best5_aqi:list[dict] = sorted_data[:5]
        def abc(value:dict)->str:
            return f"{value['county']} - {value['site_name']} - pm2.5:{value['pm25']} - 狀態:{value['status']} - {value['date']}"
        message_data:list[str] = list(map(abc,best5_aqi))
        message = "\n".join(message_data)
        print(message)
        ShowInfo(parent=self,title="pm2.5 Best 5 Districts",message=message)

    def click4(self):
        self.update_data()
        data:list[dict] = tools.AQI.aqi_records
        sorted_data:list[dict] = sorted(data,key=lambda value:value['pm25'], reverse=True)
        best5_aqi:list[dict] = sorted_data[:5]
        def abc(value:dict)->str:
            return f"{value['county']} - {value['site_name']} - pm2.5:{value['pm25']} - 狀態:{value['status']} - {value['date']}"
        message_data:list[str] = list(map(abc,best5_aqi))
        message = "\n".join(message_data)
        print(message)
        ShowInfo(parent=self,title="pm2.5 Worst 5 Districts",message=message)

class ShowInfo(Dialog):
    def __init__(self,parent:Misc,title:str | None = None,message:str=""):
        self.message = message
        super().__init__(parent=parent,title=title) 

    def body(self, master: Frame) -> Misc | None:
            text = tk.Text(self,height=10,font=('Helvetica',12),width=50)
            text.pack(padx=10,pady=10)
            text.insert(tk.INSERT,self.message)
            text.config(state='disabled')
            return None
    
    def apply(self) -> None:
        '''
        This will run when the user clicked the "ok" button in the jump out window.
        '''
        print("They clicked the 'ok' button.")

    def buttonbox(self) -> None:
        '''
        Customized button
        '''
        box=tk.Frame(self)
        self.ok_button = tk.Button(box, text='YASS!', width=10, command=self.ok)
        self.ok_button.pack(pady=(20,30),ipady=10)
        box.pack()
    
    def ok(self) -> None:
        print("OK button was clicked!")
        super().ok()

def main():
    window = Window(theme="arc")
    window.mainloop()
    

if __name__ == '__main__':
    main()
