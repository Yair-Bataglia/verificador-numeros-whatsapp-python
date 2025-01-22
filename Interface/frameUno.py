import customtkinter as ctk
import os
from utils import globalV
from tkinter import filedialog
import threading
from cores import validador
from utils import cache

class LeftFrame(ctk.CTkFrame):
    """
    Clase que controlad todo el panel izquierdo de la interfaz principal.
    """
    def __init__(self, master, rightFrame):
        super().__init__(master, width=300, fg_color="#212121")
        self.grid_propagate(False)

        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=0)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        #VARIABLES
        self.file_path_var = ctk.StringVar()
        self.rightFrame = rightFrame

        self.iniciarVerificacion_thread = None 
        self.running = False  

        self.title = ctk.CTkLabel(self, 
            width=100,
            text="VNW", 
            font=("Arial", 30), 
            anchor='w')
        self.title.grid(row=0, column=0, columnspan=2, pady=(30,200), padx=10)

        self.file_entry = ctk.CTkEntry(self, 
            textvariable=self.file_path_var, 
            width=150, 
            height=35, 
            state="disabled")
        self.file_entry.grid(row=1, column=0,padx=(0,0) ,pady=(0,0))

        self.load_button = ctk.CTkButton(self, 
            text="Cargar Archivo", 
            width=100, 
            height=35, 
            command=self.cargar_archivo)
        self.load_button.grid(row=1, column=1,padx=0, pady=(0,0))

        self.start_button = ctk.CTkButton(self, 
            text="Iniciar", 
            width=70, 
            height=40, 
            command=self.TriggerIniciarVerificacion)
        self.start_button.grid(row=2, column=0, columnspan=2,padx=0, pady=(60,0))

        self.cancelar_button = ctk.CTkButton(self, 
            text="Cancelar", 
            width=70, 
            height=40, 
            command=self.CancelarIniciarVerificacion)
        self.cancelar_button.grid(row=3, column=0, columnspan=2,padx=0, pady=(60,0))

#-----------------------------------FUNCIONES---------------------------------------------

    def cargar_archivo(self):
        """
        Abre un cuadro de dialogo para indicarle al usuario que seleccione un archivo Excel (.xslx).
        
        La ruta de este archivo se almacena en una variable que esta dentro de GLOBALV.file_path.

        Tambien guarda solamente el nombre en otra variable GLOBAL.

        Para Finalizar llama a la funcion updateExcelView() de rightFrame.
        """

        globalV.file_path = filedialog.askopenfilename(
            title="Selecciona un archivo Excel", filetypes=[("Archivos Excel", "*.xlsx")]
        )
        globalV.archivoName = os.path.basename(globalV.file_path)
        if globalV.file_path: 
            self.file_path_var.set(globalV.archivoName)

        self.rightFrame.updateExcelView()

    def TriggerIniciarVerificacion(self):
        """
        Verifica si ya esta ejecutandose el sistemas, en caso que no lo este lo va a iniciar.

        Guarda informacion global sobre el estado del proceso y crea un hilo donde se ejecuta
        iniciarVerificacion.
        """
        
        if self.iniciarVerificacion_thread and self.iniciarVerificacion_thread.is_alive():
            return

        self.running = True 
        cache.banderinTheere = self.running
        self.iniciarVerificacion_thread = threading.Thread(target=self.iniciarVerificacion)
        self.iniciarVerificacion_thread.daemon = True
        self.iniciarVerificacion_thread.start()

    def CancelarIniciarVerificacion(self):
        """
        Cancela el proceso de verificacion de Numeros.

        Primero verifica si esta corriendo, en caso de que el proceso se este ejecutando
        va a matar el hilo y cambiar las variables globales.
        """
        self.running = False  
        cache.banderinTheere = self.running

        if self.iniciarVerificacion_thread and self.iniciarVerificacion_thread.is_alive():
            if cache.validacionFin:
                self.iniciarVerificacion_thread.join(0)

    def iniciarVerificacion(self):
        """
        Inicia la funcion de validador que verifica los numeros.
        """
        self.validador = validador.ValidadorNumerosWhatsApp(self.rightFrame)
        self.validador.validarNumeros()