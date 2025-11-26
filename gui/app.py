import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from .inputs import Inputs 

class mainApplication(ThemedTk):
    def __init__(self):
        super().__init__()
        self.title("GRProgram")
        self.geometry("1800x600")
        self.configure(bg="grey")
        self.set_theme("equilux")
        
        self.create_widgets()
        
    def create_widgets(self):
        title = ttk.Label(self, text="Select driver and lap number to analyze: ")
        
        inputs = Inputs(self) 
        
        title.pack()
        inputs.pack() 
        
        

def run():
    app = mainApplication() 
    app.mainloop()