import customtkinter as ctk
import threading
import time
 
class TimerApp(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        self.seconds = 0  # Contador de segundos

        # Etiqueta para mostrar el tiempo
        self.label = ctk.CTkLabel(self, text=f"Segundos: {self.seconds}", font=("Arial", 20))
        self.label.grid(row=0, column=0, padx=20, pady=20)
        
        # Botón para iniciar el contador
        self.start_button = ctk.CTkButton(self, text="Iniciar", command=self.start_timer)
        self.start_button.grid(row=1, column=0, padx=20, pady=20)

    def start_timer(self):
        # Crear y ejecutar un hilo para el contador
        thread = threading.Thread(target=self.run_timer)
        thread.daemon = True  # El hilo se cerrará automáticamente cuando la aplicación se cierre
        thread.start()

    def run_timer(self):
        # Hacer un contador que incremente cada segundo
        for _ in range(10):  # Contar hasta 10 segundos
            time.sleep(1)  # Espera de 1 segundo
            self.seconds += 1  # Incrementar el contador
            self.update_label()  # Actualizar el label con el nuevo valor de segundos

    def update_label(self):
        # Actualizar el label en el hilo principal
        self.after(0, self._update_label_ui)

    def _update_label_ui(self):
        # Actualizar el texto del label
        self.label.configure(text=f"Segundos: {self.seconds}")


# Crear la ventana principal y agregar la interfaz del temporizador
root = ctk.CTk()
root.geometry("300x200")

timer_app = TimerApp(root)
timer_app.pack(fill="both", expand=True)

root.mainloop()
