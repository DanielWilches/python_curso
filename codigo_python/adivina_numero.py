import random

def run():
    contador = 0
    numero_aletorio = random.randint(1, 100)
    numero_elegido = int(input(f'ingresa un numero, posees:  '))
    while numero_elegido != numero_aletorio:
        contador = contador + 1
        if numero_elegido < numero_aletorio:
            print('busca un numero mas grande')
            numero_elegido = int(input('ingresa otro  numero:  '))
        else:
            print('busca un numero mas pequeño')
            numero_elegido = int(input('ingresa otro  numero:  '))
    print(f'gabaste con {contador} intentos')

if __name__ == '__main__':
    run()
