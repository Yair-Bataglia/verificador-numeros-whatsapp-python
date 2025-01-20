import customtkinter as ctk
import time

from utils import cache
from Interface.viewer import ExcelViewer
from utils import cache
from Interface.frameEstadoValidador import EstateProcess

class RightFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_propagate(False)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.excelViewer = ExcelViewer(self)
        self.estateProcess = EstateProcess(self)

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

        self.estateProcess.grid_forget()
        self.excelViewer.grid(row=1, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

        self.update_button.configure(state="disabled")
        self.update_button.grid_forget()

    def RefreshExcelViewerShow(self):
        self.after(0, self.excelViewerShow)

    def excelViewerShow(self):
        print("MOSTRAR EXCEL VIEWER")
        self.estateProcess.grid_forget()
        self.excelViewer.grid(row=1, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

        self.close_button.configure(state="normal")
        self.close_button.grid(row=0, column=1,pady=(30,10), padx=(0,0),sticky="w")

        self.update_button.configure(state="disabled")
        self.update_button.grid_forget()



    def simulacro(self):
        for i in range(10):
            time.sleep(1)
            cache.ultimaFila += i
            self.estateProcess.actualizarDato()

    def RefreshEstadoExcelViewer(self):
        self.after(0, self.estadoExcelViewer)

    def estadoExcelViewer(self):
        print("MOSTRAR ESTADO EXCEL VIEWER")
        self.excelViewer.grid_forget()

        self.estateProcess.grid(row=1, column=0, columnspan=3, sticky="nsew", padx=5, pady=5)

        self.close_button.configure(state="disabled")
        self.close_button.grid_forget()
        self.update_button.configure(state="normal")
        self.update_button.grid(row=0, column=1,pady=(30,10), padx=(0,0),sticky="w")

    def updateExcelView(self):
        self.excelViewer.display_dataframe()
        