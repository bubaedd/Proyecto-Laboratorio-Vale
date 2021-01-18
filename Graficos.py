import os.path as path
from matplotlib import  pyplot
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

    else:
        contLine =0
        countSI =0
        countNO=0
        with open("respuestas.txt") as lines:
            for line in lines:
                line.replace("\n","")
                value = line.split(';')


                for i in range(len(value)):

                    if value[i]=="SI" or value[i]=="SI\n":
                        countSI+=1

                    if value[i]=="NO" or value[i]=="NO\n":
                        countNO+=1
        resultadosEncuesta = ["SI","NO"]
        nSINO=[countSI,countNO]
        colores=["green","red"]

        pyplot.title("resultados de encuestas")
        pyplot.bar(resultadosEncuesta,height=nSINO,color=colores,width=0.5)

        pyplot.savefig("grafico.jpg")
        pyplot.show()




