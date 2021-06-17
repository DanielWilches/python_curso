def run():
    palabra = input('ingresa  tu nombre :    ')
    nombre = palabra.replace(' ', '')
    for letra in nombre:
        print(letra.upper())
        


if __name__ == '__main__':
    run()