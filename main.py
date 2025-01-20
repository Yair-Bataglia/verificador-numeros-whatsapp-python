import customtkinter as ctk

from Interface.frameUno import LeftFrame
from Interface.frameDos import RightFrame

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Visor de Excel")
        self.geometry("1000x600")
        self.resizable(False, False)
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.rightFrame = RightFrame(self)
        self.rightFrame.grid(row=0, column=1, sticky="nsew" )
        print('asdadasd')

        self.leftFrame = LeftFrame(self, self.rightFrame)
        self.leftFrame.grid(row=0, column=0, sticky="nsew")

if __name__ == "__main__":
    ctk.set_appearance_mode("dark") 
    ctk.set_default_color_theme("blue") 
    app = App()
    app.mainloop()
