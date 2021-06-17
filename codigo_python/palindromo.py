

def palindromo(palabra):
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False



def run():
    palabra = input('ingrese su palabra  ')
    es_palindromo = palindromo(palabra)
    if es_palindromo:
        print(' es palindromo')
    else:
        print('no es palindromo')


#punto de entrada en python
if __name__ == '__main__':
    run()


