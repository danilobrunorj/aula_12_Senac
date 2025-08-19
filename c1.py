class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa("André", "marques")
p2 = Pessoa("gilmar","santos")
print(p1.nome)
print(p2.nome)
print('====')
print(p2.nome)
print(p2.sobrenome)