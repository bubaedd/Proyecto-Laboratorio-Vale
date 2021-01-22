import random

LETRAS = 'AEIOU'
PRIMER_NUMERO = '01'
SEGUNDO_NUMERO = '123456789'

def generarLista(numero_respuestas):
    respuestas = ''
    i = 0
    for i in range(numero_respuestas):
        lista = []
        letra = LETRAS[random.randint(0,len(LETRAS)-1)]
        digito_uno = PRIMER_NUMERO[random.randint(0,len(PRIMER_NUMERO)-1)]
        digito_dos = SEGUNDO_NUMERO[random.randint(0,len(SEGUNDO_NUMERO)-1)]

        anyo = str(random.randint(2016,2021))
        mes = str(random.randint(1,12))
        if len(mes) < 2:
            mes = '0'+mes

        rpta1 = respuesta(random.randint(0,1))
        rpta2 = respuesta(random.randint(0,1))
        rpta3 = respuesta(random.randint(0,1))

        respuestas += letra+digito_uno+digito_dos+';'+anyo+';'+mes+';'+rpta1+';'+rpta2+';'+rpta3+'\n'

        lista.append(respuestas)

    escribirArchivo(lista)

def respuesta(valor):
    if valor == 0:
        return('NO')
    else:
        return('SI')

def escribirArchivo(lista):
    archivo = open('respuestas.txt', 'w')
    for linea in lista:
        archivo.write(linea)
    archivo.close()

num_respuestas = int(input('ingrese numero de respuestas: '))
generarLista(num_respuestas)