import customtkinter as ctk
from tkinter.ttk import Treeview
from utils import globalV
from tkinter import ttk
import pandas as pd

class ExcelViewer(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="black")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Configuración del estilo para el Treeview
        style = ttk.Style()
        style.theme_use("clam")

        style.configure(
            "Treeview",
            background="#555555", 
            foreground="#fff",
            rowheight=25,         
            fieldbackground="#555555",
            borderwidth=0 
        )

        style.configure(
            "Treeview.Heading",
            font=("Helvetica", 12, "bold"), 
            background="#333333", 
            foreground="#fff",   
            relief="flat",
            borderwidth=0
        )
        style.map(
            "Treeview.Heading",
            background=[("active", "#77aaff")] 
        )

        # Treeview (sin scrollbar visible)
        self.tree = Treeview(self, style="Treeview", show="headings")
        self.tree.grid(row=0, column=0, sticky="nsew")

        self.grid_columnconfigure(0, weight=1)

        # Vincular el Treeview con el scroll, pero sin mostrarlo
        self.tree.configure(yscrollcommand=lambda *args: None)  # Desvincula la barra de desplazamiento
        
        self.df = pd.DataFrame({})  # DataFrame vacío inicial

    def display_dataframe(self):
        df = pd.read_excel(globalV.file_path)

        # Limpiar el contenido del Treeview antes de cargar nuevos datos
        self.tree.delete(*self.tree.get_children())

        # Configura las columnas del Treeview según el DataFrame
        self.tree["columns"] = list(df.columns)
        for col in df.columns:
            self.tree.heading(col, text=col)  
            self.tree.column(col, width=200, anchor="w")

        # Inserta las filas del DataFrame en el Treeview
        for _, row in df.iterrows():
            self.tree.insert("", "end", values=list(row))
