import time
import sys
from utils import cache
detener_timer = cache.banderinTheere

def barra_progreso(duracion, sms):
    barra = 100
    intervalos = duracion / barra
    
    print(sms + " progreso:")
    for i in range(barra + 1):
        if detener_timer:
            print("\nTimer detenidoooooooooooooooo.")
            break
        
        progreso = "█" * i + "-" * (barra - i) 
        segundos_restantes = duracion - int(i * intervalos) 
        sys.stdout.write(f"\r[{progreso}] {segundos_restantes}s restantes")
        sys.stdout.flush()
        time.sleep(intervalos) 
