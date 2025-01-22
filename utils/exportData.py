import os
from datetime import datetime
from openpyxl import Workbook, load_workbook

numero = 0
estado = ''
comentario = ''

wb = None  # Variable global para almacenar el libro de trabajo
ws = None  # Variable global para la hoja activa
nombre_archivo = None  # Nombre del archivo de Excel

def generar_nombre_archivo():
    print("\nGENERAR NOMBRE")
    """Genera un nombre único para el archivo basado en la fecha y un contador."""
    fecha_actual = datetime.now().strftime('%y%m%d')
    base_nombre = f"base_verificada_{fecha_actual}_"
    contador = 0

    while True:
        archivo = f"{base_nombre}{contador}.xlsx"
        if not os.path.exists(f"export/{archivo}"):
            return archivo
        contador += 1

def crear_excel():
    """Abre un archivo existente o crea uno nuevo si no existe."""
    global wb, ws, nombre_archivo
    nombre_archivo = generar_nombre_archivo()
    print(f"\n SE VA A CREAR CON {nombre_archivo}")

    wb = Workbook()
    ws = wb.active
    ws.title = "Hoja1"
    ws.append(["Numero", "Estado", "Comentario"])  # Agrega encabezados
    
def actualizarExel():
    print("\n ACTUALIZANDO")
    ws.append([numero, estado, comentario])
    wb.save(f"export/{nombre_archivo}")

def cerrar_excel():
    print("\n CERRANDO")
    """Guarda y cierra el archivo de Excel."""
    if wb:
        wb.save(f"export/{nombre_archivo}")
        wb.close()
