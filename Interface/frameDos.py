import customtkinter as ctk
from Interface.viewer import ExcelViewer


class RightFrame(ctk.CTkFrame):
    """
    Clase que controla todo el lado derecho de la interfaz del panel principal.
    """
    def __init__(self, master):
        super().__init__(master)

        self.grid_propagate(False)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.excelViewer = ExcelViewer(self)

        self.title = ctk.CTkLabel(self, 
            width=100,
            text="Base Cargada", 
            font=("Arial", 20), 
            anchor='w')
        self.title.grid(row=0, column=0, pady=(30,10), padx=10,sticky="e")

        self.update_button = ctk.CTkButton(self, 
            text="Actualizar", 
            width=100, 
            height=35,
            state="normal",
            command=self.updateExcelView)
        self.update_button.grid(row=0, column=1,pady=(30,10), padx=(0,0),sticky="w")

        self.excelViewer.grid(row=1, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

        self.update_button.configure(state="disabled")
        self.update_button.grid_forget()


    def updateExcelView(self):
        self.excelViewer.display_dataframe()
        