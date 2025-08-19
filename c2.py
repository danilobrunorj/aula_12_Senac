class Carro:
    def __init__(self, nome ):
       self.nome = nome

    def acelerador(self):
        print(f'{self.nome} está acelerando......')

fusca = Carro('fusca')
print('Nome :', fusca.nome)
fusca.acelerador()

byd = Carro('BYD')
print('Nome :', byd.nome)
byd.acelerador()