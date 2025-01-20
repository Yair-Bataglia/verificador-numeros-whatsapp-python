import customtkinter as ctk
from tkinter import filedialog
from tkinter.ttk import Treeview  # Asegúrate de importar Treeview desde ttk
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
        style.theme_use("winnative")

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

        # Treeview donde se mostrarán los datos del Excel
        self.tree = Treeview(self, style="Treeview", show="headings")
        self.tree.grid(row=0, column=0, sticky="nsew")

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)

        # Barra de desplazamiento
        self.scrollbar = ctk.CTkScrollbar(
            self,
            command=self.tree.yview,
            fg_color="#555555",  
            button_color="#333333",  
            button_hover_color="#222222" 
        )
        self.scrollbar.grid(row=0, column=1, sticky="ns")

        self.tree.configure(yscrollcommand=self.scrollbar.set)

        # Botón para cargar archivo Excel
        self.load_button = ctk.CTkButton(self, text="Cargar Excel", command=self.load_excel)
        self.load_button.grid(row=1, column=0, padx=10, pady=10)

        self.df = pd.DataFrame({})  # DataFrame vacío inicial

    def display_dataframe(self, df):
        # Configura las columnas del Treeview según el DataFrame
        self.tree["columns"] = list(df.columns)
        for col in df.columns:
            self.tree.heading(col, text=col)  
            self.tree.column(col, width=200, anchor="w")

        # Inserta las filas del DataFrame en el Treeview
        for _, row in df.iterrows():
            self.tree.insert("", "end", values=list(row))

    def load_excel(self):
        # Abrir un cuadro de diálogo para seleccionar un archivo Excel
        file_path = filedialog.askopenfilename(filetypes=[("Archivos Excel", "*.xlsx")])
        if file_path:
            # Leer el archivo Excel con pandas
            df = pd.read_excel(file_path)
            # Mostrar el DataFrame en el Treeview
            self.display_dataframe(df)

# Crear la ventana principal
root = ctk.CTk()

# Crear instancia del visor de Excel
viewer = ExcelViewer(root)
viewer.pack(fill="both", expand=True)

root.mainloop()
