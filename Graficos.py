import os.path as path
from matplotlib import  pyplot
import os

#Funcion que elimina elementos duplicados
def EliminarDuplicados(lista):
    fLista = []
    for element in lista:
        if element not in fLista:
            fLista.append(element)
    return fLista

#Funcion que retorna el mayor valor en una lista y su indice(evaluar por pregunta el top5)
# def topFive(lista):
#     mayorP1=0
#     mayorP2=0
#     mayorP3=0
#     listaRTop=[]
#     for i in range(len(lista)):
#         data =lista[i].split(";")
#         if int(data[1])>mayorP1:
#             mayorP1=int(data[1])
#         if  int(data[2])>mayorP2:
#             mayorP2 = int(data[2])
#         if int(data[3]) > mayorP3:
#             mayorP3 = int(data[3])
#     listaRTop.append(i+';'+str())









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
        #Declaracion de variables
        contLine =0
        countSI =0
        countNO=0
        #Arreglo de respuestas por preguntas
        p1=[]
        p2=[]
        p3=[]
        #Arreglo de recorridos
        recorrido =[]
        file = open("respuestas.txt","r")
        nonempty_lines = [line.strip("\n") for line in file if line != "\n"]
        #guardando recorridos
        for i in range(len(nonempty_lines)):
            data = nonempty_lines[i].split(";")
            recorrido.append(data[0])

        recorridoF = EliminarDuplicados(recorrido)


       #Obteniendo resultados por preguntas
        for i in range(len(recorridoF)):
            data= recorridoF[i]
            #Variables de conteo segun pregunta
            contP1 = 0
            contP2 = 0
            contP3 = 0
            #recorro lista que contiene respuestas
            for j in range(len(nonempty_lines)):
                separadoData = nonempty_lines[j].split(";")
                if data == separadoData[0]:
                    if separadoData[3]=="SI":
                        contP1+=1
                    if separadoData[4]=="SI":
                        contP2+=1
                    if separadoData[5]=="SI":
                        contP3+=1
            p1.append(contP1)
            p2.append(contP2)
            p3.append(contP3)

        #ordenando datos de recorridos y puntajes
        listaRP=[]
        for i in range(len(recorridoF)):

            listaRP.append(recorridoF[i]+';'+str(p1[i])+';'+str(p2[i])+';'+str(p3[i]))











