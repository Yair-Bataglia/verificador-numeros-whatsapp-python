# Potenciador de envios (WhatsApp)

## Advertencia
Este programa es **solo para uso de pruebas**. No debe utilizarse para violar ninguna de las políticas de WhatsApp. El uso indebido de la herramienta para enviar mensajes no solicitados o realizar actividades automatizadas que contravengan los términos y condiciones de WhatsApp podría resultar en sanciones o la suspensión de la cuenta.

Asegúrate de usar este software de manera responsable y dentro de los límites legales y éticos establecidos por las plataformas que utilices.

**El autor no se hace responsable del uso indebido de este programa.**


## Descripción
**PEW** es una aplicación desarrollada en Python que permite verificar si un número tiene WhatsApp mediante Selenium y Microsoft Edge. La herramienta interactúa con WhatsApp Web sin enviar mensajes; simplemente verifica si al intentar enviar un mensaje (sin enviarlo realmente) aparece el botón de envío, lo que indica que el número tiene WhatsApp. La aplicación ofrece una interfaz gráfica personalizada con **CustomTkinter** para gestionar y visualizar los datos extraídos de archivos Excel. Utiliza **Pandas** y **Openpyxl** para la manipulación de datos de Excel y verificar los números.

## Tecnologías Utilizadas
- **Python** (para la lógica del programa)
- **CustomTkinter** (para la interfaz gráfica personalizada)
- **Selenium** (para la automatización de WhatsApp Web)
- **Pandas** (para la gestión y manipulación de datos de Excel)
- **Openpyxl** (para la lectura y escritura de archivos Excel)

## Requisitos
Antes de ejecutar el programa, asegúrate de instalar las dependencias necesarias:

```bash
pip install customtkinter selenium pandas openpyxl
```

También es necesario contar con:
- Microsoft Edge instalado
- El driver de Edge correspondiente a la versión de tu navegador (descargar desde: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)

## Estructura del Proyecto

```
GGVWhatsApp/
│── Interface/         # Contiene las interfaces gráficas de la aplicación
│   ├── frameUno.py    # Frame principal donde se carga el Excel
│   ├── frameDos.py    # Frame derecho que muestra el visor de Excel
│   ├── viewer.py      # Componente para visualizar datos de Excel con Treeview
│── utils/             # Archivos de utilidad
│   ├── globalV.py     # Variables globales (ruta del archivo Excel, etc.)
│── main.py            # Punto de entrada principal de la aplicación
│── requirements.txt   # Lista de dependencias para instalar
│── README.md          # Documentación del proyecto
```

## Uso del Programa

1. **Abrir la aplicación** ejecutando:
   ```bash
   python main.py
   ```

## Contribución
Si deseas mejorar el proyecto, puedes hacer un **fork** del repositorio y enviar un **pull request** con tus cambios.

---
Cualquier duda o sugerencia, no dudes en comunicarte. 🚀

