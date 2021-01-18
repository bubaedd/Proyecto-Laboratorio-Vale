import os.path as path
def encuesta():

    # Si el archivo respuestas.txt no existe, entonces lo crea
    if not path.exists("respuestas.txt"):
        archivo_respuestas = open("respuestas.txt","a")
        archivo_respuestas.close()

    # Abre el archivo en modo >>>>>>>>apertura<<<<<<<<<<<
    # ------------------    FALTA DEFINIR SI SE VA A USAR APERTURA O SI SE ESCRIBIRÁ DESDE 0  ------------------
    archivo_respuestas = open("respuestas.txt","a")

    #-----------------    FALTA DEFINIR EL ESQUEMA DEL ARCHIVO PARA FACILITAR LA LECTURA/APERTURRA  ------------------

    # Pregunta recorrido, mes y año
    recorrido = input("Ingresa el recorrido(Ejemplo F08): ")
    mes =input("Ingresa el mes en que usaste el recorrido que mencionaste(Ejemplo 10): ")
    año = input("Ingresa el año en el que usaste el recorrido que mencionaste(Ejemplo 2019): ")
    archivo_respuestas.write(recorrido+";"+año+";"+mes+";")

    # ---------------    FALTA COMPROBAR QUE LA RESPUESTA SEA SI O NO PARA CADA PREGUNTA    ----------------------
    # Pregunta 1
    print("ACA SE DESCRIBE QUE ES UNA SITUACIÓN DE VIOLENCIA FÍSICA")
    pregunta1 = input("¿Has vivido o presenciado violencia física dentro de la micro? (Responde con un SI o un NO: ")
    pregunta = pregunta1.upper()


    # Pregunta 2
    print("ACA SE DESCRIBE QUE ES UN ROBO DE PERTENENCIAS")
    pregunta2 = input("¿Has vivido o presenciado robo de pertenencias dentro de la micro? (Responde con un SI o un NO: ")
    pregunta = pregunta2.upper()


    # Pregunta 3
    print("ACA SE DESCRIBE QUE ES UN ASALTO A MANO ARMADA")
    pregunta3 = input("¿Has vivido o presenciado asalto a mano armada dentro de la micro? (Responde con un SI o un NO: ")
    pregunta = pregunta3.upper()
    #inserto las preguntas en el archivo
    preguntas= pregunta1.upper()+";"+pregunta2.upper()+";"+pregunta3.upper()
    archivo_respuestas.write(preguntas+"\n")

    archivo_respuestas.close()

