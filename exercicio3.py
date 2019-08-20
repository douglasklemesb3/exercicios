import statistics

data1 = [1,2,6,5,8,9,2]

x = statistics.mean(data1)
print(x)


def listas_de_compras(pessoa, *args):
    print('lista de compra de: ' + pessoa)
    for item in args:
        print (item)

listas_de_compras('joao', 'coxinha','batata','jujuba')
listas_de_compras('douglas', 'coxinhas','batata-doce','jujuba-vermelha')
listas_de_compras('karen', 'maracuja','uva', 'computador', 'argolas','cachos')

def lista_de_compras(pessoa, **kwargs):
    print('olá ' + pessoa)
    fruta = kwargs.get('fruta')
    massa = kwargs.get('massa')
    if fruta is not None:
        print('na lista de compras ha uma fruta ' + fruta)
        print('na lista tem '+ massa)

lista_de_compras('douglas' ,fruta='abacate', massa='nhoque',vertuda='alface')


def item(**kwargs):
   for k in kwargs.items():
        print(k)

item(nome='groger', id=1)
