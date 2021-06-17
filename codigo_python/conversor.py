# pesos = input('cuantos pesos colombianos tienes:  ')
# pesos = float(pesos)
# valor_dolar = 3875
# dolares = pesos / valor_dolar
# dolares = round(dolares, 2)
# dolares = str(dolares)
# print(f'tienes $  {dolares} dolares ')
# print('fin programas de pesos a dolares ')
# print('')

def pasos_comunes(cantidad, valor_moneda):
    conversion = cantidad / valor_moneda
    conversion = round(conversion, 2)
    return conversion

def coversor(moneda, cantidad):
    valor_dolar = 3708
    valor_cop = 0.00027
    if moneda == 1:
        dolares = pasos_comunes(cantidad, valor_dolar)
        print(f' el cambio se realzo y esta es la cantidad de dolares {dolares}')
        print('*' * 100)
    elif moneda == 2:
        pesos = pasos_comunes(cantidad, valor_cop)
        print(f' el cambio se realizo y la catidad de pesos es {pesos}')
        print('*' * 100)
    elif moneda >= 3:
        print('fuera de rango vulve al menu ')
        menu()
    

def menu():
    moneda = int(input('''
        Seleciona el tipo de conversion:
            1. de COP a Dolar EEUU
            2. de Dolar EEUU a COP
            3. de 
        ingresa el tipo que deseas:  '''
    ))
    print('*' * 100)
    cantidad = float(input(
        'ingrese la cantidad de dinero a realizar la conversion: '
    ))
    coversor(moneda, cantidad)



if __name__ == '__main__':
    menu()
