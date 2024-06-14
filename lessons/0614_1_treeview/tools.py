from tkinter.simpledialog import Dialog
from tkinter import ttk, Misc
import tkinter as tk
from data import Info
import tkintermapview as tkmap

class CustomMessagebox(Dialog):
    def __init__(self, parent:Misc, title:str, site:Info):
        self.site:Info = site
        super().__init__(parent=parent, title=title)

    def body(self, master):
        contain_frame = ttk.Frame(master)
        #====================    
        map_frame = ttk.Frame(contain_frame)
        map_widget = tkmap.TkinterMapView(map_frame,
                                         width=800,
                                         height=600,
                                         corner_radius=0
                                         )
        map_widget.pack()
        marker = map_widget.set_position(self.site.lat, self.site.lng, marker=True)
        marker.set_text(f'{self.site.sarea}\n {self.site.sna}\n Total Bikes: {self.site.total}\n Available Bikes: {self.site.rent_bikes}\n Available Spots: {self.site.retuen_bikes}')
        start_point = self.site.lat+0.0005,self.site.lng+0.0005
        end_point = start_point[0],start_point[1]-0.001
        down_point = end_point[0]-0.001, end_point[1]
        left_point = down_point[0], down_point[1]+0.001
        up_point = left_point[0]+0.001, left_point[1]
        path = map_widget.set_path([start_point, end_point, down_point, left_point, up_point])
        map_widget.set_zoom(20)
        map_frame.pack(expand=True,fill='both')
        #===================
        contain_frame.pack(expand=True,fill='both',pady=10,padx=30)

    def apply(self):
        pass

    def buttonbox(self):
        box = ttk.Frame(self)
        self.ok_buttton = tk.Button(box, text="Fantastic!", width=10, command=self.ok, default=tk.ACTIVE)
        self.ok_buttton.pack(side=tk.LEFT, padx=5, pady=5)
        box.pack()

    def ok(self):
        super().ok()

         