class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        print(f'ola, meu nome e {self.nome} e tenho {self.idade} anos')

       
p1 = Pessoa('maria' , 25)
p2 = Pessoa('mayara', 27)
p3 = Pessoa('clinton', 32)


p1.cumprimentar()
p2.cumprimentar()
p3.cumprimentar()

