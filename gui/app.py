import tkinter as tk 
from .inputs import Inputs 

class mainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("GRProgram")
        self.geometry("1800x600")
        
        self.create_widgets()
        
    def create_widgets(self):
        title = tk.Label(self, text="Select driver and lap number to analyze: ")
        
        inputs = Inputs(self) 
        
        title.pack()
        
        

def run():
    app = mainApplication() 
    app.mainloop()