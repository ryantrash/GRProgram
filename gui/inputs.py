import tkinter as tk
from tkinter import ttk

class Inputs(ttk.Frame): 
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        
        selected_id = tk.StringVar(self)
        selected_id.set("Select Driver ID...")
        selected_lap = tk.StringVar(self) 
        selected_lap.set("Select Desired Lap...")
        
        id_options = ["1", "2"] 
        
        self.parent = parent 
        
        self.id_label = ttk.Label(text="Driver ID: ") 
        self.id_label.pack() 
        
        self.id_dropdown = ttk.OptionMenu(self, selected_id, *id_options)
        self.id_dropdown.pack()