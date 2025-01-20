import customtkinter as ctk

from utils import cache

class EstateProcess(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.label = ctk.CTkLabel(self, 
            width=100,
            text="Prueba", 
            font=("Arial", 10), 
            anchor='w')
        self.label.grid(row=0, column=0)

    def actualizarDato(self):
        print("actualizado")
        self.after(0, self._actualizar_label)
        
    def _actualizar_label(self):
        print(cache.ultimaFila)
        print(f'SE ACTUALIZAAAAA {str(cache.ultimaFila)}')
        self.label.configure(text=f"{str(cache.ultimaFila)} numeros verificados de: {cache.cantidadFilas}")