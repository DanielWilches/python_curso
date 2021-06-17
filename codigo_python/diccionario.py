def run():
    mi_diccionario = {
        'numer1': 1,
        'numero2': 2,
        'numero3':3
    }
    print(mi_diccionario)
    # con esta forma recoremos un diccionario 
    for numero, value in mi_diccionario.items():
        print(numero, value)

if __name__ == '__main__':
    run()