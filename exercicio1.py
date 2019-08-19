numero = [1,2,5,35]

def valores(numero):
    for m in numero:
        if m % 2 == 0:
            print('numero impar')
        else:
            print('numero par')
    return numero

valores(numero)