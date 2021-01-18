# menu

from FuncionPreguntar import preguntarOperacion
from Encuesta import encuesta
from Graficos import graficos


def main():
    valor = 0
    # Muestra el menú
    print('.............Menú.............\n'
          '.                            .\n'
          '. 1) Ingresar a la encuesta  .\n'
          '. 2) Ver gráfico             .\n'
          '. 3) Salir                   .\n'
          '..............................\n')

    # Guarda la opción escogida
    opcion = input('Escribe 1, 2 o 3 para continuar: ')

    try:
        # Comprueba si la opción escogida es válida (1 o 2)
        if opcion == '1' or opcion == '2':
            # Si la opción es 1, lo llevará a la encuesta,
            if opcion == '1':
                encuesta()
                print('Ya se hizo la encuesta')

            # Si la opción es 2, lo llevará a los gráficos
            else:
                valor = graficos()

                # Si el archivo no existe, lo devuelve al menú
                if valor == 0:
                    return main()

                print('Ya se mostraron los gráficos')

            # Llama a la función preguntarOperacion para saber si quiere realizar otra cosa retornando 1 o 2
            valor = preguntarOperacion()

            # En el caso de que quiera realizar otra operación, lo llevará al menú principal
            if valor == '1':
                return main()
            # Si no, sale del programa
            else:
                exit()

        # En el caso de que la opción sea 3, se cerrará el programa
        elif opcion == '3':
            print('Escogiste la opción 3')
            exit()

        # Si la opción no es válida, le avisa al usuario y lo devuelve al menú
        else:
            print('La opción ingresada no es válida, inténtalo nuevamente')
            return main()


    except Exception as ex:
        print("Problemas en el ingreso de datos:",ex)



main()
