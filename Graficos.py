import os.path as path
import os

def graficos():

    # Se comprueba que el archivo exista
    if not path.exists("respuestas.txt"):
        print("El archivo no existe, por favor completa la encuesta para crearlo")
        return 0

    # Se comprueba que el archivo no esté vacío
    if os.stat("respuestas.txt").st_size == 0:
        print("El archivo está vacío, por favor completa la enuesta para poder ver los gráficos")
        return 0

