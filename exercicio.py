class Animal:
    def __init__(self, nome, peso, idade):
        self.nome = nome
        self.peso= peso
        self.idade = idade

girafa = Animal ('pescoção', '200', '30')
gato = Animal('batman','32','5')
leao = Animal('rei leao','250', '45')


print(f' O animal é {girafa.nome}, pesa{girafa.peso}, e tem {girafa.idade}')
print(gato.nome)
print(leao.nome)