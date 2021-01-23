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

#Funcion que obtiene los viajes más peligrosos segun respuesta p1
def Top5P1(listaP1,n):
    auxListaP1 = list(listaP1)
    auxLista=[]
    if(n<5):
        for i in range(n):
            mayorValor = 0
            indiceMayor=0
            for j in range(len(auxListaP1)):
                data = auxListaP1[j].split(';')

                if int(data[1])>mayorValor and int(data[1])!=0:
                    mayorValor=int(data[1])
                    indiceMayor=j
                    recorrido = data[0]
            if mayorValor != 0:
                auxLista.append(recorrido + ';' + str(mayorValor))
            auxListaP1.pop(indiceMayor)
        return auxLista

    if(n>=5):
        for i in range(5):
            mayorValor = 0
            indiceMayor = 0
            for j in range(len(auxListaP1)):
                data = auxListaP1[j].split(';')
                if int(data[1])>mayorValor and int(data[1])!=0:
                    mayorValor = int(data[1])
                    indiceMayor = j
                    recorrido=data[0]
            if mayorValor !=0:
                auxLista.append(recorrido + ';' + str(mayorValor))
            auxListaP1.pop(indiceMayor)

        return auxLista

#Funcion que obtiene los viajes más peligrosos segun respuesta p2
def Top5P2(lista,n):
    lista=list(lista)
    auxListaP2=[]
    if(n<5):
        for i in range(n):
            mayorValor = 0
            indiceMayor=0
            for j in range(len(lista)):
                data = lista[j].split(';')
                if int(data[2])>mayorValor and int(data[2])!=0:
                    mayorValor=int(data[2])
                    indiceMayor=j
                    recorrido = data[0]
            if mayorValor != 0:
                auxListaP2.append(recorrido + ';' + str(mayorValor))
            lista.pop(indiceMayor)
        return auxListaP2

    if(n>=5):
        for i in range(5):
            mayorValor = 0
            indiceMayor = 0
            for j in range(len(lista)):
                data = lista[j].split(';')
                if int(data[2])>mayorValor and int(data[2])!=0:
                    mayorValor = int(data[2])
                    indiceMayor = j
                    recorrido = data[0]
            if mayorValor != 0:
                auxListaP2.append(recorrido + ';' + str(mayorValor))
            lista.pop(indiceMayor)
        return auxListaP2

#Funcion que obtiene los viajes más peligrosos segun respuesta p3
def Top5P3(lista,n):
    lista=list(lista)
    auxLista=[]
    if(n<5):
        for i in range(n):
            mayorValor = 0
            indiceMayor=0
            for j in range(len(lista)):
                data = lista[j].split(';')
                if int(data[3])>mayorValor and int(data[3])!=0:
                    mayorValor=int(data[3])
                    indiceMayor=j
                    recorrido = data[0]
            if mayorValor != 0:
                auxLista.append(recorrido + ';' + str(mayorValor))
            lista.pop(indiceMayor)
        return auxLista

    if(n>=5):
        for i in range(5):
            mayorValor = 0
            indiceMayor = 0
            for j in range(len(lista)):
                data = lista[j].split(';')
                if int(data[3])>mayorValor and int(data[3])!=0:
                    mayorValor = int(data[3])
                    indiceMayor = j
                    recorrido = data[0]
            if mayorValor != 0:
                auxLista.append(recorrido + ';' + str(mayorValor))
            lista.pop(indiceMayor)
        return auxLista












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

        #Obteniendo TOP5


        rP1= Top5P1(tuple(listaRP),len(listaRP))
        rP2= Top5P2(tuple(listaRP),len(listaRP))
        rP3= Top5P3(tuple(listaRP),len(listaRP))

        #Creación de graficos de barra por pregunta

        #Grafico pregunta1

        #recorridos P1
        rp1=[]
        #puntaje P1
        pP1=[]
        for i in range(len(rP1)):
            data = rP1[i].split(";")
            rp1.append(data[0])
            pP1.append(int(data[1]))

        pyplot.bar(range(len(rp1)),pP1,edgecolor="red")
        pyplot.xticks(range(len(rp1)),rp1)
        pyplot.ylim(min(pP1)-1,max(pP1)+1)
        pyplot.title("¿Has vivido o presenciado violencia física dentro de la micro?")
        pyplot.legend(["Respuesta SI"])
        pyplot.savefig("GraficaP1.jpg")
        pyplot.show()

        # Grafico pregunta2

        # recorridos P2
        rp2 = []
        # puntaje P2
        pP2 = []
        for i in range(len(rP2)):
            data = rP2[i].split(";")
            rp2.append(data[0])
            pP2.append(int(data[1]))

        pyplot.bar(range(len(rp2)), pP2, edgecolor="red")
        pyplot.xticks(range(len(rp2)), rp2)
        pyplot.ylim(min(pP2) - 1, max(pP2) + 1)
        pyplot.title("¿Has vivido o presenciado robo de pertenencias dentro de la micro?")
        pyplot.legend(["Respuesta SI"])
        pyplot.savefig("GraficaP2.jpg")
        pyplot.show()

        # Grafico pregunta3

        # recorridos P3
        rp3 = []
        # puntaje P3
        pP3 = []
        for i in range(len(rP2)):
            data = rP3[i].split(";")
            rp3.append(data[0])
            pP3.append(int(data[1]))

        pyplot.bar(range(len(rp3)), pP3, edgecolor="red")
        pyplot.xticks(range(len(rp3)), rp3)
        pyplot.ylim(min(pP3) - 1, max(pP3) + 1)
        pyplot.title("¿Has vivido o presenciado asalto a mano armada dentro de la micro?")
        pyplot.legend(["Respuesta SI"])
        pyplot.savefig("GraficaP3.jpg")
        pyplot.show()











