def preguntarOperacion():
    print('¿Deseas realizar otra operación?\n'
          '1) Si\n'
          '2) No\n')

    valor = input('Escribe 1 o 2: ')
    if valor == '1' or valor == '2':
        return valor
    else:
        print('la opción ingresada no es válida, inténtalo nuevamente\n')
        return preguntarOperacion()

