from openpyxl import Workbook

numero = 0
estado = ''
comentario = ''


wb = Workbook()

ws = wb.active
ws.title = "Hoja1"

ws['A1'] = "Numero"
ws['B1'] = "Estado"
ws['C1'] = "Comentario"

def actualizarExel():
	ws.append([numero,estado,comentario])
	wb.save('export/archivo.xlsx')
