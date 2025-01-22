import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils import globalV
from utils import exportData
from utils import loaderBar
from utils import cache

class ValidadorNumerosWhatsApp():
    def __init__(self, rightFrame):
        self.user_data = r"C:\Users\SUPERVISION03\AppData\Local\Microsoft\Edge\User Data"
        self.perfil_Edge = "Default"

        self.file_path = globalV.file_path #UBICACION
        self.rightFrame = rightFrame

        self.data = pd.read_excel(self.file_path, dtype={"Numero": str}) #LECTURA
        cache.cantidadFilas = self.data.shape[0]

        self.options = webdriver.EdgeOptions()
        self.options.use_chromium = True
        self.options.add_argument(f"user-data-dir={self.user_data}")  # Usar el perfil existente
        self.options.add_argument(f"profile-directory={self.perfil_Edge}")

        self.service = Service(executable_path="msedgedriver.exe")
        self.driver = webdriver.Edge(service=self.service, options=self.options)

        loaderBar.barra_progreso(15, "El Navegador se esta abriendo, si no a iniciado sesion es la oportunidad")
    
    def validarNumeros(self):
        """FLUJO PRINCIPAL DONDE SE ITERAN LOS NUMEROS Y OPERAN CON CADA UNO DE ELLOS"""
        exportData.crear_excel()

        for index, row in self.data.iterrows():
            cache.validacionFin = False
            if not cache.banderinTheere:
                break

            exportData.numero = row['Numero']
            self.numero = row['Numero']

            try:
                self.numero = str(self.numero)
                self.url = f"https://web.whatsapp.com/send/?phone={self.numero}&text=hola"
                self.driver.get(self.url)

                loaderBar.barra_progreso(5, "se va a buscar el Boton")
                try:
                    send_button = WebDriverWait(self.driver, 5).until( # CREA UN OBJETO QUE ESPERA HASTA QUE SEA VERDADERO
                        EC.presence_of_element_located((By.XPATH, '//span[@data-icon="send"]')) #BUSCA EL BOTON
                    )
                    exportData.estado = 'Tiene WhatsApp'
                except Exception as e:
                    exportData.estado = 'No Tiene WhatsApp'

            except Exception as e:
                exportData.estado = 'No Se pudo procesar el numero'

            cache.ultimaFila = index
            exportData.actualizarExel()

        cache.validacionFin = True
        exportData.cerrar_excel()