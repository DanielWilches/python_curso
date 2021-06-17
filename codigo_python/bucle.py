def run():
    LIMITE = 300000
    contador = 0
    potencia_2 = 2 ** contador
    while potencia_2 <=LIMITE:
        print(f'2 elevado a {str(contador)} es igual a: {potencia_2}')
        contador = contador + 1
        potencia_2 = 2**contador
        

if __name__ == '__main__':
    run()